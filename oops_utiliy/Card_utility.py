

# Write a Program DeckOfCards.java, to initialize deck of cards having suit ("Clubs",
# "Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
# "Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then
# distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players
# using 2D Array…



import random

class Cardgame:

    #creating a constructor with private and public instanace variables
    def __init__(self):
        #different ranks
        self.__rank = [2,3,4,5,6,7,8,9,10]
        #different suits
        self.__suits = ["ace","jack","queen","king"]
        #creating a deck array to store the cards
        self.deck = []

        #adding a ranks in to a deck
        for i in self.__rank:
            self.deck.append(str(i))

        #adding a diffrent suits into a deck
        for j in self.__suits:
            self.deck.append(str(j))


    #this is method to distibute the cards to the all playears
    def distribute(self):
        try:# putting try block for a user input exception
            deck = self.deck
            # taking input from the user about number of players
            players = int(input("enter the number players : "))

            # adding all the plyaers into the array
            array = [[] for i in range(players)]

            # using a random.suffule,sufffle the deck for each players
            for i in range(players):
                random.shuffle(deck)

                # distributing the differs set of cards to the each players
                for j in range(9):
                    array[i].append(deck[j])

            return array

        except ValueError as v:# value error is for user valur type,catching ut using except block
            print("enter the correct players \n",v)



#creating a object for class
card = Cardgame()

#main mathod execution
if __name__ == "__main__":
    card.distribute()