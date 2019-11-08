# Extend the above program to create a Player Object having Deck of Cards, and
# having ability to Sort by Rank and maintain the cards in a Queue implemented using
# Linked List. Do not use any Collection Library. Further the Player are also arranged
# in Queue. Finally Print the Player and the Cards received by each Player.


from Cardgame_Queue.Implementation_Of_Queue_Using_Singlelinkedlist.Queue_Using_Singlelinkedlist import Queue
from oops_utiliy.Card_utility import Cardgame


class Card_Game1:
    #method for play card game and add the result to queue
    def plyaing_game(self):

        #creating a object for queue class
        q = Queue()

        #adding the result to the data<"list">
        card = Cardgame()
        data = card.distribute()
        print(type(data))

        #sorting and adding each element to the queue
        for hand in range(len(data)):
            data[hand].sort()
            q.EnQueue(data[hand])

        #print the data
        q.Display()

#creating a instance for card_game1 class
card1=Card_Game1()


# main method excecution
if __name__=="__main__":
    card1.plyaing_game()