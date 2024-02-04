# ISS Tracker App

This Python application is part of my 33rd day of the 100 Days of Code challenge, the tracker will send a email notifications when the International Space Station (ISS) is passing overhead during nighttime in your location.

## Features

- **ISS Location Verification:** The app checks the current location of the ISS using the [Open Notify API](http://api.open-notify.org/iss-now.json).
  
- **Nighttime Verification:** It also verifies if it's currently nighttime in your location using the [Sunrise-Sunset API](https://api.sunrise-sunset.org/json).

- **Email Notification:** If the ISS is overhead during nighttime, the app sends you an email alerting you to look up at the sky.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Requests library (`pip3 install requests`)
