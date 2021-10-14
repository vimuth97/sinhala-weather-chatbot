from datetime import date
import re


def parse_date(date_string):
        today = date.today()
        year = today.year
        try:
            m, d = re.split('-|/', date_string)
            d1 = date(year, int(m), int(d))
            delta = d1 - today
            return delta.days
        except:
            return None
