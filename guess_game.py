import math
import random
# import math
# import random
# a = [] #przypisujemy pustą liste zmiennej a 99
# a.append(random.randint(1, 99))#Nadawanie na koniec listy "a" losowo utweorznej liczby o wartości od 1-99, wykonana 10 razy.
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# a.append(random.randint(1, 99))
# for i in range(10): #otwieramy pętle, która będzie powtarzała dla i w przedziale 0-9
#     user_input = int(input("Enter an integer from 1 to 99: "))   #pobieramy wartość, rzutujemy wartość zmiennej na typ integer i przypisujemy zmienną user_input
#     while a[i] != user_input:    #rozpoczynamy pętle, któa trwa, dopóki element i z listy a jest różny od user_input
#         if user_input < a[i]:    #sprawdza czy wartość pobrana od użytkownika jest mniejsza od kolejnego elementu z listy a  
#             print("guess is low")   #wyświetla powiadomienia z konsoli, że liczba jest za mała
#             user_input = int(input("Enter an integer from 1 to 99: "))   #pobieramy wartość, rzutujemy wartość zmiennej na typ integer i przypisujemy zmienną user_input
#         elif user_input > a[i]:#w przedziwnym wypadku, sprawdza czy wartość pobrana od użytkownika jest większa od kolejnego elementu z listy a 
#             print("guess is high")#wyświetla powiadomienia z konsoli, że liczba jest za duża
#             user_input = int(input("Enter an integer from 1 to 99: "))#pobieramy wartość, rzutujemy wartość zmiennej na typ integer i przypisujemy zmienną user_input
#         else:   #jeżeli żadne warunek nie jest spełniony
#             break   #przeywa działaniue pętli
#     print("you guessed it!")#wyświetla w koncoli że zgadłeś

# b = []
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# b.append(random.randint(1, 49))
# for i in range(10):
#     user_input = int(input("Enter an integer from 1 to 49: "))
#     while b[i] != user_input:
#         if user_input < b[i]:
#             print("guess is low")
#             user_input = int(input("Enter an integer from 1 to 49: "))
#         elif user_input > b[i]:
#             print("guess is high")
#             user_input = int(input("Enter an integer from 1 to 49: "))
#         else:
#             break
#     print("you guessed it!")
TIMES_TO_PLAY = 10
def generate_random_numbers_list(maxvalue):
    random_numbers_list = []
    for i in range(TIMES_TO_PLAY):  
        random_numbers_list.append(random.randint(1, maxvalue))
    return random_numbers_list

def ask_for_input(maxvalue):
    user_number=int(input("Enter an integer from 1 to {maxvalue}:"))
    return user_number

def game_logic(maxvalue, random_number_list):
    for i in range(TIMES_TO_PLAY):
        user_input=None
    while random_number_list[i] != user_input:
        user_input=ask_for_input(maxvalue)
        
        if user_input < random_number_list[i]:
            print("guess is low")
            
        elif user_input > random_number_list[i]:
            print("guess is high")
    print("you guessed it!")

a=generate_random_numbers_list(99)
    
game_logic(99,a)


b=generate_random_numbers_list(49)

game_logic(49,a)