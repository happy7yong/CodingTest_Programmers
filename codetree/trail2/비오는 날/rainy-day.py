import math

n = int(input())
date = [] #날짜
day = [] #요일
weather = [] #날씨

#근시일 내로 비가 오는날

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Weather :
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

class Date :
    def __init__(self,yyyy,mm,dd) :
        self.y = yyyy
        self.m = mm
        self.d = dd

#date분리하는 함수
def dateSplit(date) :
    yyyy,mm,dd = map(int,date.split("-"))
    return yyyy,mm,dd

date_arr = [Date(*dateSplit(date[i])) for i in range(n)]
weather_arr = [ Weather(date_arr[i],day[i],weather[i]) for i in range(n)]

rain_Weather = []

#Rain만 보는데, 날짜 최솟값 구하기
for ele in weather_arr :
    if ele.weather == "Rain" :
        rain_Weather.append(ele)

rain_Weather.sort(key=lambda w : (w.date.y,w.date.m,w.date.d))
rainW = rain_Weather[0]
print(f"{rainW.date.y}-{rainW.date.m:02d}-{rainW.date.d:02d}", rainW.day, rainW.weather)

