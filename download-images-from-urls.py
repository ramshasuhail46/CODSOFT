import requests
import pandas as pd

urls = pd.read_csv('/Users/DELL/Desktop/ramsha_work/urls') #save the url list as a dataframe

rows = []

for index, i in urls.iterrows():
    rows.append(i[-1])

counter = 0

for index,i in enumerate(rows):
    file_name = str(counter) + '.jpg'
    
    print(file_name)
    
    response = requests.get(i)
    file = open(file_name, "wb")
    file.write(response.content)
    file.close()
    counter += 1


