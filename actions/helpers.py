from datetime import date
import re

date_map = {
    "පෙරේදා" : -2,
    "ඊයෙ" : -1,
    "අද" : 0,
    "හෙට": 1,
    "අනිද්දා": 2
}

def parse_date(date_string):
    today = date.today()
    year = today.year
    if date_string in date_map.keys():
        return date_map[date_string]
    else:
        try:
            m, d = re.split('-|/', date_string)
            d1 = date(year, int(m), int(d))
            delta = d1 - today
            return delta.days
        except:
            return None
