# WAP TO LOAD A DATASET SELECT A FEATURE AND DISPLAY IT IN A SCATTER PLOT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("DATASETS/insurance.csv")
print(df.to_markdown(index=False)) # to print the data in tabular format
x=np.arange(1,1339)
y=df["age"]
plt.scatter(x,y,color="k")
plt.savefig("file.pdf")
plt.show() 


