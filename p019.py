class Year:
    def __init__(self, year: int):
        self._year: int = year

    # check if the year is a leap year
    def is_leap_year(self):
        if self._year % 4 == 0:
            if self._year % 100 == 0:
                if self._year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # get the current year
    def get_year(self) -> int:
        return self._year

    # advance the year by certain number
    def next_year(self, years: int = 1):
        self._year += years


class Month:
    def __init__(self, month: int):
        self._month: int = month

    # get the lenght of the current month based on the current year
    def lenght(self, year: Year):
        if self._month == 2:
            if year.is_leap_year():
                return 29
            else:
                return 28
        elif self._month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    # get the current month
    def get_month(self) -> int:
        return self._month

    # advance the month
    def next_month(self):
        self._month += 1 if self._month < 12 else 1 - 12


class Day:
    def __init__(self, day: int):
        self._day: int = day

    # get the current day
    def get_day(self) -> int:
        return self._day

    # set the current day
    def set_day(self, day: int) -> None:
        self._day = day

    # advance the day by certain number
    def skip_days(self, days: int = 1) -> int:
        self._day += days
        return self._day


class Calendar:
    def __init__(self, day: int, month: int, year: int) -> None:
        self._day: Day = Day(day)
        self._month: Month = Month(month)
        self._year: Year = Year(year)

    # advance the date by certain number of days
    def advance_date(self, days: int = 1) -> None:
        self._day.skip_days(days)

        current_month_lenght = self._month.lenght(self._year)
        if self._day.get_day() > current_month_lenght:
            self._day.set_day(self._day.get_day() - current_month_lenght)

            if self._month.get_month() == 12:
                self._year.next_year()
            self._month.next_month()

    # this method returns a string representation of the date
    def __str__(self) -> str:
        return (
            f"{self._day.get_day()}/{self._month.get_month()}/{self._year.get_year()}"
        )


sundays = 0
calendar = Calendar(30, 12, 1900)

# the loop advances the date by 7 days
for i in range(1, 100 * 365, 7):
    calendar.advance_date(7)
    if calendar._day.get_day() == 1:
        sundays += 1

print(sundays)
