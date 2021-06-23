
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


playing = True


class Cards():

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"The {self.rank} of {self.suit}"


class Deck():

    def __init__(self):

        self.all_cards = []

        for x in suits:
            for y in ranks:
                self.all_cards.append(Cards(x, y))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def deal_cards(self):
        single_card = self.all_cards.pop()
        return single_card


class Hand():

    def __init__(self,):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")

        else:
            if chips.bet > chips.total:
                print(
                    f'Sorry, you dont have enough chips! You have: {chips.total} chips')
            else:
                break


def hit(deck, hand):

    hand.add_cards(deck.deal_cards())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understant that, Please enter h or s only!")
            continue

        break


def player_busts(player, dealer, chips):
    print('Bust PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS')
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH")


def show_some(player, dealer):
    print("DEALERS HAND:")
    print("one card hidden!")
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("DEALERS HAND:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYERS HAND")
    for card in player.cards:
        print(card)


while True:

    print("WELCOME TO BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_cards(deck.deal_cards())
    player.add_cards(deck.deal_cards())

    dealer = Hand()
    dealer.add_cards(deck.deal_cards())
    dealer.add_cards(deck.deal_cards())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player, dealer)

    while playing:

        hit_or_stand(deck, player)

        show_some(player, dealer)

        if player.value > 21:
            player_busts(player, dealer, player_chips)

            break

    if player.value <= 21:

        while dealer.value < player.value:
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)
        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)
        else:
            push(player, dealer)

    print(f'\n Player total chips are at {player_chips.total}')

    new_game = input("Would you like to play another hand? y/n")

    if new_game.lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing")
        break
