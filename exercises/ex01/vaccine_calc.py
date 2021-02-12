"""A vaccination calculator."""

__author__ = "730212606"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
Population: int = int(input("Population: "))
Doses_administered: int = int(input("Doses administered: "))
Doses_per_day: int = int(input("Doses per day: "))
Target_percent_vaccinated: int = int(input("Target percent vaccinated: "))
target_string = str(Target_percent_vaccinated)
percent_vaccinated: float = (Target_percent_vaccinated / 100)
new_population: int = round(Population * percent_vaccinated)
target_population: int = round(new_population - (Doses_administered / 2))
remaining_days: int = round(target_population / (Doses_per_day / 2))
remaining_string = str(round(remaining_days))
today: datetime = datetime.today()
fortnight: timedelta = timedelta(remaining_days)
future: datetime = today + fortnight 
future_final: str = future.strftime("%B %d, %Y")

print("We will reach " + target_string + "% vaccination in " + remaining_string + " days, on " + future_final)
