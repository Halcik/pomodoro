from datetime import timedelta, datetime
from playsound import playsound
import sys

def pomodoro():
    print("Czas na naukę!")
    p_beg = datetime.today()
    p_different = timedelta(minutes=25)
    p_close = p_beg
    #playsound('muzyka.mp3', False)
    while p_close-p_beg < p_different:
        p_close = datetime.today()


def short_break():
    print("Przerwa!")
    b_beg = datetime.today()
    b_different = timedelta(minutes=5)
    b_close = b_beg
    while b_close-b_beg < b_different:
        b_close = datetime.today()
    

def long_break():
    print("Pora na dłuższy odpoczynek")
    lb_beg = datetime.today()
    lb_different = timedelta(minutes=30)
    lb_close = lb_beg
    while lb_close-lb_beg < lb_different:
        lb_close = datetime.today()


def main(n_rounds):
    for i in range(n_rounds):
        pomodoro()
        if i%4==0:
            long_break()
        else:
            short_break()


if __name__ == "__main__":
    if len(sys.argv)==1:
        n_rounds = 4
    else:
        n_rounds = sys.argv[1]
    main(n_rounds)