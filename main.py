# Get you API KEY From https://www.weatherapi.com/
# Just Sign Up and Generate your secret API_Key
# Copy it paste it in the line 8 String in the place of API Key
import requests
import json
print("\nWelcome to Abdullah Bin Usman's Weather APP")
while True:
    api_key = "Your API Key"
    try:
        city = input("Enter the name of your City: ")
        if city.lower() == "exit":
            if LocationDict["current"]["is_day"] == 1:
                print("Have nice day!")
            else:
                print("Sweet dreams!")
            break
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}={city}"
        r = requests.get(url)
        LocationDict = json.loads(r.text)
        print("\n----------------------------------------------")
        print(LocationDict["location"]["name"], ",", LocationDict["location"]["region"], ",",
              LocationDict["location"]["country"])
        print(LocationDict["location"]["localtime"])
        print(LocationDict["current"]["temp_c"], "Degree Celsius")
        print("Status:", LocationDict["current"]["condition"]["text"])
        print("Feels Like:", LocationDict["current"]["feelslike_c"])
        print("----------------------------------------------\n")
    except:
        print("Invalid City!")
        print("----------------------------------------------")
