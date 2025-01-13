import csv
from datetime import datetime

class CoronaMa:
    def _init_(self, date):
        if not self.is_valid_date(date):
            raise ValueError("La date doit être comprise entre le 02/03/2020 et le 26/08/2020")
        self.date = date
        self.confirmed = 0
        self.deaths = 0
        self.recovered = 0
        self.excluded = 0

    def is_valid_date(self, date):
        start_date = datetime(2020, 3, 2)
        end_date = datetime(2020, 8, 26)
        return start_date <= date <= end_date

    def _str_(self):
        return f"Date: {self.date}\nConfirmed: {self.confirmed}\nDeaths: {self.deaths}\nRecovered: {self.recovered}\nExcluded: {self.excluded}"

    def to_json(self):
        return {
            "Date": str(self.date),
            "Confirmed": self.confirmed,
            "Deaths": self.deaths,
            "Recovered": self.recovered,
            "Excluded": self.excluded
        }

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def getStatRegionDate(region, date):
    corona_data = read_csv("corona_morocco.csv")
    total_cases = 0
    for entry in corona_data:
        if entry["Region"] == region and datetime.strptime(entry["Date"], "%d/%m/%Y") == date:
            total_cases += int(entry["Confirmed"])
    return total_cases

def getStatRegionPeriod(region, start_date, end_date):
    corona_data = read_csv("corona_morocco.csv")
    total_cases = 0
    for entry in corona_data:
        entry_date = datetime.strptime(entry["Date"], "%d/%m/%Y")
        if entry["Region"] == region and start_date <= entry_date <= end_date:
            total_cases += int(entry["Confirmed"])
    return total_cases

# Exemple d'utilisation :
region = "Rabat-Sale-Kenitra"
date = datetime(2020, 8, 1)
start_date = datetime(2020, 6, 1)
end_date = datetime(2020, 6, 30)

cases_on_date = getStatRegionDate(region, date)
cases_in_period = getStatRegionPeriod(region, start_date, end_date)

print(f"Nombre de cas positifs le {date}: {cases_on_date}")
print(f"Nombre de cas positifs entre {start_date} et {end_date}: {cases_in_period}")