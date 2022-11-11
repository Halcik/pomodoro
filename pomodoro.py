#lista zadań do wykonania wprowadzana na początku i potem odhaczanie? Każde, by się dało zrobić w 25 min

#ustawienie prorytetów - jakieś przesuwanie?

#odznaczenie wykonanych zadań

#sztuczne kroki przygotowawcze:
# - wyłączenie powiadomień
# - wyciszenie telefonu i wyłączenie wibracji
# - wyłączenie niepotrzebnych stron i aplikacji

from datetime import timedelta, datetime
from playsound import playsound

def pomodoro():
    #timer odlicza 25 minutowe odcinki czasu pracy - jakaś muzyka w tle?
    print("Czas na naukę!")
    p_beg = datetime.today()
    p_different = timedelta(minutes=25)
    p_close = p_beg
    while p_close-p_beg < p_different:
        #może w trakcie pomodoro jakieś teksty motywujące?
        p_close = datetime.today()
    #potem krótka przerwa - dzwonek na przerwę?


def short_break():
    #pierwsza przerwa - 5 min - czas na spacer po mieszkaniu, przewietrzenei czy nalanie wody
    print("Przerwa!")
    b_beg = datetime.today()
    b_different = timedelta(minutes=5)
    b_close = b_beg
    while b_close-b_beg < b_different:
        b_close = datetime.today()
    

def long_break():
    #Co czwarte pomodoro dłuższa przerwa - 15-30 min - dobre na zrobienie kawy lub herbaty, zjedzenie czy rozmowę ze znajomymi.
    print("Pora na dłuższy odpoczynek")
    lb_beg = datetime.today()
    lb_different = timedelta(minutes=30)
    lb_close = lb_beg
    while lb_close-lb_beg < lb_different:
        lb_close = datetime.today()


four_rounds = [pomodoro(), short_break(), pomodoro(), short_break(), pomodoro(), short_break(), pomodoro(), long_break()]

for i in four_rounds:
    i
