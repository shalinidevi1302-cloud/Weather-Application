#  AI Weather Assistant

##  Overview

**AI Weather Assistant** is a Python-based weather application developed using **Streamlit**. It allows users to search for a city and view its current weather information in a simple and interactive interface.

The application uses the **Open-Meteo API** to retrieve real-time weather data and the **Open-Meteo Geocoding API** to identify the location entered by the user.

Users can view important weather details such as temperature, feels-like temperature, humidity, wind speed, precipitation, and weather conditions.

---

##  Objectives

* To develop a simple and interactive weather application.
* To provide real-time weather information for different cities.
* To retrieve location details using geocoding.
* To display weather information in an easy-to-understand format.
* To understand API integration using Python.
* To provide a user-friendly interface using Streamlit.

---

## ✨ Features

* 🔍 Search weather information by city name
* 🌡️ Display current temperature
* 🤗 Display feels-like temperature
* 💧 Show humidity
* 💨 Display wind speed
* 🌧️ Show precipitation information
* ☁️ Display current weather conditions
* 🌍 Support weather search for different locations
* ⚡ Retrieve real-time weather data
* 🖥️ Simple and interactive Streamlit interface
* 🔑 No API key required
* ⚠️ Handles invalid or unavailable city names

---

## Technologies Used

* **Python** – Application development
* **Streamlit** – Web application interface
* **Requests** – API communication
* **Open-Meteo API** – Weather data
* **Open-Meteo Geocoding API** – Location search

---

##  Project Structure

```text
AI-Weather-Assistant/
│
├── app.py
├── weather_functions.py
├── requirements.txt
└── README.md
```

### File Description

| File                   | Description                                |
| ---------------------- | ------------------------------------------ |
| `app.py`               | Main Streamlit application                 |
| `weather_functions.py` | Contains weather and API-related functions |
| `requirements.txt`     | Required Python libraries                  |
| `README.md`            | Project documentation                      |

---

## How It Works

The application follows these steps:

1. The user enters a **city name**.
2. The application sends the city name to the **Open-Meteo Geocoding API**.
3. The API returns the **latitude and longitude** of the location.
4. These coordinates are used to request weather information.
5. The **Open-Meteo Weather API** provides the current weather data.
6. The application processes the received data.
7. The weather information is displayed through the Streamlit interface.

###  Workflow

```text
User enters City
       ↓
Open-Meteo Geocoding API
       ↓
Latitude & Longitude
       ↓
Open-Meteo Weather API
       ↓
Weather Data
       ↓
Python Processing
       ↓
Streamlit Interface
       ↓
Weather Information
```

---

##  API Used

This project uses the **Open-Meteo API** to retrieve weather information.

It also uses the **Open-Meteo Geocoding API** to convert a city name into geographic coordinates.

### Advantages of Open-Meteo

* No API key required
* Easy to integrate
* Provides weather data for many locations
* Suitable for educational projects
* Supports current and forecast weather information

---

##  Weather Information Displayed

The application can display:

| Weather Parameter | Description                                   |
| ----------------- | --------------------------------------------- |
| Temperature       | Current temperature of the selected location  |
| Feels Like        | Approximate temperature experienced by people |
| Humidity          | Amount of moisture in the air                 |
| Wind Speed        | Current wind speed                            |
| Precipitation     | Current precipitation information             |
| Weather Condition | Current weather status                        |

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Weather-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Weather-Assistant
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

##  Requirements

The `requirements.txt` file contains the required Python packages:

```text
streamlit
requests
```

---

##  Running the Application

Run the following command in the project folder:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

##  Example

The application provides a simple interface where users can enter a city name and view its current weather information.

**Example Input:**

```text
Chennai
```

**Example Output:**

```text
Temperature: 30°C
Feels Like: 33°C
Humidity: 70%
Wind Speed: 12 km/h
Precipitation: 0 mm
Condition: Clear
```

---

##  Error Handling

The application can handle common situations such as:

* Invalid city names
* Empty search input
* City not found
* API request errors
* Internet connection issues
* Missing weather information

This helps provide a better user experience.

---

##  Use Cases

The AI Weather Assistant can be useful for:

* Checking current weather conditions
* Planning outdoor activities
* Learning API integration
* Understanding real-time data processing
* Demonstrating Python and Streamlit projects
* Educational and academic projects

---

##  Benefits

* Easy to use
* Simple user interface
* Real-time weather information
* No API key required
* Lightweight application
* Easy to modify and extend
* Beginner-friendly Python project
* Demonstrates real-world API usage

---

##  Future Improvements

The project can be enhanced by adding:

* 📅 7-day weather forecasts
* ⏰ Hourly weather information
* 🌅 Sunrise and sunset times
* 🌡️ Minimum and maximum temperature
* 🌧️ Weather icons
* 📍 Automatic location detection
* 🌍 Multiple-city weather comparison
* 📈 Weather data visualization
* 🎤 Voice-based weather queries
* 💬 Natural-language weather questions
* 🔔 Weather alerts and notifications
* 🤖 AI-based weather summaries
* 📱 Improved mobile-friendly interface
* 🗺️ Interactive weather maps

---

## Future Scope

In future versions, the application can be transformed into a more intelligent **AI-powered weather assistant**.

Users could ask natural-language questions such as:

```text
"Will it rain today in Chennai?"

"What is the temperature tomorrow?"

"Is it suitable for an outdoor activity today?"
```

The system could analyze the weather data and provide a simple natural-language response.

---

##  Learning Outcomes

Through this project, the following concepts can be learned:

* Python programming
* Streamlit application development
* REST API integration
* HTTP requests
* JSON data handling
* Geocoding
* Real-time data retrieval
* Data processing
* User input handling
* Error handling
* Basic web application development

---

##  Conclusion

**AI Weather Assistant** is a simple and interactive weather application that demonstrates how Python, Streamlit, and APIs can be combined to create a real-world application.

The project provides users with current weather information while also serving as a practical example of **API integration, data processing, and web application development using Python**.
