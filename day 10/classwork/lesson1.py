old_list = [2, 4, 6, 2, 4, 7, 2, 9]
new_list = []
for num in old_list:
    if num != 4:
        new_list.append(num)
print(new_list)

x = "zz".join(["spam", "eggs", "ham",])
print(x)

str = "apple banana tomato"
x = str.split(' ')
print(x)

x = "hello me"
print(x.replace("me", "world"))


