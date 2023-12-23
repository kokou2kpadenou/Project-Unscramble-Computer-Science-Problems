"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

distinct_phone = []

# 
def add_to_distinct_list(records, phone_list):
    """
    Add phone number from 'records' to 'phone_list' while ensuring distinct phone number.

    Parameters:
    records (list): A list of records where each record is expected to be a list.
                    The function will consider the first two elements of each record.
    phone_list (list): A list that will be modified to store distinct phone numbers from 'records'.

    Returns:
    None
    """
    for elt in records:
        # caller/sender
        if not elt[0] in phone_list:
            phone_list.append(elt[0])
        # receiver
        if not elt[1] in phone_list:
            phone_list.append(elt[1])

# Trait texts records
add_to_distinct_list(texts, distinct_phone)
# Trait calls records
add_to_distinct_list(calls, distinct_phone)

print("There are {} different telephone numbers in the records.".format(len(distinct_phone)))
