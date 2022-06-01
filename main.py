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

red_color = functions.rgb(200, 0, 0)
green_color = functions.rgb(0, 200, 0)
yellow_color = functions.rgb(200, 200, 0)
white_color = functions.rgb(200, 200, 200)
blue_color = functions.rgb(0, 0, 200)

#MENU STUFF
selected = 0
selectedMenu = 0

menuItems = ['[🤖] GITHUB COMMITTER', '[🤖] Github commits2', '[⚙️] SETTINGS']
settingsItems = ['[🤖] COSTOMIZE GITHUB COMMITTER', '[] RETURN TO MAIN MENU']

def settings_menu():
    global selected, selectedMenu
    selectedMenu = 1;
    os.system('cls')
    os.system("color 02") 
    print("\n" * 2)
    print(menuHeader)
    print("\n" * 3)
    print("     Choose an option:")
    for idx, x in enumerate(settingsItems):
        print(f"{white_color}"+"         {0} ".format("=>" if selected == idx else " ")+x+" ")


def show_menu():
    global selected, selectedMenu
    selectedMenu = 0;
    os.system('cls')
    os.system("color 02") 
    print("\n" * 2)
    print(menuHeader)
    print("\n" * 3)
    print("     Choose an option:")
    for idx, x in enumerate(menuItems):
        print(f"{white_color}"+"         {0} ".format("=>" if selected == idx else " ")+x+" ")

def up():
    global selected, selectedMenu
    if selected <= 0:
        return
    selected -= 1
    if selectedMenu == 0:
        show_menu()

    if selectedMenu == 1:
        settings_menu()

def down():
    global selected
    if selected >= len(menuItems)-1:
        return
    selected += 1
    if selectedMenu == 0:
        show_menu()

    if selectedMenu == 1:
        settings_menu()

def enter():
    global selected
    if selected == 0 and selectedMenu == 0:
        done = functions.startCommit()
        if(done == True):
            show_menu()
    if selected == 1 and selectedMenu == 0:
        print("lol2" + str(selected))
    if selected == 2 and selectedMenu == 0:
        print("huh")
        selected = 0;
        settings_menu()

    if selected == 0 and selectedMenu == 1:
        print("yo")

    if selected == 1 and selectedMenu == 1:
        selected = 0;
        show_menu()

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()


















