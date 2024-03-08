def a(quantity):
    number = 1
    i = 0
    while i < quantity:
        print(number)
        number += 2
        i += 1
a(5)

print()

def b(quantity):
    i = 0 
    number = 2
    while i < quantity:
        print(number)
        number *= 2
        i += 1
b(7)

print()    

def c(quantity):
    i = 0
    number = 0
    while i < quantity:
        print(number ** 2)
        number += 1
        i += 1

c(8)
print()

def d(quantity):
    i = 0
    number = 2
    while i < quantity:
        print(number ** 2)
        number += 2
        i += 1

d(5)
print()

def e(quantity): 
  sequence = [1, 1]
  i = 0
  while i < quantity:
    print(sequence[i])  
    sequence.append(sequence[-1] + sequence[-2])
    i += 1

e(7)

# Sem lógica matemática por trás -> 200 o próximo número que começa com 'D'