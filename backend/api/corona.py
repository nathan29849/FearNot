from urllib.parse import urlencode, unquote
from datetime import datetime, timedelta    
from bs4 import BeautifulSoup
from api.models import TotalData
from my_settings import API_KEY
import requests

url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson"
Key = API_KEY
today = datetime.now()
yesterday = today + timedelta(days=-1)
print(yesterday, today)
today = "".join(str(today)[:10].split("-"))
yesterday = "".join(str(yesterday)[:10].split("-"))
def add_data(start, end):
    global url
    global Key
    queryString = "?" + urlencode(
        {
            'serviceKey': unquote(Key),
            'pageNo': 1,
            'numOfRows': 10,
            'startCreateDt': start,    # 데이터 시작일 20200120 (근데 이때부터 들어가는게 맞을까?)
            'endCreateDt': end,      # 데이터 베이스에 넣을 날짜
        }
    )        
    queryURL = url + queryString
    response = requests.get(queryURL)

    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all('item')
    start = datetime(int(start[:4]), int(start[4:6]),int(start[6:]))
    i = 0  # 일 별 데이터를 수집하기 위한 변수 (일별 11개의 데이터가 들어옴)
    for item in data[::-1]:
        # 하루 총 데이터 : 9개 
        if i % 11 == 0:
            total_death_toll = 0    # 총 사망자 수 (당일까지)
            total_conf = 0          # 총 감염자 수 (당일까지)
            death_by_age = [0]*(9)  # 연령별 사망자 수 (당일까지)
            conf_by_age = [0]*(9)   # 연령별 사망자 수 (당일까지)
        
        
        # 당일 날짜 계산 (15일 이전 날짜를 쉽게 구하기 위한 작업)
        createdt = item.find('createdt').get_text()
        createdt = "".join(createdt[:10].split("-"))    # 2020-04-14 -> 20200414       
        date = datetime(int(createdt[:4]), int(createdt[4:6]),int(createdt[6:]))

        confcase = item.find("confcase").get_text()
        death = item.find("death").get_text()
        gubun = item.find("gubun").get_text()

        # 분류 작업
        if gubun == '남성' or gubun == '여성':
            total_death_toll += int(death)
            total_conf += int(confcase)
        elif gubun == '0-9':
            death_by_age[0], conf_by_age[0] = death, confcase
        elif gubun == '10-19':
            death_by_age[1], conf_by_age[1] = death, confcase
        elif gubun == '20-29':
            death_by_age[2], conf_by_age[2] = death, confcase
        elif gubun == '30-39':
            death_by_age[3], conf_by_age[3] = death, confcase
        elif gubun == '40-49':
            death_by_age[4], conf_by_age[4] = death, confcase
        elif gubun == '50-59':
            death_by_age[5], conf_by_age[5] = death, confcase
        elif gubun == '60-69':
            death_by_age[6], conf_by_age[6] = death, confcase
        elif gubun == '70-79':
            death_by_age[7], conf_by_age[7] = death, confcase
        else: # gubun == '80 이상':
            death_by_age[8], conf_by_age[8] = death, confcase
        
        
        if i % 11 == 10:        # 하루 데이터가 끝나는 시점
            if date != start:   # 빠진 날짜의 데이터가 있을 때 20211117 != 20211116
                print(date, start)
                yesterday = start + timedelta(days=-1)
                print(yesterday)
                yesterday_data = TotalData()
                temp_object = TotalData.objects.get(date=yesterday)
                yesterday_data.date = start
                yesterday_data.total_conf = temp_object.total_conf
                yesterday_data.total_death_toll = temp_object.total_death_toll
                yesterday_data.day_conf = temp_object.day_conf
                yesterday_data.day_death = temp_object.day_death
                yesterday_data.total_critical_rate = temp_object.total_critical_rate
                yesterday_data.first_death = temp_object.first_death
                yesterday_data.first_conf = temp_object.first_conf
                yesterday_data.first_ciritical_rate = temp_object.first_ciritical_rate
                yesterday_data.second_death = temp_object.second_death
                yesterday_data.second_conf = temp_object.second_conf
                yesterday_data.second_ciritical_rate = temp_object.second_ciritical_rate
                yesterday_data.third_death = temp_object.third_death
                yesterday_data.third_conf = temp_object.third_conf
                yesterday_data.third_ciritical_rate = temp_object.third_ciritical_rate
                yesterday_data.save()
                start += timedelta(days=1)
            insert_data(date, total_conf, total_death_toll, death_by_age, conf_by_age)
            # temp = [date, total_conf, total_death_toll, death_by_age, conf_by_age]
            start += timedelta(days=1)

        i += 1                
            

