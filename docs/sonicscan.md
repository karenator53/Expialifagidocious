**Endpoint URLs**

An API key generated on Sonicscan can be used across all **mainnet** and **testnet** explorers.

Similarly, all endpoints and parameter formatting remain the same across testnet explorers, you are only required to change the relevant API endpoint URL as follows.

Network

URL

Documentation

Mainnet

<https://api.sonicscan.org/api>

<https://docs.sonicscan.org/>

Testnet

<https://api-testnet.sonicscan.org/api>

<https://docs.sonicscan.org/sonic-testnet>

**Accounts**

**Get S Balance for a Single Address**

Returns the S balance of a given address.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=balance

&address=0xbbbbb8c4364ec2ce52c59d2ed3e56f307e529a94

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=balance&address=0xbbbbb8c4364ec2ce52c59d2ed3e56f307e529a94&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to check for balance

tag

the string pre-defined block parameter, either earliest, pending or latest

**Get S Balance for Multiple Addresses in a Single Call**

Returns the balance of the accounts from a list of addresses.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=balancemulti

&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=balancemulti&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the strings representing the addresses to check for balance, separated by ,

up to **20 addresses** per call

tag

the integer pre-defined block parameter, either earliest, pending or latest

**Get a list of 'Normal' Transactions By Address**

Returns the list of transactions performed by an address, with optional pagination.

**​**​ ​ 📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=txlist

&address=0xbbbbb8c4364ec2ce52c59d2ed3e56f307e529a94

&startblock=0

&endblock=99999999

&page=1

&offset=10

&sort=asc

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=txlist&address=0xbbbbb8c4364ec2ce52c59d2ed3e56f307e529a94&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

the sorting preference, use asc to sort by ascending and desc to sort by descendin **Tip:** Specify a smaller startblock and endblock range for faster search results.

**Get a list of 'Internal' Transactions by Address**

Returns the list of internal transactions performed by an address, with optional pagination.

📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=txlistinternal

&address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3

&startblock=0

&endblock=2702578

&page=1

&offset=10

&sort=asc

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=txlistinternal&address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3&startblock=0&endblock=2702578&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

💡 **Tip:** Specify a smaller startblock and endblock range for faster search results

**Get 'Internal Transactions' by Transaction Hash**

Returns the list of internal transactions performed within a transaction.

📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=txlistinternal

&txhash=0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=txlistinternal&txhash=0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the string representing the transaction hash to check for internal transactions

**Get "Internal Transactions" by Block Range**

Returns the list of internal transactions performed within a block range, with optional pagination.

​​ 📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=txlistinternal

&startblock=13481773

&endblock=13491773

&page=1

&offset=10

&sort=asc

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=txlistinternal&startblock=13481773&endblock=13491773&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

**Get a list of 'ERC20 - Token Transfer Events' by Address**

Returns the list of ERC-20 tokens transferred by an address, with optional filtering by token contract.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=tokentx

&contractaddress=0xaf19a4fead8d1b7b5dd7603ea64da4f9e6c64b1f

&address=0x65ac69e771c62794e5df9d546d205180ed1abeef

&page=1

&offset=100

&startblock=0

&endblock=27025780

&sort=asc

&apikey=YourApiKeyToken

Usage:

- ERC-20 transfers from an **address**, specify the address parameter
- ERC-20 transfers from a **contract address**, specify the contract address parameter
- ERC-20 transfers from an **address** filtered by a **token contract**, specify both address and contract address parameters.

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=tokentx&contractaddress=0xaf19a4fead8d1b7b5dd7603ea64da4f9e6c64b1f&address=0x65ac69e771c62794e5df9d546d205180ed1abeef&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

**Get a list of 'ERC721 - Token Transfer Events' by Address**

Returns the list of ERC-721 ( NFT ) tokens transferred by an address, with optional filtering by token contract.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=tokennfttx

&contractaddress=0x06012c8cf97bead5deae237070f9587f8e7a266d

&address=0x6975be450864c02b4613023c2152ee0743572325

&page=1

&offset=100

&startblock=0

&endblock=27025780

&sort=asc

&apikey=YourApiKeyToken

Usage:

