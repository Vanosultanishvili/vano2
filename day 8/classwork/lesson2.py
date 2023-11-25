#for loops

i = 0 #საიტერაციო ცვლადის შეცვლა
while i < 10:
    print(i)                                        #while loop
    i += 1 #ინკრემენტაცია


for i in range(10):
    print(i)                                        #for loop


for i in range(17,20):                              #შეგვიძლია ჩავწეროთ თვის აწყების წრტილი ამ შემთხვევაში 17
    print(i)

for i in range(1,20,3):                             #შეგვიძლია ავირჩიოთ ნაბიჯი (3) 3-3 ით გაიზრდება ყოველ იტერაციაზე
    print(i)


for char in "ნიკა":
    print(char)


my_list = ["nika", "gabrieli", "dato", "soso"]

for element in my_list:
    print(element)