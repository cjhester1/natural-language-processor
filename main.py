import requests
import config
from datetime import datetime

#Getting today's date
today = datetime.now()
struct_day = today.strftime("%d/%m/%Y")
struct_time = today.strftime("%H:%M %p")

#endpoint for NLP API
natural_language_url = f"{config.BASE_URL}{config.NATURAL_LANGUAGE_ENDPOINT}"
#endpoint for Sheety API
sheety_url = config.URL
#header for NLP
headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY
}

"""
NLP is still in beta stages. Only enter one exercise at a time.
For better experience enter how long you exercised for as well.
"""
#asking user for input what excercise have they completed
exercise_text = input("What exercise have you completed? ")

"""
Natural Language Processing (NLP) Information Extraction (IE) is a process of automatically extracting structured information from unstructured text. 
This typically involves identifying and classifying key pieces of information from text documents. 
The main tasks involved in NLP information extraction include Named Entity Recognition (NER), Relation Extraction, 
and Event Extraction.

Exercise NLP processes the exercise_text looking for keywords. Based on the activity, our BMI and the duration of the activity. NLP determines how many
calories we burned from that activity. Also takes our unstructured info and structures the data with keys in json format.
"""
natural_language_params = {
    "query": exercise_text,
    "gender": config.GENDER,
    "weight_kg": config.WEIGHT_KG,
    "height_cm": config.HEIGHT_CM,
    "age": config.AGE
}


"""

To create a new row in your sheet, perform a POST request to the endpoint, with your row contents as a JSON payload in the request body.

Sheety expects your record to be nested in a singular root property named after your sheet. 
For example if your endpoint is named emails, nest your record in a property called email.
"""
response = requests.post(url=natural_language_url, json=natural_language_params, headers=headers)
data = response.json()
results = data['exercises']
print(results)
for exercise in results:
    user_input = {
        "sheet1": {
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "exercise": exercise["name"],
            "date": struct_day,
            "time": struct_time

        }
    }
    response = requests.post(url=sheety_url,json=user_input)

print(response.text)
