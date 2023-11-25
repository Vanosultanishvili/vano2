user_score1 = float(input("enter score N1: "))
user_score2 = float(input("enter score N2: "))
user_score3 = float(input("enter score N3: "))
user_score4 = float(input("enter score N4: "))

avg_score = (user_score1 + user_score2 + user_score3 + user_score4) / 4

if avg_score>=9 and avg_score<=10:
    print("გილოცავ მატრიცელო, შენი ქულაა: " + str(avg_score) + " შენ მოიგე 300 ლარიანი ბანძი ტოსტერი რომელსაც შეალიე შენი ცხოვრების წლები")
elif avg_score >5 and avg_score <9:
    print(""შენი ქულაა: " str(avg_score) + " "YOU ARE MID")
elif avg_score >10 and avg_score <0:
    print("შენი ქულაა: " + str(avg_score) + " there is something wrong with you")


