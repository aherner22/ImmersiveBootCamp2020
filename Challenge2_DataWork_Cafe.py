"""DataWork Cafe Ordering App"""

print("\n--------Welcome to DataWork Cafe!--------\n")           #greet your customers 

menu = {'coffee': {'espresso':1.50,        #create a nested dictionary for the menu
                    'americano':2.00, 
                    'caffe latte':2.25, 
                    'mocha':2.25, 
                    'cappucino':2.50, 
                    'macchiato':2.50
                   },             
               'tea': {'white tea':1.50, 
                        'green tea':2.00, 
                        'oolong tea':2.25, 
                        'black tea':2.25, 
                        'earl grey':2.25, 
                        'matcha':2.50
                       },
               'pastries': {'croissant':5.50, 
                            'cinnamon roll':4.50, 
                            'banana bread':4.25, 
                            'pumpkin bread':3.75, 
                            'sticky bun':4.25, 
                            'apple turnover':3.75
                             }
                }

#greeting question prompt
see_menu = input("Would you like to see the menu? (y/n): ")   

#if see_menu is yes 'y', print menu
if see_menu.lower() == 'y':
    for item, sub_item_list in menu.items():      #print menu categories
        print(f"\n{item.title()}: ")
        for sub_item, price in sub_item_list.items():    #print menu items and prices
            print(f"\t{sub_item.title()}________${price:.2f}")

#if see_menu is no 'n' (or any letter != 'y'), skip to order request

#Ordering question prompt
order_request = input("\nWould you like to place an order? (y/n): ")
order_request = order_request.lower()
#send customer to end of app message if order_request is no 'n'
if order_request == 'n':
    order_active = False
else:
    order_active = True      #otherwise send to while loop to order

#holds customer's order and quantity
responses = {}

#while loop so customer can order more than one item
while order_active:    #while order_request is yes 'y'
    
        order = input("What would you like to order? ")
        order = order.lower()
        quantity = input("How many of that item? ")
        quantity = int(quantity)

        not_listed = []         #fills list with 0 or 1, with each loop, if 1 then item not listed

        for request in menu.values():
            if order.lower() in request.keys():
                responses[order] = quantity
                not_listed.append(0)
            else:
                not_listed.append(1)

        if sum(not_listed) == len(not_listed):        #if the sum of all values in not_listed equals the number of items in not_listed
            print("I'm sorry, we do not carry that item.")     
                
        order_again = input("Would you like to order something else? (y/n) ")
        order_again = order_again.lower()
        if order_again == 'y':
            continue             #continue back to beg of while loop
        else:
            order_active = False   #no more orders, exit while loop

            subtotal = 0     #declare subtotal variable

            print("\nCustomer Order:")
            print("...........................")

            for ordered_item, amount in responses.items():
                print(f"{ordered_item.title()}...........{amount}...")

                #printing price of items
                for item in menu.values():
                    if ordered_item in item.keys():
                        value = item[ordered_item] * amount

                subtotal += value     #add price of each item
            tax = subtotal * 0.06     #MD state tax 6%
            cost = subtotal + tax

            print("---------------------------")
            print("   CUSTOMER RECEIPT")
            print("---------------------------")
            print(f"Subtotal:      ${subtotal:.2f}")
            print(f"Sales tax:     ${tax:.2f}")
            print(f"Grand Total:         ${cost:.2f}")

print("\nThank you for stopping by DataWork Cafe!\n")
                