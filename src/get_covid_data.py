import requests
from datetime import datetime, timedelta


def get_covid_data_by_country(country_name):
    all_data = _fetch_covid_data(country_name)
    country, confirmed_cases, recovered_cases, deaths = _extract_relevant_covid_data(all_data)
    return country, confirmed_cases, recovered_cases, deaths


def _fetch_covid_data(country_name):
    url = "https://covid-19-data.p.rapidapi.com/report/country/name"
    querystring = {"date-format": "YYYY-MM-DD", "format": "json", "date": datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d'), "name": str(country_name)}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "d488627587msh127c412ef98f220p196afbjsn78704eb4a153"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def _extract_relevant_covid_data(data):
    country_name = data[0]['country']
    confirmed_cases = data[0]['provinces'][0]['confirmed']
    recovered_cases = data[0]['provinces'][0]['recovered']
    deaths = data[0]['provinces'][0]['deaths']

    return country_name, confirmed_cases, recovered_cases, deaths


if __name__ == '__main__':
    get_covid_data_by_country("Italy")
