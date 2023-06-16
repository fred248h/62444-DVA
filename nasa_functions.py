
import json
import pandas as pd
import numpy as np
import math
import requests
import time
from datetime import datetime, timedelta
from getpass import getpass



def get_data(api_key, start_date, end_date):
    # Initialize a list to store the data
    data = []

    # Fetch data from the NASA API 7 days at a time
    # The introduction of the API is on https://api.nasa.gov, under "Browse APIs" -> "Asteroids NeoWs"
    # You can look into the example query in the link below to see what the data look like:
    # https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
    current_date = start_date
    while current_date < end_date:
        next_date = min(current_date + timedelta(days=7), end_date)
        response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={current_date.strftime("%Y-%m-%d")}&end_date={next_date.strftime("%Y-%m-%d")}&api_key={api_key}')
        data.append(response.json())
        current_date = next_date
        time.sleep(1)  # To avoid hitting the rate limit
    return data




def json_to_dataframe(df_data, data, dates_contained_in_data):
    ############# Input ################
    # df_data: pandas dataframe
    # data: list
    # dates_contained_in_data: list

    ############# Output ################
    # There is no output. The function overwrites the dataframe.
   

    index1, index2 = 0,0
    for date in dates_contained_in_data:
        week = math.floor(index1/8)
        data_list = data[week]["near_earth_objects"][date]
        index1 += 1

        for i in range(0,len(data_list)):
            index2 +=1
            dict_list = list(data_list[i].keys())

            #Generate new id 
            Id = str(index1)+str(index2)

            df_data.loc[Id,"date"] = date
            df_data.loc[Id,"week"] = week
            
            for first_dict in dict_list:
                if first_dict in ['close_approach_data', 'estimated_diameter']:
            
                    if first_dict == 'close_approach_data': new_data_list=data_list[i][first_dict][0]
                    else: new_data_list=data_list[i][first_dict]

                    new_dict_list = list(new_data_list.keys())
                    
                    for new_dict in new_dict_list:
                        try:
                            if isinstance(new_data_list[new_dict].keys(), type(new_data_list.keys()))==True:
                                end_dict_list = list(new_data_list[new_dict].keys())
                                for end_dict in end_dict_list:
                                    df_data.loc[Id, str(new_dict)+" "+str(end_dict)] = new_data_list[new_dict][end_dict]
                        except:
                            df_data.loc[Id, str(new_dict)] = new_data_list[new_dict]
                else:
                    if not first_dict =='links':
                        df_data.loc[Id, str(first_dict)] = data_list[i][first_dict]
        
