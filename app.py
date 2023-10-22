import json
from log import logging
from mashvisor import Mashvisor

logger = logging.getLogger('app.py')
mv = Mashvisor()
# Black Hawk neighborhood id: 30476 (use the mv.get_neighborhoods method to find your id)
try:
    data = mv.get_neighborhood_ltr_historical_performance(30476, 'CO', 2022)
    json_object = json.dumps(data, indent=4)
    with open("results.json", "w") as outfile:
        outfile.write(json_object)
    logger.info("JSON data saved to ./results.json")
    
except Exception as e:
    logger.error(e)