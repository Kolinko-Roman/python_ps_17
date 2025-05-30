from datetime import datetime

class UkrainianCalendar:
    def __init__(self):
        self.holidays = {
            "01-01", "07-01", "08-03", "01-05", "09-05", "28-06", "24-08", "14-10", "25-12"
        }

    def get_holiday_list(self):
        return list(self.holidays)

    def is_working_day(self, date: datetime):
        date_str = date.strftime("%d-%m")
        return date.weekday() < 5 and date_str not in self.holidays
