import re
st  = """ python w , (ifo .ejs_world9 "900") 939 1 12 """
res = re.sub(r'\(.*\)', '', st)
print(res)