- ERC-721 transfers from an **address**, specify the address parameter
- ERC-721 transfers from a **contract address**, specify the contract address parameter
- ERC-721 transfers from an **address** filtered by a **token contract**, specify both address and contract address parameters.

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=tokennfttx&contractaddress=0x06012c8cf97bead5deae237070f9587f8e7a266d&address=0x6975be450864c02b4613023c2152ee0743572325&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

**Get a list of 'ERC1155 - Token Transfer Events' by Address**

Returns the list of ERC-1155 ( Multi Token Standard ) tokens transferred by an address, with optional filtering by token contract.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=token1155tx

&contractaddress=0x76be3b62873462d2142405439777e971754e8e77

&address=0x83f564d180b58ad9a02a449105568189ee7de8cb

&page=1

&offset=100

&startblock=0

&endblock=99999999

&sort=asc

&apikey=YourApiKeyToken

Usage:

- ERC-1155 transfers from an **address**, specify the address parameter
- ERC-1155 transfers from a **contract address**, specify the contract address parameter
- ERC-1155 transfers from an **address** filtered by a **token contract**, specify both address and contract address parameters.

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=token1155tx&contractaddress=0x76be3b62873462d2142405439777e971754e8e77&address=0x83f564d180b58ad9a02a449105568189ee7de8cb&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

**Get list of Blocks Validated by Address**

Returns the list of blocks validated by an address.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=getminedblocks

&address=0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b

&blocktype=blocks

&page=1

&offset=10

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=getminedblocks&address=0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b&blocktype=blocks&page=1&offset=10&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to check for balance

blocktype

the string pre-defined block type, either blocks for canonical blocks or uncles for uncle blocks only

page

the integer page number, if pagination is enabled

offset

the number of transactions displayed per page

**Contracts**

