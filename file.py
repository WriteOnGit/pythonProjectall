
import json
cooking_book = {}
def cook_book(file):
    with open(file, 'r', encoding='UTF-8') as file:
        while True:
            name_dish = file.readline().strip().lower()
            if name_dish.strip() == '':
                break
            count_str = int(file.readline().strip())
            list_of_ingredients = []
            for string in range(count_str):
                ing = file.readline().strip().split(" | ")
                lists = {"ingredient_name": ing[0], "quantity": int(ing[1]),"measure": ing[2].strip('\n')}
                list_of_ingredients.append(lists)
            cooking_book.update({name_dish:list_of_ingredients})
            file.readline()
    return cooking_book

#print(json.dumps(cook_book('file.txt'), indent=4,ensure_ascii=False))

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
       for ingredient in cooking_book[dish]:
           new_shop_list_item = dict(ingredient)
           new_shop_list_item['quantity'] *= person_count
           if new_shop_list_item['ingredient_name'] not in shop_list:
               shop_list[new_shop_list_item['ingredient_name']] = {"measure": new_shop_list_item['measure'],"quantity": new_shop_list_item['quantity']}
           else:
               shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def yourchoise():
    people = int(input("Сколько человек будет на ужине? "))
    dishcook = input("Какие блюда приготовить? Введите через запятую ").lower().split(",")
    shoplist = get_shop_list_by_dishes(dishcook,people)
    print(json.dumps(shoplist, indent=2, ensure_ascii=False))

#print(json.dumps(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1), indent=2,ensure_ascii=False))

if __name__ == "__main__":
    cook_book('file.txt')
    yourchoise()


