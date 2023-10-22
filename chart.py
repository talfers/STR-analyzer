import seaborn as sn
import matplotlib.pyplot as plt
import json
 
# Update this filename to change which file to load into memory
filename = './analysis/occupancy-rates'
f = open(f'{filename}.json')
data = json.load(f)

# Update the location of the data below to choose where in your dataset to chart/visualize
plt.hist(data['detailed']['three_bedrooms_histogram'])
plt.savefig('./3-bed-occupancy-histogram')