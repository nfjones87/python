import os
import time

def clear():
    os.system('cls')

def again():
    print('Play again?')

    selectionList = ['yes', 'no']
    choice = selectchoice(selectionList)

    if choice == 'yes':
        print('Better luck this time!')
        time.sleep(2)
        clear()
        start(inv)
    elif choice == 'no':
        exit(0)



def intro():
    print("""//////////////////////////////////////////////////

/////////////      TRAPPED    ////////////////////

//////////////////////////////////////////////////""")
    print('Press 1 to play, or 2 to quit')

    selectionList = ['1', '2']
    choice = selectchoice(selectionList)

    if choice == '1':
        print('Good luck!')
        time.sleep(2)
        clear()
        start(inv)
    elif choice == '2':
        exit(0)

def start(inv):
    print('You wake up in a dark room. You cant see anything.')

    selectionList = ['scream', 'feel around', 'check pockets', 'hint']
    choice = selectchoice(selectionList)

    if choice == 'scream':
        print ('No one can hear you.')
        time.sleep(2)
        clear()
        start(inv)
    elif choice == 'feel around':
        print('Rock walls. Damp. Feels like a dungeon.')
        time.sleep(2)
        start(inv)
    elif choice == 'hint':
        print('Perhaps you should check your pockets')
        time.sleep(2)
        start(inv)
    elif choice == 'check pockets':
        print('You found a lighter')
        inv.append('lighter')
        time.sleep(1)
        print('Now what?')

        selectionList = ['light it']
        choice = selectchoice(selectionList)
        if choice == 'light it':
            print('You flick on the lighter, its flame bursting into existence')
            time.sleep(3)
            clear()
            lighter(inv)


def lighter(inv):
    print('You see that you are in a dungeon. Rock walls. Dripping water. There is a decomposed corpse besides you and a door.')

    selectionList = ['open door', 'search corpse', 'drink water', 'check walls', 'hint']
    choice = selectchoice(selectionList)

    if choice == 'open door':
        if 'key' in inv:
            print('You used the key to open the door')
            time.sleep(3)
            clear()
            hallway(inv)
        else:
            print('It is locked')
            time.sleep(2)
            lighter(inv)
    elif choice == 'check walls':
        print('You scan along the rock wall until you find a loose rock.')
        time.sleep(1)
        print('Now what?')

        selectionList = ['pry rock']
        choice = selectchoice(selectionList)
        if choice == 'pry rock':
            if 'dagger' in inv:
                print('You used the dagger to pry open the rock. You see a key. You take the key.')
                inv.append('key')
                time.sleep(2)
                lighter(inv)
            else:
                print('You cant quite pry it off with your fingers')
                time.sleep(3)
                lighter(inv)
    elif choice == 'drink water':
        print('Ew. It is disgusting. Youll now probably die a slow painful death')
        time.sleep(2)
        lighter(inv)
    elif choice == 'hint':
        print('The walls dont seem very stable')
        time.sleep(2)
        lighter(inv)
    elif choice == 'search corpse':
        print('You kick over the corpse to reveal a dagger.')
        time.sleep(2)
        print('It seems rusted but still viable. Now what?')

        selectionList = ['take dagger']
        choice = selectchoice(selectionList)
        if choice == 'take dagger':
            inv.append('dagger')
            print('You take the dagger')
            time.sleep(2)
            lighter(inv)




def hallway(inv):
    print('You stand in the darkness, lighter lit, dagger ready. Left or right?')
    
    selectionList = ['left', 'right']
    choice = selectchoice(selectionList)
    if choice == 'left':
        print('You go left.')
        left(inv)
    elif choice == 'right':
        print('You go right')
        right(inv)



def left(inv):
    print('You walk forward slowly, straining to see with your faint light. A door appears before you. You move towards it and accidentally step on a button.')
    if 'shield' in inv:
        time.sleep(5)
        print('As the door opens an arrow shoots out! It hits your shield and bounces off.')
        time.sleep(4)
        print('You walk forward through the door.')
        time.sleep(3)
        clear()
        room(inv)
    else:
        time.sleep(5)
        print('As the door opens an arrow shoots out! It plunges into your chest!')
        time.sleep(4)
        print('You have died.')
        time.sleep(3)
        again()


