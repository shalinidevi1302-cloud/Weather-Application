
import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌦️",
    layout="centered"
)

st.title("🌦️ AI Weather Assistant")
st.caption("LLM Function Calling + Open-Meteo Weather API")

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN is not configured. Please add it to your .env file.")
    st.stop()

client = InferenceClient(
    api_key=HF_TOKEN
)

MODEL = "Qwen/Qwen2.5-72B-Instruct"


def get_weather(city):
    try:
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "format": "json"
            },
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if "results" not in geo_data or not geo_data["results"]:
            return {
                "error": f"Could not find the city '{city}'."
            }

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                "timezone": "auto"
            },
            timeout=10
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()["current"]

        return {
            "city": location["name"],
            "country": location.get("country", ""),
            "temperature": weather_data["temperature_2m"],
            "humidity": weather_data["relative_humidity_2m"],
            "wind_speed": weather_data["wind_speed_10m"]
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Weather service error: {str(e)}"
        }

    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}"
        }


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather information for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


def ask_weather(question):

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI weather assistant. "
                "For weather-related questions, use the get_weather tool. "
                "Do not guess current weather information."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if not message.tool_calls:
        return message.content, None

    messages.append({
        "role": "assistant",
        "content": message.content,
        "tool_calls": [
            {
                "id": tool.id,
                "type": "function",
                "function": {
                    "name": tool.function.name,
                    "arguments": tool.function.arguments
                }
            }
            for tool in message.tool_calls
        ]
    })

    tool_result = None

    for tool in message.tool_calls:

        if tool.function.name == "get_weather":

            arguments = json.loads(
                tool.function.arguments
            )

            city = arguments["city"]

            tool_result = get_weather(city)

            messages.append({
                "role": "tool",
                "tool_call_id": tool.id,
                "name": "get_weather",
                "content": json.dumps(tool_result)
            })

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return final_response.choices[0].message.content, tool_result


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input(
    "Ask about the weather in any city..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Checking weather..."):

            try:

                answer, weather_data = ask_weather(question)

                st.markdown(answer)

                if weather_data and "error" not in weather_data:

                    st.divider()

                    st.subheader("🌡️ Weather Details")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "Temperature",
                            f"{weather_data['temperature']} °C"
                        )

                    with col2:
                        st.metric(
                            "Humidity",
                            f"{weather_data['humidity']}%"
                        )

                    with col3:
                        st.metric(
                            "Wind Speed",
                            f"{weather_data['wind_speed']} km/h"
                        )

                    location = weather_data["city"]

                    if weather_data["country"]:
                        location += f", {weather_data['country']}"

                    st.caption(
                        f"📍 Location: {location}"
                    )

                elif weather_data and "error" in weather_data:

                    st.error(weather_data["error"])

            except Exception as e:

                answer = (
                    "Sorry, I couldn't process your weather request."
                )

                st.error(f"Error: {str(e)}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )