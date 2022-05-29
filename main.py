import os

readmeContent = ["# Yo\n",
"### I'm currently learning more about react, web3, contracts & solidity.\n",
"### Mainly focused on frontend & backend development - and finding a place in web3\n",
"### Current websites www.javel.dk & www.apecode.io]"]

readmeContent2 = ["# Yo.\n",
"### I'm currently learning more about react, web3, contracts & solidity.\n",
"### Mainly focused on frontend & backend development - and finding a place in web3\n",
"### Current websites www.javel.dk & www.apecode.io]"]

path = 'C:\\Users\\andre\\Documents\\Github\\neaxic\\README.md'

def checkText():
    mdFile = open(path, "r")
    text = mdFile.read(5);
    print(text)
    if text.endswith('.'):
        print('ja')
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

checkText()

#git add README.md
#git commit -m navn
#git push

os.system("start \"\" cmd /k \"cd /D C:\\Users\\andre\\Documents\\Github\\neaxic\\ & color 04 & git add README.md & git commit -m idk & git push \"")