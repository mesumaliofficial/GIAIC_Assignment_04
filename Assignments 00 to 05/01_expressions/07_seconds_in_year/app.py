def main():

    print("This program calculates the number of seconds in a year.")
    
    day_per_year = 365
    hours_per_day = 24
    minutes_per_hour = 60
    seconds_per_minute = 60

    result = day_per_year * hours_per_day * minutes_per_hour * seconds_per_minute

    print(f"Seconds in a year: {result}")


if __name__ == '__main__':
    main()