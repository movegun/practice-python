from pymongo import mongo_client
import numpy as np


uri = "mongodb://localhost:27017"
mgCilent = mongo_client.MongoClient(uri)
db = mgCilent["movegunDB"]
coll = db["apartment"]

where = {'계약년도':2012}

items = coll.find(where,{'거래금액(만원)':True,'층':True})
x = []
y = []
print(x)
for item in items:
    x.append(item['층'])
    y.append(item['거래금액(만원)'])
    

x = np.array(x)
y = np.array(y)

import matplotlib.pyplot as plt

plt.plot(x,y,'o')
plt.show()
