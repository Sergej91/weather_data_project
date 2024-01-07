"""
Unit and functionality tests
"""

import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.weather_data_script import get_weather_data

def test_print_weather_data():

    data = get_weather_data("Pforzheim")
    print(data)
