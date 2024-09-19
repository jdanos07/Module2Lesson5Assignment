# Task 2: Include a function to remove items from the list.

shopping_list = []

def add_or_remove():
    decision = input('Are you adding to, or removing from, your list? Adding / Removing - ').lower()
    if decision == 'adding':
        add_item_to_shopping_list()
    elif decision == 'removing':
        remove_item_from_shopping_list()
    else:
        print('Are you sleep shopping?') 

def add_item_to_shopping_list():
    while True:
        item = input('What would you like to add to your shopping list? ').lower()
        shopping_list.append(item)

        view_list = input('View new addition on list? Yes / No - ').lower()
        if view_list =='yes':
            print(shopping_list)
            
        more_items = input('Would you like to add more items? Yes / No - ').lower()
        if more_items == 'no':
            modify_list = input('Do you need to remove anything from the list? Yes / No - ').lower()
            if modify_list == 'no':
                print('Let\'s go shopping!')
                break
            elif modify_list == 'yes':
                remove_item_from_shopping_list()
           

def remove_item_from_shopping_list():
    while True:
        try:
            print(shopping_list)
            item = input('What are you taking off of the list? ').lower()
            shopping_list.remove(item)
        except ValueError:
            print('That item wasn\'t on the list. ')

        modify_list = input('Would you like Add or remove anything else? Add / Remove - ').lower()
        if modify_list == 'add':
            add_item_to_shopping_list()
        
        

add_or_remove()