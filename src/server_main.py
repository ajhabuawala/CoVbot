import config
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from get_covid_data import get_covid_data_by_country
from get_movies_data import get_movie_details
from get_tv_show import get_tv_show_details
from get_workout_for_day import return_work_out
from get_book_details import get_random_book

app = Flask(__name__)
app.secret_key = config.session_key
incomplete_message = False

intro_messages = ['hi', 'hello', 'hey', ]


@app.route("/sms", methods=['POST'])
def incoming_sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None).lower()

    global incomplete_message

    if incomplete_message:
        return _send_country_covid_data(body)


    elif _is_suboption_selected(body):
        return _select_sub_option(body)
    else:
        # Determine the right reply for this message
        if body == '1':
            return _send_get_country_name()
        elif body == '2':
            return _send_quarantine_activity_subset()
        elif body == '3':
            return _send_workout_message()
        elif body == '4':
            return _send_help_message()
        elif body in intro_messages:
            return _send_intro_messages()
        elif body == 'reset':
            return _reset_session_cookie()
        else:
            return _send_option_no_available()


def _send_help_message():
    resp = MessagingResponse()
    resp.message('''I can do the following:
*1.* Status of *COVID 19* in my country
*2.* Suggest a *Quarantine activity*
*3.* Suggest a *Home Workout*
*4.* Ask me what I can do ''')
    return str(resp)


def _send_get_country_name():
    global incomplete_message
    resp = MessagingResponse()
    resp.message('Which country do you live in ? [Full Forms Only]')
    incomplete_message = True
    return str(resp)


def _send_option_no_available():
    resp = MessagingResponse()
    resp.message("""
    ‼️ Please choose a valid option‼️
    """)
    return str(resp)


def _send_country_covid_data(body):
    resp = MessagingResponse()
    global incomplete_message
    try:
        country, confirmed_cases, recovered_cases, deaths = get_covid_data_by_country(body)
    except Exception:
        resp.message(f"""
The country data that you entered is not found !
Maybe you entered a city name or abbreviation. Please type COUNTRY NAME again """)
        return str(resp)
    else:
        incomplete_message = False
        resp.message(f"""
The COVID19 Status in *{country}*
_Confirmed Cases_ : {confirmed_cases}
_Recovered Cases_ : {recovered_cases}
_Deaths_: {deaths} """)
        return str(resp)



def _send_intro_messages():
    resp = MessagingResponse()
    resp.message("""
*Welcome to CoVbot !*

```A simple chatbot that can
give the latest updates of
COVID-19 in a simple, quick
& easy way. Since we are all
quarantined, the bot can be
used to suggest some fun
activities to make the most
of our time at home as we
strive to keep ourselves,
friends and family safe.```

We hope you enjoy it and find it useful!

*Send 4 to get started !*
            """)
    session['sub_options'] = []
    return str(resp)


def _send_quarantine_activity_subset():
    sub_options = ['Movie 🎥',
                   'Book 📚',
                   'TV Show 📺',
                   'Go to the previous menu 🔙',
                   'Exit 🛑']
    session['sub_options'] = sub_options
    resp = MessagingResponse()
    message = [f"""_I can suggest the following_:"""]
    for i, name in enumerate(sub_options, 1):
        message.append("*{}*. for {}".format(i, name))
    resp.message('\n'.join(message))
    return str(resp)


def _is_suboption_selected(body):
    option = session.get('sub_options', [])
    if body.isdigit():
        body = int(body)
        return (body - 1 in range(len(option)))
    return False


def _send_movie_suggestion():
    name, plot, duration = get_movie_details()
    resp = MessagingResponse()
    resp.message(f"""
Here is a nice movie suggestion:
_Movie Title_ : *{name}*
_Movie Plot_  : ```{plot}```
_Movie Duration_ : *{duration}* minutes
            """)
    return str(resp)


def _send_tv_show_suggestion():
    name, plot, rating = get_tv_show_details()
    resp = MessagingResponse()
    resp.message(f"""
Here is a nice TV Show to watch:
_Name_ : *{name}*
_Plot_  : ```{plot}```
_Rating_ : *{rating}* / 10
            """)
    return str(resp)


def _send_book_suggestion():
    name, plot, img = get_random_book()
    resp = MessagingResponse()
    msg = resp.message(f"""
Here is a nice Book to read:
_Title_: *{name}*
_Summary_: ```{plot}```
            """)
    msg.media(img)
    return str(resp)


def _send_workout_message():
    workout = return_work_out()
    resp = MessagingResponse()
    resp.message(f"Here is a work out for today: {workout}")
    return str(resp)


def _select_sub_option(body):
    """docstring for _select_sub_option"""
    option = session['sub_options'][int(body) - 1]
    if option == 'Movie 🎥':
        return _send_movie_suggestion()
    elif option == 'Book 📚':
        return _send_book_suggestion()
    elif option == 'TV Show 📺':
        return _send_tv_show_suggestion()
    elif option == 'Go to the previous menu 🔙':
        session['sub_options'] = []
        return _send_help_message()
    elif option == 'Exit 🛑':
        resp = MessagingResponse()
        resp.message("Bye !")
        session['sub_options'] = []
        return str(resp)


def _reset_session_cookie():
    """docstring for reset_session_cookie"""
    session['sub_options'] = []
    resp = MessagingResponse()
    resp.message('Done')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
