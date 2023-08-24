import tkinter as tk
import requests
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast")

        self.api_key = "0145ac51a7cf4574e5335a55e4faba8d"  

        self.create_ui()

    def create_ui(self):
        self.city_label = tk.Label(self.root, text="Enter city or zip code:")
        self.city_label.pack()

        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack()

        self.fetch_button = tk.Button(self.root, text="Fetch Weather", command=self.get_weather)
        self.fetch_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()

        if not city:
            messagebox.showerror("Error", "Please enter a city or zip code.")
            return

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if data.get("cod") != 200:
                messagebox.showerror("Error", f"Weather data not found for {city}.")
                return

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_description = data["weather"][0]["description"]

            result_text = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather: {weather_description}"
            self.result_label.config(text=result_text)

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Failed to connect to the server. Check your internet connection.")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
