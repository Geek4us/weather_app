import spacy
import requests

nlp = spacy.load("en_core_web_md")

def chatbot(statement):
  weather = nlp("Current weather in a city")
  statement = nlp(statement)

api_key ="b5cee0f97c79c8ded4453b1e7872511e"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    
    response = requests.get(api_url)
    response_dict = response.json()
    
    weather = response_dict["weather"][0]["description"]
    
    if response.status_code == 200:
        return weather
    
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        
        return None
            
# end def

def chatbot(statement):
    weather = nlp("current weather in the city")
    statement = nlp(statement)
    min_similarity = 0.75
    
    if weather.similarity(statement) >= min_similarity:
        for ent in statement.ents:
            if ent.label_ == "GPE": # GeoPolitical Entity
                city = ent.text
            break
        else:
            return "You need to tell me a city to check."
        
        response = chatbot("Is it going to rain in Rome today?")
        print(response)
    """
    Purpose: 
    """
    
# end def