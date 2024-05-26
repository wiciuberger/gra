from wybora import wybora
from wyborb import wyborb
from wyborc import wyborc
from wybord import wybord
from wybore import wybore
def start():
    print("wybierz dalsza opcje swej przygody:")
    print("a. gra fabularna, rpg")
    print("b. walczanka")
    print("c. gra w karty (np. Blackjack)- hazard")
    print("d. papier kamien nozyce - ze zwierzetami.")
    print("e. sprobuj swoich sil w bitwach")
    wybor_gry = input("Wybierz literę od a do e: ").lower()

    if wybor_gry == 'a':
        wybora()
    elif wybor_gry == 'b':
        wyborb()
    elif wybor_gry == 'c':
        wyborc()
    elif wybor_gry == 'd':
        wybord()
    elif wybor_gry == 'e':
        wybore()
    else:
        print("niepoprawny wybor. wybierz litere od a do e.")

if __name__ == "__main__":
    start()