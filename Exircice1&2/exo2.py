class Weeker:
    _jour_de_se={'lun','mar','Mer','Jeu','Van','Sam','Dim'}
    def __init__(self,day) :
        if day not in self._day_of_week:
            raise ValueError("Invalid day in the week")
        self._current_day = day

    def __str__(self):
        return self._current_day
    def add_days(self , n):
        if n < 0:
            raise ValueError("")