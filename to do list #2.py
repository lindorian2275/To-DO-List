#Jonathan and Dorian
#Shopping List
#1/10/24


#Functions
def intro(user, game):
    print("Hello " + user + " you are playing the game"+ game + " have a good time!")
#Function 2 (Outro)
def outro(user, game):
    print("Thank you "+ user + " for playing the game " + game + ", goodbye")
#Thank user fopr playing game using a string


intro("Jonathan and Dorian", "Shopping List")




shoppinglist = ["Milk", "Rice", "Chicken", "Apples", "Olive oil", "Bread", "Cheetos"]


def display_list():
    #Display the current shopping list
    print("Your current shopping list is", shoppinglist)




while True:
    option = int(input("What do you want to do? \nAdd a task to the to-do list  = 1  \nView the current to-do list = 2 \nMark a task as completed  = 3 \nRemove a task from the to-do list  = 4 \nExit the program = 5 \nRemove all items from list = 6 \nSort list alphabetically = 7 \nCount number of items on list = 8 \n Action choice: "))
    if (option==1) : #adds an item to the list
        todo = input("What item would you like to add?")
        shoppinglist.append(todo)
    if (option == 2): #print the current list
        display_list()
    if (option== 3): #marks an item as done using the letter X
        ans = input("Select an item from the list to mark as done: ")
        print(ans)
        i = shoppinglist.index(ans)
        print(i)
        shoppinglist[i]=ans + " X"
        print(shoppinglist)
    if(option==4) : #removes an item from the list
        removet = input("Which item would you like to remove?")
        shoppinglist.remove(removet)
    if(option==5) : #closes the program
        print("Goodbye!")
        outro("Jonathan and Dorian", "Shopping List")
        break
    if(option==6): #removes all tasks from list
        shoppinglist.clear()
        print(shoppinglist)
    if(option==7): #sorts list alphabetically
        shoppinglist.sort()
        print(shoppinglist)
    if(option==8): #count number of items on list
        print(len(shoppinglist))
    
