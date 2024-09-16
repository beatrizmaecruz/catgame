class CardPile:
    def __init__(self, cards=None):
        if cards == None:
            self.items = []
        else:
            self.items = cards

    def __str__(self):
        return " ".join([str(number) for number in self.items])
    
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
        return print(self.items[0])

    def peek_bottom(self):
        return print(self.items[-1])

    def print_all(self, index):
        if index != 0:
            return print(" ".join([str(number) for number in self.items]))
        else:
            return print(" ".join([str(self.items[number_index]) if number_index==0 else "*" for number_index in range(len(self.items))]))
