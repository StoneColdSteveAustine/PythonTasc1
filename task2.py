number = int(input("Введите трёхзначное число: "))
while number // 1000 > 0 :   
    if number//1000 > 0:
        print("Число не является трёхзначным")
        number = int(input("Введите трёхзначное число: "))

sum = 0
while number / 10 > 0:
    sum = sum + number % 10
    number //= 10

print(f"Сумма цифр трёхзначного числа равна: {sum}")
