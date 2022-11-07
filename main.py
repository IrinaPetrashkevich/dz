n = int(input('Введите возраст: ')) #диапазон от 1 до 99

last_dig = n % 10  # остаток от деления на 10
if n<=0 or n>=100:
    print("Возраст не соответсвует заданному диапазону")
elif 10 < n < 20:
    print("Мне ", n, " лет")
elif 1 < last_dig < 5:
    print("Мне", n, "года")
elif last_dig == 1:
    print("Мне", n, "год")
else:
    print("Мне", n, "лет")