import pandas as pd

file_path = 'chatgrup.csv'
data = pd.read_csv(file_path)
data.head(), data.info()
