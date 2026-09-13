# Формула сдачи: A = Σд - Σп
# Формула недостатка покупки: r = Σп - Σд

import const

shopping_list = {}
shopping_total = 0

def main():
    write_shopping_list()
    money_sum = set_money()
    count_money()
    buying_process(money_sum)

def write_shopping_list():
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
                    print("Неверный ввод. Попробуйте ещё.")
                    continue

def set_money():
    while True:
        money_sum = input("Какова ваша сумма денег?")
    
        if money_sum.isdigit():
            money_sum = int(money_sum)
            return money_sum
        else:
            print("Пожалуйста, введите целое число.")

def count_money():
    global shopping_total
    for price in shopping_list.values():
            shopping_total += price

def buying_process(money_sum):
    if shopping_total <= money_sum:
        change = money_sum - shopping_total
    
        print_products()
        print(f"\nСдача: {change} руб.")
    else:
        remainder = shopping_total - money_sum
    
        print_products()
        print(f"\nТебе не хватает: {remainder} руб.")

# выводит булево значение
def validation(good_type):
    good_price = const.AVAILABLE_GOODS.get(good_type)

    if good_price == None:
        return False
    return True

def print_products():
    print("Покупки:")
    for key, value in shopping_list.items():
        print(f"{key} - {value} руб.")

if __name__ == "__main__":
    main()