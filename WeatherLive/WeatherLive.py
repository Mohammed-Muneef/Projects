from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


def weather(city):
    res = requests.get(f'https://www.google.com/search?q=weather+{city}', headers=headers)
    print("Search in progress...")
    soup = BeautifulSoup(res.text, 'lxml')
    
    location = soup.find("span", {"class": "BBwThe"})
    time = soup.find("div", {"class": "wob_dts"})
    info = soup.find("span", {"id": "wob_dc"})
    weather = soup.find("span", {"id": "wob_tm"})
    
    print(location.get_text())
    print(time.get_text())
    print(info.get_text())
    print(weather.get_text(),"'c")

print("enter the city name")
city=input()
weather(city)


