def compareTriplets(a, b):
    alice_point = 0
    bob_point = 0
    i = 0

    while i<=2:
        if a[i] > b[i]:
            alice_point +=1
        elif a[i] < b[i]:
            bob_point += 1
        i+=1
    return [alice_point,bob_point]


print(compareTriplets([5,6,7], [3,6,10]))