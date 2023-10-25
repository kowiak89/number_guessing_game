import random, statistics as st

records = {"Easy": [10], "Medium": [10], "Hard": [10]}

def update_record(record):
    guess = random.randint(1,10)
    record["Easy"].append(guess)
    print_record(record)


def print_record(record):
    if len(record["Easy"]) < 5:
        print(record)
        update_record(record)



update_record(records)

stats = {"Easy": {"Mean": st.mean(records["Easy"]), "Median": st.median(records["Easy"]), "Mode": st.mode(records["Easy"])},
        "Medium": {"Mean": st.mean(records["Medium"]), "Median": st.median(records["Medium"]), "Mode": st.mode(records["Medium"])},
        "Hard": {"Mean": st.mean(records["Hard"]), "Median": st.median(records["Hard"]), "Mode": st.mode(records["Hard"])}}

def update_stats(stats):
    print(stats["Easy"])

update_stats(stats)
