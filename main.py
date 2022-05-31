import os, time, keyboard, functions

menuHeader = '''    $$\        $$$$$$\  $$$$$$$\   $$$$$$\  
    $$ |      $$  __$$\ $$  __$$\ $$  __$$\ 
    $$ |      $$ /  $$ |$$ |  $$ |$$ /  \__|
    $$ |      $$$$$$$$ |$$$$$$$\ |\$$$$$$\  
    $$ |      $$  __$$ |$$  __$$\  \____$$\ 
    $$ |      $$ |  $$ |$$ |  $$ |$$\   $$ |
    $$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$  |
    \________|\__|  \__|\_______/  \______/'''

#Functions


#MENU STUFF
selected = 0

menuItems = ['GITHUB COMMITTER', 'Github commits2', 'Github 3']

def show_menu():
    global selected
    os.system('cls')
    os.system("color 04") 
    print("\n" * 2)
    print(menuHeader)
    print("\n" * 3)
    os.system("color 07") 
    print("     Choose an option:")
    for idx, x in enumerate(menuItems):
        print("         {0} ".format("=>" if selected == idx else " ")+x+" ")

def up():
    global selected
    if selected <= 0:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected >= len(menuItems)-1:
        return
    selected += 1
    show_menu()

def enter():
    global selected
    if selected == 0:
        done = functions.startCommit()
        if(done == True):
            show_menu()
    if selected == 1:
        print("lol2")

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()


















