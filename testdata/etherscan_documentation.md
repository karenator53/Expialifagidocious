# Introduction

# Introduction

### Why V2

### Single API Key

Why V2


Single API Key


This V2 update is aimed at a single goal, of unifying EVM data across 50+ chains. 🤝


With the rise of multichain apps, many projects' GitHub repositories resemble a ( shortened ) version of this.


As support for Etherscan explorers across multiple chains grew, so did the fragmentation of the developer experience.


You can now query data from any of our 50+ supported chains with a single API key.


This includes features like contract verification ✅, fetching transactions across chains 🔵 and more.


To add support for a new chain, simply append its chain ID to your array, like this JavaScript ( intern can't get Python installed on Windows )


We don't currently support all endpoints on all chains. Please feel free to reach out if you need something specific!


Last updated 6 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
ETHERSCAN_API_KEY=VZFDUWB3YGQ1YCDKTCU1D6DDSS
BSCSCAN_API_KEY=ZM8ACMJB67C2IXKKBF8URFUNSY
SNOWSCAN_API_KEY=ATJQERBKV1CI3GVKNSE3Q7RGEJ
ARBISCAN_API_KEY=B6SVGA7K3YBJEQ69AFKJF4YHVX
OPTIMISM_API_KEY=66N5FRNV1ZD4I87S7MAHCJVXFJ
ETHERSCAN_API_URL=https://api.etherscan.io/api
BSCSCAN_API_KEY=https://api.bscscan.com/api
SNOWSCAN_API_KEY=https://api.snowscan.xyz/api
ARBISCAN_API_KEY=https://api.arbiscan.io/api
OPTIMISM_API_KEY=https://api-optimistic.etherscan.io/api
```


```
ETHERSCAN_API_KEY=VZFDUWB3YGQ1YCDKTCU1D6DDSS
BSCSCAN_API_KEY=ZM8ACMJB67C2IXKKBF8URFUNSY
SNOWSCAN_API_KEY=ATJQERBKV1CI3GVKNSE3Q7RGEJ
ARBISCAN_API_KEY=B6SVGA7K3YBJEQ69AFKJF4YHVX
OPTIMISM_API_KEY=66N5FRNV1ZD4I87S7MAHCJVXFJ
ETHERSCAN_API_URL=https://api.etherscan.io/api
BSCSCAN_API_KEY=https://api.bscscan.com/api
SNOWSCAN_API_KEY=https://api.snowscan.xyz/api
ARBISCAN_API_KEY=https://api.arbiscan.io/api
OPTIMISM_API_KEY=https://api-optimistic.etherscan.io/api
```


```
const chains = [42161, 8453, 10, 534352, 81457]
for (const chain of chains) {
  // endpoint accepts one chain at a time, loop for all your chains
  const balance = fetch(`https://api.etherscan.io/v2/api?
     chainid=${chain}
     &module=account
     &action=balance
     &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
     &tag=latest&apikey=YourApiKeyToken`)
     
}
```


```
const chains = [42161, 8453, 10, 534352, 81457]
for (const chain of chains) {
  // endpoint accepts one chain at a time, loop for all your chains
  const balance = fetch(`https://api.etherscan.io/v2/api?
     chainid=${chain}
     &module=account
     &action=balance
     &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
     &tag=latest&apikey=YourApiKeyToken`)
     
}
```


---

# V2 Faq

# V2 FAQ

### TL;DR what are the breaking changes ?

### How many chains can I batch together ?

### Is there an end of support/deadline to make changes ?

### How do I reference the older V1 docs ?

### How are rate limits calculated ?

### Does this cover contract verification ?

TL;DR what are the breaking changes ?


How many chains can I batch together ?


Is there an end of support/deadline to make changes ?


How do I reference the older V1 docs ?


How are rate limits calculated ?


Does this cover contract verification ?


There are no breaking changes. All updates are backward-compatible, but we recommend switching to V2 sooner rather than later for easier multichain app development.


Please note that we do plan to deprecate V1 over time.


Our endpoint accepts one `chainId` at a time, feel free to repeat the query for each chain you need to access.


We don't have any timeline to deprecate anything yet.


Its still here.


Exactly as before—based on your plan, with a per-second request limit and an overall daily limit.


To manage this, you can set up programmatic alerts or enable overage charges if needed for peace of mind.


Soon! We're collaborating with the Hardhat and Foundry teams to streamline this process—goodbye to managing 20 different API keys.


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# V2 Quickstart

# V2 Quickstart

### If you're coming from V1

### If you're coming from another explorer, Basescan/Arbiscan/Polygonscan etc

### If you're starting with V2

If you're coming from V1


If you're coming from another explorer, Basescan/Arbiscan/Polygonscan etc


If you're starting with V2


✨
GETTING STARTED


Your base url looks like this


Just append V2 to the base url, and a chainId parameter


Your query looks something like one of these


Change your base URL to Etherscan, and point the chainId to 8453 or any chain you want


Run this complete script with Node JS, node script.js


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/api
```


`https://api.etherscan.io/api`


`chainId`


```
https://api.etherscan.io/v2/api?chainid=1
```


`https://api.etherscan.io/v2/api?chainid=1`


```
https://api.basescan.org/api
https://api.polygonscan.com/api
https://api.bscscan.com/api
https://api.apescan.io/api
```


```
https://api.basescan.org/api
https://api.polygonscan.com/api
https://api.bscscan.com/api
https://api.apescan.io/api
```


`8453`


```
https://api.etherscan.io/v2/api?chainid=8453
```


`https://api.etherscan.io/v2/api?chainid=8453`


`node script.js`


```
async function main() {
    // query ETH balances on Arbitrum, Base and Optimism
    const chains = [42161, 8453, 10]
    for (const chain of chains) {
        // endpoint accepts one chain at a time, loop for all your chains
   
        const query = await fetch(`https://api.etherscan.io/v2/api
           ?chainid=${chain}
           &module=account
           &action=balance
           &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
           &tag=latest&apikey=YourApiKeyToken`)
           
        const response = await query.json()
        const balance = response.result
        console.log(balance)
    }
}
main()
```


```
async function main() {
    // query ETH balances on Arbitrum, Base and Optimism
    const chains = [42161, 8453, 10]
    for (const chain of chains) {
        // endpoint accepts one chain at a time, loop for all your chains
   
        const query = await fetch(`https://api.etherscan.io/v2/api
           ?chainid=${chain}
           &module=account
           &action=balance
           &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
           &tag=latest&apikey=YourApiKeyToken`)
           
        const response = await query.json()
        const balance = response.result
        console.log(balance)
    }
}
main()
```


---

# Creating An Account

# Creating an Account

## 1. Register an Account

## 2. Verify Your Email

## 3. Using Your Account

1. Register an Account


2. Verify Your Email


3. Using Your Account


✨
GETTING STARTED


Having an Etherscan account allows you to use sign-in only features and tools such as watchlists, private notes and access to the APIs.


It takes about a minute to create, quick access with no long onboarding flows.


Note that creating an Etherscan account is only linked to Etherscan's block explorer services, it is not the same as creating an Ethereum address 💡.


Head over to the Account Registration page and provide a username, email and password for your account.


A confirmation link 🔗 will be sent to your email address to verify your sign up request.


Once you've clicked on the link, your account set-up process is complete and you may sign in to use your account-specific features ! 🎉


Upon signing in, you will have access to your account dashboard where you can make full use of Etherscan's features such as generating API keys 🔑 , hide unwanted tokens and add private notes.


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Getting An Api Key

# Getting an API Key

## Creating an API Key

✨
GETTING STARTED


A valid API Key is required for all queries, let us know if you run into any issues ✅


From your Account Dashboard, click on the navigation tab labelled 🗝️ API-KEYs


From there, you may click on Add to create a new key and give a name to your project.


Each Etherscan account is limited to creating 3 keys at any one time.


Last updated 14 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Supported Chains

# Supported Chains

✨
GETTING STARTED


This list, along with the relevant explorer links, is also available as an endpoint.


Ethereum Mainnet


1


Sepolia Testnet


11155111


Holesky Testnet


17000


ApeChain Curtis Testnet


33111


ApeChain Mainnet


33139


Arbitrum Nova Mainnet


42170


Arbitrum One Mainnet


42161


Arbitrum Sepolia Testnet


421614


Avalanche C-Chain


43114


Avalanche Fuji Testnet


43113


Base Mainnet


8453


Base Sepolia Testnet


84532


BitTorrent Chain Mainnet


199


BitTorrent Chain Testnet


1028


Blast Mainnet


81457


Blast Sepolia Testnet


168587773


BNB Smart Chain Mainnet


56


BNB Smart Chain Testnet


97


Celo Alfajores Testnet


44787


Celo Mainnet


42220


Cronos Mainnet


25


Fantom Opera Mainnet


250


Fantom Testnet


4002


Fraxtal Mainnet


252


Fraxtal Testnet


2522


Gnosis


100


Kroma Mainnet


255


Kroma Sepolia Testnet


2358


Linea Mainnet


59144


Linea Sepolia Testnet


59141


Mantle Mainnet


5000


Mantle Sepolia Testnet


5003


Moonbase Alpha Testnet


1287


Moonbeam Mainnet


1284


Moonriver Mainnet


1285


OP Mainnet


10


OP Sepolia Testnet


11155420


Polygon Amoy Testnet


80002


Polygon Mainnet


137


Polygon zkEVM Cardona Testnet


2442


Polygon zkEVM Mainnet


1101


Scroll Mainnet


534352


Scroll Sepolia Testnet


534351


Sonic Blaze Testnet


57054


Sonic Mainnet


146


Sophon Mainnet


50104


Sophon Sepolia Testnet


531050104


Taiko Hekla L2 Testnet


167009


Taiko Mainnet


167000


WEMIX3.0 Mainnet


1111


WEMIX3.0 Testnet


1112


World Mainnet


480


World Sepolia Testnet


4801


Xai Mainnet


660279


Xai Sepolia Testnet


37714555429


XDC Apothem Testnet


51


XDC Mainnet


50


zkSync Mainnet


324


zkSync Sepolia Testnet


300


Last updated 25 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Supported Endpoints

# Supported Endpoints

✨
GETTING STARTED


A full table of supported endpoint across chains.


Last updated 23/10/24


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Legacy V1 Api Documentation

# Legacy (V1) API Documentation

✨
GETTING STARTED


Etherscan


https://docs.etherscan.io/


Bscscan


https://docs.bscscan.com/


FTMScan


https://docs.ftmscan.com/


Optimism


https://docs.optimism.etherscan.io/


Polygonscan


https://docs.polygonscan.com/


Arbiscan


https://docs.arbiscan.io/


Arbiscan Nova


https://docs.arbiscan.io/v/nova-arbiscan


Moonbeam


https://docs.moonscan.io/


Moonriver


https://docs.moonscan.io/v/moonriver


Cronos


https://docs.cronoscan.com/


Bttcscan


https://docs.bttcscan.com/


Celoscan


https://docs.celoscan.io/


Gnosisscan


https://docs.gnosisscan.io/


Basescan


https://docs.basescan.org/


PolygonzkEVM


https://docs.polygonscan.com/v/polygon-zkevm


Lineascan


https://docs.lineascan.build/


Scrollscan


https://docs.scrollscan.com/


Wemixscan


https://docs.wemixscan.com/


Zksync Era


https://docs.zksync.network/


Fraxscan


https://docs.fraxscan.com/


Snowscan


https://docs.snowscan.xyz/


Blastscan


https://docs.blastscan.io/


Mantlescan


https://docs.mantlescan.xyz/


Taikoscan


https://docs.taikoscan.io/


Xaiscan


https://docs.xaiscan.io/


XDCScan


https://docs.xdcscan.com/


Apescan


https://docs.apescan.io/


Worldscan


https://docs.worldscan.org/


Last updated 1 month ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Accounts

# Accounts

## Get Ether Balance for a Single Address

## Get Ether Balance for Multiple Addresses in a Single Call

## Get a list of 'Normal' Transactions By Address

## Get a list of 'Internal' Transactions by Address

## Get 'Internal Transactions' by Transaction Hash

## Get "Internal Transactions" by Block Range

## Get a list of 'ERC20 - Token Transfer Events' by Address

## Get a list of 'ERC721 - Token Transfer Events' by Address

## Get a list of 'ERC1155 - Token Transfer Events' by Address

## Get list of Blocks Validated by Address

## Get Beacon Chain Withdrawals by Address and Block Range

## Get Historical Ether Balance for a Single Address By BlockNo

Get Ether Balance for a Single Address


Get Ether Balance for Multiple Addresses in a Single Call


Get a list of 'Normal' Transactions By Address


Get a list of 'Internal' Transactions by Address


Get 'Internal Transactions' by Transaction Hash


Get "Internal Transactions" by Block Range


Get a list of 'ERC20 - Token Transfer Events' by Address


Get a list of 'ERC721 - Token Transfer Events' by Address


Get a list of 'ERC1155 - Token Transfer Events' by Address


Get list of Blocks Validated by Address


Get Beacon Chain Withdrawals by Address and Block Range


Get Historical Ether Balance for a Single Address By BlockNo


🎯
API ENDPOINTS


Endpoints with  are under the API Pro subscription. To upgrade your API plan, browse through the Etherscan APIs page.


Returns the Ether balance of a given address.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


tag


the string pre-defined block parameter, either earliest, pending or latest


Returns the balance of the accounts from a list of addresses.


Try this endpoint in your browser 🔗


Query Parameters


address


the strings representing the addresses to check for balance, separated by ,


up to 20 addresses per call


tag


the integer pre-defined block parameter, either earliest, pending or latest


Returns the list of transactions performed by an address, with optional pagination.


📝 Note : This API endpoint returns a maximum of 10000 records only.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the addresses to check for balance


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


sort


the sorting preference, use asc to sort by ascending and desc to sort by descendin Tip: Specify a smaller startblock and endblock range for faster search results.


Returns the list of internal transactions performed by an address, with optional pagination.


📝 Note : This API endpoint returns a maximum of 10000 records only.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the addresses to check for balance


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


💡 Tip: Specify a smaller startblock and endblock range for faster search results


Returns the list of internal transactions performed within a transaction.


📝 Note : This API endpoint returns a maximum of 10000 records only.


Try this endpoint in your browser 🔗


Query Parameters


txhash


the string representing the transaction hash to check for internal transactions


Returns the list of internal transactions performed within a block range, with optional pagination.


📝 Note : This API endpoint returns a maximum of 10000 records only.


Try this endpoint in your browser 🔗


Query Parameters


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the list of ERC-20 tokens transferred by an address, with optional filtering by token contract.


Usage:


ERC-20 transfers from an address, specify the address parameter


ERC-20 transfers from an address, specify the address parameter


ERC-20 transfers from a contract address, specify the contract address parameter


ERC-20 transfers from a contract address, specify the contract address parameter


ERC-20 transfers from an address filtered by a token contract, specify both address and contract address parameters.


ERC-20 transfers from an address filtered by a token contract, specify both address and contract address parameters.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


contractaddress


the string representing the token contract address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the list of ERC-721 ( NFT ) tokens transferred by an address, with optional filtering by token contract.


Usage:


ERC-721 transfers from an address, specify the address parameter


ERC-721 transfers from an address, specify the address parameter


ERC-721 transfers from a contract address, specify the contract address parameter


ERC-721 transfers from a contract address, specify the contract address parameter


ERC-721 transfers from an address filtered by a token contract, specify both address and contract address parameters.


ERC-721 transfers from an address filtered by a token contract, specify both address and contract address parameters.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


contractaddress


the string representing the token contract address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the list of ERC-1155 ( Multi Token Standard ) tokens transferred by an address, with optional filtering by token contract.


Usage:


ERC-1155 transfers from an address, specify the address parameter


ERC-1155 transfers from an address, specify the address parameter


ERC-1155 transfers from a contract address, specify the contract address parameter


ERC-1155 transfers from a contract address, specify the contract address parameter


ERC-1155 transfers from an address filtered by a token contract, specify both address and contract address parameters.


ERC-1155 transfers from an address filtered by a token contract, specify both address and contract address parameters.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


contractaddress


the string representing the token contract address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the list of blocks validated by an address.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


blocktype


the string pre-defined block type, either blocks for canonical blocks or uncles for uncle blocks only


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


Returns the beacon chain withdrawals made to an address.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for beacon withdrawals


contractaddress


the string representing the token contract address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


startblock


the integer block number to start searching for transactions


endblock


the integer block number to stop searching for transactions


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the balance of an address at a certain block height.


📝 Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


blockno


the integer block number to check balance for eg. 12697906


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken
```


`string`


`string`


`earliest`


`pending`


`latest`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balancemulti
   &address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balancemulti
   &address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67
   &tag=latest
   &apikey=YourApiKeyToken
```


`strings`


`,`


`integer`


`earliest`


`pending`


`latest`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlist
   &address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlist
   &address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


`startblock`


`endblock`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3
   &startblock=0
   &endblock=2702578
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3
   &startblock=0
   &endblock=2702578
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


`startblock`


`endblock`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &txhash=0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &txhash=0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
   &apikey=YourApiKeyToken
```


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &startblock=13481773
   &endblock=13491773
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlistinternal
   &startblock=13481773
   &endblock=13491773
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```


`integer`


`integer`


`integer`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokentx
   &contractaddress=0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2
   &address=0x4e83362442b8d1bec281594cea3050c8eb01311c
   &page=1
   &offset=100
   &startblock=0
   &endblock=27025780
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokentx
   &contractaddress=0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2
   &address=0x4e83362442b8d1bec281594cea3050c8eb01311c
   &page=1
   &offset=100
   &startblock=0
   &endblock=27025780
   &sort=asc
   &apikey=YourApiKeyToken
```


`address`


`contract address`


`address`


`contract address`


`string`


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokennfttx
   &contractaddress=0x06012c8cf97bead5deae237070f9587f8e7a266d
   &address=0x6975be450864c02b4613023c2152ee0743572325
   &page=1
   &offset=100
   &startblock=0
   &endblock=27025780
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokennfttx
   &contractaddress=0x06012c8cf97bead5deae237070f9587f8e7a266d
   &address=0x6975be450864c02b4613023c2152ee0743572325
   &page=1
   &offset=100
   &startblock=0
   &endblock=27025780
   &sort=asc
   &apikey=YourApiKeyToken
```


`address`


`contract address`


`address`


`contract address`


`string`


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=token1155tx
   &contractaddress=0x76be3b62873462d2142405439777e971754e8e77
   &address=0x83f564d180b58ad9a02a449105568189ee7de8cb
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=token1155tx
   &contractaddress=0x76be3b62873462d2142405439777e971754e8e77
   &address=0x83f564d180b58ad9a02a449105568189ee7de8cb
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=asc
   &apikey=YourApiKeyToken
```


`address`


`contract address`


`address`


`contract address`


`string`


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=getminedblocks
   &address=0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b
   &blocktype=blocks
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=getminedblocks
   &address=0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b
   &blocktype=blocks
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```


`string`


`string`


`blocks`


`uncles`


`integer`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txsBeaconWithdrawal
   &address=0xB9D7934878B5FB9610B3fE8A5e441e8fad7E293f
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=100
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txsBeaconWithdrawal
   &address=0xB9D7934878B5FB9610B3fE8A5e441e8fad7E293f
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=100
   &sort=asc
   &apikey=YourApiKeyToken
```


`string`


`string`


`integer`


`integer`


`integer`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balancehistory
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &blockno=8000000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=balancehistory
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &blockno=8000000
   &apikey=YourApiKeyToken
```


`string`


`integer`


`12697906`


---

# Contracts

# Contracts

## Get Contract ABI for Verified Contract Source Codes

## Get Contract Source Code for Verified Contract Source Codes

## Get Contract Creator and Creation Tx Hash

## Verify Source Code

## Check Source Code Verification Status

## Verify Proxy Contract

### Verifying Proxy Contract using cURL

### Checking Proxy Contract Verification Submission Status using cURL

Get Contract ABI for Verified Contract Source Codes


Get Contract Source Code for Verified Contract Source Codes


Get Contract Creator and Creation Tx Hash


Verify Source Code


Check Source Code Verification Status


Verify Proxy Contract


Verifying Proxy Contract using cURL


Checking Proxy Contract Verification Submission Status using cURL


🎯
API ENDPOINTS


Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract.


Find verified contracts ✅on our Verified Contracts Source Code page.


Try this endpoint in your browser 🔗


Query Parameters


address


the contract address that has a verified source code


Returns the Solidity source code of a verified smart contract.


📩 Tip : You can also download a CSV list of verified contracts addresses of which the code publishers have provided a corresponding Open Source license for redistribution.


Try this endpoint in your browser 🔗


Query Parameters


address


the contract address that has a verified source code


Returns a contract's deployer address and transaction hash it was created, up to 5 at a time.


Try this endpoint in your browser 🔗


Query Parameters


contractaddresses


the contract address , up to 5 at a time


Submits a contract source code to an Etherscan-like explorer for verification.


🌐 Tutorial : A full walk through of submitting multichain contract verification.


📝 Note : This endpoint is limited to 100 verifications/day, regardless of API PRO tier.


Query Parameters


Requests must be sent using HTTP POST


chainId


the chain to submit verification, such as 1 for mainnet


codeformat


single file, use
solidity-single-file
JSON file ( recommended ), use solidity-standard-json-input


sourceCode


the Solidity source code


constructorArguements


optional, include if your contract uses constructor arguments


contractaddress


the address your contract is deployed at


contractname


the name of your contract, such as

contracts/Verified.sol:Verified


compilerversion


compiler version used, such as v0.8.24+commit.e11b9ed9


Returns the success or error status of a contract verification request.


Try this endpoint in your browser 🔗


Query Parameters


guid


the unique guid received from the verification request


Submits a proxy contract source code to Etherscan for verification.


Requires a valid Etherscan API key, it will be rejected otherwise


Requires a valid Etherscan API key, it will be rejected otherwise


Current daily limit of 100 submissions per day per user (subject to change)


Current daily limit of 100 submissions per day per user (subject to change)


Only supports HTTP post


Only supports HTTP post


Upon successful submission you will receive a GUID (50 characters) as a receipt


Upon successful submission you will receive a GUID (50 characters) as a receipt


You may use this GUID to track the status of your submission


You may use this GUID to track the status of your submission


Verified proxy contracts will display the "Read/Write as Proxy" of the implementation contract under the contract address's contract tab


Verified proxy contracts will display the "Read/Write as Proxy" of the implementation contract under the contract address's contract tab


Last updated 12 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getabi
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getabi
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getsourcecode
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getsourcecode
   &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getcontractcreation
   &contractaddresses=0xB83c27805aAcA5C7082eB45C868d955Cf04C337F,0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45,0xe4462eb568E2DFbb5b0cA2D3DbB1A35C9Aa98aad,0xdAC17F958D2ee523a2206206994597C13D831ec7,0xf5b969064b91869fBF676ecAbcCd1c5563F591d0
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=getcontractcreation
   &contractaddresses=0xB83c27805aAcA5C7082eB45C868d955Cf04C337F,0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45,0xe4462eb568E2DFbb5b0cA2D3DbB1A35C9Aa98aad,0xdAC17F958D2ee523a2206206994597C13D831ec7,0xf5b969064b91869fBF676ecAbcCd1c5563F591d0
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=verifysourcecode
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=verifysourcecode
   &apikey=YourApiKeyToken
```


`1`


`solidity-single-file`


`solidity-standard-json-input`


`contracts/Verified.sol:Verified`


`v0.8.24+commit.e11b9ed9`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=checkverifystatus
   &guid=x3ryqcqr1zdknhfhkimqmizlcqpxncqc6nrvp3pgrcpfsqedqi
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=contract
   &action=checkverifystatus
   &guid=x3ryqcqr1zdknhfhkimqmizlcqpxncqc6nrvp3pgrcpfsqedqi
   &apikey=YourApiKeyToken
```


`guid`


```
// example with only the mandatory contract address parameter
curl -d "address=0xcbdcd3815b5f975e1a2c944a9b2cd1c985a1cb7f" "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=verifyproxycontract&apikey=YourApiKeyToken"
// example using the expectedimplementation optional parameter
// the expectedimplementation enforces a check to ensure the returned implementation contract address == address picked up by the verifier
curl -d "address=0xbc46363a7669f6e12353fa95bb067aead3675c29&expectedimplementation=0xe45a5176bc0f2c1198e2451c4e4501d4ed9b65a6" "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=verifyproxycontract&apikey=YourApiKeyToken"
```


```
// example with only the mandatory contract address parameter
curl -d "address=0xcbdcd3815b5f975e1a2c944a9b2cd1c985a1cb7f" "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=verifyproxycontract&apikey=YourApiKeyToken"
// example using the expectedimplementation optional parameter
// the expectedimplementation enforces a check to ensure the returned implementation contract address == address picked up by the verifier
curl -d "address=0xbc46363a7669f6e12353fa95bb067aead3675c29&expectedimplementation=0xe45a5176bc0f2c1198e2451c4e4501d4ed9b65a6" "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=verifyproxycontract&apikey=YourApiKeyToken"
```


```
curl "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=checkproxyverification&guid=gwgrrnfy56zf6vc1fljuejwg6pelnc5yns6fg6y2i6zfpgzquz&apikey=YourApiKeyToken"
```


`curl "https://api.etherscan.io/v2/api?chainid=1&module=contract&action=checkproxyverification&guid=gwgrrnfy56zf6vc1fljuejwg6pelnc5yns6fg6y2i6zfpgzquz&apikey=YourApiKeyToken"`


---

# Stats

# Transactions

## Check Contract Execution Status

## Check Transaction Receipt Status

Check Contract Execution Status


Check Transaction Receipt Status


🎯
API ENDPOINTS


Returns the status code of a contract execution.


Try this endpoint in your browser 🔗


Query Parameters


txhash


the string representing the transaction hash to check the execution status


Returns the status code of a transaction execution.


📝 Note: Only applicable for post Byzantium Fork transactions.


Try this endpoint in your browser 🔗


Query Parameters


txhash


the string representing the transaction hash to check the execution status


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1&module=transaction
   &action=getstatus
   &txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1&module=transaction
   &action=getstatus
   &txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a
   &apikey=YourApiKeyToken
```


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1&module=transaction
   &action=gettxreceiptstatus
   &txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1&module=transaction
   &action=gettxreceiptstatus
   &txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76
   &apikey=YourApiKeyToken
```


`string`


---

# Blocks

# Blocks

## Get Block And Uncle Rewards by BlockNo

## Get Block Transactions Count by BlockNo

## Get Estimated Block Countdown Time by BlockNo

## Get Block Number by Timestamp

## Get Daily Average Block Size

## Get Daily Block Count and Rewards

## Get Daily Block Rewards

## Get Daily Average Time for A Block to be Included in the Ethereum Blockchain

## Get Daily Uncle Block Count and Rewards

Get Block And Uncle Rewards by BlockNo


Get Block Transactions Count by BlockNo


Get Estimated Block Countdown Time by BlockNo


Get Block Number by Timestamp


Get Daily Average Block Size


Get Daily Block Count and Rewards


Get Daily Block Rewards


Get Daily Average Time for A Block to be Included in the Ethereum Blockchain


Get Daily Uncle Block Count and Rewards


🎯
API ENDPOINTS


Endpoints with  are under the API Pro subscription. To upgrade your API plan, browse through the Etherscan APIs page.


Returns the block reward and 'Uncle' block rewards.


Try this endpoint in your browser 🔗


Query Parameters


blockno


the integer block number to check block rewards for eg. 12697906


Returns the number of transactions in a specified block.


This endpoint is only available on Etherscan, `chainId` 1


Try this endpoint in your browser 🔗


Query Parameters


blockno


the integer block number to get the transaction count for, eg. 2165403


Returns the estimated time remaining, in seconds, until a certain block is mined.


Try this endpoint in your browser 🔗


Query Parameters


blockno


the integer block number to estimate time remaining to be mined eg. 12697906


Returns the block number that was mined at a certain timestamp.


Try this endpoint in your browser 🔗


Query Parameters


timestamp


the integer representing the Unix timestamp in seconds.


closest


the closest available block to the provided timestamp, either before or after


⏳ Tip : Convert a regular date-time to a Unix timestamp.


Returns the daily average block size within a date range.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the number of blocks mined daily and the amount of block rewards.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the amount of block rewards distributed to miners daily.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the daily average of time needed for a block to be successfully mined.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the number of 'Uncle' blocks mined daily and the amount of 'Uncle' block rewards.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Last updated 12 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblockreward
   &blockno=2165403
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblockreward
   &blockno=2165403
   &apikey=YourApiKeyToken
```


`integer`


`12697906`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblocktxnscount
   &blockno=2165403
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblocktxnscount
   &blockno=2165403
   &apikey=YourApiKeyToken
```


`integer`


`2165403`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblockcountdown
   &blockno=16701588
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblockcountdown
   &blockno=16701588
   &apikey=YourApiKeyToken
```


`integer`


`12697906`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblocknobytime
   &timestamp=1578638524
   &closest=before
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=block
   &action=getblocknobytime
   &timestamp=1578638524
   &closest=before
   &apikey=YourApiKeyToken
```


`integer`


`before`


`after`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgblocksize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgblocksize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyblockrewards
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyblockrewards
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgblocktime
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgblocktime
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyuncleblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyuncleblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


---

# Logs

# Logs

## Get Event Logs by Address

## Get Event Logs by Topics

## Get Event Logs by Address filtered by Topics

Get Event Logs by Address


Get Event Logs by Topics


Get Event Logs by Address filtered by Topics


🎯
API ENDPOINTS


Returns the event logs from an address, with optional filtering by block range.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for logs


fromBlock


the integer block number to start searching for logs eg. 12878196


toBlock


the integer block number to stop searching for logs eg. 12879196


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page

limited to 1000 records per query, use the page parameter for subsequent records


Returns the events log in a block range, filtered by topics.


Usage:


For a single topic, specify the topic number such as topic0, topic1, topic2, topic3


For a single topic, specify the topic number such as topic0, topic1, topic2, topic3


For multiple topics, specify the topic numbers and topic operator either and or or such as below

topic0_1_opr (and|or between topic0 & topic1), topic1_2_opr (and|or between topic1 & topic2) topic2_3_opr (and|or between topic2 & topic3), topic0_2_opr (and|or between topic0 & topic2) topic0_3_opr (and|or between topic0 & topic3), topic1_3_opr (and|or between topic1 & topic3)


For multiple topics, specify the topic numbers and topic operator either and or or such as below

topic0_1_opr (and|or between topic0 & topic1), topic1_2_opr (and|or between topic1 & topic2) topic2_3_opr (and|or between topic2 & topic3), topic0_2_opr (and|or between topic0 & topic2) topic0_3_opr (and|or between topic0 & topic3), topic1_3_opr (and|or between topic1 & topic3)


Try this endpoint in your browser 🔗


Query Parameters


fromBlock


the integer block number to start searching for logs eg. 12878196


toBlock


the integer block number to stop searching for logs eg. 12879196


topic


the topic numbers to search for

limited totopic0, topic1, topic2, topic3


topicOperator


the topic operator when multiple topic combinations are used

limited to and or or


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page

limited to 1000 records per query, use the page parameter for subsequent records


Returns the event logs from an address, filtered by topics and block range.


Try this endpoint in your browser 🔗


Query Parameters


fromBlock


the integer block number to start searching for logs eg. 12878196


toBlock


the integer block number to stop searching for logs eg. 12879196


address


the string representing the address to check for logs


topic


the topic numbers to search for

limited totopic0, topic1, topic2, topic3


topicOperator


the topic operator when multiple topic combinations are used

limited to and or or


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page

limited to 1000 records per query, use the page parameter for subsequent records


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8
   &fromBlock=12878196
   &toBlock=12878196
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8
   &fromBlock=12878196
   &toBlock=12878196
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


`string`


`integer`


`12878196`


`integer`


`12879196`


`integer`


`page`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=12878196
   &toBlock=12879196
   &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
   &topic0_1_opr=and
   &topic1=0x0000000000000000000000000000000000000000000000000000000000000000
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=12878196
   &toBlock=12879196
   &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
   &topic0_1_opr=and
   &topic1=0x0000000000000000000000000000000000000000000000000000000000000000
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


`topic0`


`topic1`


`topic2`


`topic3`


`and`


`or`


`integer`


`12878196`


`integer`


`12879196`


`topic0`


`topic1`


`topic2`


`topic3`


`and`


`or`


`integer`


`page`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=15073139
   &toBlock=15074139
   &address=0x59728544b08ab483533076417fbbb2fd0b17ce3a
   &topic0=0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d
   &topic0_1_opr=and
   &topic1=0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=15073139
   &toBlock=15074139
   &address=0x59728544b08ab483533076417fbbb2fd0b17ce3a
   &topic0=0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d
   &topic0_1_opr=and
   &topic1=0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```


`integer`


`12878196`


`integer`


`12879196`


`string`


`topic0`


`topic1`


`topic2`


`topic3`


`and`


`or`


`integer`


`page`


---

# Geth Parity Proxy

# Geth/Parity Proxy

## eth_blockNumber

## eth_getBlockByNumber

## eth_getUncleByBlockNumberAndIndex

## eth_getBlockTransactionCountByNumber

## eth_getTransactionByHash

## eth_getTransactionByBlockNumberAndIndex

## eth_getTransactionCount

## eth_sendRawTransaction

## eth_getTransactionReceipt

## eth_call

## eth_getCode

## eth_getStorageAt

## eth_gasPrice

## eth_estimateGas

eth_blockNumber


eth_getBlockByNumber


eth_getUncleByBlockNumberAndIndex


eth_getBlockTransactionCountByNumber


eth_getTransactionByHash


eth_getTransactionByBlockNumberAndIndex


eth_getTransactionCount


eth_sendRawTransaction


eth_getTransactionReceipt


eth_call


eth_getCode


eth_getStorageAt


eth_gasPrice


eth_estimateGas


🎯
API ENDPOINTS


For the full documentation of available parameters and descriptions, please visit the official Ethereum JSON-RPC docs.


For compatibility with Parity, please prefix all hex strings with " 0x ".


Returns the number of most recent block


Try this endpoint in your browser 🔗


No parameters required.


Returns information about a block by block number.


Try this endpoint in your browser 🔗


Query Parameters


tag


the block number, in hex eg. 0xC36B3C


boolean


the boolean value to show full transaction objects.


when true, returns full transaction objects and their information, when false only returns a list of transactions.


Returns information about a uncle by block number.


Try this endpoint in your browser 🔗


Query Parameters


tag


the block number, in hex eg. 0xC36B3C


index


the position of the uncle's index in the block, in hex eg. 0x5


Returns the number of transactions in a block.


Try this endpoint in your browser 🔗


Query Parameters


tag


the block number, in hex eg. 0x10FB78


Returns the information about a transaction requested by transaction hash.


Try this endpoint in your browser 🔗


Query Parameters


txhash


the string representing the hash of the transaction


Returns information about a transaction by block number and transaction index position.


Try this endpoint in your browser 🔗


Query Parameters


tag


the block number, in hex eg. 0x10FB78


index


the position of the uncle's index in the block, in hex eg. 0x0


Returns the number of transactions performed by an address.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to get transaction count


tag


the string pre-defined block parameter, either earliest, pending or latest


Submits a pre-signed transaction for broadcast to the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


hex


the string representing the signed raw transaction data to broadcast.


💡 Tip: Send a POST request if your hex string is particularly long.


🖋️ For more information on creating a signed raw transaction, visit this page.


Returns the receipt of a transaction by transaction hash.


Try this endpoint in your browser 🔗


Query Parameters


txhash


the string representing the hash of the transaction


Executes a new message call immediately without creating a transaction on the block chain.


Try this endpoint in your browser 🔗


Query Parameters


to


the string representing the address to interact with


data


the hash of the method signature and encoded parameters


tag


the string pre-defined block parameter, either earliest, pending or latest


⛽ Note: The gas parameter is capped at 2x the current block gas limit.


Returns code at a given address.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to get code


tag


the string pre-defined block parameter, either earliest, pending or latest


Returns the value from a storage position at a given address.


This endpoint is still experimental and may have potential issues


Try this endpoint in your browser


Query Parameters


address


the string representing the address to get code


position


the hex code of the position in storage, eg 0x0


tag


the string pre-defined block parameter, either earliest, pending or latest


Returns the current price per gas in wei.


Try this endpoint in your browser 🔗


No parameters required.


Makes a call or transaction, which won't be added to the blockchain and returns the used gas.


Try this endpoint in your browser 🔗


Query Parameters


data


the hash of the method signature and encoded parameters


to


the string representing the address to interact with


value


the value sent in this transaction, in hex eg. 0xff22


gas


the amount of gas provided for the transaction, in hex eg. 0x5f5e0ff


gasPrice


the gas price paid for each unit of gas, in wei


post EIP-1559, the gasPrice has to be higher than the block's baseFeePerGas


⛽ Note: The gas parameter is capped at 2x the current block gas limit.


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_blockNumber
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_blockNumber
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getBlockByNumber
   &tag=0x10d4f
   &boolean=true
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getBlockByNumber
   &tag=0x10d4f
   &boolean=true
   &apikey=YourApiKeyToken
```


`0xC36B3C`


`boolean`


`true`


`false`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getUncleByBlockNumberAndIndex
   &tag=0xC63276
   &index=0x0
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getUncleByBlockNumberAndIndex
   &tag=0xC63276
   &index=0x0
   &apikey=YourApiKeyToken
```


`0xC36B3C`


`0x5`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getBlockTransactionCountByNumber
   &tag=0x10FB78
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getBlockTransactionCountByNumber
   &tag=0x10FB78
   &apikey=YourApiKeyToken
```


`0x10FB78`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionByHash
   &txhash=0xbc78ab8a9e9a0bca7d0321a27b2c03addeae08ba81ea98b03cd3dd237eabed44
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionByHash
   &txhash=0xbc78ab8a9e9a0bca7d0321a27b2c03addeae08ba81ea98b03cd3dd237eabed44
   &apikey=YourApiKeyToken
```


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionByBlockNumberAndIndex
   &tag=0xC6331D
   &index=0x11A
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionByBlockNumberAndIndex
   &tag=0xC6331D
   &index=0x11A
   &apikey=YourApiKeyToken
```


`0x10FB78`


`0x0`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionCount
   &address=0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionCount
   &address=0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e
   &tag=latest
   &apikey=YourApiKeyToken
```


`string`


`string`


`earliest`


`pending`


`latest`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_sendRawTransaction
   &hex=0xf904808000831cfde080
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_sendRawTransaction
   &hex=0xf904808000831cfde080
   &apikey=YourApiKeyToken
```


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionReceipt
   &txhash=0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getTransactionReceipt
   &txhash=0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb
   &apikey=YourApiKeyToken
```


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_call
   &to=0xAEEF46DB4855E25702F8237E8f403FddcaF931C0
   &data=0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_call
   &to=0xAEEF46DB4855E25702F8237E8f403FddcaF931C0
   &data=0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724
   &tag=latest
   &apikey=YourApiKeyToken
```


`string`


`string`


`earliest`


`pending`


`latest`


`gas`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getCode
   &address=0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getCode
   &address=0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c
   &tag=latest
   &apikey=YourApiKeyToken
```


`string`


`string`


`earliest`


`pending`


`latest`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getStorageAt
   &address=0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd
   &position=0x0
   &tag=latest
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_getStorageAt
   &address=0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd
   &position=0x0
   &tag=latest
   &apikey=YourApiKeyToken
```


`string`


`0x0`


`string`


`earliest`


`pending`


`latest`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_gasPrice
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_gasPrice
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_estimateGas
   &data=0x4e71d92d
   &to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843
   &value=0xff22
   &gasPrice=0x51da038cc
   &gas=0x5f5e0ff
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=proxy
   &action=eth_estimateGas
   &data=0x4e71d92d
   &to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843
   &value=0xff22
   &gasPrice=0x51da038cc
   &gas=0x5f5e0ff
   &apikey=YourApiKeyToken
```


`string`


`0xff22`


`0x5f5e0ff`


`gasPrice`


`baseFeePerGas`


`gas`


---

# Tokens

# Tokens

## Get ERC20-Token TotalSupply by ContractAddress

## Get ERC20-Token Account Balance for TokenContractAddress

## Get Historical ERC20-Token TotalSupply by ContractAddress & BlockNo

## Get Historical ERC20-Token Account Balance for TokenContractAddress by BlockNo

## Get Token Holder List by Contract Address

### Get Token Holder Count by Contract Address

## Get Token Info by ContractAddress

## Get Address ERC20 Token Holding

## Get Address ERC721 Token Holding

## Get Address ERC721 Token Inventory By Contract Address

Get ERC20-Token TotalSupply by ContractAddress


Get ERC20-Token Account Balance for TokenContractAddress


Get Historical ERC20-Token TotalSupply by ContractAddress & BlockNo


Get Historical ERC20-Token Account Balance for TokenContractAddress by BlockNo


Get Token Holder List by Contract Address


Get Token Holder Count by Contract Address


Get Token Info by ContractAddress


Get Address ERC20 Token Holding


Get Address ERC721 Token Holding


Get Address ERC721 Token Inventory By Contract Address


🎯
API ENDPOINTS


Endpoints with  are under the API Pro subscription. To upgrade your API plan, browse through the Etherscan APIs page.


Returns the current amount of an ERC-20 token in circulation.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20 token


Returns the current balance of an ERC-20 token of an address.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20 token


address


the string representing the address to check for token balance


Returns the amount of an ERC-20 token in circulation at a certain block height.


📝 Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20 token


blockno


the integer block number to check total supply for eg. 12697906


Returns the balance of an ERC-20 token of an address at a certain block height.


📝 Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20 token


address


the string representing the address to check for balance


blockno


the integer block number to check total supply for eg. 12697906


Return the current ERC20 token holders and number of tokens held.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20 token


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


Return a simple count of the number of ERC20 token holders.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC20 token


Returns project information and social media links of an ERC20/ERC721/ERC1155 token.


📝 Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


contractaddress


the contract address of the ERC-20/ERC-721 token to retrieve token info


Returns the ERC-20 tokens and amount held by an address.


Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


Returns the ERC-721 tokens and amount held by an address.


Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for balance


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


Returns the ERC-721 token inventory of an address, filtered by contract address.


📝 Note : This endpoint is throttled to 2 calls/second regardless of API Pro tier.


Try this endpoint in your browser 🔗


Query Parameters


address


the string representing the address to check for inventory


contractaddress


the string representing the ERC-721 token contractaddress to check for inventory


page


the integer page number, if pagination is enabled


offset


the number of records displayed per page

limited to 1000 records per query, use the page parameter for subsequent records


Last updated 12 days ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupply
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupply
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalance
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &tag=latest&apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalance
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &tag=latest&apikey=YourApiKeyToken
```


`contract address`


`string`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupplyhistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &blockno=8000000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupplyhistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &blockno=8000000
   &apikey=YourApiKeyToken
```


`contract address`


`integer`


`12697906`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalancehistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &blockno=8000000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalancehistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &blockno=8000000
   &apikey=YourApiKeyToken
```


`contract address`


`string`


`integer`


`12697906`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholderlist
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholderlist
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```


`contract address`


`integer`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholdercount
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholdercount
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokeninfo
   &contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokeninfo
   &contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07
   &apikey=YourApiKeyToken
```


`contract address`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokenbalance
   &address=0x983e3660c0bE01991785F80f266A84B911ab59b0
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokenbalance
   &address=0x983e3660c0bE01991785F80f266A84B911ab59b0
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


`string`


`integer`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftbalance
   &address=0x6b52e83941eb10f9c613c395a834457559a80114
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftbalance
   &address=0x6b52e83941eb10f9c613c395a834457559a80114
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


`string`


`integer`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftinventory
   &address=0x123432244443b54409430979df8333f9308a6040
   &contractaddress=0xed5af388653567af2f388e6224dc7c4b3241c544
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftinventory
   &address=0x123432244443b54409430979df8333f9308a6040
   &contractaddress=0xed5af388653567af2f388e6224dc7c4b3241c544
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```


`string`


`string`


`integer`


`page`


---

# Gas Tracker

# Gas Tracker

## Get Estimation of Confirmation Time

## Get Gas Oracle

## Get Daily Average Gas Limit

## Get Ethereum Daily Total Gas Used

## Get Daily Average Gas Price

Get Estimation of Confirmation Time


Get Gas Oracle


Get Daily Average Gas Limit


Get Ethereum Daily Total Gas Used


Get Daily Average Gas Price


🎯
API ENDPOINTS


Endpoints with  are under the API Pro subscription. To upgrade your API plan, browse through the Etherscan APIs page.


Returns the estimated time, in seconds, for a transaction to be confirmed on the blockchain.


Try this endpoint in your browser 🔗


Query Parameters


gasprice


the price paid per unit of gas, in wei


📖 Tip: Easily convert Ethereum units using our unit converter.


Returns the current Safe, Proposed and Fast gas prices.


Post EIP-1559 🔥 changes :


Safe/Proposed/Fast gas price recommendations are now modeled as Priority Fees.


Safe/Proposed/Fast gas price recommendations are now modeled as Priority Fees.


New field suggestBaseFee , the baseFee of the next pending block


New field suggestBaseFee , the baseFee of the next pending block


New field gasUsedRatio, to estimate how busy the network is


New field gasUsedRatio, to estimate how busy the network is


Learn more about the gas changes in EIP-1559.


Try this endpoint in your browser 🔗


No parameters required.


Returns the historical daily average gas limit of the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-01-31


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the total amount of gas used daily for transctions on the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-01-31


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the daily average gas price used on the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-01-31


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasestimate
   &gasprice=2000000000
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasestimate
   &gasprice=2000000000
   &apikey=YourApiKeyToken
```


`wei`


`suggestBaseFee`


`gasUsedRatio`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasoracle
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasoracle
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggaslimit
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggaslimit
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-01-31`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailygasused
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailygasused
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-01-31`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggasprice
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggasprice
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-01-31`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


---

# Stats 1

# Stats

## Get Total Supply of Ether

## Get Total Supply of Ether 2

## Get Ether Last Price

## Get Ethereum Nodes Size

## Get Total Nodes Count

## Get Daily Network Transaction Fee

## Get Daily New Address Count

## Get Daily Network Utilization

## Get Daily Average Network Hash Rate

## Get Daily Transaction Count

## Get Daily Average Network Difficulty

## Get Ether Historical Daily Market Cap

## Get Ether Historical Price

Get Total Supply of Ether


Get Total Supply of Ether 2


Get Ether Last Price


Get Ethereum Nodes Size


Get Total Nodes Count


Get Daily Network Transaction Fee


Get Daily New Address Count


Get Daily Network Utilization


Get Daily Average Network Hash Rate


Get Daily Transaction Count


Get Daily Average Network Difficulty


Get Ether Historical Daily Market Cap


Get Ether Historical Price


🎯
API ENDPOINTS


Endpoints with  are under the API Pro subscription. To upgrade your API plan, kindly visit Etherscan API Pro.


Returns the current amount of Ether in circulation excluding ETH2 Staking rewards and EIP1559 burnt fees.


Try this endpoint in your browser 🔗


No parameters required.


Returns the current amount of Ether in circulation, ETH2 Staking rewards, EIP1559 burnt fees, and total withdrawn ETH from the beacon chain.


Try this endpoint in your browser 🔗


No parameters required.


Returns the latest price of 1 ETH.


Try this endpoint in your browser 🔗


No parameters required.


Returns the size of the Ethereum blockchain, in bytes, over a date range.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


clienttype


the Ethereum node client to use, either geth or parity


syncmode


the type of node to run, either default or archive


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the total number of discoverable Ethereum nodes.


Try this endpoint in your browser 🔗


No parameters required.


Returns the amount of transaction fees paid to miners per day.


Try this endpoint in your browser 🔗


No parameters required.


Returns the number of new Ethereum addresses created per day.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the daily average gas used over gas limit, in percentage.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the historical measure of processing power of the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the number of transactions performed on the Ethereum blockchain per day.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the historical mining difficulty of the Ethereum network.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the historical Ether daily market capitalization.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Returns the historical price of 1 ETH.


Try this endpoint in your browser 🔗


Query Parameters


startdate


the starting date in yyyy-MM-dd format, eg. 2019-02-01


enddate


the ending date in yyyy-MM-dd format, eg. 2019-02-28


sort


the sorting preference, use asc to sort by ascending and desc to sort by descending


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethsupply
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethsupply
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethsupply2
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethsupply2
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethprice
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethprice
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=chainsize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &clienttype=geth
   &syncmode=default
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=chainsize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &clienttype=geth
   &syncmode=default
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`geth`


`parity`


`default`


`archive`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=nodecount
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=nodecount
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailytxnfee
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailytxnfee
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailynewaddress
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailynewaddress
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailynetutilization
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailynetutilization
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavghashrate
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavghashrate
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailytx
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailytx
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgnetdifficulty
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=dailyavgnetdifficulty
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethdailymarketcap
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethdailymarketcap
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethdailyprice
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=ethdailyprice
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```


`yyyy-MM-dd`


`2019-02-01`


`yyyy-MM-dd`


`2019-02-28`


`asc`


`desc`


---

# Chain Specific

# Chain Specific

## Polygon [137]

### Get list of Plasma Deposits by Address

Polygon [137]


Get list of Plasma Deposits by Address


🎯
API ENDPOINTS


Returns a list of Plasma Deposits received by an address.


Try this endpoint in your browser 🔗


Query Parameters


Parameter


Description


address


the string representing the address to check for balance


blocktype


the string pre-defined block type, blocksfor canonical blocks


page


the integer page number, if pagination is enabled


offset


the number of transactions displayed per page


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?chainid=137
   &module=account
   &action=txnbridge
   &address=0x4880bd4695a8e59dc527d124085749744b6c988e
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?chainid=137
   &module=account
   &action=txnbridge
   &address=0x4880bd4695a8e59dc527d124085749744b6c988e
   &apikey=YourApiKeyToken
```


`string`


`string`


`blocks`


`integer`


---

# Blocks 1

# Usage

## Check Etherscan credit usage

## List supported chains

Check Etherscan credit usage


List supported chains


🎯
API ENDPOINTS


Returns the amount of API credits available, and reset countdown.


Try this endpoint in your browser  🔗


No parameters required.


Returns a list of supported Etherscan explorer APIs, with web explorer links.


Try this endpoint in your browser 🔗


No parameters required.


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


```
https://api.etherscan.io/v2/api
   ?&module=getapilimit
   &action=getapilimit
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/api
   ?&module=getapilimit
   &action=getapilimit
   &apikey=YourApiKeyToken
```


```
https://api.etherscan.io/v2/chainlist
```


`https://api.etherscan.io/v2/chainlist`


---

# Etherscan Api Pro

# Etherscan API PRO

### Professional Endpoints

### Higher Rate Limits

## Upgrading to API PRO

Professional Endpoints


Higher Rate Limits


Upgrading to API PRO


🏆
API PRO


Etherscan API PRO  provides additional endpoints and higher rate limits to help you ship faster and support more users 🚢


Ethereum along with 50+ chains are supported chain under Etherscan API PRO, to upgrade head over to Etherscan APIs


Focus on your product and avoid manual indexing for


ETH and token balances at any point in time


ETH and token balances at any point in time


Token holders of any contract address ( selected chains )


Token holders of any contract address ( selected chains )


Token portfolio of an address ( selected chains )


Token portfolio of an address ( selected chains )


Support more users with additional rate limits, from 10 upwards of 30 calls/s.


Suitable for accounting platforms 💰 doing daily portfolio updates, exchanges 🏦 doing transaction checks, NFT platforms 🎨 indexing trades.


For enterprise usage, scale up with dedicated instances that have dedicated rate limits.


To upgrade, head over to Etherscan and select a suitable plan.


You will also have access to all Etherscan based explorer APIs.


Do note that PRO endpoints are only available on mainnet, and not to any testnets.


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Checking Usage

# Checking Usage

### Overage Charges

🤝
SUPPORT


A calming green indicator indicates your current usage, and will gradually turn red if you're close to your account limits 🌡️.


All keys contribute to the overall rate limits of your account.


You may also check each key's usage count, and the last 5 calls made with this key.


This will autoscale your app and allow uninterrupted daily limits, you will then be billed for the extra usage.


Toggle this on if you expect a burst of request at launch or mints, but please keep an eye on it.


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

# Rate Limits

# Rate Limits

### Per Second Limits

### Daily Limits

Per Second Limits


Daily Limits


🤝
SUPPORT


There are 2 parts to rate limits 🚧


The number of calls/second you can make.


On error, you will get an message like Max calls per sec rate limit reached (5/sec)


The number of calls you can make per day, resets at 00:00 UTC


If do not enable overage charges in your settings, your usage will be interrupted if you exceed your daily limits


Free


5 calls/second , up to 100,000 calls/day


Standard


10 calls/second , up to 200,000 calls/day


Advanced


20 calls/second , up to 500,000 calls/day


Professional


30 calls/second , up to 1,000,000 calls/day


Pro Plus ( includes name tags )


30 calls/second , up to 1,500,000 calls/day


Dedicated/Custom


Contact Us


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


`Max calls per sec rate limit reached (5/sec)`


`00:00 UTC`


---

# Common Error Messages

# Common Error Messages

### Missing or Unsupported Chain

### Invalid API Key

### Max rate limit

### Missing or invalid action

### Endpoint-specific errors

### Query Timeout

Missing or Unsupported Chain


Invalid API Key


Max rate limit


Missing or invalid action


Endpoint-specific errors


Query Timeout


🤝
SUPPORT


An API call that encounters an error ⚠️ will return 0 as its status code and display the cause of the error under the result field.


"Missing or unsupported chainid parameter (required for v2 api), please see chainlist for the list of supported chainids"


The chain you've specified is not supported by us yet. It could also be that you've sent multiple chains at the same time like 420,10 , you can only send one at a time.


"Invalid API Key"


This error occurs when you specify an invalid API Key.


Ensure you are using your Etherscan API Key, keys from other chains like Polygonscan/Arbiscan are not valid for V2.


Keys do take a few minutes to activate, anything longer than should be alarming.


"Max rate limit reached, please use API Key for higher rate limit"


This error occurs when you exceed the rate limit assigned to your specific API key.


To resolve, adhere to the rate limits of your available plan.


If you are using a script or application, apply throttling like a token bucket to limit the frequency of calls.


"Error! Missing Or invalid Action name"


This error occurs when you do not specify, or specify an invalid module and action name.


To resolve, double check your API query to use a valid module and action name.


If you require some help getting started, try copying the sample queries provided in the API Endpoints and pasting them into your browser.


"Error! Block number already pass"


"Error! Invalid address format"


"Contract source code not verified"


These error messages returned are specific to certain endpoints and their related parameters.


To resolve, kindly refer to the specific endpoint's documentation, and check for the correct format or values to be specified as parameters.


"Query Timeout occured. Please select a smaller result dataset"


"Unexpected err, timeout occurred or server too busy. Please try again later"


This error occurs when you have sent a particularly large query that did not manage to be completed in time.


To resolve, consider selecting a smaller date/block range, though you may ping us if you think the issue may be performance related.


Last updated 2 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


`status code`


`result`


```
{
   "status":"0",
   "message":"NOTOK",
   "result":"Max rate limit reached, please use API Key for higher rate limit"
}
```


```
{
   "status":"0",
   "message":"NOTOK",
   "result":"Max rate limit reached, please use API Key for higher rate limit"
}
```


`420,10`


`module`


`action`


---

# Getting Help

# Getting Help

## Support Tickets

## Twitter

## Freshstatus

Support Tickets


Twitter


Freshstatus


🤝
SUPPORT


Beware of phishing attempts and emails impersonating the team at Etherscan, we only communicate from the channels below


Our emails always come from the domain @etherscan.io


Keep in mind that as a block explorer service, we cannot cancel, refund or reverse transactions as we do not process them.


If your issues are related to transactions, you may find helpful articles over at the Etherscan Information Center.


Reach out to us via a support ticket.


For general updates, new feature releases and community support, keep in touch with us via Twitter.


Follow us on Twitter.


Announcements for ongoing and scheduled maintenance works that may affect certain services used.


Check Etherscan's network status.


Last updated 4 months ago


This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the privacy policy.


---

