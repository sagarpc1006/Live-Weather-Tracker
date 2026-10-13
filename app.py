import streamlit as st 
from streamlit import *
import requests  

API_KEY='cb40bebfbd2244289b4d5e4441661621'
st.set_page_config(page_title='Weather APP',page_icon='😂')
st.title('Weather APP 🌤️')
st.write('Enter the City name and click the button to fetch weather data')

city = st.text_input('Enter the city name :')
if (st.button('Submit')):
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    data=response.json() # It extracts the json data and converts to dictionary 

    # Extract weather information 
    temperature=data['main']['temp']
    humidity=data['main']['humidity']
    wind_speed=data['wind']['speed']
    weather_condition=data['weather'][0]['description']
    name=data['name']
    country=data['sys']['country']
    st.subheader(f'{country},{city}')

    col1,col2=st.columns(2)
    col3,col4=st.columns(2)

    col1.metric('Temperature🌡️',f'{temperature}°C')
    col2.metric('Humidity💦',f'{humidity}%')
    col3.metric('Wind Speed🍃',f'{wind_speed}m/s')
    col4.metric('Weather Condition🌤️',f'{weather_condition}')
















