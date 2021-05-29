#imports Pandas to get data from csv and put it into html table format
import pandas as pd

# Module to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname, "Resources", "cities.csv")


df = pd.read_csv (csv_path)

df.to_html('data.html')