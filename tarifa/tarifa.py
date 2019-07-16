"""
https://open.kattis.com/problems/tarifa

calculate available bundle in one pass

python tarifa/tarifa.py < tarifa/data/tarifa.1.in
"""
import sys


def data_plan_tracker(allowed_plan, usage):
    # calculate availbale bundle in the next month
    available_bundle = 0

    for monthly_usage in usage:
        available_bundle = available_bundle + allowed_plan - monthly_usage

    return available_bundle + allowed_plan


if __name__ == "__main__":
    data = [int(n.strip()) for n in sys.stdin.readlines()]
    allowed_plan = data[0]
    usage = data[2:]
    print(data_plan_tracker(allowed_plan, usage))
