# OpenWindow v1.0

### Inspiration
This project was inspired by my need to know when the weather is below 69 degrees so I can be informed when I should open my window and save on my electric bill.

### Overview
Using OpenWeather API to pull weather data for a user-specified location.

User-supplied location input is verified with the master location index provided by OpenWeather. 

### Dependencies
- `requests` via https://pypi.org/project/requests
  - if you don't have it -> `pip install requests`
- an API key from https://openweathermap.org/
  - it should be free
  - API doc -> https://openweathermap.org/current

### TODO
- Implement logic to understand the API response and report directly to the user if the window should be open.
- Test the location verifier for robustness.
