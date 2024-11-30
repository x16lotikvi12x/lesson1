#Тип змінної int, який містить цілі числа
number = 10
#Тип змінної float, який містить не цілі числа
price = 10.2
#Тип змінної String, який містить текст/рядок
name = "Valentine"
#Тип змінної bool(boolean), який містить True або False(1 або 0)
light = True

student = 11
price_shop = 11.00
table = "Hello World"
live = True

print("Here is my veriable: ", student)

x = 1
y = 2.01
nick = "ITStep"
work = True
sum = x + y
print(x, y)
print(type(sum))

if x > y:
    print("Hello")
elif x == y:
    print("Text")
else:
    print("Wow")


a = 1
b = 2
c = 3

d = a + b * c

if a > 2:
    if d == 3:
        print("Hello World")
    elif d == 4:
        print("Hi")
else:
    print("Error")
    


for i in range(10):
    print(a)

while b < 10:
    b += 1
    print(b)

num = 5

def game():
    num = 10
    number = 20
    print(num)
    print(number)

print(num)
game()