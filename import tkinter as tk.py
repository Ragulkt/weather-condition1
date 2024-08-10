import tkinter as tk
import requests # type: ignore
from datetime import datetime

def getweather(event=None):
    city = textfield.get()
    api_key = "a0bc2dd31ea051eada6a876553e9e29d"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = requests.get(api).json()
    if json_data.get('cod') != 200:
        label1.config(text="City not found")
        label2.config(text="")
        return

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = datetime.utcfromtimestamp(json_data['sys']['sunrise']).strftime("%I:%M:%S")
    sunset = datetime.utcfromtimestamp(json_data['sys']['sunset']).strftime("%I:%M:%S")

    final_info = f"\n{temp}°C"
    final_data = (f"\nMax Temp: {max_temp}°C\n"
                  f"Min Temp: {min_temp}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind} m/s\n"
                  f"Sunrise: {sunrise}\n"
                  f"Sunset: {sunset}")
    
    label1.config(text=final_info)
    label2.config(text=final_data)

# Initialize the main window
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Create and pack widgets
textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

# Run the application
canvas.mainloop()