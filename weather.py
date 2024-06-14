# import requests
# import json
# import win32com.client as wincom
# speak = wincom.Dispatch("SAPI.SpVoice")
# city=input("enter the name of the city: ")
# url=f"https://api.weatherapi.com/v1/current.json?key=19912d981fb542f1a9b144959230604&q={city}"
# r=requests.get(url)
# # print(r.text)
# wdic=json.loads(r.text)
# w=wdic["current"]["temp_c"]
# print(f"the current temperature in {city} is {w}°C")
# speak.Speak(f"the current temperature in {city} is {w} degree celcius")


#=======================================================================================
#GEEKS FOR GEEKS CODE
# import required libraries 
import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 
n = ToastNotifier() 

# define a function 
def getdata(url): 
	r = requests.get(url) 
	return r.text 
	
htmldata = getdata("https://weather.com/en-IN/weather/today/l/801b9b59086a78d8fad5a914f5b303e2461ac6f005619b563c1898798551f88e") 

soup = BeautifulSoup(htmldata, 'html.parser') 

#--TEMPERATURE CODE--
current_temp = soup.find_all("span", class_= "CurrentConditions--tempValue--MHmYY") 
if current_temp:
    # Extract the text content and ignores every Html tags surrounding it.
    temperature_value = current_temp[0].get_text()
    # print("temperature_with_symbol: ",temperature_with_symbol)
else:
    print("ERROR! Temperature not found!")

#--RAIN CODE--
chances_rain = soup.find_all("p", class_= "InsightNotification--text--35QdL") 
temp_rain = chances_rain[0].get_text()
# print(temp_rain)

result = "Temp: " + temperature_value + "C in guwahati assam" + "\n" + "Rainfall: " + temp_rain
n.show_toast("live Weather update", 
			result, duration = 10) 

