import requests,time,webbrowser
from datetime import date,timedelta


tomDate = date.today() + timedelta(days=+1)
print(tomDate)


headers = {

    'Host': 'www.walgreens.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'X-XSRF-TOKEN': 'm7enA1V0vKcyFw==.BcEZl25wsh116gFzqCv47Zkwq1+b8gCAHVzUlSprXcU=',
    'Content-Length': '147',
    'Origin': 'https://www.walgreens.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'Cookie': 'XSRF-TOKEN=qWmGlJwuLKcmvA==.1HigFWN7LsOf/JD/IgpoL3B/NYrmMCDu3bDZE3EjXhU=;',
    'TE': 'Trailers'
    }

url = 'https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability'

postData = {
    "serviceId":"99",
    "position":{"latitude":34.058506,"longitude":-84.521874},
    "appointmentAvailability":{"startDateTime":str(tomDate)},
    "radius":25
    }



while True:


    try:
        response = requests.post(url, headers=headers, timeout=60, json=postData)
    except:
        print("error with response")

        
    try:
        wags = response.json()
    except:
        print("Error with response")
        break

    if wags['appointmentsAvailable'] == True:

        ## appointments are available, open browser
        webbrowser.open('https://www.walgreens.com/findcare/vaccination/covid-19/location-screening', new=0, autoraise=True)
        break
        
    time.sleep(600)


