print('''
*********************************************************************************
                             _    _                  _ 
                            (_)  | |               |  |
                            _ ___| | __ _ _ __   __|  |
                            | / __| |/ _` | '_ \ / _` |
                            | \__ \ | (_| | | | | (_| |
                            |_|___/_|\__,_|_| |_|\__,_|                        
                                
*********************************************************************************
    ''')

print('''
Welcome to Treasure Island. 
Your mission is to find the treasure.           
''')

print("\n")
print("You are at a cross road with empty fields to both sides. Where do you want to go? Type 'left' or 'right'")
user_choice = input().lower()
if user_choice == "left":
    print("It got dark, and you are stuck in the empty field. Wolves are coming towards you. You are dead.")
    exit()
else:
    print("You made it out of the woods, you are now at a lake with harmful creatures in it. Do you want to swim across it or wait for a boat? Type 'swim' to swim across or type 'wait' to wait for a boat.")

user_choice = input().lower()
if user_choice == "swim":
    print("You made it across the lake but you are injured. It is about to rain. You find a haunted looking house with noises coming inside of it. Do you open the door or take your chances out in the rain? Type 'open' to open the door or type 'take' to take your chances out in the rain.")
else:
    print("You waited for a boat, but it never came. You are dead.")
    exit()

user_choice = input().lower()
if user_choice == "open":
    print("The noises were coming from a family making dinner, you ate well and slept well. You are safe! You are saved the next day! Congrats!")
else:
    print("You waited in the rain, and got pnemonia. You are dead.")
    exit()
