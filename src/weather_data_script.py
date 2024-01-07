#import debugpy
#debugpy.listen(("0.0.0.0", 5678))

import os
import numpy as np
import pandas as pd
from python_weather import Client
import pytest
import asyncio

glb_CITY = "Pforzheim"

async def async_get_weather_data(city: str)->dict:
    """
    Get dict containing latest available weather data for a single datetime
    """

    # Declare the client. The measuring unit used defaults to the imperial system (Fahrenheit, mph, etc.)
    async with Client() as client:
        # Fetch weather data for a city (replace 'City' with your desired location)
        weather = await client.get(city)

        # Extract relevant weather information
        weather_data = {
            "date": weather.current.date.strftime("%Y/%m/%d"),
            "time": weather.current.date.strftime("%H:%M"),
            "temperature": weather.current.temperature,
            "description": weather.current.description,
            "precipitation": weather.current.precipitation,
            "speed_of_wind": weather.current.wind_speed,
            "location": weather.nearest_area.name
        }

        return weather_data

def get_weather_data(city: str)->dict:
    """
    Get dict containing latest available weather data for a single datetime
    """

    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Run the asynchronous function to get weather data
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_get_weather_data(city))

def main():

    print(get_weather_data(glb_CITY))

if __name__ == '__main__':
    main()
    