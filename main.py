from tkinter import *
import random
flipped_cards = []
matched_cards = []
def flip_card(index):
    global flipped_cards, matched_cards, score

    if len(flipped_cards) < 2 and index not in flipped_cards and index not in matched_cards:
        buttons[index]['image']=card_images[index]
        flipped_cards.append(index)
        if len(flipped_cards) == 2:
            root.after(1000, check_match)
def check_match():
    global flipped_cards, matched_cards, score
    first, second = flipped_cards
    if cards[first] == cards[second]:
        matched_cards.append(cards[first])
        matched_cards.append(cards[second])
        score += 1
        scores['text']=f'Очки: {score}'
        if len(matched_cards) == 8:
            scores['text']=f'Вы победили! Итог: {score}'
    else:
        buttons[first]['image']=card_back
        buttons[second]['image']=card_back
    flipped_cards = []


root = Tk()
root.geometry('500x400')
root.title("Игра 'Найди пару'")
card_back=PhotoImage(file=
                     f'Cards/purple_back.png').subsample(7, 7)
buttons=[]
for i in range(8):
    button = Button(root, image=card_back,
                    width=100, height=150, command=lambda x=i: flip_card(x))
    button.grid(row=i//4, column=i%4, padx=10, pady=10)
    buttons.append(button)
score=0
scores=Label(root, text=f'Очки: {score}', font=('Arial', 15))
scores.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

card_names = ['AC', 'AD', 'AH', 'AS']
cards = card_names * 2
random.shuffle(cards)
card_images=[]
for name in cards:
    img=PhotoImage(file=f'Cards/{name}.png').subsample(7, 7)
    card_images.append(img)
root.mainloop()
