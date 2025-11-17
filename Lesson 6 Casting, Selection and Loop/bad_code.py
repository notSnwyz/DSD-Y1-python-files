def hospital():
    NAME = input("enter Patient Name:")
    Age = int(input("AGE:"))
    height = float(input("height"))
    weight = float(input("WEIGHT"))
    bmi = weight / (height * height)

    if bmi > 30:
        print("overweight")
    else:
        print("ok")

    if Age > 65:
        print("Old person discount applied")

    print("Patient:",NAME,"has bmi of",bmi)

hospital()