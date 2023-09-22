import pandas as pd
import matplotlib.pyplot as plt 

def plot(data,graph_type:str,Title:str):
    plt.figure(figsize=(12, 8))
    data.plot(kind=f'{graph_type}', color='skyblue')
    plt.title(f'{Title}')
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
