import random, statistics as st
records = {"Easy": [99], "Medium": [99], "Hard": [99]}
games_played = 7
stats = {"Easy": {"Mean": st.mean(records["Easy"]), "Median": st.median(records["Easy"]), "Mode": st.mode(records["Easy"])},
        "Medium": {"Mean": st.mean(records["Medium"]), "Median": st.median(records["Medium"]), "Mode": st.mode(records["Medium"])},
        "Hard": {"Mean": st.mean(records["Hard"]), "Median": st.median(records["Hard"]), "Mode": st.mode(records["Hard"])}}

print(records.keys())
records["Easy"].append(5)

# print("Can you beat the best records?")
# print("Easy: " + str(min(records["Easy"])) + "  Medium: " + str(min(records["Medium"])) +  "  Hard: " + str(min(records["Hard"])))
# print(f"Easy: {min(records["Easy"])}")
def print_stats(stat_dict, left_width, right_width):
    print("GAME STATISTICS".center(left_width + right_width + 5, "-"))
    print(f"Games Played: {games_played}\n")
    for k, v in stat_dict.items():
        print(k)
        for key in v:
            print("  - " + key.ljust(left_width, ".") + str(v[key]).rjust(right_width))

for k,v in stats.items():
    print(f"K: {k} V: {v}")
    for ik,iv in v.items():
        print(f"IK: {ik} IV: {iv}")

print_stats(stats, 12, 5)

print("     *** GAME STATISTICS ***")
print(f"Games Played: {games_played}\n")
print("-------Easy----Medium----Hard------")
print("Mean:   " + str(stats["Easy"]["Mean"]) + "       " + str(stats["Medium"]["Mean"]) + "       " + str(stats["Hard"]["Mean"]))
print("Median: " + str(stats["Easy"]["Median"]) + "       " + str(stats["Medium"]["Median"]) + "       " + str(stats["Hard"]["Median"]))
print("Mode:   " + str(stats["Easy"]["Mode"]) + "       " + str(stats["Medium"]["Mode"]) + "       " + str(stats["Hard"]["Mode"]))

# print("Game Statistics\n")
# print("EASY: " + str(stats["Easy"]))