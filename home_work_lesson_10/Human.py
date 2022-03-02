from datetime import date, datetime

class Human:

    def __init__(self,first_name:str,last_name:str,date_of_birth:datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):

        today = date.today()
        born_date = datetime.strptime(self.date_of_birth, "%d/%m/%Y")
        age = today.year - born_date.year #- ((today.month, today.day) < (born_date.month, born_date.day))
        return age

    def __str__(self):
        return f'{self.first_name} {self.last_name} age {get_age(self)}'

