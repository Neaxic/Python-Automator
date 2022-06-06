from this import d
import requests, json, Secrets

class NFT:
    def __init__(self, name, token, slug):
        self.name = name
        self.token = token
        self.slug = slug
        self.fp = 0.0

walletNFT = []

apiKey = Secrets.getSecrets().OSAPI
print(apiKey)

header = {
    "X-API-KEY": apiKey,
    "Accept": "application/json"
}

data = {
    "name": "geek",
    "passion": "coding",
}

def fetchNFTs(wallet):
    response = requests.get("https://api.opensea.io/api/v1/assets?owner="+wallet+"", headers=header)
    jsonAssets = response.json()['assets']
    for i in jsonAssets:
        nft = NFT(i['name'], i['token_id'], i['collection']['slug'])
        walletNFT.append(nft)
    return len(walletNFT)

def fetchSales():
    walletWorth = 0.0
    for i in walletNFT:
        response = requests.get("https://api.opensea.io/api/v1/collection/"+i.slug+"/stats", headers=header)
        nftPrice = response.json()['stats']['floor_price']
        if(isinstance(nftPrice, float)):
            i.fp = nftPrice
            walletWorth += nftPrice
    return walletWorth