# 0-9 0       
# 10-19 0
# 20-29 12
# 30-39 25
# 40-49 48
# 50-59 196
# 60-69 481
# 70-79 890
# 80 이상 1676            

# 새 모델 생성 후 데이터 삽입
def insert_data(date, total_conf, total_death_toll, death_by_age, conf_by_age):
    pre_date = date + timedelta(days=-15)   # 15일 이전 날짜 계산
    try:
        pre_total_data = TotalData.objects.get(date=pre_date)
        pre_conf, pre_death = pre_total_data.total_conf, pre_total_data.total_death_toll
        total_critical_rate = calculate_critical_rate(total_conf, total_death_toll, pre_conf, pre_death)
    except:
        pre_total_data = 0 # Null 대신 빈 문자열 사용하는 것이 장고 convention
        total_critical_rate = 0

    
    new_data = TotalData()
    new_data.date = date
    new_data.total_conf = total_conf
    new_data.total_death_toll = total_death_toll
    new_data.total_critical_rate = total_critical_rate
    
    yesterday = date + timedelta(days=-1)
    if date == datetime(2020, 1, 20):       # 첫 감염자 발생 시점
        yesterday_conf, yesterday_death = 0, 0
    elif date == datetime(2020, 2, 20):     # 첫 사망자 발생 시점
        yesterday_total_data = TotalData.objects.get(date=yesterday)
        yesterday_conf, yesterday_death = yesterday_total_data.total_conf, total_death_toll
    else:
        yesterday_total_data = TotalData.objects.get(date=yesterday)
        yesterday_conf, yesterday_death = yesterday_total_data.total_conf, yesterday_total_data.total_death_toll
            
    new_data.day_conf = total_conf - yesterday_conf
    new_data.day_death = total_death_toll - yesterday_death
    # print(new_data.date, 'clear')
    
    
    for i in range(9):
        temp_death, temp_conf = 0, 0
        temp_death += int(death_by_age[i])
        temp_conf += int(conf_by_age[i])
        
        if i == 3:          # ~ 40세 미만
            new_data.first_death = temp_death
            new_data.first_conf = temp_conf
            try:
                temp_pre_conf = pre_total_data.first_conf
                temp_pre_death = pre_total_data.first_death
                first_ciritical_rate = calculate_critical_rate(temp_conf, temp_death, temp_pre_conf, temp_pre_death)
                new_data.first_ciritical_rate = first_ciritical_rate
            except:
                new_data.first_ciritical_rate = 0
            temp_death, temp_conf = 0, 0
        elif i == 6:        # 40세 이상 ~ 70세 미만
            new_data.second_death = temp_death
            new_data.second_conf = temp_conf
            try:
                temp_pre_conf = pre_total_data.second_conf
                temp_pre_death = pre_total_data.second_death
                second_ciritical_rate = calculate_critical_rate(temp_conf, temp_death, temp_pre_conf, temp_pre_death)
                new_data.second_ciritical_rate = second_ciritical_rate
            except:
                new_data.second_ciritical_rate = 0
            temp_death, temp_conf = 0, 0        
        elif i == 8:        # 70세 이상 ~
            new_data.third_death = temp_death
            new_data.third_conf = temp_conf  
            try:
                temp_pre_conf = pre_total_data.third_conf
                temp_pre_death = pre_total_data.third_death
                third_ciritical_rate = calculate_critical_rate(temp_conf, temp_death, temp_pre_conf, temp_pre_death)
                new_data.third_ciritical_rate = third_ciritical_rate
            except:
                new_data.third_ciritical_rate = 0
    new_data.save()    
    

# 치명률 계산
def calculate_critical_rate(conf, death, pre_conf, pre_death):
    numerator = death - pre_death      # numerator : 분자
    denominator = conf - pre_conf      # denominator : 분모
    fraction = round((numerator / denominator)*100, 2)
    return fraction



check_day = datetime.today()
check_day = str(check_day)[:10]
check_day = "".join(check_day.split("-"))    # 2020-04-14 -> 20200414       


# 2020년 1월 20일부터 DB에 넣는 날까지를 param으로 넣어줌

add_data("20200120", "20211115")