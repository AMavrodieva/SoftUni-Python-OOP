import calendar

class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, creation_year = [int(x) for x in date.split(".")]
        creation_month = calendar.month_name[month]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else "not rented"
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction ' \
               f'{self.age_restriction}. Status: {status}'
