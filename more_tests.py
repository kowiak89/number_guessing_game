import random, statistics as st

records = {"Easy": [], "Medium": [10], "Hard": [10]}

def update_record(record):
    for k in record:
        if record[k] == []:
            record[k] = "N/A"
    
    print(record)

update_record(records)