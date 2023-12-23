"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Dictionary to hold phone number with time spent on the phone during September 2016.
# ex: {{"phone number": "temie spent"}}
phone_time_spent = dict()

for call in calls:
    # Caller time spent on phone
    if call[0] in phone_time_spent:
        phone_time_spent.update({call[0]: phone_time_spent[call[0]] + int(call[3])})
    else:
        phone_time_spent[call[0]] = int(call[3])

    # Called time spent answering.
    if call[1] in phone_time_spent:
        phone_time_spent.update({call[1]: phone_time_spent[call[1]] + int(call[3])})
    else:
        phone_time_spent[call[1]] = int(call[3])


longest_time = 0
phone_number = ""
for key, value in phone_time_spent.items():
    if value > longest_time:
        longest_time = value
        phone_number = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, longest_time))
