#JSON FILE TO CSV FILE USING PYTHON

#IMPORT PANDAS LIB

import pandas

df=pandas.read_json('Cell_Phones_and_Accessories_5.json',lines=True) #'Cell_Phones_and_Accessories_5.json IS THE JSON FILE I NEEDED TO CONVERT

df.to_csv('Cell_Phones_and_Accessories_.csv') #'Cell_Phones_and_Accessories_.csv' IS THE NAME OF THE CSV FILE WHICH I NEEDED TO CREATE FROM THE JSON FILE