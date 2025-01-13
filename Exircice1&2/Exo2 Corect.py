class Weeker:
    _days_of_week = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
 
    def __init__(self, day):
        self.jour = day
 
    def __str__(self):
        return self.jour
 
    def add_days(self, n):
        index = self._days_of_week.index(self.jour)
        new_index = (index + n) % len(self._days_of_week)
        self.jour = self._days_of_week[new_index]

    def subtract_days(self, n):
        index = list(self._days_of_week).index(self.jour)
        new_index = (index - n)% len(self._days_of_week)
        self.jour = list(self._days_of_week)[new_index]

weekday = Weeker('Dim')
print(weekday)
weekday.subtract_days(29)
print(weekday)

