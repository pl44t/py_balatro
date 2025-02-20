#-------------------------Imports---------------------------------
import random

#-------------------------Variables--------------------------------
trails = 0
choice_blind_ask = 0
Small_blind_dis = ("Score at least: ⛂300     Rewards: $$$")
Big_blind_dis = ("Score at least: ⛂600     Rewards: $$$$$")
The_Hook_dis = ("Discard 2 random per hand played:     Score at least: ⛂300    Rewards: $$$$$$$$$$$")

Hands = 3
Discard = 3
points = 0
bounis_points = 0
final_points = 0
cash = final_points
rounds = 0
#---------------------------Lists----------------------------------
gamemodes = ["1. Play","2. Options","3. Quit","4. Collection"]
dif_blinds = ["1, Small blind", "2. Big blind", "3. The Hook", "4. Main menu"]
play_list = ["","",""]
collection_inventory = []
options_menu = []
Play_menu = []
Game_choice = ["What do u feel like playing:", "Ready to play again huh:", "Someones is on the grind:"]

play_list_discription = [Small_blind_dis, Big_blind_dis, The_Hook_dis]

hand_deck = []
Straight_flush = []
Four_of_a_kind = []
Full_House = []
Flush = []
Straight = []
Three_of_a_kind = []
Two_Pair = []
Pair = []
High_Card = []

in_game_options = ["1. Play hand", "2. Discard hand", "3. options", "4. quit"]

Cards_deck = ["Ace_spades", "Ace_diamonds", "Ace_hearts", "Ace_clubs", "King_spades", "King_diamonds", "King_hearts", "King_clubs",
              "Queen_spades", "Queen_diamonds", "Queen_hearts", "Queen_clubs", "Jack_spades", "Jack_diamonds", "Jack_hearts", "Jack_clubs",
              "10_spades", "10_diamonds", "10_hearts", "10_clubs", "9_spades", "9_diamonds", "9_hearts", "9_clubs",
              "8_spades", "8_diamonds", "8_hearts", "8_clubs", "7_spades", "7_diamonds", "7_hearts", "7_clubs",
              "6_spades", "6_diamonds", "6_hearts", "6_clubs", "5_spades", "5_diamonds", "5_hearts", "5_clubs",
              "4_spades", "4_diamonds", "4_hearts", "4_clubs", "3_spades", "3_diamonds", "3_hearts", "3_clubs",
              "2_spades", "2_diamonds", "2_hearts", "2_clubs"]

# ------------------------Dictionary-------------------------------
#Point_system = {
    #Straight_flush : 100,
    #Four_of_a_kind : 60,
    #Full_House : 40,
    #Flush : 35,
    #Straight : 30,
    #Three_of_a_kind : 30,
    #Two_Pair : 20,
    #Pair : 10,
    #High_Card : 5
#}


cards_value = 0
   

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def main_menu():
    print()
    print("-------------𝕭𝖆𝖑𝖆𝖙𝖗o------------")
    print()
    print()
    for menus in gamemodes:
        print(menus)
       
    choice_menu = input("What would you like to do?: ")

    #if the option u chose was avg speed if will go to that function
    if choice_menu == "Play" or choice_menu == "1":
        Play()

    elif choice_menu == "Options" or choice_menu == "2":
        Options()

    elif choice_menu == "Quit" or choice_menu == "3":
        quit()

    elif choice_menu == "Collection" or choice_menu == "4":
        Collection()

    else:
        print("There seems to be a problem, TRY AGAIN")
        main_menu()


