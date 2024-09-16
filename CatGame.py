# Beatriz Cruz | bcru868
# AssCool.py: What Ass.py wishes it could be.
import random

class Cat:
    def __init__(self, name):
        if name == "cat" or name == "Cat":
            print("(Not very original but ok.)")
        self.name = name
        self.eating_type = random.choice(["simple", "habitual", "picky"])
        
    def __str__(self):
        return f"{self.name} is a {self.eating_type} eater!"

    def explain_eating(self, card_amount):
        if self.eating_type == "simple":
            eating_condition = "in ascending order in one bowl."
        elif self.eating_type == "picky":
            eating_condition = f"from 1 to {card_amount//2} in one bowl and {(card_amount//2 +1)} to {card_amount} in another."
        elif self.eating_type == "habitual":
            eating_condition = "split in ascending odds in one bowl and ascending evens in another bowl."
        return f"Since {self.name} is a {self.eating_type} eater, they will only eat if the food is {eating_condition}"

    def get_eating_type(self):
        return self.eating_type

    def get_name(self):
        return self.name

class CardPile:
    def __init__(self, cards=None):
        if cards == None:
            self.items = []
        else:
            self.items = cards

    def __str__(self):
        return " ".join([str(number) for number in self.items])

    def get_full_pile(self):
        return self.items
    
    def add_top(self, item):
        return self.items.insert(0, item)
        
    def add_bottom(self, item):
        return self.items.append(item)

    def remove_top(self):
        return self.items.pop(0)

    def remove_bottom(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek_top(self):
        return self.items[0]

    def peek_bottom(self):
        return self.items[-1]

    def print_all(self, index):
        if index != 0:
            return print(" ".join([str(number) for number in self.items]))
        else:
            return print(" ".join([str(self.items[number_index]) if number_index==0 else "♥" for number_index in range(len(self.items))]))


class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = round(self.num_cards * 1.75)
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
            
    def get_pile(self, i):
        return self.piles[i]

    def get_piles(self):
        return [self.piles[i].get_full_pile() for i in range(len(self.piles))]

    def display(self):
        for pile_index in range(self.num_piles):
            if pile_index == 0:
                print(f"Packs (0): ", end="")
            else:
                print(f"Bowl {pile_index}: ", end="")
            self.piles[pile_index].print_all(pile_index)
        return

    def move(self, p1, p2, eating_type):
        if p1 == p2 == 0 and self.piles[0].size() != 0:
                self.piles[0].add_bottom(self.piles[0].remove_top())
                
        if eating_type == "simple":
            if p1 == 0 and p2 > 0 and self.piles[0].size() != 0:
                if self.piles[p2].size() > 0 and self.piles[0].peek_top() == (self.piles[p2].peek_bottom()) + 1:
                        self.piles[p2].add_bottom(self.piles[0].remove_top())
                elif self.piles[p2].size() == 0:
                    self.piles[p2].add_bottom(self.piles[0].remove_top())
            elif p1 > 0 and p2 > 0 and self.piles[p1].size() != 0 and self.piles[p2].size() != 0 and self.piles[p1].peek_top() == (self.piles[p2].peek_bottom() + 1):
                [self.piles[p2].add_bottom(self.piles[p1].remove_top()) for round in range(self.piles[p1].size())]
                
        elif eating_type == "habitual":
            if p1 == 0 and p2 > 0 and self.piles[0].size() != 0:
                if self.piles[p2].size() > 0 and self.piles[0].peek_top() == (self.piles[p2].peek_bottom()) + 2:
                        self.piles[p2].add_bottom(self.piles[0].remove_top())
                elif self.piles[p2].size() == 0:
                    self.piles[p2].add_bottom(self.piles[0].remove_top())
            elif p1 > 0 and p2 > 0 and self.piles[p1].size() != 0 and self.piles[p2].size() != 0 and self.piles[p1].peek_top() == (self.piles[p2].peek_bottom() + 2) :
                [self.piles[p2].add_bottom(self.piles[p1].remove_top()) for round in range(self.piles[p1].size())]
                
        elif eating_type == "picky":
            midpoint_bottom = self.num_cards // 2
            midpoint_top = self.num_cards//2 + 1
            if p1 == 0 and p2 > 0 and self.piles[0].size() != 0:
                if self.piles[p2].size() == 0:
                    self.piles[p2].add_bottom(self.piles[0].remove_top())
                elif self.piles[0].peek_top() == (self.piles[p2].peek_bottom() + 1):
                    if self.piles[0].peek_top() != midpoint_top and self.piles[p2].peek_bottom() != midpoint_bottom:
                        self.piles[p2].add_bottom(self.piles[0].remove_top())
                        
            elif p1 > 0 and p2 > 0 and self.piles[p1].size() != 0 and self.piles[p2].size() != 0:
                if self.piles[p1].peek_top() == (self.piles[p2].peek_bottom() + 1) and (self.piles[p1].peek_top() != midpoint_top or self.piles[p2].peek_bottom() != midpoint_bottom):
                    [self.piles[p2].add_bottom(self.piles[p1].remove_top()) for round in range(self.piles[p1].size())]
            

    def is_complete(self, eating_type):
        piles_with_cards = [index for index in range(self.num_piles) if self.piles[index].size() != 0]
        
        if eating_type == "simple":
            if self.piles[0].size() != 0 or len(piles_with_cards) != 1:
                return False
            else:
                pile_index = piles_with_cards[0]
                for card_index in range((self.piles[pile_index].size())-1):
                    if self.piles[pile_index].items[card_index] != self.piles[pile_index].items[card_index+1]-1:
                        return False            
            return True
        
        elif eating_type == "habitual":
            if self.piles[0].size() != 0 or len(piles_with_cards) != 2:
                return False
            else:
                for pile_index in piles_with_cards:
                    for card_index in range((self.piles[pile_index].size())-1):
                        if self.piles[pile_index].items[card_index] != self.piles[pile_index].items[card_index+1]-2:
                            return False
                return True
            
        elif eating_type == "picky":
            if len(piles_with_cards) == 2:
                valid_list_1 = [value for value in range(1, (self.num_cards // 2)+1)]
                valid_list_2 = [value for value in range((self.num_cards//2) + 1, self.num_cards+1)]
                if valid_list_1 in self.get_piles() and valid_list_2 in self.get_piles() and self.get_piles()[0] == []:
                    return True
            return False
            
        
    def play(self, cat):
        print("{:^100}".format(" CATSITTING "), end="\n")
        move_number = 1

        while move_number <= self.max_num_moves and not self.is_complete(cat.get_eating_type()):
            print("{:-^100}".format(f" ROUND {move_number} OF {self.max_num_moves} "))
            self.display()
            row1 = int(input("From "))
            row2 = int(input("To "))
            if row1 >= 0 and row2 >= 0 and row1 < self.num_piles and row2 < self.num_piles:
                self.move(row1, row2, cat.get_eating_type())
            move_number += 1
            
        print("{:-^100}".format(f" CATSITTING IS OVER "))
        self.display()
        
        if self.is_complete(cat.get_eating_type()):
            print(cat.get_name(), "is a happy cat! You fed them in", move_number - 1, "moves!\n")
        else:
            print(cat.get_name(), "is not happy with this. They've phoned SPCA. Don't ask how they translated from meows.")

def main():
    cat = Cat(input("You've just adopted a cat.\nName this fluffball right now: "))
    cards_amount = random.randrange(10, 26)
    cards = [number for number in range(1, 16)]
    random.shuffle(cards)
    print("\nCongratulations on your new cat!\nBe aware that", cat, "\n")
    print(cat.explain_eating(len(cards)), "\n")
    
    game = Solitaire(cards)
    game.play(cat)

main()

