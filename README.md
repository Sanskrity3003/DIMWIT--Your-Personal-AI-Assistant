# Dimwit: Your Personal AI Assistant

Dimwit is a personal AI assistant designed to make your life easier by providing a variety of functionalities. It can perform tasks such as web searches, telling jokes, fetching COVID-19 statistics, providing weather updates, and much more. Dimwit utilizes several Python libraries to achieve these tasks, including speech recognition, text-to-speech, and web scraping.

## Features

- **Voice Interaction**: Dimwit can take voice commands and respond using text-to-speech.
- **Web Searches**: Perform web searches on Wikipedia and open various websites like YouTube, Google, etc.
- **COVID-19 Statistics**: Get up-to-date COVID-19 statistics for any country.
- **Weather Updates**: Fetch current weather information for any city.
- **Time and Date**: Tell the current time and date.
- **Jokes**: Listen to jokes to lighten up your mood.
- **System Commands**: Execute system commands like shutdown, restart, hibernate, etc.
- **Notes**: Write and read notes.
- **Country and State Information**: Get information about countries and states, such as their capitals.
- **Personal Interaction**: Dimwit can greet you and engage in basic personal interaction.

## Requirements

Before running Dimwit, ensure you have the following libraries installed:

```bash
pip install webbrowser pyttsx3 speech_recognition wikipedia smtplib pyjokes requests beautifulsoup4 wolframalpha countryinfo feedparser
```
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/dimwit-assistant.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd dimwit-assistant
    ```
3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the assistant, simply run the main script:

```bash
python dimwit.py
```
## Main Functions

- **`wishme()`**: Greets the user based on the time of the day.
- **`speak(audio)`**: Converts text to speech.
- **`takeCommand()`**: Listens to user commands and returns them as text.
- **`main_screen()`**: Sets up the main GUI for Dimwit.
- **`assistantname()`**: Introduces the assistant.
- **`get_info(country_name)`**: Fetches COVID-19 statistics for the specified country.
- **`username()`**: Asks for and stores the user's name.

## Voice Commands

- **Wikipedia**: `search wikipedia [topic]`
- **Open Websites**: `open youtube`, `open google`, `open lms`, etc.
- **Time**: `the time`
- **Jokes**: `tell me a joke`
- **Weather**: `weather [city name]`
- **COVID-19 Statistics**: `covid cases`
- **Country Information**: `capital of [country]`
- **State Information**: `capital of [state]`
- **Shutdown**: `shutdown system`
- **Restart**: `restart`
- **Hibernate**: `hibernate`
- **Notes**: `write a note`, `show note`
- **Personal Interaction**: `how are you`, `who made you`, `what is love`, etc.


## Contributions

Feel free to fork this repository and contribute to Dimwit's development. Pull requests are welcome.


## License

This project is licensed under [MIT](https://choosealicense.com/licenses/mit/) license.


