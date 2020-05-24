'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
'''
def not_string(str):
  if str.split()[0] == "not":
    return str
  else:
    return "not {}".format(str)