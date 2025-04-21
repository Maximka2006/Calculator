from octal_compf import OctalCompf



# Левоассоциативность 
left_c = OctalCompf()
print(left_c.compile("10-5-1")==left_c.compile("(10-5)-1"))

# Правоассоциативность
right_c = OctalCompf(right_assoc=["-"])
print(right_c.compile("10-5-1")==right_c.compile("10-(5-1)"))
print(right_c.compile("10+5+1")==right_c.compile("10+(5+1)"))