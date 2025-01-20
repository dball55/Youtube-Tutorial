#Python Telegram Bot V2

from dotenv import load_dotenv
import os
import requests
import telebot

load_dotenv()
api_key = os.getenv("api_key")
print("API Key:", api_key)
if not api_key:
    raise ValueError("API key is not set in the .env file or environment variables.")
bot = telebot.TeleBot(api_key)
to_do_list = []

#Weather Data Collection Function
def get_location_from_ip():
    response = requests.get("https://ipinfo.io/")
    data_0 = response.json()
    print(data_0)
    location = data_0.get("region")  
    if location:
        print(location)
        return location
    else:
        print("Location not found!")

def get_weather(location):
    api_key_weather = "cf11bd064808492c96bce2fed7fb05b1"
    print(f"You retreived weather data for {location}")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key_weather}"
    response = requests.get(url)
    data_1 = response.json()
    print(data_1)
    if response.status_code != 200:
        response.raise_for_status()
    return data_1

def format_weather_message(data_1):
    temperature_k = data_1["main"]["temp"]
    temperature_c = temperature_k - 273.15
    weather_id = data_1["weather"][0]["id"]
    weather_description = data_1["weather"][0]["description"]
    return temperature_c, weather_description


@bot.message_handler(commands = ["start", "hello", "fatty"])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello, what would you like to do?\n"
                 "1. View today's weather\n"
                 "2. View To-Do List\n"
                 "3. Add to To-Do List\n"
                 "4. Remove activity from list")

@bot.message_handler(func = lambda message: message.text == "1")
def give_weather(message):
    bot.reply_to(message, "Here is the weather for today!")
    location = get_location_from_ip()
    weather_data = get_weather(location)
    temperature_c, weather_description = format_weather_message(weather_data)
             
    bot.reply_to(message,
                 f"Here are the weather conditions for today in {location}:\n"
                 f"Temperature: {temperature_c:.2f}°C\n"
                 f"Description: {weather_description}")
    send_welcome(message)


@bot.message_handler(func = lambda message: message.text == "2")
def handle_view_list(message):
    if to_do_list:
        bot.reply_to(message,"Here's your To-Do List:\n" + "\n".join(f"{i + 1}. {item}" for i, item in enumerate(to_do_list)))
    else:
        bot.reply_to(message, "Your To-Do List is empty.")
    send_welcome(message)

@bot.message_handler(func = lambda message: message.text == "3")
def handle_add_to_list(message):
    msg = bot.reply_to(message, "Type in the activity you would like to add:")
    bot.register_next_step_handler(msg, add_to_list)
def add_to_list(message):
    to_do_list.append(message.text)
    bot.reply_to(message, f"Added to your To-Do List: {message.text}")
    send_welcome(message)

@bot.message_handler(func = lambda message: message.text == "4")
def handle_remove_from_list(message):
    if not to_do_list:
        bot.reply_to(message, "Your To-Do List is empty. Nothing to remove.")
        send_welcome(message)
    else:
        msg = bot.reply_to(message,"Which activity would you like to remove? Send the number of the activity.")
        bot.register_next_step_handler(msg, remove_from_list)

def remove_from_list(message):
    try:
        index = int(message.text) - 1
        if 0 <= index < len(to_do_list):
            removed_item = to_do_list.pop(index)
            bot.reply_to(message, f"Removed from your To-Do List: {removed_item}")
        else:
            bot.reply_to(message, "Invalid number. Please try again.")
    except ValueError:
        bot.reply_to(message, "Please send a valid number.")
    send_welcome(message)

bot.polling()
