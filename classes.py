class Penerbangan():
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.penumpang = []

    def add_penumpang(self, name):
        if not self.open_kursi():
            return False
        self.penumpang.append(name)
        return True
    
    def open_kursi(self):
        return self.kapasitas - len(self.penumpang)

Penerbangan = Penerbangan(3)

people = ["Udin", "Tono", "Wawan", "Yusuf"]

for person in people:
    if Penerbangan.add_penumpang(person):
        print(f"Menambahkan {person} Ke Penerbangan [Successfully]")
    else:
        print(f"No available seat for {person}")