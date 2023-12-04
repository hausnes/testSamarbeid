class Karakter():
    def __init__(self, navn, hp, styrke):
        self.navn = navn
        self.hp = hp
        self.styrke = styrke
    
    def __str__(self):
        return f"Navn: {self.navn}, HP: {self.hp}, Styrke: {self.styrke}"