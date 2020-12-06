import math
import itertools

input_string = """1721
979
366
299
675
1456"""

print(math.prod({sum(xs): xs for xs in itertools.combinations((map(int, input_string.split("\n"))), 2)}.get(2020)))
