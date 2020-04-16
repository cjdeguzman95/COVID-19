import requests
import csv

def create_csv(writer):
    writer.writerow(['Country', 'Date', 'Confirmed', 'Deaths', 'Recovered'])

def update_csv(writer, row):
    writer.writerow(row)

def retrieve_live_data(data):
    result = []
    for country in data:
        previous_day_confirmed = 0
        previous_day_deaths = 0
        previous_day_recovered = 0
        for item in data[country]:
            if country == "Taiwan*":
                country = "Taiwan"
            elif country == "US":
                country = "USA"
            confirmed_cases = item["confirmed"] - previous_day_confirmed
            previous_day_confirmed = item["confirmed"]
            death_cases = item["deaths"] - previous_day_deaths
            previous_day_deaths = item["deaths"]
            recovered_cases = item["recovered"] - previous_day_recovered
            previous_day_recovered = item["recovered"]
            result.append([
                country,
                item['date'],
                confirmed_cases,
                death_cases,
                recovered_cases
            ])
    return result

if __name__ == '__main__':
    writer = csv.writer(open("Newcases_Data.csv", "w"), lineterminator='\n')
    create_csv(writer)
    url = "https://pomber.github.io/covid19/timeseries.json"
    covid_json_data = requests.get(url).json()
    live_covid_data = retrieve_live_data(covid_json_data)
    for row in live_covid_data:
        update_csv(writer, row)