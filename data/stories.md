
## grow businsess happy path
* greet
  - action_greet_user
* business_help
  - utter_quarter_report
* accepted
  - utter_report_display
  - utter_to_see_each_customer
* accepted
  - action_search_next_customer
  - utter_close_search_customer
* ignore
  - action_search_next_customer
  - utter_close_search_customer

## grow businsess rejected path
* greet
 - action_greet_user
* business_help
  - utter_quarter_report
* rejected
  - utter_to_see_each_customer
* rejected
  - utter_close_search_customer
* I_am_done
  - utter_goodbye_seek_help

## grow businsess accept no and done
* greet
  - action_greet_user
* business_help
  - utter_quarter_report
* rejected
  - utter_to_see_each_customer
* rejected
  - utter_to_done_or_continue
* Continue
  - utter_to_see_each_customer

## fallback story
* out_of_scope
  - action_default_fallback