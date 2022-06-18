import pandas as pd

dInsol = pd.read_csv('crimes-19.csv', sep=',', header=0, low_memory=False)

dInsol = dInsol.drop('ID', axis=1)
dInsol = dInsol.drop('Case Number', axis=1)
dInsol = dInsol.drop('Primary Type', axis=1)
dInsol = dInsol.drop('Description', axis=1)
dInsol = dInsol.drop('Location Description', axis=1)
dInsol = dInsol.drop('X Coordinate', axis=1)
dInsol = dInsol.drop('Y Coordinate', axis=1)
dInsol = dInsol.drop('Updated On', axis=1)
dInsol = dInsol.drop('Latitude', axis=1)
dInsol = dInsol.drop('Longitude', axis=1)
dInsol = dInsol.drop('Location', axis=1)
dInsol = dInsol.drop('Date', axis=1)
dInsol = dInsol.drop('Block', axis=1)
dInsol = dInsol.drop('FBI Code', axis=1)

print(dInsol)

#%%
