import os

readmeContent = ["# \U0001f1ef Yo\n",
"### 🔭 I'm currently learning more about react, web3, contracts & solidity.\n",
"### 🌏 Mainly focused on frontend & backend development - and finding a place in web3\n",
"### 📫 Current websites www.javel.dk & www.apecode.io]"]

path = 'C:\\Users\\andre\\Documents\\Github\\neaxic\\README.md'

mdFile = open(path, "w")
mdFile.writelines(readmeContent);
mdFile.write("29/05/2022");

mdFile.close()

