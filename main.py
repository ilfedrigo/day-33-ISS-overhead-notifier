import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -15.826691
MY_LNG = -47.921822
MY_EMAIL = "ilfedrigo.python.100days@gmail.com"
MY_PASSWORD = "ioqr rpwy jwdu xzig"

def is_iss_overhead():
    current_location = requests.get(url="http://api.open-notify.org/iss-now.json")
    current_location.raise_for_status()
    iss_data = current_location.json()

    latitude = float(iss_data["iss_position"]["latitude"])
    longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    my_data = response.json()
    sunrise = int(my_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(my_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
     time.sleep(60)
     if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                        from_addr=MY_EMAIL, 
                        to_addrs=MY_PASSWORD["email"], 
                        msg=f"Subject:Look up! ISS is Overhead!\n\nYou can find ISS on the sky!"
                        )