import requests
from urllib.parse import quote
from config import Config

config = Config()

class Mashvisor:
    def __init__(self):
        self.base_url = config.mashvisor_api_base_url
        self.headers = {
            "X-RapidAPI-Key": config.mashvisor_api_key,
            "X-RapidAPI-Host": config.mashvisor_api_host
        }

    def return_response(self, response):
        if response.json()['status'] == 'success': return response.json()['content']
        else: raise Exception(f'Error getting neighborhoods! Error: {response.json()["message"]}')

    
    def get_neighborhoods(self, city="Denver", state="CO"):
        response = requests.get(f"{self.base_url}/city/neighborhoods/{quote(state)}/{quote(city)}", headers=self.headers)
        return self.return_response(response)
        
        
    
    def get_market_summary(self, city="Denver", state="CO"):
        response = requests.get(f"{self.base_url}/airbnb-property/market-summary", headers=self.headers, params={"state":state,"city":city})
        return self.return_response(response)
    
    
    def get_top_airbnb_cities(self, state="CO", items=5):
        querystring = {"state":state,"page":"1","items":str(items)}
        response = requests.get(f"{self.base_url}/trends/cities", headers=self.headers, params=querystring)
        return self.return_response(response)
    
    
    def get_city_summary(self, city="Denver", state="CO"):
        response = requests.get(f"{self.base_url}/trends/summary/{state}/{quote(city)}", headers=self.headers)
        return self.return_response(response)
        
        
    def get_occupancy_rates(self, city="Denver", state="CO"):  
        response = requests.get(f"{self.base_url}/airbnb-property/occupancy-rates", headers=self.headers, params={"state":state,"city":city})
        return self.return_response(response)
    
    
    def get_neighborhood_ltr_historical_performance(self, id=30476, state="CO", year=None):
        querystring = {"state":state,"year":str(year)}
        response = requests.get(f"{self.base_url}/neighborhood/{id}/historical/traditional", headers=self.headers, params=querystring)
        return self.return_response(response)
    
    
    def get_neighborhood_str_historical_performance(self, id=30476, state="CO", average_by="price", percentile=1, beds=None):
        # average_by = "occupancy", "price", "revenue"
        # percentile = 1, 0
        querystring = {"state":state,"average_by":average_by,"percentile_rate":str(percentile), "beds": beds}
        response = requests.get(f"{self.base_url}/neighborhood/{id}/historical/airbnb", headers=self.headers, params=querystring)
        return self.return_response(response)
    
    
    def get_neighborhood_overview(self, id=30476, state="CO"):
        response = requests.get(f"{self.base_url}/neighborhood/{id}/bar", headers=self.headers, params={"state":state})
        return self.return_response(response)
    
    
    def get_location_heatmap(self, map_type, ne_lat, sw_lng, ne_lng, sw_lat, state="CO"):
        # map_type = "AirbnbCoc", "listingPrice", "TraditionalCoc", "OccupancyRate", "AirbnbRental", "TraditionalRental"
        querystring = {"type":map_type,"ne_lat":str(ne_lat),"sw_lng":str(sw_lng),"ne_lng":str(ne_lng),"state":state,"sw_lat":sw_lat}
        response = requests.get(f"{self.base_url}/search/heatmap", headers=self.headers, params=querystring)
        return self.return_response(response)

    
    def get_city_performance(self, city="Denver", state="CO"):
        response = requests.get(f"{self.base_url}/city/investment/{state}/{quote(city)}", headers=self.headers)
        return self.return_response(response)
    

    def get_rental_rates(self, state="CO", source="airbnb", city="Denver", zipcode=None):
        # source = "traditional" or "airbnb"
        querystring = {"state":state,"source":source,"city":quote(city),"zip_code":str(zipcode)}
        response = requests.get(f"{self.base_url}/rental-rates", headers=self.headers, params=querystring)
        return self.return_response(response)
    
    
    def __str__(self):
        pass
    


    
    
    
    
    
    
        
           
    