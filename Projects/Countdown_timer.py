import time

def countdown(t):
    while t > 0:
        mins, secs = divmod(t,60)
        temps = '{:02d}:{:02d}'.format(mins,secs)
        print(temps, end='\r')
        time.sleep(1)
        t -= 1
    print("Fire in the hole!!")
t= int(input("Entre le temps en secondes"))  
countdown(t)