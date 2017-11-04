import sys
import re

pattern_1 = r"`[^']*'"
pattern_2 = r"'[^`]*`"
for line in sys.stdin:
    new_str = line.strip()
    print(re.sub(pattern_1, r"`'", new_str, 1))
    print(re.sub(pattern_2, r"'`", new_str, 1))
