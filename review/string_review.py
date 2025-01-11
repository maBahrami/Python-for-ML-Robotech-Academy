# double quote
# escape charcter
# raw string
# triplet quote



# ------ double quote
"this is Mammad's pc"


# ------ escape charcter
print('this is mammad\'s pc')  # \'
# \"
# \t
# \n
# \\

# ------ raw string
print(r"that's Carol\'s cat.")


# ------ triplet quote
print(''' Dear Alice,
      blah blahhhhhh
      blah
      blahh

      blah
      
      Mammad''')

# --------- multiline comment -------------------------------
'''
multiline comment

blaaaaaah

blah
'''
# ----------------------------------------

a = 'salam mammadoo'

a[0]

a[2:5]

a[5:]

print('salam' in a)         # true

print('gholi' not in a)     # ture

# -------- string interpolation --------------------
name = 'gholi'
age = 103
print('His name is %s. He is %s years old.' %(name, age))


# -------- f-string -------------------
name = 'gholi'
age = 103
print(f'His name is {name}. He is {age} years old.')



# -------- methods -----------------------
a = 'saALam mamMad'

b = a.title()       # 'Salam Mammad'

b = a.upper()

b = a.lower()

print(a.islower())

print(a.isupper())


b = a.upper().lower().isupper()



', '.join(['cats', 'rats', 'bats'])

' '.join(['cats', 'rats', 'bats'])



'my name is Mammad'.split()         # returns a list

'my,name,is,Mammad'.split(',')      





