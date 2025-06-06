import random
player_points = 0
player_inventory = [["◆","★","✿"]]
theme = ["◆","★","✿"]

def treasure_hunt():

    def manage_inventory():
        global player_inventory, theme
        print("\n---------------------------------------------------")
        print(f"Your current inventory: ")
        for each_theme in player_inventory:
            print(f"    {each_theme}")
        print("---------------------------------------------------")
        print(f"\nYour current theme: {theme}")
        print(f"\nChange current theme? type (yes/no)")
        change_theme_or_not = input().lower()
        if change_theme_or_not == "1" or change_theme_or_not == "yes":
            print("\nchoose from the following themes: ")
            theme_count = 1
            for themes in player_inventory:
                print(f"{theme_count}. {themes}")
                theme_count +=1
            selected_theme_number = input(f"\nSelect theme from [1 --> {theme_count-1}]: ")
            selected_theme_number = int(selected_theme_number)
            if selected_theme_number < theme_count:
                theme.clear()
                theme.extend(player_inventory [selected_theme_number-1])
                print(f"\nCurrent theme: {theme}\n")
            else:
                print("\nInvalid theme selected")
                print("Process cancelled!\n")
        else:
            print("\nProcess cancelled!")

    def the_game():

        global player_points,theme
        shape1 = theme[0]
        shape2 = theme[1]
        shape3 = theme[2]
        grid = []
        position = [0,0] 
        avatar = {'left':'◄', 'up':'▲', 'down':'▼','right':'►','<':'◄', '^':'▲', 'v':'▼', '>':'►'}
        points = 0  

        def make_list (grid):
            all_elements = ["•"]*44 + [shape1]*3 + [shape2]*2 + [shape3] #list of all elements in the grid that can be chosen randomely to generate one random grid each time
            for index1 in range(9): #generates 9 rows and makes the final grid
                rows = []
                for index2 in range(9): #makes one row containing 9 elements
                    random_selector = random.randint(0, len(all_elements) - 1) #chooses number between 1 and 49
                    element = all_elements[random_selector] #assigns element based on index of the random number
                    rows.append(element) #assigns element to the inner row
                grid.append(rows) # assigns all fabricated rows into one single grid
                grid[0][0] = "O"  #chooses the player's location 

        def move(movement_type, grid, position):
            direction = {'right':(0,1),'left':(0,-1), 'up':(-1,0), 'down':(1,0), '<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)} #key containing x and y coordinates for all directions
            x = direction[movement_type][0] #assigns x to first tuble of the chosen direction
            y = direction[movement_type][1] #assigns y to second tuble of the chosen direction
            if (position[0]+x < 9 and position[0]+x > -1) and (position[1]+y < 9 and position[1]+y > -1): #checks to make sure player isnt's out of bounds
                if grid[position[0]+x][position[1]+y] == "•": #checks if the next position is "•"
                    change_position(x,y,grid,position, movement_type) #function to change x and y positions and place player avatar in new position
                elif grid[position[0]+x][position[1]+y] in [shape1, shape2, shape3]: #checks if the next position is one of the prize symbols
                    symbol = grid[position[0]+x][position[1]+y] #assigns the current prize symbol to a variable to be passed onto the function that collects points based on the current shape
                    change_position(x,y,grid,position, movement_type)
                    collect_points(symbol)
            else:
                print("Cannot move there!") #message appears if the player is out of bounds

        def change_position(x,y,grid,position,movement_type):
            grid[position[0]][position[1]] = "•" #makes current postion "•" instead of avatar
            position[0]+=x #changes position in x direction
            position[1]+=y #changes position in y direction
            grid[position[0]][position[1]] = avatar[movement_type] #changes new position into the player's avatar
            print_updated_list(grid) #prints updated version of the grid with the new position

            
        def play(grid):
            allowed_movements = ["right", "left", "up", "down", ">", "<", "^", "v"] #a list of all allowed inputs and movement types
            while True :
                whole_string_s = "".join(map(str,grid)) #converts grid into one single string
                if shape1 not in whole_string_s and shape2 not in whole_string_s and shape3 not in whole_string_s: #checks to see if there are no more prizes to collect and ends the game
                    print("\nYou win!")
                    break
                movement_type = input().lower() #takes the chosen movement from the user
                if movement_type == "exit": #ensures player can exit at anytime and reak out of the loop
                    break
                elif movement_type in allowed_movements: #ensures the chosen movement is whithin the allowed ones from the list above
                    move(movement_type, grid, position) #runs the function responsible for moving thee player in all directions
                
        def collect_points(symbol): #function that identifies the prize and assigns points ased on that specific prize
            nonlocal points
            if(symbol) == shape1:
                points += 1
                print (f"+1 point!")
            elif(symbol) == shape2:
                points += 3
                print (f"+3 points!")
            elif(symbol) == shape3:
                points += 5
                print (f"+5 points!")

                            
        def print_updated_list(grid): #prints the grid as 9 seperate strings for better readability for the player
            print("----------------------------")
            for row in grid:
                string_s = " ".join(map(str, row))
                print(string_s)
            print("\nType \"exit\" to exit the game anytime")
    
        make_list(grid)   
                    
        print("O ---> you")
        print(f"{shape1} = 1 point")
        print(f"{shape2} = 3 points")
        print(f"{shape3} = 5 points")   
            
        print ("""----------------------------
        Actions:          type:
            
        (move left)  -->  "left"  or "<"
        (move right) -->  "right" or ">"
        (move up)    -->  "up"    or "^"
        (move down)  -->  "down"  or "v"
        (exit game)  -->  "exit"        
        ----------------------------
        """)
        print_updated_list(grid) 
        play(grid)
        print(f"+{points} points earned in total!")
        player_points += points #passes earnings to the global main player points for later use
        print(f"Total points = {player_points}")

    def gamestore():
        price = 30
        themes = {'1':["🍎", "🍌", "🍇"],
                '2':["🍕","🍔","🍟"], 
                '3':["🍦","🧁","🍰"],
                '4':["⚾️","🏀","⚽️"],
                '5':["🐰","🦊","🦁"], 
                '6':["🦐","🐟","🦑"],
                '7':["🌻","🌹","🌷"],
                '8':["🐤","🦢","🦉"], 
                '9':["✨","🌎","🌞"],
                '10':["🥒","🍅","🧄"]}
                
        
        print (f"\nTotal points owned: {player_points}")  
        print("-------------------theme store---------------------")
        print (f"1.Fruits theme:   {themes['1']}")
        print (f"2.Fastfood theme: {themes['2']}")
        print (f"3.sweets theme:   {themes['3']}")
        print (f"4.sporty theme:   {themes['4']}")
        print (f"5.animal theme:   {themes['5']}")
        print (f"6.marine theme:   {themes['6']}")
        print (f"7.flora theme:    {themes['7']}")
        print (f"8.birds theme:    {themes['8']}")
        print (f"9.space theme:    {themes['9']}")
        print (f"10.veggies theme: {themes['10']}")



        def take_theme_choice():
            global player_points, player_inventory
            possible_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]
            purchase_or_not = input("\nWould you like to purchase a theme? type (yes/no): ").lower()
            if purchase_or_not == "yes":
                theme_choice = input("\nChoose a theme from [1 --> 10]: ")
                if theme_choice in possible_choices:
                    print(f"\nthis theme --> {themes[theme_choice]} is worth 30 points.")
                    purchase_choice = input("\nProceed with the purchase? type (yes/no): ").lower()
                    if purchase_choice == "yes":
                        if player_points >= price:
                            player_points -= price
                            print("\npurchase complete!")
                            print(f"Total points = {player_points}\n")
                            player_inventory.append(themes[theme_choice])
                        else:
                            print("\nInsufficient balance!\n")
                    else:
                        print("\npurchase cancelled\n")
                else:
                    print("\nInvalid selection")
                    print("purchase cancelled\n")
            
        take_theme_choice()         
    while True:
        print("\n-------------------treasure hunt-------------------")
        print("\n1.[play]")  
        print("2.[change theme/inventory]") 
        print("3.[store]")
        print("4.[exit to main menu]\n") 
        print("---------------------------------------------------")
        print("Type from [1 --> 4] to choose")
        play_or_theme_or_store = input().lower()
        if play_or_theme_or_store == "1" or play_or_theme_or_store == "play":
         the_game () 
        elif play_or_theme_or_store == "2" or play_or_theme_or_store == "change theme":
            manage_inventory()
        elif play_or_theme_or_store == "3" or play_or_theme_or_store == "store":
            gamestore()           
        elif play_or_theme_or_store == "4" or play_or_theme_or_store == "exit":
            print("Thanks for playing!")  
            break 


              
                
treasure_hunt()



          
        























