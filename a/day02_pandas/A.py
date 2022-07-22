import pandas as pd

ds = {
    'animals': ["tiger","lion","rabbit"],
    'count' : [4,8,3]        
}

a = pd.DataFrame(ds)
print(a)
print("-------------------------------")

print("pd.__version__ :",pd.__version__)