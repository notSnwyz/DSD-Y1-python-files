import requests

def get_location(place_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": place_name,
        "count": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error contacting geocoding API.")
        return None

    data = response.json()

    if "results" not in data:
        return None

    return data["results"][0]

def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error contacting weather API.")
        return None

    return response.json()

def main():

    while True:
        place = input("Enter a place name (or 'quit'): ")

        if place.lower() == "quit":
            print("Exiting program.")
            break

        location = get_location(place)

        if location is None:
            print("Location not found.\n")
            continue

        name = location["name"]
        country = location.get("country", "Unknown")
        latitude = location["latitude"]
        longitude = location["longitude"]

        print(f"\nPlace: {name}, {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

        weather = get_weather(latitude, longitude)

        if weather is None:
            continue

        # Current hourly temperature
        time = weather["hourly"]["time"][0]
        temperature = weather["hourly"]["temperature_2m"][0]

        # Daily forecast
        max_temp = weather["daily"]["temperature_2m_max"][0]
        min_temp = weather["daily"]["temperature_2m_min"][0]

        print("\nWeather Forecast:")
        print(f"Current Time: {time}")
        print(f"Current Temperature: {temperature}°C")
        print(f"Today's Max Temperature: {max_temp}°C")
        print(f"Today's Min Temperature: {min_temp}°C\n")


if __name__ == "__main__":
    main()