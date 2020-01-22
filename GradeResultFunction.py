def grades():
    try:
        grade = float(input("Please enter a student grade "))
    except:
        print("Please enter a numeric value")

    if grade > 1.0:
        raise Exception("Only numbers between 0.0 and 1.0 allowed")
    elif grade>=0.9:
        print(str("A"))
    elif grade<0.9 and grade>=0.8:
        print(str("B"))
    elif grade<0.8 and grade>=0.7:
        print(str("C"))
    elif grade<0.7 and grade>=6:
        print(str("D"))
    else:
        print(str("F"))

grades()