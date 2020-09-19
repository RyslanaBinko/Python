import json
from _datetime import timedelta

with open("acdc.json") as f:
    data = json.load(f)
    duration = [int(track["duration"]) for track in data ["album"]["tracks"]["track"]]
    print(timedelta(seconds = (sum(duration))))
