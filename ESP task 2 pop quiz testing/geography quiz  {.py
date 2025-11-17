quiz = {
    "kazakhstan": "what is the country shareing the largest border with uzbekistan?",
    "5": "How many countries border Albania",
    "3": "How many countries meet at the schengen triangle"
}
score = 0
ans_1 = input(quiz["kazakhstan"])
if ans_1 == "kazakhstan":
    print("correct")
    new_score_1 = 1
else:
    print("incorrect")
    new_score_1 = 0

ans_2 = input(quiz["5"])
if ans_2 == "5":
    print("correct")
    new_score_2 = 1 
else:
    print("incorrect")
    new_score_2 = 0

ans_3 = input(quiz["3"])
if ans_3 == "3":
    print("correct")
    new_score_3 = 1
else:
    print("incorrect")
    new_score_3 = 0

total = new_score_1 + new_score_2 + new_score_3
print("congradulations on finishing the quiz")
print("your final score is", total, "/3")