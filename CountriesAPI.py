import requests
from tabulate import tabulate


class CountriesAPI:
    def __init__(self):
        self.url = 'https://restcountries.com/v3.1/all'

    def json_data(self):
        api_response = requests.get(self.url)
        clean_api = api_response.json()
        return clean_api

    def get_country_info(self):
        countries = self.json_data()
        country_info_list = []

        for country in countries:
            try:
                country_name = country['name']['common']
                country_capital = country.get('capital', ['N/A'])[0]
                country_flag = country['flags']['png']
                country_info_list.append([country_name, country_capital, country_flag])
            except KeyError as e:
                print(f"Missing key {e} in country data: {country}")

        return tabulate(country_info_list, headers=["Name", "Capital", "Flag"])


countries_api = CountriesAPI()
print(countries_api.get_country_info())
