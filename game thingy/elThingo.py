#testing classes and maybe making a game?
#Parker Behagg
#11-9-26
class Player:
    def __init__(self, pname, x=0, y=0):
        self.name = pname
        self.pos_x = x
        self.pos_y = y
        self.stats = {"health":10, "items":{1:"blank",2:"blank",3:"blank",4:"blank",5:"blank"}, "selected_item":1}
    def move_up(self):
        self.pos_y += 1
    def move_down(self):
        self.pos_y -= 1
    def move_right(self):
        self.pos_x += 1
    def move_left(self):
        self.pos_x -= 1
    def __str__(self):
        return f"Player {self.name} is at ({self.pos_x},{self.pos_y}), Stats are: {self.stats}"
def main():
    choice = "y"
    player = Player("Mimic")
    while choice not in ["n", "N", "NO", "no", "No", "nO"]:
        choice = input("input: ")
        if choice == "w":
            player.move_up()
        elif choice == "s":
            player.move_down()
        elif choice == "a":
            player.move_left()
        elif choice == "d":
            player.move_right()
        else:
            print("invalid input, displaying stats")
        print(player)
if __name__ == "__main__":
    main()