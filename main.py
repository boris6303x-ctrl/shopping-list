# Формула сдачи: A = Σд - Σп
# Формула недостатка покупки: r = Σп - Σд

import const

def main():
    shopping_list = {}
    while True:
        new_good = input("Какой товар Вы бы хотели добавить в список покупок?\n")

        if new_good == "":
            print("Ввод пустой. Попробуйте ещё.")
        elif not validation(new_good):
            print("Товар не существует в магазине. Попробуйте ещё.")
        else:
            new_good_dict = {new_good: const.AVAILABLE_GOODS.get(new_good)}
            shopping_list.update(new_good_dict)

            again_prompt = input("Кое что ещё? (Введите 1, если да; 0, если нет)\n")

            if again_prompt == "0":
                break
            elif again_prompt == "1":
                continue
            else:
                print("Неверный ввод. Запустите код сначала.")
                return

    while True:
        moneysum = input("Какова ваша сумма денег?")

        if moneysum.isdigit():
            moneysum = int(moneysum)
            break
        else:
            print("Пожалуйста, введите целое число.")

    shopping_total = 0

    for price in shopping_list.values():
        shopping_total += price

    if shopping_total < moneysum:
        change = moneysum - shopping_total

        print("Список покупок:")
        for key, value in shopping_list.items():
            print(f"{key} - {value} руб.")
        print(f"\nСдача: {change} руб.")
    else:
        remainder = shopping_total - moneysum

        print("Список покупок:")
        for key, value in shopping_list.items():
            print(f"{key} - {value} руб.")
        print(f"\nТебе не хватает: {remainder} руб.")


# выводит булево значение
def validation(good_type):
    good_price = const.AVAILABLE_GOODS.get(good_type)

    if good_price == None:
        return False
    return True

if __name__ == "__main__":
    main()
