## Introduction

CoVbot is a simple and intuitive Whatsapp based chatbot. The main feature of the bot is: 

**It can give you the latest status of COVID-19 in the country of choice in a simple and intuitive way.** 

Additionally, the bot can suggest fun **activities to do AT HOME** such as: 

1) *Suggest a Movie* - A movie to watch from the Top 10 movies list, with a short overview of the plot and duration. Since this list is not hard coded in software this will always give you the latest updates based on current trends. 

2) *Suggest a TV Show* - A tv show to watch from the most popular TV shows, with a short overview of the plot and ratings. Since this list is not hard coded in software this will always give you the latest updates based on current trends. 

3) *Suggest a Book* - A book to read from the Top 10 Book list, with the blurb and cover image of the book. 

4) *Daily workouts* - This is a video based on a 7 day workout schedule provided by CRANK gym on their Instagram Account. 

Checkout my post for the Twilio Hackathon [here](https://dev.to/ajhabuawala/covbot-a-simple-whatsapp-chatbot-4fhn)

## Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=_5d5K91jMKA" target="_blank"><img src="http://img.youtube.com/vi/_5d5K91jMKA?t=6" alt="VIDEO TO DEMO" width="240" height="180" border="10" /></a>

## Try it yourself

To begin testing, connect to your sandbox by sending a WhatsApp message from your device to +1 415 523 8886 with code **join problem-carried**.

Then say **Hi** and see the magic happen!!

DISCLAIMER: I host this server on my local computer, so this will only work till 4th of May 2020 and then will be disabled


## Make it yourself

### Twilio 

Follow the twilio quickstart guide to get whatsapp and sandbox working 

[Twilio Website](https://www.twilio.com/console/sms/whatsapp/learn)

### Backend Server
The project requires Python >= 3.6 and Pip (Using version 20.0.2) already to be installed

1) Clone repositery

``` git clone ajhabuawala/CoVbot . ```

2) Install the required libraries

Automatic

```pip install -r requirments.txt ```

OR

Manually PIP install the Python library's in requirements.txt

2) After the libraries have been installed you need to get an API keys from the following webistes:

[COVID-19 data](https://rapidapi.com/Gramzivi/api/covid-19-data)

[TMDB API for Movies and TV Shows details](https://www.themoviedb.org/)

Also the session key for the flask session needs to be generated:

```python
python -c 'import os; print(os.urandom(16))'
```

Then in the src dir of the project, create a config.py file and put this data in it:

```
session_key = <REPLACE WITH GENERATED SESSION KEY >
api_key = < THIS IS THE API KEY YOU GET FROM TMDB >
rapid_api_key = < THIS IS THE API KEY YOU GET FROM COVID-19 DATA API >

```

3) Then it times to run the 

``` python src/server_main.py ```

This starts a server on localhost:5000, in order to allow Twilio to access the server we need to use ngrok

Follow the steps on this [website](https://ngrok.com/download) to install and start ngrok (remember to start on port 5000)

Put the ngrok public ip like this

```
<ngrok_address>/sms
```

in the Sandbox configuration on the twilio [website](https://www.twilio.com/console/sms/whatsapp/sandbox)


Then you are all set !

Just send a **Hi** message to your sandbox number and see the magic happen
