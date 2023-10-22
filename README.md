# STR Analyzer

This is an application setup to pull various datasets relating to short and long term rentals based on sites like Airbnb. There is a main [Mashvisor](./mashvisor.py) class that contains all the methods you need to collect ample data to use for your analysis.


## Clone the repo

In order to run this application you will need to clone this repository. To do this simply open your terminal and run the following command:

_NOTE: If you receive errors on this step make sure you have [Git](https://git-scm.com/downloads) installed on your computer._


```console
git clone https://github.com/talfers/STR-analyzer.git
```

After this, you will need to ensure you are in the application directory before continuing with the following steps. Simply run the following command to switch directories:

```console
cd STR-analyzer
```


## Setup
Setup is very simple. There are 3 easy steps:

1. Go to [RapidAPI](https://rapidapi.com/mashvisor-team/api/mashvisor) and sign up for the free tier of the Mashvisor API. Once you have signed up, grab your `X-RapidAPI-Key` from your account.

2. Next, open the [secrets.example.env](./secrets.example.env) file and remove the word `blah` from the `MASHVISOR_API_KEY` variable. Then paste your `X-RapidAPI-Key` into the variable between the quotes. Rename and save this file as `secrets.env` (just remove the `.example` from the filename).

3. Lastly, run the following 2 commands in your terminal to create a virtual environment and install all necessary dependencies:

_NOTE: If you get an error that you do not have python, pip or venv on your computer, see the [Troubleshooting](#troubleshooting) section below._

First create the virtual environment:
```console
python3 -m venv venv
```

Then install your dependencies:
```console
pip install -r requirements.txt
```

**That is it! You are ready to run some numbers!**


## Run
There are 2 main scripts that utilize the Mashvisor class to pull and visualize the data:

### [`app.py`](./app.py)
This is a small script that allows you to run any function the Mashvisor class can call inside a try/except block. Running this script pulls the data using the Mashvisor API and saves it to a JSON file called `results.json` for easy analysis.

_NOTE: For more information on the Mashvisor class and it's methods, go to [mashvisor.py](./mashvisor.py)._

```python
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
```

To try this script, simply go to your terminal and run:
```console
python app.py
```


### [`chart.py`](./chart.py)
This script simply pulls in a Mashvisor returned JSON file that contains histogram, heatmap or other charting data and uses [matplotlib](https://matplotlib.org/) and/or [seaborn](https://seaborn.pydata.org/) to create beautiful charts to easily interpret the data.

```python
import seaborn as sn
import matplotlib.pyplot as plt
import json
 
# Update this filename variable BELOW to change which file to load into memory
filename = './analysis/occupancy-rates'
f = open(f'{filename}.json')
data = json.load(f)

# Update the location of the data BELOW to choose where in your dataset to chart/visualize
plt.hist(data['detailed']['three_bedrooms_histogram'])
plt.savefig('./whatever_filename_you_want')
```

To try this script, simply go to your terminal and run:
```console
python app.py
```


## Example Data

See the [analysis](./analysis) directory for various examples on how the data is returned and saved using Black Hawk, Colorado.



## Troubleshooting

If you cannot install your virtual environment or application dependencies without throwing errors, you will need to ensure [Python](https://www.python.org/downloads/) is downloaded on your computer, which usually has [pip](https://pypi.org/project/pip/) already included. Then, to ensure you have venv installed, simply go to your terminal and run:

```console
pip install virtualenv
```

If everything above ran successfully, you should no longer see errors.
