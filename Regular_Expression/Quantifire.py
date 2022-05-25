import re
matcher=re.finditer("x","abaabaaab")
for match in matcher:
	print(match.start(),"	",match.group())