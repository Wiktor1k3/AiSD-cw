class House:
    doors: int
    color: str

    def __init__(self, doors: int, color: str) -> None:
        self.doors = doors
        self.color = color

    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            raise ValueError("New color should be different")

        self.color = new_color

    def __str__(self) -> str:
        return f'liczba drzwi: {self.doors},' \
                f'kolor elewacji: {self.color}'

    def __len__(self)-> int:
        return 100


green_house: House = House(doors=15, color='green')
blue_house: House = House(doors=10, color='blue')

print(green_house.doors)
print(green_house.color)

print(green_house)
print(blue_house)

print(len(green_house))
