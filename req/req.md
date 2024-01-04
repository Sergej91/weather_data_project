# Requirements

## Table of Contents
1. [Specification Overview](#specification-overview)
2. [Tools](#tools)
3. [Abbreviations and Names](#abbreviations-and-names)
4. [System Requirements](#system-requirements)
5. [Software Requirements](#software-requirements)
   1. [src_weather](#src_weather)

## 1. Specification Overview <a name="specification-overview"></a>

|                   |
|-------------------|
| Training and demonstration project for beginner-level automation, Docker, and MongoDB. |
| SW collects weather data from the internet and writes the data to the database. |
| SW gets and writes weather data history if available. |
| The database can be viewed in a UI. |

## 2. Tools <a name="tools"></a>

| Tool                  | Purpose                               |
|-----------------------|---------------------------------------|
| Python                | Scripts for data collection and writing to the database |
| python-weather        | Python package for getting weather data       |
| pytest                | Unit and functional testing           |  
| Docker                | Containerization platform             |
| MongoDB               | Database                        |

## 3. Abbreviations and Names <a name="abbreviations-and-names"></a>

|                       |                                                                       |
|-----------------------|-----------------------------------------------------------------------|
| SW      | Software, can also be an independent script                             |
| scr_weather | Script for collection and writing to the database of weather data |
| db         | (MongoDB) database                                                   |

## 4. System Requirements <a name="system-requirements"></a>

|                                                                                              |
|----------------------------------------------------------------------------------------------|
| scr_weather gets and writes weather information to the db every minute |
| Weather information contains: date, time, temperature, state of rain, state of cloudiness, speed of wind <a name="req_weather_info"></a>|
| scr_weather deployed in a Docker container with internet access |
| db deployed in a Docker container |
| db accessible via username and password |
| mongo express runs in a Docker container and is connected to the db |

## 5. Software Requirements <a name="software-requirements"></a>

### 5.1 src_weather <a name="src_weather"></a>

|                                                              |
|--------------------------------------------------------------|
| Failed data retrieval and errors, including exceptions, are logged |
| All exceptions handled. The script does not throw unhandled exceptions |
| [Weather information requirement](#req_weather_info) |
