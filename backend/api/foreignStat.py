# Hannah Ritchie, Edouard Mathieu, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Esteban Ortiz-Ospina, Joe Hasell, Bobbie Macdonald, Diana Beltekian and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]
import requests
import json
import pandas as pd


def getForeignStat():
    # 데이터 받아오기
    response = requests.get(
        "https://covid.ourworldindata.org/data/owid-covid-data.json")
    death_json = json.loads(response.text)
    # 오늘에 대한 인덱스
    today = -1

    # 필요자료만을 받을 데이터프레임
    data_needed = pd.DataFrame(
        columns=["country", "today_total_case", "past_total_case", "today_death", "past_death", "chimyong", "vaccinated_percent"])
    countries = death_json.keys()

    # 자료 받기
    for country in countries:
        temp = death_json.get(country)
        # 국가 이름
        temp_name = temp['location']
        # 해당 날짜
        try:
            temp_today = temp.get("data")[today]['date']
        except:
            temp_today = "NA"
        # 오늘 총 확진자
        try:
            temp_today_total = temp.get("data")[today]['total_cases']
        except:
            temp_today_total = "NA"
        # 15일 전 총 확진자
        try:
            temp_past_total = temp.get("data")[today-15]['total_cases']
        except:
            temp_past_total = "NA"
        # 오늘 총 사망자
        try:
            temp_today_death = temp.get("data")[today]['total_deaths']
        except:
            temp_today_death = "NA"
        # 15일 전 총 사망자
        try:
            temp_past_death = temp.get("data")[today-15]['total_deaths']
        except:
            temp_past_death = "NA"
        # 오늘 백신 접종률
        for i in range(today, -32, -1):
            try:
                temp_vacc = temp.get(
                    "data")[i]['people_fully_vaccinated_per_hundred']
            except:
                temp_vacc = "NA"
            if(type(temp_vacc) == float):
                # print("!성공!{0}--{1}--{2}".format(temp_vacc, temp_name, i))
                break

        # 치명률 계산
        if((temp_today_total != "NA") and (temp_past_total != "NA") and (temp_today_death != "NA") and (temp_past_death != "NA")):
            temp_chimyong = (temp_today_death-temp_past_death) / \
                (temp_today_total-temp_past_total+1) * 100
        else:
            temp_chimyong = "NA"
        temp_array = pd.Series(
            [temp_name, temp_today_total, temp_past_total, temp_today_death, temp_past_death, temp_chimyong, temp_vacc], index=data_needed.columns)
        data_needed = data_needed.append(temp_array, ignore_index=True)

    # data_needed.to_excel('ForeignData.xlsx')
    to_drop = data_needed[data_needed['chimyong'] == "NA"].index
    data_needed = data_needed.drop(to_drop)
    data_needed = data_needed.sort_values(
        by=['chimyong'], axis=0, ascending=False)

    return data_needed
