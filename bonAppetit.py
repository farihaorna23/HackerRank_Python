def bonAppetit(bill, k, b):
    total = 0
    length = len(bill)
    for i in range(length):
        if i != k:
            total += bill[i]
    total = total//2
    
    if total == b:
        print("Bon Appetit")
    else:
        print(b - total)