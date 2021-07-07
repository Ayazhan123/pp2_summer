  
import re
s = input()
m = re.search(r'(?!_)(\d|\w)\1',s)
if m: print(m.group(0)[0])
else:print(-1)