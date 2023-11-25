#დავალება: ბილეთი ღირს 25 ლარი მაგრამ ბავშვებისთვის უფასოა გვყავს 13 ადამიანი აქიდან 10 დიდი და 3 ბავშვი
#გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ (while loop - ის და continue - ს გამოყენებით)

i = 0
while i <= 13:
    i += 1
    if i == 4:
        print("children 1 (free)")
        continue
    if i == 7:
        print("children 2 (free)")
        continue
    elif i == 9:
        print("children 3 (free)")
        continue
    elif i == 1:
        print("1 adult 25$")
    elif i == 2:
        print("2 adult 25$")
    elif i == 3:
        print("3 adult 25$")
    elif i == 5:
        print("4 adult 25$")
    elif i == 6:
        print("5 adult 25$")
    elif i == 8:
        print("6 adult 25$")
    elif i == 10:
        print("7 adult 25$")
    elif i == 11:
        print("8 adult 25$")
    elif i == 12:
        print("9 adult 25$")
    elif i == 13:
        print("10 adult 25$")
    

print("10 adults and 3 children in total 25 x 10 = 250 dollars ")