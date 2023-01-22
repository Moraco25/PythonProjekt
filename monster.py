
import time


def clear_console():
    print("\033c", end='')
    print("")


while True:

    clear_console()

    print ("Willkomen bei MONSTER")

    time.sleep (2)

    clear_console()

    time.sleep (2)

    print ("Starten wir")

    time.sleep (2)

    clear_console ()

    time.sleep (2)

    print ("Iergendwo da drausen...")

    time.sleep (2)

    print ("...läuft ein Monster herum")

    time.sleep (2)

    clear_console()


    antwort = input ("Möchtest du dich verstecken oder es jagen? ")
    if antwort == "jagen":
        print ("Du bist tot.")
        time.sleep(2)
        clear_console()
        print(":(")
        time.sleep (1)
        
    elif antwort == "verstecken":
        print ("lass uns in den Keler gehen")        
        
        time.sleep (1)

        print ("Dort ist es am sichersten")

        time.sleep (2)

        clear_console ()

        print ("aber...")

        time.sleep (2)

        clear_console ()

        print (" ooooohhh neeeiinn")

        time.sleep (1)

        clear_console ()

        print ("der schlüssel für unser haus ist weg!!!")

        time.sleep (2)

        print ("ich habe ihn wohl im park liegen gelassen")

        time.sleep (2)

        clear_console ()

        hausschlüssel = input ("Sollen wir ihn hohlen gehen oder in den Wald flüchten?")
        if hausschlüssel == "hohlen":
            print("Wie du willst aber es ist ziemlich gefährlich im Park")
            time.sleep(2.5)
            print(":(")
            time.sleep (2)
            clear_console()
            print("Du bist Tot")
        elif hausschlüssel == "flüchten":  
            clear_console ()

            print ("Ok du wilst es so")

            time.sleep (2)

            print ("Dann nix wie hin")

            time.sleep (2)
            


        


        print ("Das verstehe ich nicht. Wir haben keine zeit mehr. Wir sind Tot")
    print ("Das verstehe ich nicht. Wir haben keine Zeit mehr. Wir sind Tot")





time.sleep (2)

clear_console()


