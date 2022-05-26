txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.5))

txt1 = "My name is {fname}, I'm {age}".format(fname = "Rafael", age=22)

print(txt1)

txt3 = 'The temperature is betwween {:-} and {:-} degrees celsius.'
print(txt3.format(-3, -7))

import keyword
print(keyword.kwlist)