def Play():
    global trails
    global Game_choice
    global choice_blind_ask
    trails + 1
    print()
    print("----------Ｓｅｌｅｃｔ ｇａｍｅｍｏｄｅ-----------")
    print()
    #the min just ensures that we only loop up to the length of the shorter list
    min_length = min(len(dif_blinds), len(play_list_discription))
   
    for i in range(min_length):
        print(dif_blinds[i])
        print(play_list_discription[i])
        print()

    #added on bounse that when a player has played the game more then one time, the game will treat it like that
   
    if trails == 0:
        choice_blind_ask = Game_choice[0]
       
    elif trails == 1:
        choice_blind_ask = Game_choice[1]
       
    else:
        choice_blind_ask = Game_choice[2]

    choice_blind = input(choice_blind_ask)

    # this is for going to the different difficaltes
    if choice_blind == "Small blind" or choice_blind == "1":
        small_blind()

    elif choice_blind == "Big blind" or choice_blind == "2":
        big_blind()

    elif choice_blind == "The Hook" or choice_blind == "3":
        the_hook()

    elif choice_blind == "Main menu" or choice_blind == "4":
        main_menu()

    else:
        print("There seems to be a problem, TRY AGAIN")
        main_menu()

def draw_hand():
    global hand_deck
    random.shuffle(Cards_deck)
    #randomly shuffles the deck
    return random.sample(Cards_deck, 8)
    #it returns a sample of 8 cards from the Cards deck

def discard_hand():
    global hand_deck
    global Discard
    hand = hand_deck
    print("You discarded your hand and drew new cards!")
    Discard - 1

def play_hand():
    global final_points
    global Hands
    # plus equal as it adds on the the new  equal amount
    for card in range(len(hand)):
        final_points += cards_value[hand["value"]]
    print(f"You played a hand and scored ⛂{final_points}!")
    Hands - 1
 
def small_blind():
    global hand_deck
    global Hand
    global points
    global bounis_points
    global final_points
    global cash
    global rounds
    global Discard
    for i in range(100):
        print()

    while True:
       
        for i in range(20):
            print()
        print()
        print("------------Ｓｍａｌｌ ｂｌｉｎｄ--------------")
        print()
        print("                         Score at least ")
        print("𝕊𝕞𝕒𝕝𝕝 𝕓𝕝𝕚𝕟𝕕 =    ⛂300")
        print("                         Reward = $$$")
        print()
        print(f"𝕣𝕠𝕦𝕟𝕕 𝕤𝕔𝕠𝕣𝕖 =   ⛂{final_points}")
        print(f"                {points}X{bounis_points}                    ")
        print()
        print()

        hand = draw_hand()
        print("Your Hand:", hand)
       
        print()
        print()
        print(f" Type            Hand:{Hands}       Discard:{Discard}")
        print(" info")
        print()
        print(f"                 ${cash}                ")
        print()
        print(" Type")
        print(f" Options                     Round:{rounds}")
        rounds + 1

        print()
        print()
        print()
        print()
        for In_game in in_game_options:
            print(In_game)

        game_choice = input("What would u like to do: ")

        if game_choice == ["1", "Play hand"] and Hands > 0:
            play_hand()

        elif Hands <= 0:
            print()
            print("ran out of hands")
            print()
           
        elif game_choice in ["2", "Discard hand"] and Discard > 0:
            discard_hand()

        elif Discard <= 0:
            print()
            print("ran out of discards")
            print()
           
        elif game_choice in ["3", "Options"]:
            Options()
           
        elif game_choice in ["4", "Quit"]:
            quit()
        else:
            print("Invalid choice. Try again.")
   


def big_blind():
    print()
    print("----------Ｂｉｇ ｂｌｉｎｄ-----------")
    print("ｗｏｒｋ ｉｎ ｐｒｏｓｓｅｓ")
    main_menu()

def the_hook():
    print()
    print("----------Ｔｈｅ Ｈｏｏｋ-----------")
    print("ｗｏｒｋ ｉｎ ｐｒｏｓｓｅｓ")
    main_menu()

def Options():
    print()
    print("----------Ｏｐｔｉｏｎｓ-----------")
    print("ｗｏｒｋ ｉｎ ｐｒｏｓｓｅｓ")
    main_menu()

def Collection():
    print()
    print("----------Ｃｏｌｌｅｃｔｉｏｎ-----------")
    print("ｗｏｒｋ ｉｎ ｐｒｏｓｓｅｓ")
    main_menu()

   

main_menu()
