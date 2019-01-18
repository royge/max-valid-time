import datetime
from itertools import permutations

def max_valid_time(A, B, C, D):
    def valid_time(args, last_time):
        time_text = "{0}{1}:{2}{3}".format(*args)
        try:
            time = datetime.datetime.strptime(time_text, "%H:%M")
            if last_time is None:
                return time

            if time > last_time:
                return time

            return last_time
        except ValueError:
            return last_time

    biggest_time = None
    combinations = list(permutations([A, B, C, D]))
    for x in combinations:
        biggest_time = valid_time(x, biggest_time)

    if biggest_time is None:
        return "NOT POSSIBLE"

    return biggest_time.strftime("%H:%M")

