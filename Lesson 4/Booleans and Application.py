def get_int(x):
    return int(input(x))

def get_float(x):
    return float(input(x))

def get_string(x):
    return str(input(x))

name = get_string("Enter your name: ")
age = get_int("Enter your age: ")
testScore = get_float("Enter your test score: ")
passedExam = False

if age >= 16:
    if testScore >= 65:
        passedExam = True
    
    elif testScore < 65:
        passedExam = False
    
    else:
        print(f'Invalid test score')

else:
    print(f'You are not old enough to have taken the test')

if passedExam == True:
    print(f'Well done! you have passed the test with {testScore} marks out of 100 marks!')

else:
    print(f'You have failed the test')
        