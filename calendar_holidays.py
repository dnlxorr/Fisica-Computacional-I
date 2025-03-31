import calendar

import holidays.countries
from holidays import countries


# Function to print a well-formatted calendar for a given year
def print_year_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(f"\n{'=' * 60}")
    print(f"          Calendar for {year}".center(60))
    print(f"{'=' * 60}\n")
    print(cal.formatyear(year, 2, 1, 1, 3))


def print_holidays(year):
    col_holidays = holidays.countries.COL(years=year, observed=True)

    holidays_in_colombia = []
    for date, name in sorted(col_holidays.items()):
      day_of_week = date.strftime("%A")
      formatted_date = date.strftime("%B %d, %Y")
      holidays_in_colombia.append((name, formatted_date, day_of_week))

    # Print holidays in a formatted table
    print(f"\n{'=' * 60}")
    print(f"      Holidays for {year}".center(60))
    print(f"{'=' * 60}\n")
    print("Holiday".ljust(35) + "Date".ljust(20) + "Day")
    print("-" * 60)
    for holiday, date, day in holidays_in_colombia:
        print(f"{holiday.ljust(35)}{date.ljust(20)}{day}")


# Main execution
def main():
    year = 2025
    print_year_calendar(year)
    print_holidays(year)


if __name__ == "__main__":
    main()