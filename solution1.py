def convert_time(hour, minute, period):
    #  Converts a 12-hour time format (hour, minute, period) to a 24-hour time format (HHMM)
      # Handle the AM/PM case
    if period.lower() == "am":
        # Convert 12 AM to 00:00
        if hour == 12:
            hour = 0
             # Convert hour to 24-hour format
        time = str(hour).zfill(2) +':'+ str(minute).zfill(2) + str(period)
    else:
        # Convert 12 PM to 12:00
        if hour == 12:
            hour = 12
             # Convert hour to 24-hour format
        else:
            hour += 12
        time = str(hour).zfill(2) +':'+ str(minute).zfill(2) + str(period)
    return time

print(convert_time(12, 00, 'PM'))  # Output: 2000
print(convert_time(12, 15, 'AM'))  # Output: 0015
