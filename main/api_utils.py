import requests
from .creds import ai_trip_planner_key,booking_hotels_locations_key,booking_hotels_search_key

RESPONSE_STRUCTURE = {
    "message": "",
    "success": False,
    "data": [],
}


def get_trip_plan(body):
    api_url = "https://ai-trip-planner.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Key": ai_trip_planner_key,
        "X-RapidAPI-Host": "ai-trip-planner.p.rapidapi.com"
    }
    req = requests.request("GET", api_url, headers=headers, params=body)
    if req.status_code == 200:
        print(req.json())
        RESPONSE_STRUCTURE['message'] = "Successfully fetched the API."
        RESPONSE_STRUCTURE['success'] = True
        RESPONSE_STRUCTURE['data'] = req.json()
        print(req.json())
        print("inside api call")
        return req.json()
    else:
        RESPONSE_STRUCTURE['message'] = "Failed to fetch the data from API"
        return RESPONSE_STRUCTURE


def get_city_location_code(body):
    print("hey inside api")
    api_url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
    headers = {
	"X-RapidAPI-Key": booking_hotels_locations_key,
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
    }
    req = requests.request("GET", api_url, headers=headers, params=body)
    print(req.status_code)
    if req.status_code == 200:
        print(req.json())
        RESPONSE_STRUCTURE['message'] = "Successfully fetched the API."
        RESPONSE_STRUCTURE['success'] = True
        RESPONSE_STRUCTURE['data'] = req.json()
        print(RESPONSE_STRUCTURE)
        return req.json()
    else:
        RESPONSE_STRUCTURE['message'] = "Failed to fetch the data from API"
        return RESPONSE_STRUCTURE

def get_hotels_info(body):
    api_url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    headers = {
	"X-RapidAPI-Key": booking_hotels_search_key,
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
    }
    req = requests.request("GET", api_url, headers=headers, params=body)
    print(req.status_code)
    if req.status_code == 200:
        print(req.json())
        RESPONSE_STRUCTURE['message'] = "Successfully fetched the API."
        RESPONSE_STRUCTURE['success'] = True
        RESPONSE_STRUCTURE['data'] = req.json()
        print(RESPONSE_STRUCTURE)
        return req.json()
    else:
        RESPONSE_STRUCTURE['message'] = "Failed to fetch the data from API"
        return RESPONSE_STRUCTURE