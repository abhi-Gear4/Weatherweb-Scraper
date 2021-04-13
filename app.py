import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=31.46273304600004&lon=-99.33305008999997#.YHTgwohKhPY')

soup = BeautifulSoup(page.content,'html.parser')
weather_week = soup.find(id = 'seven-day-forecast-list')
items = weather_week.findAll(class_='tombstone-container')
period = ([item.find(class_='period-name').get_text() for item in items])
decription = ([decrip.find(class_='short-desc').get_text() for decrip in items])
temp = ([temp.find(class_='temp').get_text() for temp in items])

weather_report = pd.DataFrame(
    {
        'period':period,
        'descrip':decription,
        'temperature':temp,
    }
)
print(weather_report)

weather_report.to_csv('report.csv')
