import seaborn as sn
import matplotlib.pyplot as plt
import json
 
filename = './analysis/occupancy-rates'
f = open(f'{filename}.json')
data = json.load(f)

# hm = sn.heatmap(data = data)
plt.hist(data['detailed']['four_bedrooms_histogram'])
plt.savefig('./4bed-occupancy-histogram')

