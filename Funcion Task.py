def most_frequent():
    string=input("Enter the string")
    D = {}
    for key in string:
        if key not in D:
            D[key] = 1
        else:
            D[key] = D[key] + 1
    print(D)
most_frequent()