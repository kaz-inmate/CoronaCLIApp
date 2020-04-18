# CoronaCLIApp
CLI application to get the worlwide and country specefic details regarding the COVID-19 cases. The Api used for the fetching the data is [here](https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/details).


## Getting started

* Get a api key required from rapidapi

* Clone the repo and open it in your text editor

* Add your rapid api and host key to the headers in corona.py


## Commands
```
1. There are 2 commands available.

2. Run corona.py --total form the terminal to get the worldwide data.

3. Run corona.py --get [iso country code] to get the data of particular country.

```

You can find the ISO country codes [here](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

## Example

```
* python corona.py --total (displays worldwide information)
* python corona.py --get CHN (displays China's Covid-19 info)

```
