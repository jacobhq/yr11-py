max = int(input("How many terms to generate: "))
fibonnaci = [0, 1]

while len(fibonnaci) < max:
    fibonnaci.append(fibonnaci[-2:][0] + fibonnaci[-2:][1])

print(fibonnaci)