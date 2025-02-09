planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

# ---------------------------------------------------------------

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

# ------------------------------------------------------------------

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')   

# -------------------------------------------------------------------

for i in range(5):
    print("Doing important work. i =", i)

# ---------------------------------------------------------------------

i = 0
while i < 10:
    i += 1 # increase the value of i by 1
    print(i, end=' ')

# --------------------------------------------------------------------

squares = [n**2 for n in range(10)]
print('\n',squares)

# ----------------------------------------------------------------------

planet = [planet for planet in planets if len(planet)<6]
print(planet)

pla = [pla.upper()+'!' for pla in planets if len(pla)>5]
print(pla)