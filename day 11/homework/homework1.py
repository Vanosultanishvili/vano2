def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("ეს ასამკუთხედი იარსებებს")
    else:
        print("ეს სამკუთხდი არ იარსებებს")

triangle(6,4,4)
triangle(6,2,2)