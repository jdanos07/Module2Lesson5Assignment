# Task 1: Write a function that lets the user add items to a list.


def add_item_to_shopping_list():
    while True:
        item = input('What would you like to add to your shopping list? ').lower()
        shopping_list.append(item)

        view_list = input("View new addition on list? Yes / No - ").lower()
        if view_list =='yes':
            print(shopping_list)
            
        more_items = input('Would you like to add more items? Yes / No - ').lower()
        if more_items == 'no':
            print('Let\'s go shopping!')
            break

shopping_list = []

add_item_to_shopping_list()
