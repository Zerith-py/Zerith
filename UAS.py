import random #Menambahkan module pada program

class Character: #Membuat class Character
    def __init__(self, name):
        self.name = name #Membuat atribut name
        self.health = 100 #Membuat atribut health
        self.happiness = 100 #Membuat atribut happiness
        self.money = 50 #Membuat atribut money
        self.stamina = 100  #Mmbuat atribut stamina
        self.experience = 0 #Membuat atribut experience
        self.level = 1 #Membuat atribut level
        
#Memnampilkan Status Character
    def display_status(self):
        print(f"\nStatus {self.name}:")
        print(f"Kesehatan: {self.health}")
        print(f"Kebahagiaan: {self.happiness}")
        print(f"Uang: {self.money}")
        print(f"Pengalaman : {self.experience}")
        print(f"Level: {self.level}")
        
#Membuat program untuk level character
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()

#Program level up character
    def level_up(self):
        self.level +=1
        self.experience = 0
        self.health += 10
        self.happiness += 10
        self.money += 50
        self.stamina += 10
        print(f'{self.name} naik Level! Sekarang Kamu Berada di Level {self.level}!')

#Memampilkan pilihan kegiatan       
def daily_decision(character):
    print("\nHari baru! Apa yang ingin kamu lakukan?")
    print("1. Bekerja")
    print("2. Berolahraga")
    print("3. Bersantai")
    print("4. Makan di restoran")
    
    choice = input("Pilih tindakan (1-4): ")
    
    if choice == '1':
        print('\nPilih Pekerjaan:')
        print("1. Bertani")
        print("2. Menambang")
        print("3. Berdagang")
        print("4. Batal")

        pekerjaan = input("Pilih pekerjaan (1-4): ")
        print('')
        if pekerjaan == '1':
            print(f'{character.name} Bertani' )
            character.money += 30
            character.happiness += 15
            character.health -= 10
            character.stamina -= 10
            character.gain_experience(20)
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            
        elif pekerjaan == '2':
            print(f'{character.name} Menambang')
            character.money += 50
            character.happiness -= 10
            character.health -= 20
            character.stamina -= 20
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            character.gain_experience(10)
            
        elif pekerjaan == '3':
            print(f'{character.name} Berdagang')
            character.money += 40
            character.happiness += 10
            character.health -= 5
            character.stamina -= 5
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            character.gain_experience(25)
            
        elif pekerjaan == '4':
            print(f'{character.name} membatalkan pekerjaan.')
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            
        else:
            print("Pilihan tidak valid.")
            
      
    elif choice == '2':
        print('\nPilih Jenis Olahraga : ')
        print('1. Sepak Bola')
        print('2. Berenang')
        print('3. Lari')
        print('4. Batal')
        print('')
        olahraga = input('Pilih Jenis Olahraga (1-4) : ')
        print('')
        if olahraga == '1':
            print(f"{character.name} Bermain Sepak Bola.")
            character.health -= 35
            character.happiness += 5
            character.stamina -= 20
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            character.gain_experience(20)
            
        elif olahraga == '2':
            print(f"{character.name} Berenang.")
            character.health -= 5
            character.happiness += 25
            character.stamina -= 15
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            character.gain_experience(15)
            
        elif olahraga == '3':
            print(f'{character.name} Lari')
            character.health -= 20
            character.happiness += 10
            character.stamina -= 25
            print(f'Hapinnes : {character.happiness}')
            print(f'Health : {character.health}')
            print(f'Stamina : {character.stamina}')
            character.gain_experience(10)
            
        elif olahraga == '4':
            print(f'{character.name} membatalkan olahraga.')
            
        else:
            print("Pilihan tidak valid.")
            
    #Menu Bersantai       
    elif choice == '3':
        print('')
        print(f"{character.name} bersantai di rumah.")
        character.happiness += 15
        character.health += 30
        character.stamina += 30
        print(f"Happiness: {character.happiness}")
        print(f"Health: {character.health}")
        print(f"Stamina: {character.stamina}")
        character.gain_experience(0)
        print('Istirahat adalah pilihan bagus ketika kamu sudah merasa terlalu lelah untuk bekerja')
        
    elif choice == '4':
        print('')
        print('\nPilihan Makanan : ')
        print('1. Nasi Padang : 25')
        print('2. Ayam Geprek : 15')
        print('3. Mie Ayam    : 10')
        print('4. Batal')
        
        makanan = input('Pilih Makanan (1-4) : ')
        print('')
        if makanan == '1':
            if character.money >= 25:
               character.happiness += 20
               character.health += 10
               character.money -= 25
               print(f"{character.name} memesan Nasi Padang.")
            else:
               print("Uang tidak cukup untuk memesan Nasi Padang.")
            
            
        elif makanan == '2':
            if character.money >= 15:
               character.happiness += 15
               character.health += 5
               character.money -= 15
               print(f"{character.name} memesan Ayam Geprek.")
            else:
               print("Uang tidak cukup untuk memesan Ayam Geprek.")
            
        
        elif makanan == '3':
            if character.money >= 10:
               character.happiness += 10
               character.health += 5
               character.money -= 10
               print(f"{character.name} memesan Mie Ayam.")
            else:
             print("Uang tidak cukup untuk memesan Mie Ayam.")
            
        elif makanan == '4':
         print(f"{character.name} membatalkan pemesanan makanan.")  
      
    else:
        print("Pilihan tidak valid.")

def main():
    print("Selamat datang di Simulasi Kehidupan Virtual!")
    name = input("Masukkan nama karakter: ")
    character = Character(name)

    days = 0
    while character.health > 0 and character.happiness > 0 and days < 10:
        character.display_status()
        daily_decision(character)
        days += 1

    if character.health <= 0:
        print(f"\n{character.name} telah kehabisan kesehatan. Permainan berakhir.")
    elif character.happiness <= 0:
        print(f"\n{character.name} telah kehilangan semua kebahagiaan. Permainan berakhir.")
    else:
        print(f"\n{character.name} telah menyelesaikan 10 hari! Permainan berakhir.")

if __name__ == "__main__":
    main()