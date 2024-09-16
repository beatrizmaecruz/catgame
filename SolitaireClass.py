class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
            
    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for pile_index in range(self.num_piles):
            print(f"{pile_index}: ", end = "")
            self.piles[pile_index].print_all(pile_index)
        return
