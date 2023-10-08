sum = 0
while True:
    tiv = input("Greq tiv: ")
    try:
        if tiv == '':
            # print(sum)
            break
        else:
            tiv = float(tiv)
            sum += tiv
        # print(sum)
    except ValueError:
        print("Enter True Value[float]")