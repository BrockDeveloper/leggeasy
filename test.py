import re

reg = "^^(?:\d+|[a-z])\).*"

art = "1)mamma mia"


print(re.match(reg, art))