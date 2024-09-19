# Task 3: Add a function that prints out the entire list in a formatted way.

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
            modify_list = input('Do you need to add or remove anything from the list? Add / Remove / Done- ').lower()
            if modify_list == 'add':
                add_item_to_shopping_list()
            elif modify_list == 'remove':
                remove_item_from_shopping_list()
            else:
                formatted_shopping_list()
            break

def remove_item_from_shopping_list():
    while True:
        try:
            print(shopping_list)
            item = input('What are you taking off of the list? ').lower()
            shopping_list.remove(item)
        except ValueError:
            print('That item wasn\'t on the list. ')

        modify_list = input('Would you like Add or remove anything else? Add / Remove / Done- ').lower()
        if modify_list == 'add':
            add_item_to_shopping_list()
        elif modify_list == 'remove':
            remove_item_from_shopping_list()
        else:
            formatted_shopping_list()
        break
        
def formatted_shopping_list():
    dummy_proof_list = input('Are you ready to print the shopping list? Yes / No - ').lower()
    if dummy_proof_list == 'yes':
        for index, item in enumerate(shopping_list, start=1):
            print(f'{index}- {item}')
    elif dummy_proof_list == 'no':
        add_or_remove()    

add_or_remove()