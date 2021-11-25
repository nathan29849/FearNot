from django.db import models

# Create your models here.
class Calc(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    rate = models.FloatField()
    count = models.IntegerField()



"""
치명률 계산식
(당일까지 사망자 수 - 15일 전까지 사망자 수) / (당일까지 감염자 수 - 15일 전까지 감염자 수)

first : ~ 40세 미만
second : 40세 이상 ~ 70세 미만
third : 70세 이상
"""


class TotalData(models.Model):
    date = models.DateField(auto_now = False, auto_now_add=False)
    total_conf = models.IntegerField()                  # 총 감염자 수 
    total_death_toll = models.IntegerField()            # 총 사망자 수
    day_conf = models.IntegerField()                    # 당일 감염자 수
    day_death = models.IntegerField()                   # 당일 사망자 수
    total_critical_rate = models.FloatField(null=True)  # 치명률 
    first_death = models.IntegerField()                 # 연령별로도 그날의 치명률 제공
    first_conf = models.IntegerField()     
    first_ciritical_rate = models.FloatField(null=True)
    second_death = models.IntegerField()    
    second_conf = models.IntegerField() 
    second_ciritical_rate = models.FloatField(null=True)
    third_death = models.IntegerField()     
    third_conf = models.IntegerField()
    third_ciritical_rate = models.FloatField(null=True)
