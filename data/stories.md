## hospital search happy path
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"dashboard", "widget": "Case Breakdown"}
  - action_facility_search
  - slot{"address":"Case Breakdown is one of the ESM widget"}
* thanks
  - utter_goodbye

## hospital search + location
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"dashboard"}
  - utter_ask_widgets
* inform{"widget":"Case Breakdown"}
  - action_facility_search
  - slot{"address":"Case Breakdown is one of the ESM widget"}
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
