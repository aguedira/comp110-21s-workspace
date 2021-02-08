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
population: int = int(input("population: "))
doses_administered: int = int(input("doses administered: "))
doses_per_day: int = int(input("doses per day: "))
target_percent_vaccinated: int = int(input("target percent vaccinated: "))
targetpercentstring = str(target_percent_vaccinated)
percent_vaccinated: float = (target_percent_vaccinated / 100)
new_population: int = round(population * percent_vaccinated)
target_population: int = new_population - (doses_administered / 2)
remaining_days: int = target_population / (doses_per_day / 2)
remainingdaysstring = str(round(remaining_days))
today: datetime = datetime.today()
fortnight: timedelta = timedelta(remaining_days)
future: datetime = today + fortnight 
future_final: datetime = future.strftime("%B %d, %Y")

print("We will reach " +  targetpercentstring + "% in " + remainingdaysstring +" days, which falls on " + future_final)
