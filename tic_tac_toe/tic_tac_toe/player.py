class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def get_name(self) -> str:
        return self.name

    def get_symbol(self) -> str:
        return self.symbol
