# Counts the total runtime of a WRF simulation
# Usage: python3 wrf_total_time.py rsl.out.0000

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
args = parser.parse_args()

f = open(args.input, "r")
lines = [l.strip() for l in f]
f.close()

total_time = 0.0
num_steps = 0
first_step = True

for l in lines:
    if "Timing for main" in l:
        ls = l.split()
        time = float(ls[-3])
        if not first_step:
            total_time += time
            num_steps += 1
        else:
            first_step = False

print("Total steps: {}".format(num_steps))
print("Total time (s): {}".format(total_time))

