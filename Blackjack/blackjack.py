import random
import tkinter


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    for suit in suits:
        for card in range(1, 11, 1):
            name = "./Blackjack/cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        for card in face_cards:
            name = "./Blackjack/cards/{}_{}.{}".format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # Add the image to a label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # Return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards i the hand
    # Only one case can have the avleu 11 and this will reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would go bust, chekc if there is an act and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def setup_game():
    global cards
    global deck
    global dealer_hand
    global player_hand
    global dealer_card_frame
    global player_card_frame
    # Clear UI elements
    for card in dealer_card_frame.slaves():
        card.destroy()
    for card in player_card_frame.slaves():
        card.destroy()
    result_text.set("")
    # Shuffle deck
    deck = list(cards)
    random.shuffle(deck)
    # Deal Starting Hands
    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)
    deal_player()


def play():
    setup_game()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(
    mainWindow, relief="sunken", borderwidth=1, background="green"
)

card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(
    row=0, column=0
)

tkinter.Label(
    card_frame, textvariable=dealer_score_label, background="green", fg="white"
).grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(
    row=2, column=0
)
tkinter.Label(
    card_frame, textvariable=player_score_label, background="green", fg="white"
).grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Hold", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Hit", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=setup_game)
new_game_button.grid(row=0, column=2)
cards = []
load_images(cards)

# create a new deck and shuffle
deck = list(cards)
dealer_hand = []
player_hand = []


if __name__ == "__main__":
    play()
