class Human:
    import datetime.date
    from dateutil.relativedelta import relativedelta
    def __init__(self,first_name:str,last_name:str,date_of_birth:datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        return relativedelta(datetime.date(datetime.now()), self.date_of_birth).years

me = Human('Anatoli','Barbaros','02/06/1986')