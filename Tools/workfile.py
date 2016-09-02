amount_of_days = int(raw_input("Enter the number of days. Must be at least 1."))
amount_of_boxes = int(raw_input("Enter the amount of boxes of strips cut in one day. Must be at least 1."))

t1_box = 1500; """Time in seconds"""

time_per_day = t1_box * amount_of_boxes
work_hours_per_day = ((float(time_per_day) / 60) / 60)
hourly_wage = 13.50
daily_pay = hourly_wage * work_hours_per_day
total_cost = daily_pay * amount_of_days

print "Total Pay for the day: %r" % (daily_pay)
print "Total Cost for %r : %r" % (amount_of_days, total_cost)


#saves 6 times
