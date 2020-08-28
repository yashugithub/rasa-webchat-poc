# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

def getLoginUser():
    
    resp = requests.get('http://localhost:5001/cybershield/api/users/me/details')

    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /dashboards/ {}'.format(resp.status_code))
    reponse = resp.json()
    return '{} {}'.format(reponse['firstName'], reponse['lastName'])     

class SearchNextCustomer(Action):
 def name(self):
  """name of the custom action"""
  return "action_search_next_customer"

 def run(self,dispatcher,tracker,domain):
    buttons = []
    
    buttons.append({"payload": "/add_customer", "title": "Shield 8"})
    buttons.append({"payload": "/add_customer", "title": "Shield 9"})
    buttons.append({"payload": "/add_customer", "title": "Shield 10"})

    dispatcher.utter_button_message(text='Add shields to customer ABC', buttons=buttons)
    return []

class ActionGreetingMessage(Action):
 def name(self):
  """name of the custom action"""
  return "action_greet_user"

 def run(self,dispatcher,tracker,domain):
    user = getLoginUser()
    dispatcher.utter_message(text='Hello {}, how can I help you?'.format(user))
    return []
