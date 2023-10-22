# STR Analyzer

## Setup
Setup is very simple. There are only 3 easy steps:

1. Go to [RapidAPI](https://rapidapi.com/mashvisor-team/api/mashvisor) and sign up for the free tier of the Mashvisor API. Once you have signed up, grab your `X-RapidAPI-Key` from your account.
2. Next, open the [secrets.example.env](./secrets.example.env) file and remove the word `blah` from the `MASHVISOR_API_KEY` variable. Then paste your `X-RapidAPI-Key` into the variable between the quotes. Rename and save this file as `secrets.env` (just remove the `.example` from the filename).
3. Lastly, run the following 2 commands in your terminal to create a virtual environment and install all necessary dependencies:

First create the virtual environment:
```sh
python3 -m venv venv
```

Then install your dependencies:
```sh
pip install -r requirements.txt
```

**That is it! you are ready to run some numbers!**


## Run
There are 2 simple scripts that utilize the Mashvisor class to pull data:

### [app.py](./app,py)
This is a small script that allows you to run any function the Mashvisor class can call inside a try/except block. Running this script pulls the data using the Mashvisor API and saves it to a JSON file for easy analysis.

```python
import json
from log import logging
from mashvisor import Mashvisor

logger = logging.getLogger('app.py')
mv = Mashvisor()
# Black Hawk neighborhood id: 30476
try:
    data = mv.get_neighborhood_ltr_historical_performance(30476, 'CO', 2022)
    json_object = json.dumps(data, indent=4)
    with open("results.json", "w") as outfile:
        outfile.write(json_object)
    logger.info("JSON data saved to ./results.json")
    
except Exception as e:
    logger.error(e)
```

### [chart.py](./chart.py)
This script simply pulls in a Mashvisor returned JSON file that contains histogram, heatmap or other charting data and uses matplotlib and/or seaborn to create beautiful charts to easily interpret data.

```python
import seaborn as sn
import matplotlib.pyplot as plt
import json
 
filename = './analysis/occupancy-rates'
f = open(f'{filename}.json')
data = json.load(f)

plt.hist(data['detailed']['three_bedrooms_histogram'])
plt.savefig('./3-bed-occupancy-histogram')
```