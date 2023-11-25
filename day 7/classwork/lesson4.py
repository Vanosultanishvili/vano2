#brake (დამუხრუჭება გაჩერების ბრძანება) statement

i = 5

while True:

    print(i)

    i = i - 1

    if i <= 2:
      
      break

#continue (გადახტომა გაგრძელება იტერაციის გამოტოვება)
i = 0
while i<5:
    i += 1
    if i == 3:
       print("skipping 3")
       continue
    print(i)

    
  