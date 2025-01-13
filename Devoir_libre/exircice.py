#1
import csv
from datetime import datetime
def getStatRegionDate(region, date):
    with open('corona_morocco.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Region'] == region and row['Date'] == date:
                return int(row['Confirmed'])
    return 0
#2
def getStatRegionPeriod(region, start_date, end_date):
    with open('corona_morocco.csv', 'r') as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            if row['Region'] == region and row['Date'] >= start_date and row['Date'] <= end_date:
                total += int(row['Confirmed'])
        return total
#3
class CoronaMa:
    def __init__(self, date):
        with open('corona_morocco.csv', 'r') as file:
            reader = csv.DictReader(file)
            row = next(reader)
            if row['Date'] == date:
                self.Date = date
                self.Confirmed = int(row['Confirmed'])
                self.Deaths = int(row['Deaths'])
                self.Recovered = int(row['Recovered'])
                self.Excluded = int(row['Excluded'])
            else:
                raise ValueError('Invalid date')
            
#4
def __str__(self):
    return f'Date: {self.Date}\nConfirmed: {self.Confirmed}\nDeaths: {self.Deaths}\nRecovered: {self.Recovered}\nExcluded: {self.Excluded}'
