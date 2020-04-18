#!/usr/bin/python3
import requests
import argparse
import json
import time
import sys
import os
import datetime
# from keys import *  create a keys.py file to store your oist and api key

headers = {
        'x-rapidapi-host': os.getenv('API_HOST'), #your host key here
        'x-rapidapi-key': os.getenv('API_KEY')    #your api key here
    }
    
yesterday = datetime.date.today() -  datetime.timedelta(days=1)

def get_overall():
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    querystring = {"date":yesterday}

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_json = json.loads(response.text)
    total_deaths = response_json['data'].get('deaths')
    total_confirmed = response_json['data'].get('confirmed')
    total_recovered = response_json['data'].get('recovered')
    total_active = response_json['data'].get('active')
    print(f'As of {yesterday}:')
    time.sleep(2)
    print(f'\n\nTotal deaths worldwide:{total_deaths} \
        \n\nTotal confirmed cases: {total_confirmed}\
        \n\nTotal recovered cases: {total_recovered}\
        \n\nTotal active cases: {total_active}')
    time.sleep(2)
    sys.exit()


def get_by_country(iso):
    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    querystring = {"iso":iso}
    response = requests.request("GET", url, headers=headers, params=querystring)

    response_json = json.loads(response.text)

    deaths = sum(map(lambda x: int(x['deaths']), response_json['data']))
    confirmed = sum(map(lambda x: int(x['confirmed']), response_json['data']))
   
    print(f'As of {yesterday}:')
    time.sleep(2)
    print(f'\n\nTotal confirmed cases: {confirmed}\
        \n\nTotal deaths: {deaths}')
    time.sleep(2)
    print("\n\n-----Exiting in 2 secs --------BYE")
    time.sleep(2)
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("--get", help="list all information by country iso code", type=get_by_country, action="store")
parser.add_argument("--total", help="worldwide data",action="store_true")
args = parser.parse_args()

if args.total:
    get_overall()