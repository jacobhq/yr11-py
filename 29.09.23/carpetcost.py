w = int(input("Width: "))
h = int(input("Height: "))

initial_cost = 150

def cost(w, h):
  cost = (w * h) + initial_cost
  return round(cost, 2)

print(f"Cost is £{cost(w, h)}")