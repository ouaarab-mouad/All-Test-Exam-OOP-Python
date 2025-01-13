class Weeker:
    _days_of_week = {'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'}

    def __init__(self, day):
        if day not in self._days_of_week:
            raise ValueError("Invalid day of the week")
        self._current_day = day

    def __str__(self):
        return self._current_day

    def add_days(self, n):
        if n < 0:
            raise ValueError("Number of days to add should be non-negative")
        index = list(self._days_of_week).index(self._current_day)
        new_index = (index + n) % len(self._days_of_week)
        self._current_day = list(self._days_of_week)[new_index]

    def subtract_days(self, n):
        if n < 0:
            raise ValueError("Number of days to subtract should be non-negative")
        index = list(self._days_of_week).index(self._current_day)
        new_index = (index - n) % len(self._days_of_week)
        self._current_day = list(self._days_of_week)[new_index]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lundi')  # This will raise a ValueError
except ValueError as e:
    print("Sorry, I can't serve your request. Error:", e)