**Get Contract ABI for** [**Verified Contract Source Codes**](https://sonicscan.org/contractsVerified)

Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract.

Find verified contracts ✅on our [**Verified Contracts Source Code**](https://sonicscan.org/contractsVerified) page.

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=getabi

&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=contract&action=getabi&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the contract address that has a verified source code

**Get Contract Source Code for** [**Verified Contract Source Codes**](https://sonicscan.org/contractsVerified)

Returns the Solidity source code of a verified smart contract.

📩 **Tip :** You can also download a [**CSV list of verified contracts addresses**](https://sonicscan.org/exportData?type=open-source-contract-codes) of which the code publishers have provided a corresponding Open Source license for redistribution.

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=contract&action=getsourcecode&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=YourApiKeyToken) 🔗

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=getsourcecode

&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413

&apikey=YourApiKeyToken

RequestResponse

Query Parameters

Parameter

Description

address

the contract address that has a verified source code

**Get Contract Creator and Creation Tx Hash**

Returns a contract's deployer address and transaction hash it was created, up to 5 at a time.

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=getcontractcreation

&contractaddresses=0xB83c27805aAcA5C7082eB45C868d955Cf04C337F,0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45,0xe4462eb568E2DFbb5b0cA2D3DbB1A35C9Aa98aad,0xdAC17F958D2ee523a2206206994597C13D831ec7,0xf5b969064b91869fBF676ecAbcCd1c5563F591d0

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=contract&action=getcontractcreation&contractaddresses=0xB83c27805aAcA5C7082eB45C868d955Cf04C337F,0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45,0xe4462eb568E2DFbb5b0cA2D3DbB1A35C9Aa98aad,0xdAC17F958D2ee523a2206206994597C13D831ec7,0xf5b969064b91869fBF676ecAbcCd1c5563F591d0&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddresses

the contract address , up to 5 at a time

**Verify Solidity Source Code**

Submits a contract source code to an [**Sonicscan-like**](https://docs.sonicscan.org/contract-verification/supported-chains) explorer for verification.

🌐 **Tutorial :** A full walk through of submitting [**multichain contract verification**](https://docs.sonicscan.org/contract-verification/multichain-verification).

📝 **Note :** This endpoint is limited to **100 verifications/day**, regardless of API PRO tier.

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=verifysourcecode

&apikey=YourApiKeyToken

RequestResponse

Query Parameters

Requests must be sent using **HTTP POST**

Parameter

Description

chainId

the [**chain**](https://docs.sonicscan.org/contract-verification/supported-chains) to submit verification, such as 1 for mainnet

codeformat

single file, use solidity-single-file JSON file ( recommended ), use solidity-standard-json-input

sourceCode

the Solidity source code

constructorArguements

optional, include if your contract uses constructor arguments

contractaddress

the address your contract is deployed at

contractname

the name of your contract, such as contracts/Verified.sol:Verified

compilerversion

[**compiler version**](https://sonicscan.org/solcversions) used, such as v0.8.24+commit.e11b9ed9

**Verify Vyper Source Code**

Submits a Vyper contract source code to Sonicscan for verification.

📝 **Note :** This endpoint is limited to **100 verifications/day**, regardless of API PRO tier.

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=verifysourcecode

&apikey=YourApiKeyToken

RequestResponse

Query Parameters

Requests must be sent using **HTTP POST**

Parameter

Description

codeformat

use vyper-json

sourceCode

the Vyper source code, in [**JSON format**](https://docs.vyperlang.org/en/stable/compiling-a-contract.html#compiler-input-and-output-json-description)

constructorArguments

optional, include if your contract uses constructor arguments

contractaddress

the address your contract is deployed at

contractname

the name of your contract, such as contracts/Verified.vy:Verified

compilerversion

compiler version used, such as vyper:0.4.0

optimizationUsed

use 0 for no optimisation and 1 for optimisation used

**Check Source Code Verification Status**

Returns the success or error status of a contract verification request.

Copy

<https://api.sonicscan.org/api>

?module=contract

&action=checkverifystatus

&guid=x3ryqcqr1zdknhfhkimqmizlcqpxncqc6nrvp3pgrcpfsqedqi

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=contract&action=checkverifystatus&guid=x3ryqcqr1zdknhfhkimqmizlcqpxncqc6nrvp3pgrcpfsqedqi&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

guid

the unique guid received from the verification request

**Verify Proxy Contract**

Submits a proxy contract source code to Sonicscan for verification.

1. Requires a valid Sonicscan API key, it will be rejected otherwise
2. Current daily limit of 100 submissions per day per user (subject to change)
3. Only supports HTTP post
4. Upon successful submission you will receive a GUID (50 characters) as a receipt
5. You may use this GUID to track the status of your submission
6. Verified proxy contracts will display the "Read/Write as Proxy" of the implementation contract under the contract address's contract tab

**Verifying Proxy Contract using cURL**

RequestResponse

Copy

// example with only the mandatory contract address parameter

curl -d "address=0xcbdcd3815b5f975e1a2c944a9b2cd1c985a1cb7f" "<https://api.sonicscan.org/api?module=contract&action=verifyproxycontract&apikey=YourApiKeyToken>"

// example using the expectedimplementation optional parameter

// the expectedimplementation enforces a check to ensure the returned implementation contract address == address picked up by the verifier

curl -d "address=0xbc46363a7669f6e12353fa95bb067aead3675c29&expectedimplementation=0xe45a5176bc0f2c1198e2451c4e4501d4ed9b65a6" "<https://api.sonicscan.org/api?module=contract&action=verifyproxycontract&apikey=YourApiKeyToken>"

**Checking Proxy Contract Verification Submission Status using cURL**

RequestResponse

Copy

curl "<https://api.sonicscan.org/api?module=contract&action=checkproxyverification&guid=gwgrr>

**Transactions**

**Check Contract Execution Status**

Returns the status code of a contract execution.

Copy

<https://api.sonicscan.org/api>

?module=transaction

&action=getstatus

&txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=transaction&action=getstatus&txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the string representing the transaction hash to check the execution status

**Check Transaction Receipt Status**

Returns the status code of a transaction execution.

📝 **Note:** Only applicable for post [**Byzantium Fork**](https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/) transactions.

Copy

<https://api.sonicscan.org/api>

?module=transaction

&action=gettxreceiptstatus

&txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=transaction&action=gettxreceiptstatus&txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the string representing the transaction hash to check the execution status

**Blocks**

**Get Block And Uncle Rewards by BlockNo**

Returns the block reward and 'Uncle' block rewards.

Copy

<https://api.sonicscan.org/api>

?module=block

&action=getblockreward

&blockno=2165403

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=block&action=getblockreward&blockno=2165403&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the integer block number to check block rewards for eg. [12697906](https://sonicscan.org/block/12697906)

**Get Estimated Block Countdown Time by BlockNo**

Returns the estimated time remaining, in seconds, until a certain block is mined.

Copy

<https://api.sonicscan.org/api>

?module=block

&action=getblockcountdown

&blockno=16701588

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=block&action=getblockcountdown&blockno=16701588&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the integer block number to estimate time remaining to be mined eg. [12697906](https://sonicscan.org/block/12697906)

**Get Block Number by Timestamp**

Returns the block number that was mined at a certain timestamp.

Copy

<https://api.sonicscan.org/api>

?module=block

&action=getblocknobytime

&timestamp=1578638524

&closest=before

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=block&action=getblocknobytime&timestamp=1578638524&closest=before&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

timestamp

the integer representing the Unix timestamp in **seconds**.

closest

the closest available block to the provided timestamp, either before or after

⏳ **Tip :** Convert a regular date-time to a [**Unix timestamp.**](https://www.unixtimestamp.com/)

**Logs**

**Get Event Logs by Address**

Returns the event logs from an address, with optional filtering by block range.

Copy

<https://api.sonicscan.org/api>

?module=logs

&action=getLogs

&address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8

&fromBlock=12878196

&toBlock=12878196

&page=1

&offset=1000

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=logs&action=getLogs&address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8&fromBlock=12878196&toBlock=12878196&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to check for logs

fromBlock

the integer block number to start searching for logs eg. 12878196

toBlock

the integer block number to stop searching for logs eg. 12879196

page

the integer page number, if pagination is enabled

offset

the number of transactions displayed per page limited to **1000 records** per query, use the page parameter for subsequent records

**Get Event Logs by Topics**

Returns the events log in a block range, filtered by topics.

Copy

<https://api.sonicscan.org/api>

?module=logs

&action=getLogs

&fromBlock=12878196

&toBlock=12879196

&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef

&topic0_1_opr=and

&topic1=0x0000000000000000000000000000000000000000000000000000000000000000

&page=1

&offset=1000

&apikey=YourApiKeyToken

Usage:

- For a single topic, specify the topic number such as topic0, topic1, topic2, topic3
- For multiple topics, specify the topic numbers **and** topic operator either and or or such as below topic0_1_opr (and|or between topic0 & topic1), topic1_2_opr (and|or between topic1 & topic2) topic2_3_opr (and|or between topic2 & topic3), topic0_2_opr (and|or between topic0 & topic2) topic0_3_opr (and|or between topic0 & topic3), topic1_3_opr (and|or between topic1 & topic3)

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=logs&action=getLogs&fromBlock=12878196&toBlock=12879196&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&topic0_1_opr=and&topic1=0x0000000000000000000000000000000000000000000000000000000000000000&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

fromBlock

the integer block number to start searching for logs eg. 12878196

toBlock

the integer block number to stop searching for logs eg. 12879196

topic

the topic numbers to search for limited totopic0, topic1, topic2, topic3

topicOperator

the topic operator when multiple topic combinations are used limited to and or or

page

the integer page number, if pagination is enabled

offset

the number of transactions displayed per page limited to **1000 records** per query, use the page parameter for subsequent records

**Get Event Logs by Address filtered by Topics**

Returns the event logs from an address, filtered by topics and block range.

Copy

<https://api.sonicscan.org/api>

?module=logs

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

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=logs&action=getLogs&fromBlock=15073139&toBlock=15074139&address=0x59728544b08ab483533076417fbbb2fd0b17ce3a&topic0=0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d&topic0_1_opr=and&topic1=0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

fromBlock

the integer block number to start searching for logs eg. 12878196

toBlock

the integer block number to stop searching for logs eg. 12879196

address

the string representing the address to check for logs

topic

the topic numbers to search for limited totopic0, topic1, topic2, topic3

topicOperator

the topic operator when multiple topic combinations are used limited to and or or

page

the integer page number, if pagination is enabled

offset

the number of transactions displayed per page limited to **1000 records** per query, use the page parameter for subsequent records

**Geth/Parity Proxy**

For the full documentation of available parameters and descriptions, please visit the official [**Ethereum JSON-RPC**](https://eth.wiki/json-rpc/API) docs.

For compatibility with **Parity**, please prefix all hex strings with " **0x** ".

**eth_blockNumber**

Returns the number of most recent block

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_blockNumber

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

**eth_getBlockByNumber**

Returns information about a block by block number.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getBlockByNumber

&tag=0x10d4f

&boolean=true

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getBlockByNumber&tag=0x10d4f&boolean=true&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. 0xC36B3C

boolean

the boolean value to show full transaction objects.

when true, returns **full transaction objects** and their information, when false only returns a **list of transactions.**

**eth_getUncleByBlockNumberAndIndex**

Returns information about a uncle by block number.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getUncleByBlockNumberAndIndex

&tag=0xC63276

&index=0x0

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getUncleByBlockNumberAndIndex&tag=0xC63276&index=0x0&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. 0xC36B3C

index

the position of the uncle's index in the block, in hex eg. 0x5

**eth_getBlockTransactionCountByNumber**

Returns the number of transactions in a block.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getBlockTransactionCountByNumber

&tag=0x10FB78

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getBlockTransactionCountByNumber&tag=0x10FB78&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. 0x10FB78

**eth_getTransactionByHash**

Returns the information about a transaction requested by transaction hash.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getTransactionByHash

&txhash=0xbc78ab8a9e9a0bca7d0321a27b2c03addeae08ba81ea98b03cd3dd237eabed44

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getTransactionByHash&txhash=0xbc78ab8a9e9a0bca7d0321a27b2c03addeae08ba81ea98b03cd3dd237eabed44&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the string representing the hash of the transaction

**eth_getTransactionByBlockNumberAndIndex**

Returns information about a transaction by block number and transaction index position.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getTransactionByBlockNumberAndIndex

&tag=0xC6331D

&index=0x11A

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getTransactionByBlockNumberAndIndex&tag=0xC6331D&index=0x11A&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. 0x10FB78

index

the position of the uncle's index in the block, in hex eg. 0x0

**eth_getTransactionCount**

Returns the number of transactions performed by an address.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getTransactionCount

&address=0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getTransactionCount&address=0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to get transaction count

tag

the string pre-defined block parameter, either earliest, pending or latest

**eth_sendRawTransaction**

Submits a pre-signed transaction for broadcast to the Ethereum network.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_sendRawTransaction

&hex=0xf904808000831cfde080

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_sendRawTransaction&hex=0xf904808000831cfde080&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

hex

the string representing the signed raw transaction data to broadcast.

💡 **Tip:** Send a **POST** request if your hex string is particularly long.

🖋️ For more information on creating a **signed raw transaction**, visit this [**page.**](https://docs.sonicscan.org/tutorials/signing-raw-transactions)

**eth_getTransactionReceipt**

Returns the receipt of a transaction by transaction hash.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getTransactionReceipt

&txhash=0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getTransactionReceipt&txhash=0xadb8aec59e80db99811ac4a0235efa3e45da32928bcff557998552250fa672eb&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the string representing the hash of the transaction

**eth_call**

Executes a new message call immediately without creating a transaction on the block chain.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_call

&to=0xAEEF46DB4855E25702F8237E8f403FddcaF931C0

&data=0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_call&to=0xAEEF46DB4855E25702F8237E8f403FddcaF931C0&data=0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

to

the string representing the address to interact with

data

the hash of the method signature and encoded parameters

tag

the string pre-defined block parameter, either earliest, pending or latest

⛽ **Note:** The gas parameter is capped at **2x** the current block gas limit.

**eth_getCode**

Returns code at a given address.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getCode

&address=0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getCode&address=0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to get code

tag

the string pre-defined block parameter, either earliest, pending or latest

**eth_getStorageAt**

Returns the value from a storage position at a given address.

This endpoint is still **experimental** and may have potential issues

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_getStorageAt

&address=0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd

&position=0x0

&tag=latest

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_getStorageAt&address=0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd&position=0x0&tag=latest&apikey=YourApiKeyToken)

RequestResponse

Query Parameters

Parameter

Description

address

the string representing the address to get code

position

the hex code of the position in storage, eg 0x0

tag

the string pre-defined block parameter, either earliest, pending or latest

**eth_gasPrice**

Returns the current price per gas in wei.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_gasPrice

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

**eth_estimateGas**

Makes a call or transaction, which won't be added to the blockchain and returns the used gas.

Copy

<https://api.sonicscan.org/api>

?module=proxy

&action=eth_estimateGas

&data=0x4e71d92d

&to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843

&value=0xff22

&gasPrice=0x51da038cc

&gas=0x5f5e0ff

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=proxy&action=eth_estimateGas&data=0x4e71d92d&to=0xf0160428a8552ac9bb7e050d90eeade4ddd52843&value=0xff22&gasPrice=0x51da038cc&gas=0x5f5e0ff&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

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

post **EIP-1559**, the gasPrice has to be higher than the block's baseFeePerGas

⛽ **Note:** The gas parameter is capped at **2x** the current block gas limit.

**Tokens**

**Get ERC20-Token TotalSupply by ContractAddress**

Returns the current amount of an ERC-20 token in circulation.

Copy

<https://api.sonicscan.org/api>

?module=stats

&action=tokensupply

&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=stats&action=tokensupply&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the contract address of the ERC-20 token

**Get ERC20-Token Account Balance for TokenContractAddress**

Returns the current balance of an ERC-20 token of an address.

Copy

<https://api.sonicscan.org/api>

?module=account

&action=tokenbalance

&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055

&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761

&tag=latest&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=account&action=tokenbalance&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the contract address of the ERC-20 token

address

the string representing the address to check for token balance

**Stats**

**Get Total Supply of S**

Returns the current amount of S in circulation.

Copy

<https://api.sonicscan.org/api>

?module=stats

&action=ethsupply

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=stats&action=ethsupply&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

**Get S Last Price**

Returns the latest price of 1 S.

Copy

<https://api.sonicscan.org/api>

?module=stats

&action=ethprice

&apikey=YourApiKeyToken

Try this endpoint in your [**browser**](https://api.sonicscan.org/api?module=stats&action=ethprice&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

**Common Error Messages**

An API call that encounters an error ⚠️ will return 0 as its status code and display the cause of the error under the result field.

Copy

{

"status":"0",

"message":"NOTOK",

"result":"Max rate limit reached, please use API Key for higher rate limit"

}

**Invalid API Key**

"Invalid API Key"

This error occurs when you specify an invalid API Key, or use a key from an explorer on a [**different chain**](https://docs.sonicscan.org/support/faq#can-the-same-api-keys-be-used-across-different-explorers).

To resolve, ensure that you have copy pasted the right key from the right explorer.

New API Keys may also take a moment to be fully activated, so if your fresh key is throwing an error consider waiting for a few minutes.

**Max rate limit**

"Max rate limit reached, please use API Key for higher rate limit"

This error occurs when you **exceed the rate limit** assigned to your specific API key.

To resolve, adhere to the [**rate limits**](https://docs.sonicscan.org/support/rate-limits) of your available plan by waiting for a certain amount of time before each request. If you are using a script or application, **apply throttling** to limit the frequency of calls.

**Missing or invalid action**

"Error! Missing Or invalid Action name"

This error occurs when you **do not specify**, or specify an **invalid** module and action name.

To resolve, **double check** your API query to use a valid module and action name.

If you require some help getting started, try copying the sample queries provided in the [**API Endpoints**](https://github.com/BlockSolutions/etherscan-api-docs/blob/master/support/broken-reference/README.md) and pasting them into your browser.

**Endpoint-specific errors**

"Error! Block number already pass"

"Error! Invalid address format"

"Contract source code not verified"

These error messages returned are specific to certain endpoints and their **related parameters.**

To resolve, kindly refer to the specific endpoint's documentation, and check for the **correct format** or **values** to be specified as **parameters.**

**Query Timeout**

"Query Timeout occured. Please select a smaller result dataset"

"Unexpected err, timeout occurred or server too busy. Please try again later"

This error occurs when you have sent a particularly large query that did not manage to be completed in time.

To resolve, consider selecting a smaller date/block range, though you may [**ping us**](https://docs.sonicscan.org/support/getting-help) if you think the issue may be performance related.