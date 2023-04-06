


















# import requests
# import json
# import geocoder
# from twilio.rest import Client

# # # initialize the Google API and AccuWeather API keys
# google_api_key = "ttCJnkzroGsQZsu0iGFAJvczTIPuQZGJ"
# accuweather_api_key = "ttCJnkzroGsQZsu0iGFAJvczTIPuQZGJ"

#  #initialize the Twilio API credentials
# account_sid = "ACace0e78474bace765c1b311d9614ac3f"
# auth_token = "db48b5b334b863f91798449b12fa27b1"
# client = Client(account_sid, auth_token)

# # initialize the advise variable
# advise = ""
# # get the user's location using their IP address
# g = geocoder.ip('me')
# location = ",".join(map(str,g.latlng))
# # ask the user what crop they are farming
# crop = input("What crop are you farming? ")
# # retrieve information about the crop using the Google API
# crop_info_url = f"https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx=005060689417799447664:axvhssjrxwv&q={crop} site:wikipedia.org&num=1"
# crop_info_response = requests.get(crop_info_url)
# crop_info_json = json.loads(crop_info_response.text)
# # check if the response contains a list of search results
# if "items" in crop_info_json:
#     # extract the crop description from the top search result
#     crop_description = crop_info_json["items"][0]["snippet"]
#     print(f"Description of {crop}: {crop_description}")
# else:
#     # handle the case where there are no search results
#     print(f"No search results found for query: {crop_info_url}")
#     crop_description = ""
# # get the current weather conditions for the user's location using the AccuWeather API
# current_conditions_url = f"http://dataservice.accuweather.com/currentconditions/v1/{accuweather_api_key}?q={location}"
# current_conditions_response = requests.get(current_conditions_url)
# current_conditions_json = json.loads(current_conditions_response.text)
# # check if current_conditions_json contains any data
# weather_description = ""
# if current_conditions_json and isinstance(current_conditions_json, list) and len(current_conditions_json) > 0:
#     weather_description = current_conditions_json[0]["WeatherText"]
#     # check if the weather conditions are suitable for the crop
#     if crop_description != "" and weather_description.lower() in crop_description.lower():
#         print(f"The weather conditions are good for growing {crop}.")
#     else:
#         print(f"The weather conditions are not suitable for growing {crop}.")
#         if "rain" in weather_description.lower():
#             advise = f"Wait until the rain stops before growing {crop}"
#         else:
#             advise = f"It would be best to grow {crop} during {weather_description}."
#         print(advise)
# else:
#     print(f"No data was returned for query: {current_conditions_url}")
#     print("Unable to retrieve weather information")
# # send an SMS message to the user with the crop information
# message = client.messages.create(
#     body=f"Description of {crop}: {crop_description}\nWeather conditions for {location}: {weather_description}\n{advise}",
#     from_="+15855600918",
#     to="+233554127614"
# )
# print(f"SMS message sent to {message.to}: {message.body}")
