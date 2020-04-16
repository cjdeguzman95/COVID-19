import sys
sys.path.append('../src/')
import covid_data_with_cumulate
import csv
import os
import requests

test_file = "test.csv"

def test_create_csv():
    with open(test_file, "w+") as file:
        writer = csv.writer(file)
        covid_data_with_cumulate.create_csv(writer)

    with open(test_file, "r") as file:
        reader = csv.reader(file)
        first_row = next(reader)

        assert len(first_row) == 5
        assert first_row[0] == "Country"
        assert first_row[1] == "Date"
        assert first_row[2] == "Type"
        assert first_row[3] == "Number of Cases"
        assert first_row[4] == "Cumulative Cases"

    os.remove(test_file)

def test_update_csv():
    with open(test_file, "w+") as file:
        writer = csv.writer(file)
        covid_data_with_cumulate.update_csv(writer, ["test1", "test2"])

    with open(test_file, "r") as file:
        reader = csv.reader(file)
        first_row = next(reader)

        assert len(first_row) == 2
        assert first_row[0] == "test1"
        assert first_row[1] == "test2"

    os.remove(test_file)

covid_live_data = covid_data_with_cumulate.retrieve_live_data(requests.get("https://pomber.github.io/covid19/timeseries.json").json())

def test_retrieve_live_data():
    first_row = covid_live_data[0]
    assert len(first_row) == 5
    assert first_row[0] == "Afghanistan"
    assert first_row[1] == "2020-1-22"
    assert first_row[2] == "Confirmed"
    assert first_row[4] == 0
