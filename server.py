from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app  = Flask(__name__)

# define routes

# route for index and root
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# route for weather
@app.route('/weather')
def get_weather():
# get city from html
    city = request.args.get('city')

# check for emtpy strings or string with only spaces
    if not bool(city.strip()):
        city = 'Pune'

    weather_data = get_current_weather(city)

# city not found by api
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    

# send data to template
    return  render_template(
        "weather.html",
        title= weather_data['name'],
        status=weather_data['weather'][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )






if __name__ == "__main__":
    serve(app, host='0.0.0.0',port=8000)