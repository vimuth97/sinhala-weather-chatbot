# weather-chatbot

### This is a simple weather chatbot built using RASA in Sinhala language.

## Requirements
* RASA 2.8.7v
* Anaconda 4.10.3
* python 3.8
* Tensorflow 2.3.4
* ujson 4.0.2

## How to run the project
1. Insall RASA in an Anaconda environment
    - refer [this video](https://www.youtube.com/watch?v=GlR60CvTh8A) if you are using Windows 10
2. Clone this repository to your local machine
3. Go to root folder and run `rasa train`
4. Run `rasa run actions` on a separate terminal
5. Run `rasa shell` to chat with the bot in the terminal or run `rasa run --enable-api --cors="*"` to chat on a browser with the UI
6. Run `python -m http.server` to start a http server
7. Visit [http://localhost:8000/](http://localhost:8000/) on your browser
8. Chat with Sinhala Weather Chatbot and enjoy

## What you can ask
* General weather conditions for a specific location and a given date(3 previous days, current date and 3 upcoming days)
    - Location can be either a district or a province in Sri Lanka
    - Date can be in formats - mm/dd or mm-dd
* Specific weather information like rainfall, wind speed or humidity
    - Date and location are required
* Weather summary of the whole country for a given date
    - If this query is followed by one of above queries date will be assumed to be the same unless specified
    - Date is required otherwise
* Refer `data/sample_messages.yml` to look at sample messages you can enter for each intent

N.B. - The returned weather information are available at `dummy_data/data.py`. No API was connected to recieve real time data because this project focuses on functionality of the chatbot.

<br>

## Useful commands

* `conda install -c [channel_name] [package_name]` - install a package using anaconda
* `rasa init` - initiate rasa project 
* `rasa train` - train new model on nlu data stories
* `rasa shell` - load most recently trained model on command line
* `rasa interactive` - load most recently trained model on interactive mode
* `rasa run` -  start a new server with the trained model
* `rasa run actions` - run actions on a server
* `rasa run --enable-api --cors="*"` - run server allow API and all CORS

* `python -m http.server` - start a basic http server

## Further reading

* For additional help refer RASA [documentations](https://rasa.com/docs/)
* The UI was build by [scalableminds](https://github.com/scalableminds/chatroom)