def right(inv):
    print('You make your way down the dark hallway, your lighter struggling to illuminate. You hear a noise in front of you. You strain to see and are suddenly face to face with an undead warrior. It lunges at you.')
    time.sleep(4)
    print('What do you do?')

    selectionList = ['attack', 'run', 'scream']
    choice = selectchoice(selectionList)
    if choice == 'run':
        print('You turn to run. You spin around, but before you make any distance, a sword plunges through your back')
        time.sleep(4)
        print('You are dead.')
        time.sleep(3)
        again()
    elif choice == 'scream':
        print('You scream, frozen in fear. The sword is the last thing you see.')
        time.sleep(4)
        print('You are dead.')
        again()
    elif choice == 'attack':
        print('You side step and forcefully plunge your dagger into its skull. It instantly drops into a pile of bones.')
        time.sleep(4)
        print('Now what?')

        selectionList = ['search bones', 'go back', 'keep going']
        choice = selectchoice(selectionList)

        if choice == 'go back':
            time.sleep(1)
            clear()
            hallway(inv)
        elif choice == 'keep going':
            print('You step over the bones and move forward only to come to a solid wall. A dead end')
            time.sleep(3)
            print('Now what?')

            selectionList = ['go back']
            choice = selectchoice(selectionList)

            if choice == 'go back':
                time.sleep(1)
                clear()
                hallway(inv)
            
        elif choice == 'search bones':
            print('You kick over the pile of bones to reveal a sword and shield. You take both')
            inv.append('sword')
            inv.append('shield')
            time.sleep(2)
            print('Now what?')

            selectionList = ['go back', 'keep going']
            choice = selectchoice(selectionList)

            if choice == 'go back':
                time.sleep(1)
                clear()
                hallway(inv)
            elif choice == 'keep going':
                print('You step over the bones and move forward only to come to a solid wall. A dead end')
                time.sleep(2)
                print('Now what?')

                selectionList = ['go back']
                choice = selectchoice(selectionList)

                if choice == 'go back':
                    time.sleep(1)
                    clear()
                    hallway(inv)



def room(inv):
    clear()
    print('As you creep forward into the darkness, you suddenly see light pouring from the ceiling and a ladder! The way out!')
    time.sleep(3)
    print('But before you can reach the ladder, a presence makes itself known, standing between you and freedom.')
    time.sleep(3)
    print('A Grue looms large, lurking in the shadows.')
    time.sleep(3)
    print('What do you do?')

    selectionList = ['run', 'attack']
    choice = selectchoice(selectionList)

    if choice == 'run':
        print('You attempt to flee, but the Grue is quicker.')
        time.sleep(2)
        print('He snatches you up before you can escape, eating you alive.')
        time.sleep(3)
        print('You have died')
        time.sleep(3)
        again()
    elif choice == 'attack':
        print('You lunge at the Grue, swinging your sword.')
        time.sleep(2)
        print('A direct hit! It stumbles back for a moment, but then charges you!')
        time.sleep(2)
        print('Now what?')

        selectionList = ['block', 'attack']
        choice = selectchoice(selectionList)

        if choice == 'attack':
            print('You attempt to swing your sword in retaliation, but the Grue connects firsts..')
            time.sleep(2)
            print('The force of the blow knocks you down.')
            time.sleep(2)
            print('You get dragged into the darkness.')
            time.sleep(2)
            print('You have died.')
            time.sleep(3)
            again()
        elif choice == 'block':
            print('You raise your shield, blocking the attack just in time!')
            time.sleep(2)
            print('The Grue stumbles back, stunned!')
            time.sleep(2)
            print('Now what?')

            selectionList = ['attack']
            choice = selectchoice(selectionList)

            if choice == 'attack':
                print('You thrust your sword forward, plunging it into the Grue.')
                time.sleep(2)
                print('It shreaks out in agony then collapses to the floor.')
                time.sleep(2)
                print('You have killed the Grue.')
                time.sleep(4)
                print('You look up into the blinding light, and ascend the ladder.')
                time.sleep(4)
                print('You have escaped.')
                time.sleep(4)
                again()



def selectchoice(selectionList):
    choice = input('? ')
    if choice in selectionList:
        return choice
    elif choice  == 'quit':
        exit(0)
    else:
        print('Invalid input')
        return selectchoice(selectionList)


    
clear()
inv = ['']

intro()
