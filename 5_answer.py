ni = int(input("number of interior walls "))
ne = int(input("number of exterior walls "))
sum_i = 0
sum_e = 0

if ni > 0 and ne > 0:
    for walls in range(ni):
       sum_i += float(input(f"Surface area of interior wall {walls+1} "))
    for walls in range(ne):
       sum_e += float(input(f"Surface area of exterior wall {walls+1} "))

print(f"Total estimated cost: {round((18*sum_i + 12*sum_e), 2)} INR")       