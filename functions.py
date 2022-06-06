import os, time, nftApi

readmeContent = ["# Yo\n",
"### I'm currently learning more about react, web3, contracts & solidity.\n",
"### Mainly focused on frontend & backend development - and finding a place in web3\n",
"### Current websites www.javel.dk & www.apecode.io]"]
readmeContent2 = ["# Yo.\n",
"### I'm currently learning more about react, web3, contracts & solidity.\n",
"### Mainly focused on frontend & backend development - and finding a place in web3\n",
"### Current websites www.javel.dk & www.apecode.io]"]

path = 'C:\\Users\\andre\\Documents\\Github\\neaxic\\README.md'
wallet = '0xb504439D29220A07fB5efd6D881df671934C3B51'

def checkText():
    mdFile = open(path, "r")
    text = mdFile.read(5);
    if text.endswith('.'):
        writenew()
    else:
        writenew2()

def writenew():
    mdFile = open(path, "w")
    mdFile.writelines(readmeContent);
    mdFile.close()

def writenew2():
    mdFile = open(path, "w")
    mdFile.writelines(readmeContent2);
    mdFile.close()

def rgb(red, green, blue):
  return f'\x1b[38;2;{red};{green};{blue}m'

red_color = rgb(200, 0, 0)
green_color = rgb(0, 200, 0)
yellow_color = rgb(200, 200, 0)
blue_color = rgb(0, 0, 200)

def startCommit():
    os.system("color 07") 
    os.system('cls')
    print("\n" * 5)
    print(f'{yellow_color}     > [⌛] Updating readme...')
    checkText()
    time.sleep(1)
    print(f'{yellow_color}     > [⏳] Commiting & pushing update...')
    os.system("start \"\" cmd /k \"cd /D C:\\Users\\andre\\Documents\\Github\\neaxic\\ & color 04 & git add README.md & git commit -m idk & git push & exit\"")
    time.sleep(3)
    print(f'{green_color}     > [✅] Task done. Returning to menu...')
    time.sleep(2)
    return True

def customizeGithub():
    os.system('cls')
    print("\n" * 5)
    print("     > [TIP] You can always type quit if you regret.")
    print("     > [] Input readme.md path (ie. C:\\\\Users\\\\andre\\\\Documents\\\\Github\\\\neaxic\\\\README.md) (Remember: \\\\) ")
    tmpPath = input('     > [] Enter path: ')
    if(tmpPath == 'quit'):
        return True
    print("     > [] This is the final path: "+tmpPath+", agreed? y/n")
    valgLoop = True
    while(valgLoop):
        valg = input("     > [] Option: ")
        if(valg == 'y'):
            valgLoop = False
            path = tmpPath
            return True
        if(valg == 'n'):
            valgLoop = False
            customizeGithub()

    return True

def customizeWallet():
    os.system('cls')
    print("\n" * 5)
    print("     > [TIP] You can always type quit if you regret.")
    print("     > [] Input new wallet address (Remember: 0x) ")
    tmpWallet = input('     > [] Enter address: ')
    if(tmpWallet == 'quit'):
        return True
    print("     > [] This is the final address: "+tmpWallet+", agreed? y/n")
    valgLoop = True
    while(valgLoop):
        valg = input("     > [] Option: ")
        if(valg == 'y'):
            valgLoop = False
            wallet = tmpWallet
            return True
        if(valg == 'n'):
            valgLoop = False
            customizeGithub()

    return True

def checkNFTS():
    os.system("color 05") 
    os.system('cls')
    print("\n" * 5)
    print(f'{yellow_color}     > [⌛] Fetching NFTs...')
    # check return
    walletSize = nftApi.fetchNFTs(wallet)
    time.sleep(3)
    print(f'{green_color}     > [✅] NFTs loaded... Theres currently: '+ str(walletSize) +' NFTs in wallet')
    print(f'{yellow_color}     > [⏳] Fetching NFTs sales statistics...')
    walletWorth = nftApi.fetchSales()
    print(f'{green_color}     > [✅] NFTs loaded... Wallet is currently worth: '+ str(walletWorth) +' ETH')
    print(f'{green_color}     > [✅] Task done. Returning to menu...')
    time.sleep(2)
    return True