import os
import time

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

    selectionList = ['scream', 'feel around', 'check pockets']
    choice = selectchoice(selectionList)

    if choice == 'scream':
        print ('No one can hear you.')
        time.sleep(2)
        clear()
        start(inv)
    elif choice == 'feel around':
        print('Rock walls. Damp. Feels like a dungeon.')
        time.sleep(2)
        clear()
        start(inv)
    elif choice == 'check pockets':
        print('You found a lighter')
        inv.append('lighter')
        time.sleep(1)
        print('Now what?')

        selectionList = ['light lighter']
        choice = selectchoice(selectionList)
        if choice == 'light lighter':
            print('You flick on the lighter, its flame bursting into existence')
            time.sleep(3)
            clear()
            lighter(inv)


def lighter(inv):
    print('You see that you are in a dungeon. Rock walls. Dripping water. There is a decomposed corpse besides you and a door.')

    selectionList = ['open door', 'check corpse', 'drink water', 'check walls']
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
            clear()
            lighter(inv)
    elif choice == 'check walls':
        print('You scan along the rock wall until you find a loose rock.')
        time.sleep(1)
        print('Now what?')

        selectionList = ['move rock']
        choice = selectchoice(selectionList)
        if choice == 'move rock':
            if 'dagger' in inv:
                print('You used the dagger to pry open the rock. You see a key. You take the key.')
                inv.append('key')
                time.sleep(2)
                clear()
                lighter(inv)
            else:
                print('You cant quite pry it off with your fingers')
                time.sleep(3)
                clear()
                lighter(inv)
    elif choice == 'drink water':
        print('Ew. It is disgusting. Youll now probably die a slow painful death')
        time.sleep(2)
        clear()
        lighter(inv)
    elif choice == 'check corpse':
        print('You kick over the corpse to reveal a dagger.')
        time.sleep(2)
        print('It seems rusted but still viable. Now what?')

        selectionList = ['take dagger']
        choice = selectchoice(selectionList)
        if choice == 'take dagger':
            inv.append('dagger')
            print('You take the dagger')
            time.sleep(2)
            clear()
            lighter(inv)




def hallway(inv):
    print('You step out into the darkness, lighter lit, dagger ready. Left or right?')



def selectchoice(selectionList):
    choice = input('? ')
    if choice in selectionList:
        return choice
    elif choice  == 'quit':
        exit(0)
    else:
        print('Invalid input')
        return selectchoice(selectionList)

def clear():
    os.system('cls')
    
clear()
inv = ['']

intro()
