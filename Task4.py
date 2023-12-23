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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

caller_set = set()
called_set = set()
for call in calls:
    if call[0][:3] != "140":
        caller_set.add(call[0])
    called_set.add(call[1])

text_sender = set()
text_receiver = set()
for text in texts:
    text_sender.add(text[0])
    text_receiver.add(text[1])

suspects = sorted(caller_set - text_sender - called_set - text_receiver)

print("These numbers could be telemarketers: ")
for suspect in suspects:
    print(suspect)
