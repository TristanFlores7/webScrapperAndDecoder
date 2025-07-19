import requests
import string
import pandas as pd
import numpy as np

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub" #data

def decoder(url):
    response = requests.get(url) #returns '200' if the request is successful
    data = pd.read_html(url, encoding='utf-8') #reads data
    reshape = np.reshape(data, shape=(351,3)) #reshapes data
    df = pd.DataFrame(reshape, columns=['x', 'char', 'y']).drop(0) #creates dataframe
    df["x"] = pd.to_numeric(df["x"]) #converts 'x' column data to integers
    df["y"] = pd.to_numeric(df["y"]) #converts 'y' column data to integers
    sb = string #declares string builder
    maxes = df.max() #1x3 array of max number in each column of data
    xMax = int(maxes[0]) #column 'x' max number
    yMax = int(maxes[2]) #column 'y' max number
    for j in range(yMax, -1, -1): #increments 'y' axis data from the top down
        sb = "" #resets string builder for each line
        for i in range(0, xMax): #increments 'x' axis data from left to right
            result = df[(df['x'] == i) & (df['y'] == j)]['char'] #grabs character from 'char' column at position 'j' in column 'y' and position 'i' in column 'x'
            if(result.size > 0):
                sb += sb.join(map(str, result)) #adds non-blank data to string builder
            else:
                sb += " " #adds blank data to string builder as a space
        print(sb) #prints line before iterating to next line down

decoder(url) #calls decoder method