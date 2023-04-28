while True:
    number = input("Введите шестизначный номер билета: ")
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print("Поздравляю, Ваш билет счастливый!")
        else:
            print("К сожалению, Ваш билет не счастливый.")
        break
    else:
        print("Пожалуйста введите корректный номер билета")
