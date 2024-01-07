"""
Unit and functionality tests
"""

import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.weather_data_script import get_weather_data

def test_get_weather_data_structure():
    data = get_weather_data("Pforzheim")
    assert isinstance(data, dict)
    assert "date" in data
    assert "time" in data
    assert "temperature" in data
    assert "description" in data
    assert "precipitation" in data
    assert "speed_of_wind" in data
    assert "location" in data

def test_get_weather_data_types():
    data = get_weather_data("Pforzheim")
    assert isinstance(data["date"], str)
    assert isinstance(data["time"], str)
    assert isinstance(data["temperature"], int)
    assert isinstance(data["description"], str)
    assert isinstance(data["precipitation"], float)
    assert isinstance(data["speed_of_wind"], int)
    assert isinstance(data["location"], str)
