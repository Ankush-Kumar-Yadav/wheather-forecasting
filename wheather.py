import tkinter as tk
from tkinter import messagebox
import requests


class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key

        self.root = tk.Tk()
        self.root.title("Weather Forecast App")

        self.city_label = tk.Label(self.root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city.")
            return

        try:
            weather_data = self.fetch_weather_data(city)
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            result_text = f"The current temperature in {city} is {temperature}°C\nDescription: {description}"
            self.result_label.config(text=result_text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve weather data: {str(e)}")

    def fetch_weather_data(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'units': 'metric',
            'appid': self.api_key
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'

    if api_key == 'YOUR_API_KEY':
        print("Please replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.")
    else:
        app = WeatherApp(api_key)
        app.run()
