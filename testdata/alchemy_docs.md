# Ethereum Basics


Ethereum Basics
Learn the basics of Ethereum including Proof-of-Stake, gas, accounts, nodes, transactions, frontend libraries, and how to access data with JSON-RPC.
Suggest Edits
Ethereum is a layer one blockchain that supports smart contracts. To become a web3 developer, understanding the basics of Ethereum's network and consensus mechanism is essential.
This section of Alchemy University covers:
What is Ethereum?
What is Proof-of-Stake?
How does Ethereum gas work?
What are Ethereum accounts?
How to Read Data with JSON-RPC
How to Create a JSON REST API for Ethereum
What are Ethereum nodes?
How do Ethereum transactions work?
Introduction to Ethereum Frontend Libraries
This series of content starts with a high level overview of Ethereum, and then explains Proof-of-Stake, which is Ethereum's consensus mechanism.
Next, the content will explain the concept of gas, which pays for the cost of completing transactions on the network. Then, we'll go in-depth on Ethereum "Accounts", which is the fancy term for wallets and smart contracts.
Lastly, we'll explain how to read data from Ethereum, creating a REST API to streamline the process, and show you all the great frontend libraries you can use to unlock the full power of Ethereum's vast and valuable data.
By the end of this section, you'll know how Ethereum works down to the bytecode level!
Learn More About Ethereum
This content series is from Alchemy University's free, 7-week Ethereum Developer Bootcamp. To learn more about Ethereum and earn an official certification, sign up for Alchemy University today!
Updated over 1 year ago
TABLE OF CONTENTS
Learn More About Ethereum
---

# How does Ethereum gas work?


How does Ethereum gas work?
Ethereum gas is the cost of executing operations. Demand determines the price, with a base fee to incentivize transactions. The fee is burned, and miners receive tips.
Suggest Edits
In the previous article, we talked about the cost of operation codes in terms of gas. In this article, we’ll take a look at the actual price of gas and understand what determines it.
EIP-1559
As many of you may know, the price of gas is something that changes with every block. Historically, gas prices on Ethereum have been unpredictable and at times, astronomically high making transactions inaccessible to most people.
However, In August 2021, after years of research and planning there was an EIP proposed to improve the calculation of gas prices on Ethereum, known as EIP-1559. Instead of covering the antiquated computation of gas prices from before EIP-1559, we’re just going to focus on how this works for the current state of Ethereum (post EIP-1559). If you want to learn more about the specific dynamics of EIP-1559 from a developer perspective, check out this resource hub.
Denomination Value in Ether Common Usage
Wei 10^-18 Technical implementations
Gwei (giga-wei) 10^-9 Human-readable gas fees
Gas Prices
The cost of operations on Ethereum is fixed and measured in the amount of “gas”, however, the price of that gas (measured in Gwei) is ever-changing. We are going to understand how these prices are set so that you can be more informed about transaction costs.
⛽
To view the latest gas prices you can check out Etherscan’s Ethereum Gas Tracker that gets updated in realtime.
With EIP-1559 the mechanism for setting the gas price has shifted from the previous model. We’ll be discussing the current way gas prices are determined since the legacy mechanism has been deprecated.
Denominations of Ether
Just like dollars, Ether has different denominations that are used to express smaller values, particularly when describing gas costs. For example, similar to how 1 dollar is equal to 100 pennies, 1 ether is equal to 10^18 Wei (the smallest denomination of Ether) or 10^9 Gwei. Here is a table with the relevant denominations for ether and their common use cases:
You’ll often see gas cost estimates listed in Gwei, however, if gas were to become much more or much less expensive we may see that denomination change to a different value.
✅
Gwei vs. Gas
Gwei is not the same value as “gas” that we discussed as fixed cost for operation codes in the Intro to Ethereum section.
How is the price of a gas set?
Every block has a maximum amount of gas that can be used within it. This is how the number of transactions included within a block is determined. Every block has the capacity to use 30 million gas but has a target of 15 million gas in total.
The price of gas is determined by the amount of demand for transactions (or block space), where demand is measured by how filled the previous block was relative to the target gas. So let’s look at an example here:
The above screenshot shows two different blocks, one where block space was in high demand, and another where it was in lower demand. The network first sets a base fee, in an ideal world, this base fee would result in 15 million gas getting used in a block, no more, no less. However, what happens in practice is the actual gas can be above or below the target gas.
When blocks are above the target, the gas price (or base fee) is automatically increased, increasing the cost and barrier to entry for sending transactions and thereby reducing the number of people who are competing to fill the block. When the block is below the target the base fee is lowered to incentivize people to transact by lowering the barrier to entry for paying for a transaction.
This base fee helps users select an efficient gas amount that is likely to get their transaction mined rather than wasting tons of money on unnecessarily high gas prices like we’ve seen in the past. These mechanisms also make it easy to predict future gas prices by looking at how “full” the previous blocks were.
We can actually see what this looks like in practice by visiting etherscan. Let’s take a look at block 16128921 for example:
we can see here that we are 57% below the desired gas target (only using 6.4 million gas instead of 15 million) and our base fee per gas is 12.044621651 Gwei. What do we think will happen with the next block? Will the base fee increase or decrease?
Here is a screenshot of block 16128922
We can see that the base fee decreased to 11.18 Gwei and by doing so this incentivized more people to send transactions and the gas used skyrocketed up to almost 30 million, 100% above the gas target! Now what do we think will happen with block 16128923? See for yourself!
What happens to the base fee?
Instead of going straight into the miners pocket, the base fee actually gets burned. There are several reasons why the base fee is burned instead of being given to the miner:
This prevents the miner from circumventing the payment of the base fee since they have to pay at least base fee of transactions for the block that the mine
Burning the Ether also creates deflationary pressure on Ether as an asset since supply is being taken out of the market
Setting the gas for your transaction
Turns out that when you are sending a transaction, you’re not actually setting the base fee value, but rather your setting the max fee which represents the maximum amount that you're willing to pay to get your transaction included. Luckily, unlike with the previous gas usage model, your transaction will only ever use the base fee** amount to execute, the rest of the value (max fee - base fee) will be returned to you.
As a dApp developer, you can actually create your own algorithm to determine how much gas to include in your transactions using endpoints like eth_feeHistory. If you’re interested in learning how to build this, check out How to Build a Gas Fee Estimator using EIP-1559.
How are miners paid?
Since the base fee is entirely burned, the new incentive for miners is now known as the miner tip. In a perfect world, the miner tip is the minimum amount that the miner is willing to accept in order to execute your transaction. This tip was originally set as 1gwei but can fluctuate depending on how full blocks are. Since the target gas value in blocks is 15M, in general, so long as blocks are hitting or near the target amount, there will always be room to add more transactions within a block. This is why the miner tip does not need to be insanely high to get your transaction included.
Typically when you set the gas for your transaction you’re setting a value called maxPriorityFee which is equal to the max fee + the miner tip . We’ll learn more about sending transactions later on this week!
Learn More About Ethereum Development
Alchemy University offers free web3 development bootcamps that explain Ethereum Gas in-depth and help developers master the fundamentals of web3 technology. Sign up for free, and start building today!
Updated over 1 year ago
TABLE OF CONTENTS
EIP-1559
Gas Prices
Denominations of Ether
How is the price of a gas set?
What happens to the base fee?
Setting the gas for your transaction
How are miners paid?
Learn More About Ethereum Development
| Denomination | Value in Ether | Common Usage |
| --- | --- | --- |
| Wei | 10^-18 | Technical implementations |
| Gwei (giga-wei) | 10^-9 | Human-readable gas fees |


---

# What are Ethereum Accounts?


What are Ethereum Accounts?
Ethereum has two types of accounts: externally owned accounts (EOAs) and contract accounts. EOAs are like Bitcoin key pairs, while contract accounts are for smart contracts.
Suggest Edits
EOAs vs. Contract Accounts
There are two types of accounts in Ethereum: externally owned accounts and contract accounts.
Externally Owned Accounts 🔑
Externally Owned Accounts (or EOAs for short!) are similar to Bitcoin private/public key pairs. In both models, the address and public key are associated to a private key via an Elliptic Curve Digital Signature.
However, the method to get from a private key to an address in Ethereum is different than Bitcoin. The resulting address in Ethereum is a 40-character hexadecimal string as opposed to a 26-35 alphanumeric string in Bitcoin.
📘
Another difference is that Bitcoin addresses end in a checksum to ensure the address is typed properly. Ethereum addresses don't have a checksum by default, although EIP-55 introduced a capitalization scheme that can be validated by wallet software.
The biggest difference between EOAs and Bitcoin Addresses is that EOAs have a balance. This means that the global state of the blockchain actively tracks how much ether every active address on the network holds.
🥸
Minor clarification here: an active address refers to an address that has interacted on the Ethereum blockchain. There are technically 16^40 (or 2^160 if you're thinking in binary!) possible Ethereum addresses which can be generated.
These addresses are not included in the global state tree until they have interacted with the blockchain. Otherwise, this would be a massive amount of data stored! Take a look at EIP-161 which was implemented when flaws in the Ethereum system allowed an attacker to create 19 million accounts at extremely low gas costs.
Accounts vs UTXOs
To transfer value in Bitcoin we spend UTXOs. In Ethereum, there are no UTXOs. Instead, at the end of a transaction transferring ether, the transferred amount is subtracted from the sender's address balance and added to the recipient's address balance in the global state tree.
Compared to UTXOs, an account balance is quite straightforward, especially from an application developer's perspective. The EVM has an operation BALANCE that allows us to look up an addresses balance inside code running on the EVM. This is much simpler than adding all unspent transaction outputs that have a particular address as their recipient.
Each Ethereum address also contains a nonce. The nonce keeps a count of all transactions sent from that particular address. To understand why this is necessary, let's consider an example. 👇
Let's say you have 2 ether in your account and you want to send 1 ether to Bob:
JavaScript
{
  to: BOBS_ADDRESS,
  value: 100000000000000000 // 1 ether
}
You'll be able to broadcast this transaction to the network once you sign it with your private key. 🔑 🌐
At that point, with the current parameters specified, what's stopping Bob from re-transmitting this same transaction again to the network? 🤔
NOTHING 😱
To combat this, Ethereum tracks the number of transactions sent by an account, called the account nonce. Each time a transaction is sent, the nonce is incremented:
JavaScript
{
  to: BOBS_ADDRESS,
  value: 100000000000000000, // 1 ether
  nonce: 0x0 // this is the first transaction, nonce is zero!
}
If Bob tried to re-broadcast the transaction now, the network would reject it. Once the first transaction is successfully mined the miners enforce the rule that the nonce of your next transaction should be 0x1.
💭
You may be thinking: "What if Bob tried to increment the nonce himself?" But, of course, Bob would need you to sign the transaction after he incremented the nonce. The result of a digital signature does not leave room for the underlying data to be tampered with.
The word "nonce" simply means it's a number we're using once for its particular purpose. It's a rather ambiguous term. Accounts in Ethereum have a nonce that keeps a count of transactions to be used once per transaction. Blocks in Proof of Work have a nonce that allows it to randomly search for a valid hash to be used once in the search for that block hash.
To summarize, the difference between Ethereum EOAs and Bitcoin addresses is that active EOAs are stored with a balance and a nonce. Whereas in Bitcoin the client only keeps track of UTXOs which contain an owner address.
📘
For more reasons why Ethereum chose accounts instead of UTXOs, it's best to refer to the Design Rationale document in the Ethereum wiki.
Contract Accounts
Finally, we broach the most exciting part of Ethereum: Smart Contracts! 💃🏻
The term Smart Contract sounds pretty intimidating at first glance. Don't worry about the name, it's simply a program that runs in the blockchain execution environment.
As a developer, you would write a Smart Contract when you want to decentralize a program's execution. Smart Contracts are generally written in a high-level language like Solidity or Vyper. Once you've completed the code (and tested it thoroughly!) you can deploy the contract to the Ethereum blockchain. You can do so by running a transaction from your Externally Owned Account with the bytecode of the compiled smart contract.
This contract has its own account in that it also has a balance and address. The contract account cannot be controlled by a private key like a EOA. Instead, EOAs make transactions to call functions on the contract. From there, contracts can also make calls to other contracts synchronously. Once a contract is deployed, the code cannot be changed. However, the storage (persistent memory) of a contract can be updated through transactions.
📘
A contract can store an address of another contract that it needs to interact with. Since the address is held in storage it can be updated through transactions. Therefore it's possible to upgrade a system by deploying new contracts and running a transaction to update references to point to the new addresses. This can be a bit of a challenging subject and is generally referred to as smart contract upgradeability.
🏁 Wrap Up
In this article we discussed both types of accounts on Ethereum: Externally Owned Accounts and Contract Accounts. We talked about some of the differences between an account-based model and a UTXO model.
We also briefly touched on Smart Contracts from a high-level perspective, we'll dive into these concepts further when we start programming our own smart contracts!
Learn More About Ethereum Accounts
Alchemy University offers free web3 development bootcamps that explain Ethereum in-depth and help developers master the fundamentals of web3 technology. Sign up for free, and start building today!
Updated over 1 year ago
TABLE OF CONTENTS
EOAs vs. Contract Accounts
Externally Owned Accounts 🔑
Accounts vs UTXOs
Contract Accounts
🏁 Wrap Up
Learn More About Ethereum Accounts
```
{
  to: BOBS_ADDRESS,
  value: 100000000000000000 // 1 ether
}
```


```
{
  to: BOBS_ADDRESS,
  value: 100000000000000000, // 1 ether
  nonce: 0x0 // this is the first transaction, nonce is zero!
}
```


---

# What are Ethereum nodes?


What are Ethereum nodes?
Ethereum nodes uphold network integrity and data. Full nodes store and validate all blocks and transactions locally. Ethereum uses Merkle Patricia Tries for data storage.
Suggest Edits
Ethereum nodes are what maintain the integrity and data on the network. There are several different types of Ethereum nodes that are participating in the network and are used depending on what type of data is needed.
Full nodes store and validate all blocks and transactions over the entire blockchain locally. When a smart contract transaction is executed, Ethereum full nodes execute all of the instructions in the smart contract. Together, full nodes determine whether the smart contract execution is producing the desired result. However, running full Ethereum nodes is expensive to and can consume a great deal of energy.
Luckily, Alchemy provides access to all archive data (from block 0) and the latest data (from the most recent and pending blocks) completely for free.
Understanding Ethereum Nodes
In the below video we will break down how nodes work, why they can be extremely challenging for applications at scale, and how to solve data consistency issues.
Bonus Material: Data Storage
We've talked about Ethereum Nodes storing information locally, although we haven't really talked about how they store the data locally. Let's take a closer look. 🔬
Ethereum stores data in Merkle Patricia Tries. . We already know this from week 2 content on tries :)
📘
The term "trie" seems to have originated from the term "retrieval". It is used quite interchangeably with the word "tree" and is often pronounced the same way.
Merkle Patricia Tries retain the properties of the Merkle Tree. The root hash of the trie represents the entirety of its contents (if any data changes, the root is completely different). Also, data can be proven to be part of a Merkle Patricia Trie without providing all of the data.
In addition to the Merkle Tree properties, the Merkle Patricia Trie has some major performance benefits for storing large amounts of data. You can find the full specification of the Patricia Tree here as well as the design rationale here.
There are four types of tries used to store data in Ethereum:
State Trie - This is the global state of the Ethereum network. There is only one state trie and it is constantly being updated by transactions when they are mined into the blockchain.
Storage Trie - Each account has its own storage trie. This keeps track of all persistent variables within a contract account, also known as its storage.
Transactions Trie - There is one transaction trie per block and it contains all of the transactions in a specific order determined by the miner.
Receipts Trie - For each transaction, a receipt is stored that contains logs, gas used, and post-transaction state. This receipts trie stores all of that data.
That's quite a lot of trees! 😋
👆🏼 Don't worry about memorizing this information; you will likely never need to interface with these tries directly. Either you'll invoke an opcode on the EVM when you write a Smart Contract or you'll use the JSON-RPC API (often with the assistance of a library) to interact with an Ethereum Node on a much higher level.
🏁 Wrap Up
We discussed the potential issues you might run into with Ethereum nodes and how data is stored on full nodes, which is admittedly pretty intense! 😅
Much of the Ethereum system is designed around incentives on how these nodes are able to store and validate transactions, so this is an important thing to keep in mind! 🧠
In upcoming lessons we'll be moving more high-level. We'll start to interact with these nodes using our Alchemy endpoint and learn to use libraries to make our lives easier as developers.
Learn More About Ethereum Development
Alchemy University offers free web3 development bootcamps that explain Ethereum Nodes in-depth and help developers master the fundamentals of web3 technology. Sign up for free, and start building today!
Updated over 1 year ago
TABLE OF CONTENTS
Understanding Ethereum Nodes
Bonus Material: Data Storage
🏁 Wrap Up
Learn More About Ethereum Development
---

# Introduction to Ethereum Frontend Libraries


Introduction to Ethereum Frontend Libraries
Ethers.js and web3.js are popular Ethereum Javascript libraries for JSON-RPC protocol interaction. Ethers.js is lightweight, well-tested, and ideal for new projects.
Suggest Edits
Previous Section Recap


Virtually every web3 website, or dapp that you have ever used uses one of web3.js or ethers.js. Together, they are the two most popular Ethereum Javascript libraries that allow developers to interact with Ethereum or EVM-compatible blockchains using the JSON-RPC (Javascript Object Notation- Remote Procedure Call) protocol.
In other words, these are JavaScript libraries that allow you to do things that fundamental to almost every dapp: deploy smart contracts, create wallets, sign transactions, query the blockchain, etc. without having to make raw API calls to the blockchain.
One of the most common questions developers ask when starting out with web3 development is which library to use in their projects. In this guide, we will cover what ethers.js and web3.js libraries are, what they can do, and how they differ so you're able to make a choice depending on the requirements of your project.
📘
If you're using Ethers.js but you also want access to certain Alchemy-specific features such as our NFT API, Enhanced WebSockets, Transact features, or Token API, read on!
We built a strict superset of Ethers.js that makes it simple to integrate your Ethers.js code into Alchemy's custom endpoints, called the Alchemy SDK. You'll get the same syntax and features as Ethers while gaining access to Alchemy's best-in-class infrastructure and Enhanced APIs.
Alchemy SDK Quickstart
Advantages of ethers.js
Ethers can do everything that web3.js can when it comes to interacting with the blockchain. In addition to that, it has a few more perks:
A Broader License
Ethers is available under the MIT License which not only allows developers to use it for free, but also allows modifications to it.
The latter is also allowed under the LGPL-3.0 license that web3 uses but it also forces you to release the source code containing the modifications.
Smaller Size
Ethers is an extremely lightweight library. It's only 77 KB compressed and 284 KB uncompressed.
ENS Compatible
Ethers knows how to parse ENS domain names by default. Therefore, you can replace a hexadecimal address with a .eth domain without any extra boilerplate code.
A Large Number of Test Cases
Ethers is extraordinarily well-tested, with close to 10,000 test cases; a significant chunk being written by Richard Moore himself. Ethers was a pioneer with respect to maintaining a well-tested Ethereum library (web3 has since managed to catch up to an extent).
Drawbacks of ethers.js
Ethers is a relatively new library. Hence, it is hard to find it in use in older, more foundational projects and companies. If you work or are planning to work in such a company, it may be worthwhile to spend more time learning web3.
When to Use ethers.js
Ethers is a fantastic library to use if you're building a new project. At the time of writing, the popularity (in terms of weekly downloads, beginner tutorials, and community support) has either surpassed or quickly catching up to that of web3.
Given the small size of the library, it is especially lucrative on the frontend as it can improve the performance of your website/app significantly.
Important ethers.js Class Abstractions
These are the core class abstractions that you will need to use to write scripts that interact with the Ethereum computer. These are also the base abstractions that the Alchemy SDK uses 1-to-1.
Provider: Represents any connection to an Ethereum node
Wallet: EOA (private key holder) with ability to sign and send messages to network
Contract: Represents a smart contract executable deployed on the network
Conclusion
Front-end libraries like ethers.js and software development kits like the Alchemy SDK make our life as developers extremely easy. Can you imagine what a pain it would be to be coding out all of our scripts in raw JSON-RPC?
So, web3 developers use front-end libraries that work to abstract the lower level away from them so that they can focus on streamlined development. This is the flow typical of web3 dApps:
Your dApp uses some front-end library that uses JSON-RPC under the hood to communicate with an Ethereum node (which is essentially, communicating with the entire Ethereum network).
Learn More About Ethereum Libraries
Alchemy University offers free web3 development bootcamps that explain Ethereum in-depth and help developers master the fundamentals of web3 technology. Sign up for free, and start building today!
Updated over 1 year ago
TABLE OF CONTENTS
Advantages of ethers.js
Drawbacks of ethers.js
When to Use ethers.js
Important ethers.js Class Abstractions
Conclusion
Learn More About Ethereum Libraries
---

# Ethereum Transactions - Pending, Mined, Dropped & Replaced


Ethereum Transactions - Pending, Mined, Dropped & Replaced
Explanation for different transaction states on Ethereum and other blockchains and how to handle each state to ensure your transaction gets mined in time.
Suggest Edits
TL;DR: Alchemy just released support for “Dropped & Replaced” transactions in the Mempool Watcher, a browser-based user interface that allows web3 developers to browse, filter, and track transactions that were sent to the blockchain and help you debug pending transactions. With “Dropped & Replaced” transactions, a new blockchain developer tool, it will be dramatically easier to understand when transactions fail, when they are replaced, and the current state of the mempool.
What is a Mempool?
A mempool, or memory pool, is a collection of pending transactions waiting for validation from a node before they are committed to a new block on the blockchain. Put simply, the mempool is a staging area for unconfirmed transactions in a node. Every blockchain node in the network has a mempool, and they all intercommunicate to share information about the latest pending transactions.
Mempools exist because only ~200 transactions can be confirmed per block, which are mined about once every 15 seconds.
As a result, pending transactions are broadcasted throughout the entire network of mempools with an associated gas price (i.e. the gas fees that the sender is willing to pay to complete their transaction). When a block is mined, the ~200 pending transactions with the highest gas prices are confirmed onto the blockchain by the node that mines the latest block.
If transactions fail to pass a series of validation checks or are submitted with too little gas, those transactions will eventually be dropped from the mempool.
What is a nonce?
A nonce is a 0-indexed number corresponding to the number of confirmed transactions sent by a particular address. That is, if an address has 0 confirmed transactions, it marks its first transaction with a nonce of 0, and the subsequent transaction it would like to send with a nonce of 1.
Every confirmed transaction by a particular sender address must have a unique nonce value. For example, if a sender submits two transactions with a nonce value of 1, only one can succeed.
Why do you need to set your nonce?
Nonces exist to protect against replay attacks.
For example, a transaction sending 20 coins from A to B can be replayed by B over and over to continually drain A’s balance if it didn’t have a nonce. Because transactions are submitted as hashed values, B could simply copy the hashed transaction published to the blockchain and re-run it over and over again.
However, if you set a unique nonce before creating the hashed transaction, it will prevent a replay attack, since every confirmed transaction must have a unique nonce value and subsequent identical transactions will fail.
It’s important for senders to set their nonce values correctly to ensure transactions have the opportunity to be confirmed because transactions that are submitted with an out-of-order or duplicate nonce value will be dropped from the mempool.
Nonces are also useful to guarantee ordering of transactions. For example, if a sender can submit 5 transactions with nonces from 0 - 4, they can expect that the transactions will be executed strictly in the order of their nonces.
What transaction lifecycle states can a mempool transaction be in?
Traditionally, mempool transactions fall into one of the following three buckets:
Pending Transactions
Transactions that have been submitted to the mempool and are waiting to be included in the next block mined by a miner. Learn more about debugging pending transactions..
Mined Transactions
Transactions that have been selected and are included in the latest block by a miner. The results of these transactions are then broadcasted to the entire network. Mined transactions can have two statuses:
Success
These transactions are successfully executed and modify state on-chain. The status field for a successful transaction is 0x1.
Failure/Execution Reverted
These transactions are not successfully executed but are still included in the block. This can occur if the execution process hits an error, runs out of gas, or encounters some other issue. The status field for a failed transaction is 0x0.
To check whether a mined transaction was successful or failed you can call eth_getTransactionReceipt passing in your transaction hash. In the payload, you will find a status field which will be 0x0 for failed and 0x1 for success.
Dropped Transactions
Transactions that have failed to be confirmed. This could happen because the transaction failed certain validation tests, the nonce was incorrect, the submitted gas price was too low and it timed out, or a number of other errors. Dropped transactions return their assets and gas fees to the sender, as if the transaction never happened.
Need help troubleshooting dropped transactions? Watch our tutorial on how to fix pending or stuck transactions with Alchemy’s Mempool Watcher.
What are Dropped & Replaced transactions?
A new category has become a common feature request by developers. When a transaction is dropped, the sender will oftentimes send a replacement transaction with the same nonce value to “replace” that failed transaction.
If the second transaction is confirmed onto the blockchain (e.g. by sending a new transaction with the same nonce and a higher gas price), the “dropped” transaction will be moved into the new transaction status category known as “Dropped & Replaced”.
Similarly, if multiple transactions are simultaneously sent with the same nonce value, typically the transaction with a higher transaction fee will be selected for confirmation onto a block. The other transactions will fall into the “Dropped & Replaced” category.
This transaction status is useful for smart contract developers as it allows them to track which transactions have been successfully re-broadcasted to the blockchain network (“dropped and replaced”) and which dropped transactions still need to be re-broadcasted (“dropped”).
How to track Dropped & Replaced transactions
If you submit your transactions via Alchemy, we provide a convenient web3 developer tool to rapidly filter and explore transactions you’ve recently submitted: the Mempool Watcher.
Before the Mempool Watcher tool was released, developers would have to track transactions via Etherscan (which was often unreliable), or by manually querying their nodes to retrieve the current state of the mempool and parse the response for the relevant transaction status details.


Using the Mempool Watcher, web3 developers using Alchemy can now see all their transactions in a single UI, and filter them by mined, pending, dropped, and dropped & replaced transactions. Builders can also search transactions by these filters:
Date of submission
Sender address
Associated transaction hash
Web3 developers can also use the Alchemy Notify API (webhook alerts for transaction activity) to:
Create notifications for dropped and mined transactions
Send transaction status notifications with Zapier
Integrate transaction notifications with a dApp
How do I start using the Mempool Watcher?
Sign up for a free Alchemy account today to access the Mempool Watcher, start tracking your dropped & replaced transactions, and access a host of other powerful blockchain developer tools! At our current pricing, you’ll be able to send 1.2 million transactions to the mempool each month on our free tier - the most generous in the web3 ecosystem.
Updated almost 2 years ago
TABLE OF CONTENTS
What is a Mempool?
What is a nonce?
Why do you need to set your nonce?
What transaction lifecycle states can a mempool transaction be in?
Pending Transactions
Mined Transactions
Dropped Transactions
What are Dropped & Replaced transactions?
How to track Dropped & Replaced transactions
How do I start using the Mempool Watcher?
---

# eth_getUserOperationReceipt


eth_getUserOperationReceipt
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get the UserOperationReceipt based on the userOpHash value.
📘
Supported EntryPoints
eth_getUserOperationReceipt supports both v0.6 and v0.7 userOps. The format of the returned userOp depends on the version found with the requested hash. Check our FAQs to learn the differences between v0.6 and v0.7.
🚧
Want to get push notifications for mined userOps?
Follow this guide to learn how to use Custom Webhooks and get real time alerts and receipts for mined userOperations.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_supportedEntryPoints


eth_supportedEntryPoints
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of the entryPoint addresses supported by the client.
📘
Supported Entry Points
Please note that the eth_supportedEntryPoints method returns an array of supported EntryPoints. Currently, we support EntryPoint v0.7. at 0x0000000071727De22E5E9d8BAf0edAc6f37da032 and v0.6.0 at0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789. Check our FAQs to determine which version you should use.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUserOperationByHash


eth_getUserOperationByHash
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Return a UserOperation based on a hash (userOpHash).
📘
Supported EntryPoints
eth_getUserOperationByHash supports both v0.6 and v0.7 userOps. The format of the returned userOp depends on the version found with the requested hash. Check our FAQs to learn the differences between v0.6 and v0.7.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendUserOperation


eth_sendUserOperation
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Sends a user operation to the given EVM network.
📘
Supported EntryPoints
eth_sendUserOperation supports versions v0.6 and v0.7 of ERC-4337. Check our FAQs to determine which version you should use.
🚧
Replacement Underpriced Error
You might get a "Replacement Underpriced Error" when using eth_sendUserOperation. View our FAQs for a description of this error along with resolution steps.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateUserOperationGas


eth_estimateUserOperationGas
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Estimates the gas values for a UserOperation.
📘
Supported EntryPoints
eth_sendUserOperation supports versions v0.6 and v0.7 of ERC-4337. Check our FAQs to determine which version you should use.
🚧
Dummy Signature
This endpoint requires a dummy signature in the userOp. Check our FAQs to learn what a dummy signature is and which dummy signature you should use.
Parameters
UserOperation (Object): Contains gas limits and prices (optional). This can be either a v0.6 or v0.7 user operation but must match the version of the EntryPoint at the address of the second parameter.
entryPoint (String): The address to which the request should be sent. This must be one of the EntryPoint returned by the supportedEntryPoints method and should match the version of the userOp in the first parameter.
stateOverrideSet (Object): Allows changes to the state of a contract before executing the call. For example, you can modify variable values (like balances or approvals) for that call without changing the contract itself on the blockchain.
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity (Hex string) ≤32 Fake balance to set for the account before executing the call.
nonce Quantity (Hex string) ≤8 Fake nonce to set for the account before executing the call.
code Binary (Hex string) any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity (Hex string) | ≤32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity (Hex string) | ≤8 | Fake nonce to set for the account before executing the call. |
| code | Binary (Hex string) | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_cancelPrivateTransaction


eth_cancelPrivateTransaction
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Request to cancel private transactions on Ethereum that are sent via eth_sendPrivateTransaction.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendPrivateTransaction


eth_sendPrivateTransaction
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Send a single private transaction through Flashbots. Private transactions are sent directly to miners and not included in the public mempool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# Ethereum API Quickstart


Ethereum API Quickstart
How to get started building on Ethereum and using the JSON-RPC API
To use the Ethereum API you'll need to create a free Alchemy account first!

What is the Ethereum API?
The Ethereum API allows applications to connect to an Ethereum node that is part of the Ethereum blockchain. Developers can interact with on-chain data and send different types of transactions to the network by utilizing the endpoints provided by the API. The API follows a JSON-RPC standard. JSON-RPC is a stateless, lightweight, remote procedure call (RPC) protocol that is commonly used when interacting with Ethereum.
Getting Started Instructions
1. Choose a Package Manager (npm or yarn)
For this guide, we will be using npm or yarn as our package manager to install necessary packages.
npm
To get started with npm, follow the documentation to install Node.js and npm for your operating system: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
yarn
To get started with yarn, follow these steps: https://classic.yarnpkg.com/lang/en/docs/install
2. Set Up Your Project
To kickstart your project, open your terminal and execute the following commands:
npm
yarn
mkdir ethereum-api-quickstart
cd ethereum-api-quickstart
npm init --yes
3. Install Axios
For making API requests, we'll use Axios, a widely-used HTTP client. Install Axios with the following command:
npm
yarn
npm install axios
4. Make Your First Request
You are all set now to use Ethereum API and make your first request. For instance, let's make a request to get the latest block. Create an index.js file in your project directory and paste the following code snippet into the file.
index.js
import axios from "axios";

const url = `https://eth-mainnet.g.alchemy.com/v2/${yourAlchemyAPIKey}`;

const payload = {
  jsonrpc: '2.0',
  id: 1,
  method: 'eth_blockNumber',
  params: []
};

axios.post(url, payload)
  .then(response => {
    console.log('The latest block number is', parseInt(response.data.result, 16));
  })
  .catch(error => {
    console.error(error);
  });
Remember to replace yourAlchemyAPIKey with your actual Alchemy API key that you can get from your Alchemy dashboard.
You can also make these requests on testnets like eth-sepolia or eth-holesky by just replacing the request URL:
Text
# Mainnet
https://eth-mainnet.g.alchemy.com/v2/
# Sepolia Testnet
https://eth-sepolia.g.alchemy.com/v2/
# Holesky Testnet
https://eth-holesky.g.alchemy.com/v2/
5. Run Your Script
To execute your script and make a request to the Ethereum network, run:
Shell
node index.js
You should see the latest block number outputted to your console.
Shell
The latest block number is 11043912

You must not stop here! Want to build your first Dapp and use Ethereum APIs?
Head towards Alchemy Tutorials.
View: https://docs.alchemy.com/docs
Updated 8 months ago
getNftsForContract - SDK
Ethereum API FAQ
Did this page help you?
Yes
No
TABLE OF CONTENTS
What is the Ethereum API?
Getting Started Instructions
1. Choose a Package Manager (npm or yarn)
2. Set Up Your Project
3. Install Axios
4. Make Your First Request
5. Run Your Script
```
mkdir ethereum-api-quickstart
cd ethereum-api-quickstart
npm init --yes
```


```
npm install axios
```


```
import axios from "axios";

const url = `https://eth-mainnet.g.alchemy.com/v2/${yourAlchemyAPIKey}`;

const payload = {
  jsonrpc: '2.0',
  id: 1,
  method: 'eth_blockNumber',
  params: []
};

axios.post(url, payload)
  .then(response => {
    console.log('The latest block number is', parseInt(response.data.result, 16));
  })
  .catch(error => {
    console.error(error);
  });
```


```
# Mainnet
https://eth-mainnet.g.alchemy.com/v2/
# Sepolia Testnet
https://eth-sepolia.g.alchemy.com/v2/
# Holesky Testnet
https://eth-holesky.g.alchemy.com/v2/
```


```
node index.js
```


```
The latest block number is 11043912
```


---

# Ethereum API FAQ


Ethereum API FAQ
Frequently Asked Questions about the Ethereum API
What testnet should developers use for Ethereum development?
All developers getting started on Alchemy should use Sepolia as their testnet of choice for development!
The Ethereum Foundation winded down support for the Rinkeby, Ropsten, and Kovan networks after Ethereum's transition to a proof-of-stake model and the Goerli testnet is also deprecated. To ensure that your testnet applications remain fully functional after the transition, we recommend using Sepolia, which will remain unchanged. Learn more at Choosing a Web3 Network.
What API does Ethereum use?
Ethereum uses the JSON-RPC API standard. The Ethereum JSON-RPC API serves as the backbone for the Ethereum network and powers any blockchain interaction. In aggregate, this API suite allows users to read block/transaction data, query chain information, execute smart contracts, store data on-chain, etc. Developers and consumers alike interact with Ethereum’s base JSON-RPC APIs to communicate with its decentralized network of nodes.
What is an Ethereum API Key?
When accessing the Ethereum network via a node provider, API services like Alchemy require an API key, which allows developers to monitor personal apps and access usage metrics.
While many Ethereum development environments have a set of default shared API keys, they are often throttled during periods of high usage leading to slower response times and a higher likelihood of request failures.
For the best development experience, we recommend that you sign up for a free API key!
With a dedicated API key, developers are able to:
access higher request throughput and increased concurrent requests.
query Enhanced APIs, gaining access to free archive data, logs, and higher-level API abstractions.
leverage individualized usage metrics.
Does Ethereum only use JSON-RPC?
The raw Ethereum client only uses JSON-RPC notation to encode remote procedure calls for interpreting requests and serving up responses. However, most developers use libraries that actually abstract away the JSON-RPC standard. Libraries like AlchemyWeb3.js wrap the base Ethereum JSON-RPC API to create more intuitive methods that make debugging and developing easier. Likewise, developers can find a host of different web3 libraries wrapper libraries spanning different programming languages like Javascript, Python, Golang, etc. which use JSON-RPC under the hood.
How does Alchemy's Ethereum API work?
Alchemy's Ethereum API gives developers and users access to read and write data to the Ethereum blockchain.
If you’re not familiar with how a blockchain works, here’s a quick recap:
The Ethereum blockchain is made up of blocks of data.
Blocks are stored on distributed Ethereum nodes.
Each node in the network serves as a “mini-server” that allows its operator to read/write blocks of data.
Alchemy provides access to our higher-level infrastructure that allows developers to interface with the Ethereum network. With API access, Alchemy developers are able to send read/write requests to the blockchain.
We take care of the hard stuff so that developers can focus on their products!
Can you use Python for Ethereum?
Yes! While Javascript libraries have historically gained traction in the Ethereum development community, Python developers are also able to read and write the same data. One commonly used blockchain interaction library is web3.py which wraps many of the same methods featured in web3.js and Ethers.js.
For Python-based EVM development, Brownie offers a full suite of Web3 developer tools for compiling, testing, and deploying dApps similar to its peer environments Hardhat and Truffle.
How do I get the timestamp for a transaction?
There are three steps to get the timestamp for a transaction:
Grab the blockNumber field in your transaction object
If you only have the transaction hash, you can get the full object by making a request to eth_getTransactionByHash.
Get the block info by calling [ref:eth-getblockbynumber)
Grab the timestamp field in the returned block object
Here is an example request.
It's important to note that block numbers themselves are Ethereum's measure of time, however standard timestamps are available by looking at the block data.
How do I distinguish between a contract address and a wallet address?
A super easy way to distinguish between a contract address and a wallet address is by calling eth_getCode, which will return contract code if it's a contract and nothing if it's a wallet. Here's an example of both using our composer tool:
0x Contract Address
Vitalik's Wallet Address
What is the difference between DATA and QUANTITY?
The difference between the types “DATA” and “QUANTITY” is that “DATA” always comes specified with a required length (ex: 20 Bytes), so you'll need to make sure the string you pass in is the right length. In contrast, QUANTITY does not have length requirements.
For example given a parameter type: “DATA, 20 Bytes”, a valid input would be:
"0x0000000000000000000000000000000000000003"
note: every two hex characters make one byte, so that string is 0x followed by forty hex characters
However, if this were a QUANTITY, a valid input would be:
"0x3"
What is the Default Block Parameter?
The default block parameter is used to specify the block height in your request. It is an additional parameter on all of the following methods:
eth_getBalance
eth_getCode
eth_getTransactionCount
eth_getStorageAt
eth_call
The following options are possible for the defaultBlock parameter:
HEX String - an integer block number
String earliest for the earliest/genesis block
String latest - for the latest mined block
String pending - for the pending state/transactions
What methods does Alchemy support for the Ethereum API?
You can find the list of all the methods Alchemy support for the Ethereum API on the Ethereum API Endpoints Overview.
My question isn't here, where can I get help?
Don't worry, we got you. Check out our feel free to post in discord with any questions you have!
TABLE OF CONTENTS
What testnet should developers use for Ethereum development?
What API does Ethereum use?
What is an Ethereum API Key?
Does Ethereum only use JSON-RPC?
How does Alchemy's Ethereum API work?
Can you use Python for Ethereum?
How do I get the timestamp for a transaction?
How do I distinguish between a contract address and a wallet address?
What is the difference between DATA and QUANTITY?
What is the Default Block Parameter?
What methods does Alchemy support for the Ethereum API?
My question isn't here, where can I get help?
```
"0x0000000000000000000000000000000000000003"
```


```
"0x3"
```


---

# Ethereum API Endpoints


Ethereum API Endpoints
List of all Ethereum API endpoints
Ethereum API Endpoints by use case
Getting Blocks
Reading Transactions
Writing Transactions & EVM Execution
Account Information
Event Logs
Chain Information
Getting Uncles
Gas Estimation
Web3
Real-time Events
Available Enhanced APIs
NFT API
Transfers API
Transaction Receipts API
Token API
Notify API
Trace API
Subscription API
Getting Blocks
Retrieves information from a particular block in the blockchain.
eth_getBlockByHash
eth_blocknumber
eth_getBlockByNumber
eth_getBlockReceipts
eth_getBlockTransactionCountByHash
eth_getBlockTransactionCountByNumber
Reading Transactions
Retrieves information on the state data for addresses regardless of whether it is a user or a smart contract.
eth_getTransactionByHash
eth_getTransactionByBlockHashAndIndex
eth_getTransactionByBlockNumberAndIndex
eth_getTransactionReceipt
eth_getTransactionCount
Writing Transactions & EVM Execution
Allows developers to send ETH from one address to another, write data on-chain, and interact with smart contracts.
eth_sendRawTransaction
eth_call
Account Information
Returns information regarding an address's stored on-chain data.
eth_getCode
eth_getBalance
eth_accounts
eth_getStorageAt
eth_getProof
Event Logs
Returns logs which are records that denote/provide context on specific events within a smart contract, like a token transfer or a change of ownership, for example.
eth_getLogs
eth_newFilter
eth_newPendingTransactionFilter
eth_newBlockFilter
eth_getFilterChanges
eth_getFilterLogs
eth_uninstallFilter
Chain Information
Returns information on the Ethereum network and internal settings.
eth_chainId
eth_protocolVersion
net_listening
net_version
Getting Uncles
Returns information on uncle blocks which are network rejected blocks and replaced by a canonical block instead.
eth_getUncleCountByBlockHash
eth_getUncleByBlockNumberAndIndex
eth_getUncleByBlockHashAndIndex
eth_getUncleCountByBlockNumber
Gas Estimation
Returns information on the Ethereum network gas estimates.
eth_estimateGas
eth_gasPrice
eth_feeHistory
eth_maxPriorityFeePerGas
eth_createAccessList
Web3
Returns Ethereum network configuration information.
web3_clientVersion
web3_sha3
Real-time Events
Introduces WebSocket-based requests/responses which leverage a network connection allowing developers to listen for changes continuously without the need for HTTP polling.
eth_subscribe
eth_unsubscribe
Available Enhanced APIs
NFT API
All Networks Mainnet Only
getNfts, getNFTMetadata, getContractsForOwner, getOwnersForToken, getOwnersForCollection, isHolderOfCollection, getContractMetadata, getNFTsForCollection
getNFTMetadataBatch [searchContractMetadata]
(ref:searchcontractmetadata), reingestContract , getSpamContracts, isSpamContract , getFloorPrice, getNFTSales , computeRarity , summarizeNFTAttributes, reportSpamContract
Transfers API
All Networks Mainnet and Goerli Only
- ERC20 Transfers - ERC1155 Transfers - ERC721 Transfers - External Transfers - Internal Transfers
Transaction Receipts API
All Networks
- alchemy_getTransactionReceipts
Token API
All Networks
- alchemy_getTokenAllowance - alchemy_getTokenBalances - alchemy_getTokenMetadata
Notify API
All Networks Mainnet and Goerli Only
- Mined Transaction - Dropped Transactions - Address Activity - NFT Activity - NFT Meta Updates
Trace API
Mainnet and Goerli Only
All methods:

- trace_call
- trace_block
- trace_get
- trace_filter
- trace_transaction
- trace_rawTransaction
- trace_replayBlockTransactions
- trace_replayTransaction
Subscription API
All Networks
- newHeads - logs - newPendingTransactions - alchemy_minedTransactions - alchemy_pendingTransactions
TABLE OF CONTENTS
Ethereum API Endpoints by use case
Available Enhanced APIs
Getting Blocks
Reading Transactions
Writing Transactions & EVM Execution
Account Information
Event Logs
Chain Information
Getting Uncles
Gas Estimation
Web3
Real-time Events
NFT API
Transfers API
Transaction Receipts API
Token API
Notify API
Trace API
Subscription API
| All Networks | Mainnet Only |
| --- | --- |
| getNfts, getNFTMetadata, getContractsForOwner, getOwnersForToken, getOwnersForCollection, isHolderOfCollection, getContractMetadata, getNFTsForCollection
getNFTMetadataBatch | [searchContractMetadata]
(ref:searchcontractmetadata), reingestContract , getSpamContracts, isSpamContract , getFloorPrice, getNFTSales , computeRarity , summarizeNFTAttributes, reportSpamContract |


| All Networks | Mainnet and Goerli Only |
| --- | --- |
| - ERC20 Transfers - ERC1155 Transfers - ERC721 Transfers | - External Transfers - Internal Transfers |


| All Networks |
| --- |
| - alchemy_getTransactionReceipts |


| All Networks |
| --- |
| - alchemy_getTokenAllowance - alchemy_getTokenBalances - alchemy_getTokenMetadata |


| All Networks | Mainnet and Goerli Only |
| --- | --- |
| - Mined Transaction - Dropped Transactions - Address Activity | - NFT Activity - NFT Meta Updates |


| Mainnet and Goerli Only |
| --- |
| All methods:

- trace_call
- trace_block
- trace_get
- trace_filter
- trace_transaction
- trace_rawTransaction
- trace_replayBlockTransactions
- trace_replayTransaction |


| All Networks |
| --- |
| - newHeads - logs - newPendingTransactions - alchemy_minedTransactions - alchemy_pendingTransactions |


---

# eth_blockNumber - Ethereum


eth_blockNumber - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBalance - Ethereum


eth_getBalance - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
📘
Note
eth_getBalance only returns the balance of the native chain currency (ex: ETH for Ethereum or Matic for Polygon) and does not include any ERC20 token balances for the given address.
To get ERC20 token balances, please use alchemy_getTokenBalances.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Use Cases for eth_getBalance
How to Get ETH Balance at a Point in Time
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Ethereum


eth_getLogs - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Use cases for eth_getLogs
Understanding Logs: Deep Dive into eth_getLogs
How to query events occurred on the blockchain
🚧
Log Limits
You can make eth_getLogs requests on any block range with a cap of 10K logs in the response OR a 2K block range with no cap on logs in the response and 150MB limit on the response size
If you need to pull logs frequently, we recommend using the Subscription API to push new logs to you when they are available.
📘
Understanding Logs
Want to understand how logs and events work on the EVM? Check out this guide: Understanding Logs: Deep Dive into eth_getLogs.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_chainId - Ethereum


eth_chainId - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
Don’t have an API key?
Start using this API in your app today.
Get started for free
The chain ID returned should always correspond to the information in the current known head block. This ensures that caller of this RPC method can always use the retrieved information to sign transactions built on top of the head.
If the current known head block does not specify a chain ID, the client should treat any calls to eth_chainId as though the method were not supported, and return a suitable error.
You should prefer eth_chainId over net_version, so that you can reliably identify the chain you are communicating with.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByNumber - Ethereum


eth_getBlockByNumber - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Parameters
QUANTITY|TAG - integer of a block number, or the string "earliest", "latest" or "pending", as in the default block parameter.
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0x1b4', 
    true
]
Returns
See eth_getBlockByHash
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
params: [
    '0x1b4', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
```


---

# eth_accounts - Ethereum


eth_accounts - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
Don’t have an API key?
Start using this API in your app today.
Get started for free
🚧
Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_feeHistory - Ethereum


eth_feeHistory - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a collection of historical gas information.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Returns a collection of historical gas information from which you can decide what to submit as your maxFeePerGas and/or maxPriorityFeePerGas. This method was introduced with EIP 1559.
Parameters
blockCount - Number of blocks in the requested range. Between 1 and 1024 blocks can be requested in a single query. Less than requested may be returned if not all blocks are available.
newestBlock - Highest number block of the requested range.
rewardPercentiles - (optional) A monotonically increasing list of percentile values to sample from each block's effective priority fees per gas in ascending order, weighted by gas used.
Returns
Object
oldestBlock - Lowest number block of the returned range.
baseFeePerGas - An array of block base fees per gas. This includes the next block after the newest of the returned range, because this value can be derived from the newest block. Zeroes are returned for pre-EIP-1559 blocks.
gasUsedRatio - An array of block gas used ratios. These are calculated as the ratio of gasUsed and gasLimit.
reward - (Optional) An array of effective priority fees per gas data points from a single block. All zeroes are returned if the block is empty.
baseFeePerBlobGas - An array of base fees per blob gas for blocks. This includes the next block following the newest in the returned range, as this value can be derived from the latest block. For blocks before EIP-4844, zeroes are returned.
blobGasUsedRatio - An array showing the ratios of blob gas used in blocks. These ratios are calculated by dividing blobGasUsed by the maximum blob gas per block.
Example
Request
Alchemy SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
const { Network, Alchemy } = require("alchemy-sdk");

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

async function main() {
  // Using send method from alchemy-sdk with specific transaction details
  const res = await alchemy.core.send("eth_feeHistory", ["0x5", "latest", []]);

  console.log(res);
}

main();
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "oldestBlock": "0x130b1e6",
    "reward": [
      ["0x5041e1e", "0xdd221b80"],
      ["0x5041e1e", "0xb8346df0"],
      ["0x55d4a80", "0xb2d05e00"],
      ["0x4dd9818", "0x3b9aca00"]
    ],
    "baseFeePerGas": [
      "0x52d80a82c",
      "0x50f43f659",
      "0x50012de8d",
      "0x4e30357d6",
      "0x57efff9e7"
    ],
    "gasUsedRatio": [
      0.40875283333333334,
      0.45308523333333334,
      0.4091907,
      0.9987537
    ],
    "baseFeePerBlobGas": ["0x1", "0x1", "0x1", "0x1", "0x1"],
    "blobGasUsedRatio": [0.5, 1, 0.6666666666666666, 1]
  }
}
❗️
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
const { Network, Alchemy } = require("alchemy-sdk");

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

async function main() {
  // Using send method from alchemy-sdk with specific transaction details
  const res = await alchemy.core.send("eth_feeHistory", ["0x5", "latest", []]);

  console.log(res);
}

main();
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "oldestBlock": "0x130b1e6",
    "reward": [
      ["0x5041e1e", "0xdd221b80"],
      ["0x5041e1e", "0xb8346df0"],
      ["0x55d4a80", "0xb2d05e00"],
      ["0x4dd9818", "0x3b9aca00"]
    ],
    "baseFeePerGas": [
      "0x52d80a82c",
      "0x50f43f659",
      "0x50012de8d",
      "0x4e30357d6",
      "0x57efff9e7"
    ],
    "gasUsedRatio": [
      0.40875283333333334,
      0.45308523333333334,
      0.4091907,
      0.9987537
    ],
    "baseFeePerBlobGas": ["0x1", "0x1", "0x1", "0x1", "0x1"],
    "blobGasUsedRatio": [0.5, 1, 0.6666666666666666, 1]
  }
}
```


---

# eth_estimateGas - Ethereum


eth_estimateGas - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
📘
Note
The estimate may be significantly more than the amount of gas actually used by the transaction, for a variety of reasons including EVM mechanics and node performance. Estimates are served directly from nodes, we're not doing anything special to the value so the rest of the network is likely seeing the same.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address to which the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending", see the default block parameter.
🚧
Note
eth_estimateGas will check the balance of the sender (to make sure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Request
alchemyweb3.js
ethers.js
web3.py
cURL
Postman
SDK
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
🚧
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_gasPrice - Ethereum


eth_gasPrice - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
Don’t have an API key?
Start using this API in your app today.
Get started for free
📘
If you are curious about the difference in gas price between this method and the eth gas station, check out this GitHub issue.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBlockTransactionCountByHash - Ethereum


eth_getBlockTransactionCountByHash - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Parameters
DATA, 32 Bytes - hash of a block.
JavaScript
params: [ 
    '0x8243343df08b9751f5ca0c5f8c9c0460d8a9b6351066fae0acbd4d3e776de8bb' 
]
Returns
QUANTITY - integer of the number of transactions in this block.
Example
Request
cURL
Postman
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x8243343df08b9751f5ca0c5f8c9c0460d8a9b6351066fae0acbd4d3e776de8bb"],"id":0}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "0xb0"
}
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
params: [ 
    '0x8243343df08b9751f5ca0c5f8c9c0460d8a9b6351066fae0acbd4d3e776de8bb' 
]
```


```
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x8243343df08b9751f5ca0c5f8c9c0460d8a9b6351066fae0acbd4d3e776de8bb"],"id":0}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "0xb0"
}
```


---

# eth_getBlockTransactionCountByNumber - Ethereum


eth_getBlockTransactionCountByNumber - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Ethereum


eth_getCode - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
Don’t have an API key?
Start using this API in your app today.
Get started for free
📘
Use Cases
Distinguish between contract addresses and wallet addresses
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getProof - Ethereum


eth_getProof - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof. This call can be used to verify that the data you are pulling from is not tampered with.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Parameters
DATA, 20 Bytes - address of the account.
ARRAY, 32 Bytes - an array of storage-keys that should be proofed and included. See eth_getStorageAt
QUANTITY|TAG - integer block number, or the string "latest" or "earliest", see the default block parameter
Returns
Object - A account object:
balance: QUANTITY - the balance of the account. Seeeth_getBalance
codeHash: DATA, 32 Bytes - hash of the code of the account. For a simple Account without code it will return "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"
nonce: QUANTITY, - nonce of the account. See eth_getTransactionCount
storageHash: DATA, 32 Bytes - SHA3 of the StorageRoot. All storage will deliver a MerkleProof starting with this rootHash.
accountProof: ARRAY - Array of rlp-serialized MerkleTree-Nodes, starting with the stateRoot-Node, following the path of the SHA3 (address) as key.
storageProof: ARRAY - Array of storage-entries as requested. Each entry is an object with these properties:
key: QUANTITY - the requested storage key
value: QUANTITY - the storage value
proof: ARRAY - Array of rlp-serialized MerkleTree-Nodes, starting with the storageHash-Node, following the path of the SHA3 (key) as path.
Example
Request
alchemyweb3.js
ethers.js
web3.py
cURL
Postman
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
    // Import the AlchemyWeb3 library. Filepath to functions: 
 // /@alch/alchemy-web3/dist/alchemyWeb3.js
 const { createAlchemyWeb3 } = require("@alch/alchemy-web3");

    // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`);
 
 // Query the blockchain (replace example parameters)
     const account = await web3.eth.getProof({
     address: '0x7e5814a',
  keys: ["0x56e81f,0x283s34"],
  tag: 'latest',
   }); 
    
 // Print the output to console
 console.log(account);
   }

main();
Result
JavaScript
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "accountProof": [
      "0xf90211a...0701bc80",
      "0xf90211a...0d832380",
      "0xf90211a...5fb20c80",
      "0xf90211a...0675b80",
      "0xf90151a0...ca08080"
    ],
    "balance": "0x0",
    "codeHash": "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
    "nonce": "0x0",
    "storageHash": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "storageProof": [
      {
        "key": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "proof": [
          "0xf90211a...0701bc80",
          "0xf90211a...0d832380"
        ],
        "value": "0x1"
      }
    ]
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
    // Import the AlchemyWeb3 library. Filepath to functions: 
 // /@alch/alchemy-web3/dist/alchemyWeb3.js
 const { createAlchemyWeb3 } = require("@alch/alchemy-web3");

    // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`);
 
 // Query the blockchain (replace example parameters)
     const account = await web3.eth.getProof({
     address: '0x7e5814a',
  keys: ["0x56e81f,0x283s34"],
  tag: 'latest',
   }); 
    
 // Print the output to console
 console.log(account);
   }

main();
```


```
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "accountProof": [
      "0xf90211a...0701bc80",
      "0xf90211a...0d832380",
      "0xf90211a...5fb20c80",
      "0xf90211a...0675b80",
      "0xf90151a0...ca08080"
    ],
    "balance": "0x0",
    "codeHash": "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
    "nonce": "0x0",
    "storageHash": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "storageProof": [
      {
        "key": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "proof": [
          "0xf90211a...0701bc80",
          "0xf90211a...0d832380"
        ],
        "value": "0x1"
      }
    ]
  }
}
```


---

# eth_getStorageAt - Ethereum


eth_getStorageAt - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Ethereum


eth_getTransactionByBlockHashAndIndex - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Ethereum


eth_getTransactionByHash - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Ethereum


eth_getTransactionCount - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Ethereum


eth_getTransactionReceipt - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Use cases for eth_getTransactionReceipt
Retrieve general information about a transaction: This can also be used to get general information about a transaction or to track the status of a transaction since the result will be null until the transaction is mined. However, using the Mined Transaction Webhook is a better option for tracking the status of a transaction. Unlike eth_getTransactionByHash, which returns null for unknown transactions, and a non-null response with three (3) null fields for a pending transaction, eth_getTransactionReceipt returns null for both pending and unknown transactions.
This call can also be used to get the contract address for a contract creation tx. However, if you use tools like Hardhat to deploy the contracts, you can get the address of the newly created contract by using the Hardhat toolbox.
🚧
Note
The receipt is not available for pending transactions.
Parameters
DATA, 32 Bytes - hash of a transaction
JavaScript
params: [ 
    '0xab059a62e22e230fe0f56d8555340a29b2e9532360368f810595453f6fdd213b' 
]
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
params: [ 
    '0xab059a62e22e230fe0f56d8555340a29b2e9532360368f810595453f6fdd213b' 
]
```


---

# eth_getUncleByBlockHashAndIndex - Ethereum


eth_getUncleByBlockHashAndIndex - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Ethereum


eth_getUncleByBlockNumberAndIndex - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Ethereum


eth_getUncleCountByBlockHash - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Ethereum


eth_getUncleCountByBlockNumber - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_maxPriorityFeePerGas - Ethereum


eth_maxPriorityFeePerGas - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a fee per gas that is an estimate of how much you can pay as a priority fee, or 'tip', to get a transaction included in the current block.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Generally you will use the value returned from this method to set the maxFeePerGas in a subsequent transaction that you are submitting. This method was introduced with EIP 1559.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_protocolVersion - Ethereum


eth_protocolVersion - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current ethereum protocol version.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Ethereum


eth_sendRawTransaction - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
Don’t have an API key?
Start using this API in your app today.
Get started for free
🚧
Alchemy does not store keys, so transactions sent via Alchemy must be signed ahead of time using another provider like ethers (via eth_signTransaction) and sent with eth_sendRawTransaction.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getTransactionByBlockNumberAndIndex - Ethereum


eth_getTransactionByBlockNumberAndIndex - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - Ethereum


eth_call - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_getBlockByHash - Ethereum


eth_getBlockByHash - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Parameters
Hash - Hash of the block
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
Returns
object - A block object, or null when no block was found. The returned object has the following properties:
number - The block number of the requested block encoded as a hexadecimal string. null if pending.
hash - The block hash of the requested block. null if pending.
parenthash - Hash of the parent block.
nonce - Hash of the generated proof-of-work. null if pending.
sha3uncles - SHA3 of the uncles data in the block.
logsbloom - The bloom filter for the logs of the block. null if pending.
transactionsroot - The root of the transaction trie of the block.
stateroot - The root of the final state trie of the block.
receiptsroot - The root of the receipts trie of the block.
miner - The address of the beneficiary to whom the mining rewards were given.
difficulty - Integer of the difficulty for this block encoded as a hexadecimal string.
totaldifficulty - Integer of the total difficulty of the chain until this block encoded as a hexadecimal string.
extradata - The “extra data” field of this block.
size - The size of this block in bytes as an Integer value encoded as hexadecimal.
gaslimit - The maximum gas allowed in this block encoded as a hexadecimal string.
gasused - The total used gas by all transactions in this block encoded as a hexadecimal string.
timestamp - The unix timestamp for when the block was collated.
transactions - Array of transaction objects - please see eth_getTransactionByHash for exact shape.
uncles - Array of uncle hashes.
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
```
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
```


---

# eth_createAccessList - Ethereum


eth_createAccessList - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Ethereum API - Creates an EIP2930 type accessList based on a given Transaction object. Returns list of addresses and storage keys that are read and written by the transaction (except the sender account and precompiles), plus the estimated gas consumed when the access list is added.
Don’t have an API key?
Start using this API in your app today.
Get started for free
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Ethereum


eth_newFilter - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getFilterChanges - Ethereum


eth_getFilterChanges - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Ethereum


eth_getFilterLogs - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Ethereum


eth_newBlockFilter - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newPendingTransactionFilter - Ethereum


eth_newPendingTransactionFilter - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Ethereum


eth_uninstallFilter - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockReceipts - Ethereum


eth_getBlockReceipts - Ethereum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Ethereum.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_subscribe


eth_subscribe
Subscribe to different Ethereum event types like newHeads, logs, pendingTransactions, and minedTransactions using WebSockets.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Creates a new subscription for desired events. Sends data as soon as it occurs.
Parameters
Event types- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
Optional params - optional parameters to include to describe the type of event to listen to (ex: address)
Returns
While the subscription is active, you will receive events formatted as an object described below:
Event Object:
jsonrpc: Always "2.0"
method: Always "eth_subscription"
params: An object with the following fields:
subscription: The subscription ID returned by the eth_subscribe call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe
result: An object whose contents vary depending on the event type.
Event types
The following event types are accepted in all eth_subscribe WebSocket requests through your Alchemy endpoint. You can view the individual docs for example requests and responses.
Subscription Type Description
alchemy_minedTransactions Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags.
alchemy_pendingTransactions Emits full transaction objects or hashes that are sent to the network, marked as "pending", based on provided filters.
newPendingTransactions Emits transaction hashes that are sent to the network and marked as "pending".
newHeads Emits new blocks that are added to the blockchain.
logs Emits logs attached to a new block that match certain topic filters.
Request
wscat
alchemy-sdk
// initiate websocket stream first
wscat -c wss://eth-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
Result
results
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
WebSocket Limits
There is a limit of 20,000 WebSocket connections per API Key as well as 1,000 parallel WebSocket subscriptions per WebSocket connection, creating a maximum of 20 million subscriptions per application.
The maximum size of a JSON-RPC batch request that can be sent over a WebSocket connection is 20
Free tier users will be limited to 10 concurrent requests per WebSocket connection.
TABLE OF CONTENTS
Parameters
Returns
Event types
Request
Result
WebSocket Limits
```
// initiate websocket stream first
wscat -c wss://eth-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
```


```
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
```


| Subscription Type | Description |
| --- | --- |
| alchemy_minedTransactions | Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags. |
| alchemy_pendingTransactions | Emits full transaction objects or hashes that are sent to the network, marked as "pending", based on provided filters. |
| newPendingTransactions | Emits transaction hashes that are sent to the network and marked as "pending". |
| newHeads | Emits new blocks that are added to the blockchain. |
| logs | Emits logs attached to a new block that match certain topic filters. |


---

# eth_unsubscribe


eth_unsubscribe
Unsubscribe from different Ethereum event types with a regular RPC call with eth_unsubscribe as the method and the subscriptionId as the first parameter.
Don’t have an API key?
Start using this API in your app today.
Get started for free
Parameters
Subscription ID, as previously returned from an eth_subscribe call.
Returns
true if a subscription was successfully canceled, or false if no subscription existed with the given ID.
Example
Request
wscat
alchemy-sdk
wscat -c wss://eth-mainnet.g.alchemy.com/v2/<key>

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
Result
JSON
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
TABLE OF CONTENTS
Parameters
Returns
Example
Request
Result
```
wscat -c wss://eth-mainnet.g.alchemy.com/v2/<key>

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```


```
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```


---

# eth_accounts - Polygon PoS


eth_accounts - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client on Polygon. Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - Polygon PoS


eth_call - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain on Polygon.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_chainId - Polygon PoS


eth_chainId - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID on Polygon, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - Polygon PoS


eth_estimateGas - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete on Polygon. The transaction will not be added to the blockchain.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas. Note: most of our users (95%+) never set the gasPrice on eth_call.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending", see the default block parameter.
🚧
Note
eth_estimateGas will check the sender's balance (to ensure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
SDK
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
❗️
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
```
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_gasPrice - Polygon PoS


eth_gasPrice - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei for Polygon.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBalance - Polygon PoS


eth_getBalance - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address on Polygon.
📘
Note
eth_getBalance only returns the balance of the native chain currency (ex: ETH for Ethereum or Matic for Polygon) and does not include any ERC20 token balances for the given address.
To get ERC20 token balances, please use alchemy_getTokenBalances.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - Polygon PoS


eth_getBlockByHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block on Polygon by block hash.
Parameters
DATA, 32 Bytes - Hash of a block.
Boolean - If true it returns the full transaction objects, if false it returns only the hashes of the transactions.
JavaScript
params: [
    '0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
    true
]
Returns
Object - A block object with the following fields, or null when no block was found:
number: QUANTITY - the block number. null when its pending block.
hash: DATA, 32 Bytes - hash of the block. null when its pending block.
parentHash: DATA, 32 Bytes - hash of the parent block.
nonce: DATA, 8 Bytes - hash of the generated proof-of-work. null when its pending block.
sha3Uncles: DATA, 32 Bytes - SHA3 of the uncles data in the block.
logsBloom: DATA, 256 Bytes - the bloom filter for the logs of the block. null when its pending block.
transactionsRoot: DATA, 32 Bytes - the root of the transaction trie of the block.
stateRoot: DATA, 32 Bytes - the root of the final state trie of the block.
receiptsRoot: DATA, 32 Bytes - the root of the receipts trie of the block.
miner: DATA, 20 Bytes - the address of the beneficiary to whom the mining rewards were given.
difficulty: QUANTITY - integer of the difficulty for this block.
totalDifficulty: QUANTITY - integer of the total difficulty of the chain until this block.
extraData: DATA - the "extra data" field of this block.
size: QUANTITY - integer the size of this block in bytes.
gasLimit: QUANTITY - the maximum gas allowed in this block.
gasUsed: QUANTITY - the total used gas by all transactions in this block.
timestamp: QUANTITY - the unix timestamp for when the block was collated.
transactions: Array - Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter.
uncles: Array - Array of uncle hashes.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
SDK
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e", true],"id":0}'
Result
JavaScript
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": {
        "difficulty": "0x13",
        "extraData": "0xd783010a0383626f7288676f312e31352e35856c696e7578000000000000000029adbbaf99a3f97b2baefa11e865cf9d74435716ef8618caaa388619f5ae7d8e5d2cadab0cd2f5becd4ebf7d48f5584c9e414c2a4a6ea2bc6ea8f02dbf5675cd01",
        "gasLimit": "0x1385aa8",
        "gasUsed": "0x1380a56",
        "hash": "0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e",
        "logsBloom": "0x3eb4221d73001e540126a703d8666026b3480983cccc083c04ba806267cc27149835341b440290711abcd3188b4c1da12b84cd48131caa0860a6c1d136bebe8a89918c04184b6e00827328c802a23ca738981432097c0300823b0d34d0d0c6c4682508ecdaf0b4190deb480c4b5a9ca01db86eacca08c5f1d7d0d2f6245c099a010967474dcab60810d55c224564a88b0b29fcdba123000a78643a750604e002f68930330062607a9eaa05ca59a60a4e4449de00f2bb86708121d1093ac8415b18048416334214e80491cc6613434e0272df878498eab4320239d4d77881fbc433d0ca83051d010128102226cd58a248cb008e2240fcd658148169358e502d53",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0xf93d47",
        "parentHash": "0x745ffd6d21e961040b0821f93be0f9533d2f01f87289abe78af4d8052a4c5528",
        "receiptsRoot": "0xc9cb68ece0290f11a0c3e96e8c7ef52bc0b7a6f0543360c4967400750c2ea23f",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0xf747",
        "stateRoot": "0xdd45900534469c5fcbf7b9ac3a56639e2ff6821500804347a5b9332bfa880813",
        "timestamp": "0x60dcae89",
        "totalDifficulty": "0xa4be87e",
        "transactions": [
            {
                "blockHash": "0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e",
                "blockNumber": "0xf93d47",
                "from": "0x8a18a2fee7dc9c2002e21fda8c10f0feb0abf05e",
                "gas": "0x61899",
                "gasPrice": "0x17a27db936",
                "hash": "0x78f825c7d0c09709b82a54b170887d000c58408725cd8d44d10df3382fc5fa1c",
                "input": "0xf98a9e410000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000007b0900000000000000f5a20b000000002791bca1f2de4661ed88a30c99a7a9449aa841741e00f38a214f0f8c02b5b1f5b93fe646a4390e842a2d1e014395bb4d53f0f9fe088a7b1a0c2924e4eab7712f1e01d4deec3fd8578887ba3cd6549e188307033600d91e01f36ad6a25ed157b896ce5178ffd82ee6203d760d0000000000",
                "nonce": "0xa9ee",
                "to": "0xeee49495242da9e0bdbe29a7098388cea8348de4",
                "transactionIndex": "0x0",
                "value": "0x0",
                "type": "0x0",
                "v": "0x136",
                "r": "0x8aa119caab9667a1cad06f6fdaf1d01ee80b3c50cf5b53a71dcaff557dfb9b24",
                "s": "0x305482180355f212cad7a07fda4ce4e1832f1c3013316b660c647f3e5f8c231b"
            }
            ...
        ],
        "transactionsRoot": "0xe3394943ac8e86ee3f0112719f1f4e9eb229b7221792a4279c2bdb390bce1ba3",
        "uncles": []
    }
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
```
params: [
    '0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
    true
]
```


```
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e", true],"id":0}'
```


```
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": {
        "difficulty": "0x13",
        "extraData": "0xd783010a0383626f7288676f312e31352e35856c696e7578000000000000000029adbbaf99a3f97b2baefa11e865cf9d74435716ef8618caaa388619f5ae7d8e5d2cadab0cd2f5becd4ebf7d48f5584c9e414c2a4a6ea2bc6ea8f02dbf5675cd01",
        "gasLimit": "0x1385aa8",
        "gasUsed": "0x1380a56",
        "hash": "0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e",
        "logsBloom": "0x3eb4221d73001e540126a703d8666026b3480983cccc083c04ba806267cc27149835341b440290711abcd3188b4c1da12b84cd48131caa0860a6c1d136bebe8a89918c04184b6e00827328c802a23ca738981432097c0300823b0d34d0d0c6c4682508ecdaf0b4190deb480c4b5a9ca01db86eacca08c5f1d7d0d2f6245c099a010967474dcab60810d55c224564a88b0b29fcdba123000a78643a750604e002f68930330062607a9eaa05ca59a60a4e4449de00f2bb86708121d1093ac8415b18048416334214e80491cc6613434e0272df878498eab4320239d4d77881fbc433d0ca83051d010128102226cd58a248cb008e2240fcd658148169358e502d53",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0xf93d47",
        "parentHash": "0x745ffd6d21e961040b0821f93be0f9533d2f01f87289abe78af4d8052a4c5528",
        "receiptsRoot": "0xc9cb68ece0290f11a0c3e96e8c7ef52bc0b7a6f0543360c4967400750c2ea23f",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0xf747",
        "stateRoot": "0xdd45900534469c5fcbf7b9ac3a56639e2ff6821500804347a5b9332bfa880813",
        "timestamp": "0x60dcae89",
        "totalDifficulty": "0xa4be87e",
        "transactions": [
            {
                "blockHash": "0xe2885b25d0863ce4df48facee18d5dd4b4be7366abc59133c2de66ab57d7b71e",
                "blockNumber": "0xf93d47",
                "from": "0x8a18a2fee7dc9c2002e21fda8c10f0feb0abf05e",
                "gas": "0x61899",
                "gasPrice": "0x17a27db936",
                "hash": "0x78f825c7d0c09709b82a54b170887d000c58408725cd8d44d10df3382fc5fa1c",
                "input": "0xf98a9e410000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000007b0900000000000000f5a20b000000002791bca1f2de4661ed88a30c99a7a9449aa841741e00f38a214f0f8c02b5b1f5b93fe646a4390e842a2d1e014395bb4d53f0f9fe088a7b1a0c2924e4eab7712f1e01d4deec3fd8578887ba3cd6549e188307033600d91e01f36ad6a25ed157b896ce5178ffd82ee6203d760d0000000000",
                "nonce": "0xa9ee",
                "to": "0xeee49495242da9e0bdbe29a7098388cea8348de4",
                "transactionIndex": "0x0",
                "value": "0x0",
                "type": "0x0",
                "v": "0x136",
                "r": "0x8aa119caab9667a1cad06f6fdaf1d01ee80b3c50cf5b53a71dcaff557dfb9b24",
                "s": "0x305482180355f212cad7a07fda4ce4e1832f1c3013316b660c647f3e5f8c231b"
            }
            ...
        ],
        "transactionsRoot": "0xe3394943ac8e86ee3f0112719f1f4e9eb229b7221792a4279c2bdb390bce1ba3",
        "uncles": []
    }
}
```


---

# eth_getBlockByNumber - Polygon PoS


eth_getBlockByNumber - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block on Polygon by block number.
Parameters
QUANTITY|TAG - integer of a block number, or the string "earliest", "latest" or "pending", as in the default block parameter.
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0x1b4', 
    true
]
Returns
Object - A block object with the following fields, or null when no block was found:
number: QUANTITY - the block number. null when its pending block.
hash: DATA, 32 Bytes - hash of the block. null when its pending block.
parentHash: DATA, 32 Bytes - hash of the parent block.
nonce: DATA, 8 Bytes - hash of the generated proof-of-work. null when its pending block.
sha3Uncles: DATA, 32 Bytes - SHA3 of the uncles data in the block.
logsBloom: DATA, 256 Bytes - the bloom filter for the logs of the block. null when its pending block.
transactionsRoot: DATA, 32 Bytes - the root of the transaction trie of the block.
stateRoot: DATA, 32 Bytes - the root of the final state trie of the block.
receiptsRoot: DATA, 32 Bytes - the root of the receipts trie of the block.
miner: DATA, 20 Bytes - the address of the beneficiary to whom the mining rewards were given.
difficulty: QUANTITY - integer of the difficulty for this block.
totalDifficulty: QUANTITY - integer of the total difficulty of the chain until this block.
extraData: DATA - the "extra data" field of this block.
size: QUANTITY - integer the size of this block in bytes.
gasLimit: QUANTITY - the maximum gas allowed in this block.
gasUsed: QUANTITY - the total used gas by all transactions in this block.
timestamp: QUANTITY - the unix timestamp for when the block was collated.
transactions: Array - Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter.
uncles: Array - Array of uncle hashes.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
SDK
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
Result
JavaScript
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": {
        "difficulty": "0x7",
        "extraData": "0xd58301090083626f7286676f312e3133856c696e757800000000000000000000e14198dde4da0ea1015e9d38ad288f5ba62cf8d1b9a98ccd02fb6f75553ee51c70caa1c376cf4a937c644cae060effe8bf25409cef9ecd25013a608b3a51cbef00",
        "gasLimit": "0xe984c2",
        "gasUsed": "0x0",
        "hash": "0xa284f649d7d9a3c0dea48e3bf3d295767a4893902e61d27e1590d4cece691b6f",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0x1b4",
        "parentHash": "0x9481d3bb2bbe842f0e4703cb5be094d95650fe8345b4da5642ed27bec3acd0d5",
        "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0x260",
        "stateRoot": "0x01b797385461764bd56336dd5e810f3d57529d47bcbf3260c7d9c770bf6c5af4",
        "timestamp": "0x5ed28d86",
        "totalDifficulty": "0xbed",
        "transactions": [],
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "uncles": []
    }
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
```
params: [
    '0x1b4', 
    true
]
```


```
curl https://polygon-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
```


```
{
    "jsonrpc": "2.0",
    "id": 0,
    "result": {
        "difficulty": "0x7",
        "extraData": "0xd58301090083626f7286676f312e3133856c696e757800000000000000000000e14198dde4da0ea1015e9d38ad288f5ba62cf8d1b9a98ccd02fb6f75553ee51c70caa1c376cf4a937c644cae060effe8bf25409cef9ecd25013a608b3a51cbef00",
        "gasLimit": "0xe984c2",
        "gasUsed": "0x0",
        "hash": "0xa284f649d7d9a3c0dea48e3bf3d295767a4893902e61d27e1590d4cece691b6f",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "miner": "0x0000000000000000000000000000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x0000000000000000",
        "number": "0x1b4",
        "parentHash": "0x9481d3bb2bbe842f0e4703cb5be094d95650fe8345b4da5642ed27bec3acd0d5",
        "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0x260",
        "stateRoot": "0x01b797385461764bd56336dd5e810f3d57529d47bcbf3260c7d9c770bf6c5af4",
        "timestamp": "0x5ed28d86",
        "totalDifficulty": "0xbed",
        "transactions": [],
        "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        "uncles": []
    }
}
```


---

# eth_getBlockTransactionCountByHash - Polygon PoS


eth_getBlockTransactionCountByHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Polygon PoS


eth_getBlockTransactionCountByNumber - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Polygon PoS


eth_getCode - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address on Polygon.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - Polygon PoS


eth_getFilterChanges - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Polygon PoS


eth_getFilterLogs - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id on Polygon. Can compute the same results with an eth_getLogs call.
📘
Note on Filters
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Polygon PoS


eth_getLogs - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
🚧
Log Limits
You can make eth_getLogs requests on any block range with a cap of 10K logs in the response OR a 2K block range with no cap on logs in the response and 150MB limit on the response size
If you need to pull logs frequently, we recommend using WebSockets to push new logs to you when they are available.
📘
Understanding Logs
Want to understand how logs and events work on the EVM? Check out this guide: Understanding Logs: Deep Dive into eth_getLogs
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getRootHash - Polygon PoS


eth_getRootHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the root hash given a block range on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getSignersAtHash - Polygon PoS


eth_getSignersAtHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Returns all signs given a blockhash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getStorageAt - Polygon PoS


eth_getStorageAt - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Polygon PoS


eth_getTransactionByBlockHashAndIndex - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - Polygon PoS


eth_getTransactionByBlockNumberAndIndex - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Polygon PoS


eth_getTransactionByHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash on Polygon. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Polygon PoS


eth_getTransactionCount - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address on Polygon.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Polygon PoS


eth_getTransactionReceipt - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash on Polygon.
This can also be used to track the status of a transaction, since result will be null until the transaction is mined. However, unlike eth_getTransactionByHash which returns null for unknown transactions, and a non-null response with 3 null fields for a pending transaction, eth_getTransactionReceipt returns null for both pending and unknown transactions.
This call is also commonly used to get the contract address for a contract creation tx.
🚧
Note: the receipt is not available for pending transactions.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceiptsByBlock - Polygon PoS


eth_getTransactionReceiptsByBlock - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Returns all transaction receipts for the given block number or hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Polygon PoS


eth_sendRawTransaction - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.

Note: Due to network constraints, transactions on Polygon Mainnet must be submitted with a minimum gasPrice of 30 gwei.
🚧
NOTE
Due to network constraints, transactions on Polygon Mainnet must be submitted with a minimum gasPrice of 30 gwei.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Polygon PoS


eth_uninstallFilter - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Polygon PoS


eth_getUncleCountByBlockHash - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Polygon PoS


eth_getUncleCountByBlockNumber - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Polygon PoS


eth_newBlockFilter - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Polygon PoS

eth_newFilter - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Creates a filter object, based on filter options, to notify when the state changes (logs).
PATH PARAMS
apiKey
string
required
Defaults to docs-demo
For higher throughput, create your own API key
BODY PARAMS
id
integer
Defaults to 1
jsonrpc
string
Defaults to 2.0
method
string
Defaults to eth_newFilter
params
array of objects
OBJECT
blockHash
string
Using blockHash is equivalent to fromBlock = toBlock = the block number with hash blockHash. If blockHash is present in the filter criteria, then neither fromBlock nor toBlock are allowed.
address
array of strings
Defaults to 0xb59f67a8bff5d8cd03f6ac17265c550ed8f33907
Contract address or a list of addresses from which logs should originate.
STRING
ADD STRING
fromBlock
string
Defaults to 0x429d3b
String - Either the hex value of a block number OR block tags:
block number (in hex) OR
block tag (one of the following):
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
toBlock
string
Defaults to latest
String - Either the hex value of a block number OR block tags:
block number (in hex) OR
block tag (one of the following):
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
topics
array of strings
Defaults to 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef,0x00000000000000000000000000b46c2526e227482e2ebb8f4c69e4674d262e75,0x00000000000000000000000054a2d42a40f51259dedd1978f6c118a0f0eff078
Array of 32 Bytes DATA topics. Topics are order-dependent. Each topic can also be an array of DATA with "or" options.
STRING
STRING
STRING
ADD STRING
RESPONSE
200
Returns a filter id.
RESPONSE BODY
object
id
integer
jsonrpc
string
result
string
Updated about 1 year ago
eth_newBlockFilter - Polygon PoS
eth_newPendingTransactionFilter - Polygon PoS
Did this page help you?
Yes
No
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
CURL REQUEST
EXAMPLES
1
curl --request POST \
2
     --url https://eth-mainnet.g.alchemy.com/v2/docs-demo \
3
     --header 'accept: application/json' \
4
     --header 'content-type: application/json' \
5
     --data '
6
{
7
  "id": 1,
8
  "jsonrpc": "2.0",
9
  "method": "eth_newFilter",
10
  "params": [
11
    {
12
      "address": [
13
        "0xb59f67a8bff5d8cd03f6ac17265c550ed8f33907"
14
      ],
15
      "fromBlock": "0x429d3b",
16
      "toBlock": "latest",
17
      "topics": [
18
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
19
        "0x00000000000000000000000000b46c2526e227482e2ebb8f4c69e4674d262e75",
20
        "0x00000000000000000000000054a2d42a40f51259dedd1978f6c118a0f0eff078"
21
      ]
24
}
25
'
Try It!
RESPONSE
EXAMPLES
Click Try It! to start a request and see the response here! Or choose an example:
application/json
200
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - Polygon PoS


eth_newPendingTransactionFilter - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive on Polygon. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_createAccessList - Polygon PoS


eth_createAccessList - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon API - Creates an EIP2930 type accessList based on a given Transaction object. Returns list of addresses and storage keys that are read and written by the transaction (except the sender account and precompiles), plus the estimated gas consumed when the access list is added.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - Polygon PoS


eth_blockNumber - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block on Polygon.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getProof - Polygon PoS


eth_getProof - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof on Polygon. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getUncleByBlockNumberAndIndex - Polygon PoS


eth_getUncleByBlockNumberAndIndex - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_maxPriorityFeePerGas - Polygon PoS


eth_maxPriorityFeePerGas - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a fee per gas that is an estimate of how much you can pay as a priority fee, or 'tip', to get a transaction included in the current block.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockReceipts - Polygon PoS


eth_getBlockReceipts - Polygon PoS
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Polygon.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygon-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_subscribe - Polygon PoS


eth_subscribe - Polygon PoS
Subscribe to different Polygon event types like newHeads, logs, pendingTransactions, and minedTransactions using WebSockets.
Creates a new subscription for desired events. Sends data as soon as it occurs.
Parameters
Event types- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
Optional params - optional parameters to include to describe the type of event to listen to (ex: address)
Returns
While the subscription is active, you will receive events formatted as an object described below:
Event Object:
jsonrpc: Always "2.0"
method: Always "eth_subscription"
params: An object with the following fields:
subscription: The subscription ID returned by the eth_subscribe call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe
result: An object whose contents vary depending on the event type.
Event types
The following event types are accepted in all eth_subscribe WebSocket requests through your Alchemy endpoint. You can view the individual docs for example requests and responses.
Subscription Type Description
alchemy_minedTransactions Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags.
alchemy_pendingTransactions Emits full transaction objects or hashes that are sent to the network, marked as "pending", based on provided filters.
newPendingTransactions Emits transaction hashes that are sent to the network and marked as "pending".
newHeads Emits new blocks that are added to the blockchain.
logs Emits logs attached to a new block that match certain topic filters.
Request
wscat
alchemy-sdk
// initiate websocket stream first
wscat -c wss://polygon-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
Result
results
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
WebSocket Limits
There is a limit of 20,000 WebSocket connections per API Key as well as 1,000 parallel WebSocket subscriptions per WebSocket connection, creating a maximum of 20 million subscriptions per application.
The maximum size of a JSON-RPC batch request that can be sent over a WebSocket connection is 20
Free tier users will be limited to 10 concurrent requests per WebSocket connection.
TABLE OF CONTENTS
Parameters
Returns
Event types
Request
Result
WebSocket Limits
```
// initiate websocket stream first
wscat -c wss://polygon-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
```


```
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
```


| Subscription Type | Description |
| --- | --- |
| alchemy_minedTransactions | Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags. |
| alchemy_pendingTransactions | Emits full transaction objects or hashes that are sent to the network, marked as "pending", based on provided filters. |
| newPendingTransactions | Emits transaction hashes that are sent to the network and marked as "pending". |
| newHeads | Emits new blocks that are added to the blockchain. |
| logs | Emits logs attached to a new block that match certain topic filters. |


---

# eth_unsubscribe - Polygon PoS


eth_unsubscribe - Polygon PoS
Unsubscribe from different Polygon event types with a regular RPC call with eth_unsubscribe as the method and the subscriptionId as the first parameter.
Parameters
Subscription ID, as previously returned from an eth_subscribe call.
Returns
true if a subscription was successfully canceled, or false if no subscription existed with the given ID.
Example
Request
wscat
alchemy-sdk
wscat -c wss://polygon-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
Result
JSON
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
TABLE OF CONTENTS
Parameters
Returns
Example
Request
Result
```
wscat -c wss://polygon-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```


```
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```


---

# eth_getTransactionCount - Polygon zkEVM


eth_getTransactionCount - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - Polygon zkEVM


eth_call - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the blockchain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest" or "earliest" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_chainId - Polygon zkEVM


eth_chainId - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Polygon zkEVM


eth_newBlockFilter - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon zkEVM API - Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - Polygon zkEVM


eth_estimateGas - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
📘
Note
The estimate may be significantly more than the amount of gas actually used by the transaction, for a variety of reasons including EVM mechanics and node performance. Estimates are served directly from nodes, we're not doing anything special to the value so the rest of the network is likely seeing the same.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address to which the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest" or "earliest", see the default block parameter.
🚧
Note
eth_estimateGas will check the balance of the sender (to make sure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Request
alchemyweb3.js
ethers.js
web3.py
cURL
Postman
SDK
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
🚧
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_newFilter - Polygon zkEVM


eth_newFilter - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon zkEVM API - Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_gasPrice - Polygon zkEVM


eth_gasPrice - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei for Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Polygon zkEVM


eth_sendRawTransaction - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions on the Polygon zkEVM network.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBalance - Polygon zkEVM


eth_getBalance - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Polygon zkEVM


eth_uninstallFilter - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polygon zkEVM API - Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren not requested with eth_getFilterChanges for a period of time.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - Polygon zkEVM


eth_getBlockByHash - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block on Polygon zkEVM by block hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByNumber - Polygon zkEVM


eth_getBlockByNumber - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block on Polygon zkEVM by block number.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByHash - Polygon zkEVM


eth_getBlockTransactionCountByHash - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Polygon zkEVM


eth_getBlockTransactionCountByNumber - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Polygon zkEVM


eth_getCode - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address on the Polygon zkEVM network.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - Polygon zkEVM


eth_getFilterChanges - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Polygon zkEVM


eth_getFilterLogs - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id on Polygon zkEVM. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Polygon zkEVM


eth_getLogs - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getStorageAt - Polygon zkEVM


eth_getStorageAt - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address on the Polygon zkEVM network, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Polygon zkEVM


eth_getTransactionByBlockHashAndIndex - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - Polygon zkEVM


eth_getTransactionByBlockNumberAndIndex - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Polygon zkEVM


eth_getTransactionByHash - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash on Polygon zkEVM. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getCompilers - Polygon zkEVM


eth_getCompilers - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of installed compilers (Deprecated). Response is always empty in Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - Polygon zkEVM


eth_getUncleByBlockHashAndIndex - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle block by block hash and uncle index position. Response for this method is always empty on Polygon zkEVM.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Polygon zkEVM


eth_getUncleByBlockNumberAndIndex - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle block by block number and uncle index position. Response for this method is always empty on Polygon zkEVM.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Polygon zkEVM


eth_getUncleCountByBlockHash - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block specified by block hash. Response for this method is always 0 on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Polygon zkEVM


eth_getUncleCountByBlockNumber - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block specified by block number. Response for this method is always 0 on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_protocolVersion - Polygon zkEVM


eth_protocolVersion - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current network protocol version as a string. Response for this method is always 0 on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - Polygon zkEVM


eth_blockNumber - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Polygon zkEVM


eth_getTransactionReceipt - Polygon zkEVM
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash on Polygon zkEVM.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
polygonzkevm-cardona
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - Arbitrum


eth_call - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_estimateGas - Arbitrum


eth_estimateGas - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
Parameters
Object - The transaction call object.
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas. Note: most of our users (95%+) never set the gasPrice on eth_call.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see the Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending", see the default block parameter.
🚧
Note
eth_estimateGas will check the sender's balance (to ensure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
❗️
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
```
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_accounts - Arbitrum


eth_accounts - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
Parameters
none
Returns
Array of DATA, 20 Bytes - addresses owned by the client.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}'
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": []
}
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}'
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": []
}
```


---

# eth_blockNumber - Arbitrum


eth_blockNumber - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
Parameters
none
Returns
QUANTITY - integer of the current block number the client is on.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":0}'
```
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "0xa1c054"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":0}'
```
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "0xa1c054"
}
```


---

# eth_chainId - Arbitrum


eth_chainId - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
Parameters
None.
Returns
QUANTITY - integer of the current chain ID.
Example
Alchemy Composer
The Alchemy Composer allows you to make a no-code example request via your browser. Try it out above!
Request
cURL
Postman
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":83}'
Result
JavaScript
{
  "id": 83,
  "jsonrpc": "2.0",
  "result": "0x3d" // 61
}
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
curl https://arb-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":83}'
```


```
{
  "id": 83,
  "jsonrpc": "2.0",
  "result": "0x3d" // 61
}
```


---

# eth_gasPrice - Arbitrum


eth_gasPrice - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBalance - Arbitrum


eth_getBalance - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
📘
Note
eth_getBalance only returns the balance of the native chain currency (ex: ETH for Ethereum or Matic for Polygon) and does not include any ERC20 token balances for the given address.
To get ERC20 token balances, please use alchemy_getTokenBalances.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByHash - Arbitrum


eth_getBlockTransactionCountByHash - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Arbitrum


eth_getBlockTransactionCountByNumber - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Arbitrum


eth_getCode - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - Arbitrum


eth_getFilterChanges - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Arbitrum


eth_getFilterLogs - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Arbitrum


eth_getLogs - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
🚧
Log Limits
You can make eth_getLogs requests on any block range with a cap of 10K logs in the response OR a 2K block range with no cap on logs in the response and 150MB limit on the response size
If you need to pull logs frequently, we recommend using WebSockets to push new logs to you when they are available.
📘
Understanding Logs
Want to understand how logs and events work on the EVM? Check out this guide: Understanding Logs: Deep Dive into eth_getLogs
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getStorageAt - Arbitrum


eth_getStorageAt - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Arbitrum


eth_getTransactionByBlockHashAndIndex - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position in Arbitrum network.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Arbitrum


eth_getTransactionCount - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Arbitrum


eth_getUncleByBlockNumberAndIndex - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Arbitrum


eth_getUncleCountByBlockHash - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Arbitrum


eth_getUncleCountByBlockNumber - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Arbitrum


eth_newBlockFilter - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Arbitrum


eth_newFilter - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - Arbitrum


eth_newPendingTransactionFilter - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Arbitrum


eth_uninstallFilter - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Arbitrum


eth_sendRawTransaction - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_createAccessList - Arbitrum


eth_createAccessList - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Arbitrum API - Creates an EIP2930 type accessList based on a given Transaction object. Returns list of addresses and storage keys that are read and written by the transaction (except the sender account and precompiles), plus the estimated gas consumed when the access list is added.
Resources
More info on EIP2930
accessList contains all storage slots and addresses that are read and written by the transaction, except for the sender account and the precompiles
An accessList can be used to unstuck contracts that became inaccessible due to gas cost increases.
Like eth_estimateGas, the gas estimate and accessList returned from this method is an estimation; the list could change when the transaction is actually mined
Adding an accessList to your transaction does not necessary result in lower gas usage compared to a transaction without an accessList
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_maxPriorityFeePerGas - Arbitrum


eth_maxPriorityFeePerGas - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a fee per gas that is an estimate of how much you can pay as a priority fee, or 'tip', to get a transaction included in the current block.
PATH PARAMS
apiKey
string
required
Defaults to docs-demo
For higher throughput, create your own API key
BODY PARAMS
id
integer
Defaults to 1
jsonrpc
string
Defaults to 2.0
method
string
Defaults to eth_maxPriorityFeePerGas
RESPONSE
200
Returns the estimated priority fee per gas.
RESPONSE BODY
object
id
integer
jsonrpc
string
result
string
Updated about 1 year ago
eth_createAccessList - Arbitrum
eth_getBlockByHash - Arbitrum
Did this page help you?
Yes
No
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
eth-mainnet
.g.alchemy.com/v2
/{apiKey}
CURL REQUEST
EXAMPLES
1
curl --request POST \
2
     --url https://eth-mainnet.g.alchemy.com/v2/docs-demo \
3
     --header 'accept: application/json' \
4
     --header 'content-type: application/json' \
5
     --data '
6
{
7
  "id": 1,
8
  "jsonrpc": "2.0",
9
  "method": "eth_maxPriorityFeePerGas"
10
}
11
'
Try It!
RESPONSE
EXAMPLES
Click Try It! to start a request and see the response here! Or choose an example:
application/json
200
---

# eth_getBlockByHash - Arbitrum


eth_getBlockByHash - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash on the Arbitrum network.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBlockByNumber - Arbitrum


eth_getBlockByNumber - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number on the Arbitrum network.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getTransactionByBlockNumberAndIndex - Arbitrum


eth_getTransactionByBlockNumberAndIndex - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Arbitrum


eth_getTransactionByHash - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getProof - Arbitrum


eth_getProof - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof on Arbitrum. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getTransactionReceipt - Arbitrum


eth_getTransactionReceipt - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - Arbitrum


eth_getUncleByBlockHashAndIndex - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockReceipts - Arbitrum


eth_getBlockReceipts - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Arbitrum.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_feeHistory - Arbitrum


eth_feeHistory - Arbitrum
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a collection of historical gas information.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
arb-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_subscribe


eth_subscribe
Subscribe to different Arbitrum event types like newHeads, logs, pendingTransactions, and syncing using WebSockets.
Creates a new subscription for desired events. Sends data as soon as it occurs.
Parameters
Event types- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
Optional params - optional parameters to include to describe the type of event to listen to (ex: address)
Returns
While the subscription is active, you will receive events formatted as an object described below:
Event Object:
jsonrpc: Always "2.0"
method: Always "eth_subscription"
params: An object with the following fields:
subscription: The subscription ID returned by the eth_subscribe call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe
result: An object whose contents vary depending on the event type.
Event types
The following event types are accepted in all eth_subscribe WebSocket requests through your Alchemy endpoint. You can view the individual docs for example requests and responses.
Subscription Type Description
alchemy_minedTransactions Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags.
newHeads Emits new blocks that are added to the blockchain.
[logs][ref:logs] Emits logs attached to a new block that match certain topic filters.
Request
wscat
alchemy-sdk
// initiate websocket stream first
wscat -c wss://arb-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
Result
results
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
WebSocket Limits
There is a limit of 20,000 WebSocket connections per API Key as well as 1,000 parallel WebSocket subscriptions per WebSocket connection, creating a maximum of 20 million subscriptions per application.
The maximum size of a JSON-RPC batch request that can be sent over a WebSocket connection is 20
Free tier users will be limited to 10 concurrent requests per WebSocket connection.
TABLE OF CONTENTS
Parameters
Returns
Event types
Request
Result
WebSocket Limits
```
// initiate websocket stream first
wscat -c wss://arb-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
```


```
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
```


| Subscription Type | Description |
| --- | --- |
| alchemy_minedTransactions | Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags. |
| newHeads | Emits new blocks that are added to the blockchain. |
| [logs][ref:logs] | Emits logs attached to a new block that match certain topic filters. |


---

# eth_unsubscribe


eth_unsubscribe
Unsubscribe from different Arbitrum event types with a regular RPC call with eth_unsubscribe as the method and the subscriptionId as the first parameter.
Parameters
Subscription ID, as previously returned from an eth_subscribe call.
Returns
true if a subscription was successfully canceled, or false if no subscription existed with the given ID.
Example
Request
wscat
alchemy-sdk
wscat -c wss://arb-mainnet.g.alchemy.com/v2/<key>

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
Result
JSON
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
TABLE OF CONTENTS
Parameters
Returns
Example
Request
Result
```
wscat -c wss://arb-mainnet.g.alchemy.com/v2/<key>

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```


```
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```


---

# eth_call - Optimism


eth_call - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_estimateGas - Optimism


eth_estimateGas - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
📘
Note
The estimate may be significantly more than the amount of gas actually used by the transaction, for a variety of reasons including EVM mechanics and node performance. Estimates are served directly from nodes, we're not doing anything special to the value so the rest of the network is likely seeing the same.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas. Note: most of our users (95%+) never set the gasPrice on eth_call.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending", see the default block parameter.
🚧
Note
eth_estimateGas will check the sender's balance (to ensure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Request
cURL
Postman
curl https://opt-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
```
curl https://opt-mainnet.g.alchemy.com/v2/your-api-key \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_accounts - Optimism


eth_accounts - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - Optimism


eth_blockNumber - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_chainId - Optimism


eth_chainId - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_gasPrice - Optimism


eth_gasPrice - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBalance - Optimism


eth_getBalance - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
📘
Note
eth_getBalance only returns the balance of the native chain currency (ex: ETH for Ethereum or Matic for Polygon) and does not include any ERC20 token balances for the given address.
To get ERC20 token balances, please use alchemy_getTokenBalances.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByHash - Optimism


eth_getBlockTransactionCountByHash - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Optimism


eth_getBlockTransactionCountByNumber - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Optimism


eth_getCode - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - Optimism


eth_getFilterChanges - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Optimism


eth_getFilterLogs - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Optimism


eth_getLogs - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
🚧
Log Limits
You can make eth_getLogs requests on any block range with a cap of 10K logs in the response OR a 2K block range with no cap on logs in the response and 150MB limit on the response size
If you need to pull logs frequently, we recommend using WebSockets to push new logs to you when they are available.
📘
Understanding Logs
Want to understand how logs and events work on the EVM? Check out this guide: Understanding Logs: Deep Dive into eth_getLogs
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getStorageAt - Optimism


eth_getStorageAt - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Optimism


eth_getTransactionByBlockHashAndIndex - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - Optimism


eth_getTransactionByBlockNumberAndIndex - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Optimism


eth_getTransactionByHash - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Optimism


eth_getTransactionCount - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Optimism


eth_getTransactionReceipt - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - Optimism


eth_getUncleByBlockHashAndIndex - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Optimism


eth_getUncleByBlockNumberAndIndex - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Optimism


eth_getUncleCountByBlockHash - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Optimism


eth_getUncleCountByBlockNumber - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Optimism


eth_newBlockFilter - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Optimism


eth_newFilter - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - Optimism


eth_newPendingTransactionFilter - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_protocolVersion - Optimism


eth_protocolVersion - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current ethereum protocol version.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Optimism


eth_sendRawTransaction - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_syncing - Optimism


eth_syncing - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Optimism


eth_uninstallFilter - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - Optimism


eth_getBlockByHash - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
Parameters
Hash - Hash of the block
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
Returns
object - A block object, or null when no block was found. The returned object has the following properties:
number - The block number of the requested block encoded as a hexadecimal string. null if pending.
hash - The block hash of the requested block. null if pending.
parenthash - Hash of the parent block.
nonce - Hash of the generated proof-of-work. null if pending.
sha3uncles - SHA3 of the uncles data in the block.
logsbloom - The bloom filter for the logs of the block. null if pending.
transactionsroot - The root of the transaction trie of the block.
stateroot - The root of the final state trie of the block.
receiptsroot - The root of the receipts trie of the block.
miner - The address of the beneficiary to whom the mining rewards were given.
difficulty - Integer of the difficulty for this block encoded as a hexadecimal string.
totaldifficulty - Integer of the total difficulty of the chain until this block encoded as a hexadecimal string.
extradata - The “extra data” field of this block.
size - The size of this block in bytes as an Integer value encoded as hexadecimal.
gaslimit - The maximum gas allowed in this block encoded as a hexadecimal string.
gasused - The total used gas by all transactions in this block encoded as a hexadecimal string.
timestamp - The unix timestamp for when the block was collated.
transactions - Array of transaction objects - please see eth_getTransactionByHash for exact shape.
uncles - Array of uncle hashes.
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
```


---

# eth_getBlockByNumber - Optimism


eth_getBlockByNumber - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
Parameters
QUANTITY|TAG - integer of a block number, or the string "earliest", "latest" or "pending", as in the default block parameter.
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0x1b4', 
    true
]
Returns
See eth_getBlockByHash
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
```
params: [
    '0x1b4', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
```


---

# eth_getProof - Optimism


eth_getProof - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof on Optimism. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBlockReceipts - Optimism


eth_getBlockReceipts - Optimism
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Optimism.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
opt-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_subscribe


eth_subscribe
Subscribe to different Optimism event types like newHeads, logs, and syncing using WebSockets.
Creates a new subscription for desired events. Sends data as soon as it occurs.
Parameters
Event types- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
Optional params - optional parameters to include to describe the type of event to listen to (ex: address)
Returns
While the subscription is active, you will receive events formatted as an object described below:
Event Object:
jsonrpc: Always "2.0"
method: Always "eth_subscription"
params: An object with the following fields:
subscription: The subscription ID returned by the eth_subscribe call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe
result: An object whose contents vary depending on the event type.
Event types
The following event types are accepted in all eth_subscribe WebSocket requests through your Alchemy endpoint. You can view the individual docs for example requests and responses.
Subscription Type Description
alchemy_minedTransactions Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags.
newHeads Emits new blocks that are added to the blockchain.
[logs][ref:logs] Emits logs attached to a new block that match certain topic filters.
Request
wscat
alchemy-sdk
// initiate websocket stream first
wscat -c wss://opt-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
Result
results
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
WebSocket Limits
There is a limit of 20,000 WebSocket connections per API Key as well as 1,000 parallel WebSocket subscriptions per WebSocket connection, creating a maximum of 20 million subscriptions per application.
The maximum size of a JSON-RPC batch request that can be sent over a WebSocket connection is 20
Free tier users will be limited to 10 concurrent requests per WebSocket connection.
TABLE OF CONTENTS
Parameters
Returns
Event types
Request
Result
WebSocket Limits
```
// initiate websocket stream first
wscat -c wss://opt-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
```


```
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
```


| Subscription Type | Description |
| --- | --- |
| alchemy_minedTransactions | Emits full transaction objects or hashes that are mined on the network based on provided filters and block tags. |
| newHeads | Emits new blocks that are added to the blockchain. |
| [logs][ref:logs] | Emits logs attached to a new block that match certain topic filters. |


---

# eth_unsubscribe


eth_unsubscribe
Unsubscribe from different Optimism event types with a regular RPC call with eth_unsubscribe as the method and the subscriptionId as the first parameter. It returns a bool indicating if the subscription was canceled successfully.
Parameters
Subscription ID, as previously returned from an eth_subscribe call.
Returns
true if a subscription was successfully canceled, or false if no subscription existed with the given ID.
Example
Request
wscat
alchemy-sdk
wscat -c wss://opt-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
Result
JSON
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
TABLE OF CONTENTS
Parameters
Returns
Example
Request
Result
```
wscat -c wss://opt-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```


```
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```


---

# eth_accounts - Base


eth_accounts - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - Base


eth_blockNumber - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - Base


eth_call - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_chainId - Base


eth_chainId - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - Base


eth_estimateGas - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
📘
Note
The estimate may be significantly more than the amount of gas actually used by the transaction, for a variety of reasons including EVM mechanics and node performance. Estimates are served directly from nodes, we're not doing anything special to the value so the rest of the network is likely seeing the same.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address to which the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million Gwei per request. Reach out to us at support@alchemy.com if you want to increase this limit.
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending", see the default block parameter.
🚧
Note
eth_estimateGas will check the balance of the sender (to make sure that the sender has enough gas to complete the request). This means that even though the call doesn't consume any gas, the from address must have enough gas to execute the transaction.
If no gas is specified geth uses the block gas limit from the pending block as an upper bound. As a result, the returned estimate might not be enough to execute the call/transaction when the amount of actual gas needed is higher than the pending block gas limit.
Returns
QUANTITY - the amount of gas used.
Example
Request
alchemyweb3.js
ethers.js
web3.py
cURL
Postman
SDK
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
Result
JavaScript
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
🚧
The below parameter inputs do not work, please reference the section above instead.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
// Installation instructions: https://github.com/alchemyplatform/alchemy-web3

async function main() {
 // alchemy-token-api/alchemy-web3-script.js
 import { createAlchemyWeb3 } from "@alch/alchemy-web3";
 
 // Replace with your Alchemy API key:
 const apiKey = "demo";
 
 // Initialize an alchemy-web3 instance:
 const web3 = createAlchemyWeb3(
   `https://eth-mainnet.g.alchemy.com/v2/${apiKey}`,);
 
 // Query the blockchain (replace example parameters)
     const estGas = await web3.eth.estimateGas({
     from: "0xge61df",
     to: "0x087a5c",
     data: "0xa9059c",
     gasPrice: "0xa994f8",
   }) 

 // Print the output to console
   console.log(estGas);
   }

main();
```


```
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```


---

# eth_feeHistory - Base


eth_feeHistory - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a collection of historical gas information.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_gasPrice - Base


eth_gasPrice - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBalance - Base


eth_getBalance - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - Base


eth_getBlockByHash - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByNumber - Base


eth_getBlockByNumber - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByHash - Base


eth_getBlockTransactionCountByHash - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Base


eth_getBlockTransactionCountByNumber - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Base


eth_getCode - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - Base


eth_getFilterChanges - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Base


eth_getFilterLogs - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Base


eth_getLogs - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getProof - Base


eth_getProof - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof on Base. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getStorageAt - Base


eth_getStorageAt - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Base


eth_getTransactionByBlockHashAndIndex - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - Base


eth_getTransactionByBlockNumberAndIndex - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Base


eth_getTransactionByHash - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Base


eth_getTransactionCount - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Base


eth_getTransactionReceipt - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - Base


eth_getUncleByBlockHashAndIndex - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Base


eth_getUncleByBlockNumberAndIndex - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - Base


eth_getUncleCountByBlockHash - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - Base


eth_getUncleCountByBlockNumber - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_maxPriorityFeePerGas - Base


eth_maxPriorityFeePerGas - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a fee per gas that is an estimate of how much you can pay as a priority fee, or 'tip', to get a transaction included in the current block.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Base


eth_newBlockFilter - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Base


eth_newFilter - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - Base


eth_newPendingTransactionFilter - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_protocolVersion - Base


eth_protocolVersion - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current ethereum protocol version.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Base


eth_sendRawTransaction - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_syncing - Base


eth_syncing - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Base


eth_uninstallFilter - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockReceipts - Base


eth_getBlockReceipts - Base
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Base.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
base-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_accounts - Astar


eth_accounts - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - Astar


eth_getTransactionReceipt - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_maxPriorityFeePerGas - Astar


eth_maxPriorityFeePerGas - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns a fee per gas that is an estimate of how much you can pay as a priority fee, or 'tip', to get a transaction included in the current block.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - Astar


eth_blockNumber - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
---

# eth_call - Astar


eth_call - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
Don’t have an API key?
Start using this API in your app today.
Get started for free
This is one of the most commonly used API calls. It is used to read from the blockchain which includes executing smart contracts but does not publish anything to the blockchain. This call does not consume any Ether.
We can call any function of a smart contract using the eth_call method and it returns us any data that the function returns (in hex format). For read-only functions, it returns what the read-only function returns. For functions that change the state of the contract, it executes that transaction locally and returns any data returned by the function.
Calling the read-only function is a common use case because all read-only functions return something that we can read using this method.
Use cases for eth_call
eth_call is used to call read-only functions of a smart contract. For example, calling the balanceOf function of an ERC20 token contract.
How to Get ERC-20 Token Balance at a Given Block
How to decode an eth_call response
🚧
Starting from Geth 1.9.13, eth_callwill check the balance of the sender (to make sure that the sender has enough gas to complete the request) before executing the call when one of the following conditions is true:
the gas_price parameter is populated, or
the contract function being called (i.e. in data modifies blockchain state)\
In these two cases, even though the eth_call requests don't consume any gas, the from address must have enough gas to execute the call as if it were a write transaction because eth_call is being used to simulate the transaction.
Parameters
Object - The transaction call object
from: DATA, 20 Bytes - (optional) The address the transaction is sent from.
to: DATA, 20 Bytes - The address the transaction is directed to.
gas: QUANTITY - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions. NOTE: this parameter has a cap of 550 million gas per request. Reach out to us at support@alchemy.com if you want to increase this limit!
gasPrice: QUANTITY - (optional) Integer of the gasPrice used for each paid gas.
value: QUANTITY - (optional) Integer of the value sent with this transaction
data: DATA - (optional) Hash of the method signature and encoded parameters. For details see Ethereum Contract ABI
QUANTITY|TAG - integer block number, or the string "latest", "earliest" or "pending" (see the default block parameter), OR the blockHash (in accordance with EIP-1898) NOTE: the parameter is an object instead of a string and should be specified as: {"blockHash": "0x<some-hash>"}. Learn more here.
Object - State override set
The State Override Set option allows you to change the state of a contract before executing the call. This means you can modify the values of variables stored in the contract, such as balances and approvals for that call without actually modifying the contract on the blockchain.
ㅤ
In more technical terms, the state override set is an optional parameter that allows executing the call against a modified chain state. It is an address-to-state mapping, where each entry specifies some state to be overridden prior to executing the call. Each address maps to an object containing:
FIELD TYPE BYTES DESCRIPTION
balance Quantity <32 Fake balance to set for the account before executing the call.
nonce Quantity <8 Fake nonce to set for the account before executing the call.
code Binary any Fake EVM bytecode to inject into the account before executing the call.
state Object any Fake key-value mapping to override all slots in the account storage before executing the call.
stateDiff Object any Fake key-value mapping to override individual slots in the account storage before executing the call.
Override Example:
Here's a simple code snippet in JavaScript that shows how you can use the State Override Set to mock an approval for a token transfer:
Override Example
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
Code Explanation:
We first import the ethers.js library, which provides a convenient set of tools for working with EVM chains.
Next, we define the address of the DAI token contract and the addresses of the sender and recipient.
We then calculate the index for the allowance mapping in the token contract. This involves using the solidityKeccak256 function from the ethers.js library to calculate a unique identifier for the mapping based on the sender and recipient addresses.
The stateDiff object is created to mock an approval, which is done by setting the state of the index in the allowance mapping to the maximum possible value (ethers.constants.MaxUint256).
An instance of the Ethereum provider is created. This provider will be used to make calls to the Ethereum network.
The callParams constant is created that specifies the parameters for the eth_call method.
The contract method is called without state overrides and the result is stored in the call1 constant.
The contract method is called with state overrides and the result is stored in the call2 constant.
The results of both calls are logged to the console.
The State Override option is mainly used for testing purposes, as it allows developers to temporarily modify the state of the chain to simulate specific scenarios and test the behavior of smart contracts.
❗️
Note
eth_call has a timeout restriction at the node level. Batching multiple eth_call together on-chain using pre-deployed smart contracts might result in unexpected timeouts that cause none of your calls to complete. Instead, consider serializing these calls, or using smaller batches if they fail with a node error code.
JavaScript
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
Returns
DATA - the return value of the executed contract.
Example
Request
SDK
ethers.js
web3.py
cURL
Postman
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
LANGUAGE
Shell
JavaScript
Python
```
// Import the ethers.js library
const ethers = require("ethers");

// The address of the DAI token contract
const dai = "0x6b175474e89094c44da98b954eedeac495271d0f";

// The address of the sender
const fromAddr = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe";

// The address of the recipient
const toAddr = "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5";

// The allowance slot on the DAI contract (this may differ from contract to contract)
const slot = 3; 

// Use the solidityKeccak256 function from the ethers.js library to calculate the index for the allowance mapping
const temp = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [fromAddr, slot]
);
const index = ethers.utils.solidityKeccak256(
  ["uint256", "uint256"],
  [toAddr, temp]
);

// The stateDiff object to mock an approval
const stateDiff = {
  [dai]: {
    stateDiff: {
      [index]: ethers.constants.MaxUint256.toHexString(), // setting the allowance to the max value of uint256
    },
  },
};

// Create an instance of the Ethereum provider
const provider = new ethers.providers.JsonRpcProvider("Your-Alchemy-API-URL");

// The parameters for the eth_call method
const callParams = [
  {
    to: dai,
    data: "0xdd62ed3e..." // The method signature and arguments for the call
  },
  "latest"
];

// Call the contract method without state overrides
const call1 = await provider.send("eth_call", callParams);

// Call the contract method with state overrides
const call2 = await provider.send("eth_call", [...callParams, stateDiff]);

// Log the results of both calls
console.log(call1); 
console.log(call2);
```


```
params: [
    {
        "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
        "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
        "gas": "0x76c0",
        "gasPrice": "0x9184e72a000",
        "value": "0x9184e72a",
        "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    }, 
    "latest"
]
```


```
// Setup: npm install alchemy-sdk
// Github: https://github.com/alchemyplatform/alchemy-sdk-js
import { Network, Alchemy } from "alchemy-sdk";

// Optional config object, but defaults to demo api-key and eth-mainnet.
const settings = {
  apiKey: "demo", // Replace with your Alchemy API Key.
  network: Network.ETH_MAINNET, // Replace with your network.
};
const alchemy = new Alchemy(settings);

// Make a sample eth_call
alchemy.core
  .call({
    to: "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    gas: "0x76c0",
    gasPrice: "0x9184e72a000",
    data: "0x3b3b57debf074faa138b72c65adbdcfb329847e4f2c04bde7f7dd7fcad5a52d2f395a558",
  })
  .then(console.log);
```


```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x"
}
```


| FIELD | TYPE | BYTES | DESCRIPTION |
| --- | --- | --- | --- |
| balance | Quantity | <32 | Fake balance to set for the account before executing the call. |
| nonce | Quantity | <8 | Fake nonce to set for the account before executing the call. |
| code | Binary | any | Fake EVM bytecode to inject into the account before executing the call. |
| state | Object | any | Fake key-value mapping to override all slots in the account storage before executing the call. |
| stateDiff | Object | any | Fake key-value mapping to override individual slots in the account storage before executing the call. |


---

# eth_chainId - Astar


eth_chainId - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_gasPrice - Astar


eth_gasPrice - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getBalance - Astar


eth_getBalance - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
📘
Note
eth_getBalance only returns the balance of the native chain currency (ex: ETH for Ethereum or Matic for Polygon) and does not include any ERC20 token balances for the given address.
To get ERC20 token balances, please use alchemy_getTokenBalances.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - Astar


eth_getBlockByHash - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
Parameters
Hash - Hash of the block
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
Returns
object - A block object, or null when no block was found. The returned object has the following properties:
number - The block number of the requested block encoded as a hexadecimal string. null if pending.
hash - The block hash of the requested block. null if pending.
parenthash - Hash of the parent block.
nonce - Hash of the generated proof-of-work. null if pending.
sha3uncles - SHA3 of the uncles data in the block.
logsbloom - The bloom filter for the logs of the block. null if pending.
transactionsroot - The root of the transaction trie of the block.
stateroot - The root of the final state trie of the block.
receiptsroot - The root of the receipts trie of the block.
miner - The address of the beneficiary to whom the mining rewards were given.
difficulty - Integer of the difficulty for this block encoded as a hexadecimal string.
totaldifficulty - Integer of the total difficulty of the chain until this block encoded as a hexadecimal string.
extradata - The “extra data” field of this block.
size - The size of this block in bytes as an Integer value encoded as hexadecimal.
gaslimit - The maximum gas allowed in this block encoded as a hexadecimal string.
gasused - The total used gas by all transactions in this block encoded as a hexadecimal string.
timestamp - The unix timestamp for when the block was collated.
transactions - Array of transaction objects - please see eth_getTransactionByHash for exact shape.
uncles - Array of uncle hashes.
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
```
params: [
    '0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
--data '{"method":"eth_getBlockByHash","params":["0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",false],"id":1,"jsonrpc":"2.0"}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0xf8e3d7",
    "hash": "0xe76d777791f48b5995d20789183514f4aa8bbf09e357383e9a44fae025c6c50a",
    "transactions": [
      "0x501251dd9097bcba3074c7e699be2bc28a343228e321251342188a34e9e54871",
      "0x1e4009ac7b59a0a64fe3f42918185a160ce22ad666215fa182ea1d927a8e1a22",
      "0xa04bdde31cba595dbb6749b4b2f4c712119d1f40c94c402592c2922416dd08a1",
      "0xdc23dd5f6c6ba68d6e73227b5dda9ddd5168beb829fdc3b432ae5d1755022c3b",
      "0x67c6d7216f8a7acce412dcdecea36bc983e040d16f9a594f4f89d785d9b960a3",
      "0x457f0eaf34ac47ded9064b34c8b9277c13eb6bbf1486372f8d021c52cf9f3e0d",
      "0x96fdb2d418087efd71eed95e93c5f298dd497de02c17645932e8937bdb549c8e",
      "0xffe5c80b63f32de4f4f45574eef78c150d6cd175d737686b6fc1b986e62fb6ca",
      "0x8835b74a99a4c3fe85d9f279c218b4d0cca2cee98b036e4b9d8586b6cc9618be",
      "0x05c01c306cffb2ecc9253a8aad1684e91951f0c8fcf1c50a5fe646f6d370ecdb",
      "0x6d619935cf8d20d8815cc428a13cee5fb07516f9f969e9232065e18c533fca4e",
      "0x0cb567356701cd3fcfbabe2b94d3558b9f4ec05e993f94f60f71df3225f52bf2",
      "0xd5fe8a26d9ba05b5f1acc0f897d925d1347477d76e338b6de26d5376f1a6d5fd",
      "0x964c91eda0e40c47f876968088c5a15f76a04d0e407d195a017c16bc184f7b32",
      "0x3d98f1ab95b0392e7937692da71cd3a78e564c03f02441079ffcff0f4ea66596",
      "0x91879b45d4be904960aa4a306ab69ef1093e1dbbf1629cdac64b9dcec84c8563",
      "0x984e3d3aefd00ef6d80e904a67aa7ad5be9f360fae67134ab62bd7ad22d39b45",
      "0x2217d2980b61f4f9fc261b2b1aa9204f488f2380e617c2ff9e91ee017bdc8338",
      "0x753612ae9ea6b78ffde78d02b900f45162b64daeebac77365fce2eefb3010712",
      "0xf3d63f3fbe39fe299df53e4f79f6563f88240baa4b2c03f7fb5afadb2d1ea7b2",
      "0x34065fc0f0d0348a7682179f45ca99bb3ada4443b6e8b518fb6981de64d8dcae",
      "0x44980c7a6e5b741d0104ac469a2600352fe112347ae0af6b046d434877e63ff6",
      "0x81fe70a281f453cb3dfd6772c5c95bd3bf887d4df9d4fd65040b2dae161a790a",
      "0xba1894fd141b711fab3cbdf39d9f37f99e56ec156f4cb7009d7e91c29add88fd",
      "0x6638f7136b2a0049deae40173d2e30b0ec0458572060bf4e0fbbbac93f2f9eeb",
      "0x473d73e7733ff48a75c4f5e46e0775fabd6c071c65b7b695fc06c3944e2c133d",
      "0x2e7c3eb520250471cfd1fe78a42358f361ce10bbea779491a74e94a819338835",
      "0xb71509c9e40700024080db1ae47d0758602e7945e81d062720975d9af8f324b8",
      "0x291da6e412f4089e975863a549feb94afffd690367fcbf05a3d684d492fde084",
      "0x0068510c2323c93f02297e14208cd6afdb961c4f038b487fb5c3d305bbd7269e",
      "0xcde26d0a20a4bd5f8dd1f0b04c6853db7e565bfcfb3eafa3969a7f68fd31630e",
      "0x85ae5f147cee6e69cff58696934dc679a92f37824147041855fe1c8ad4ac56d1",
      "0xf09bce5b2fcdc138eda773a8fff72e74e7f4532a9032ecb5e8ce64fab19c96c4",
      "0xfb05e26b190200b65d5968f0c89912a93856fa65b4f17a0b71cca17a8f4c22e4",
      "0x5aa199dc76f005326fa65fe4613439febd3e3c139ba088c13681abee5196fca8",
      "0x8078b675486a3869f15d4c310d54b12e38fee5a6c5bb157fed87ec66d48f0191",
      "0xa5ef1aaba1eb538760acfbd112af97834ad91dd4375d044278817cdd2bb46ae6",
      "0x2a9b9393d163278644cfd60fd5d74a6e2fff9ce633048408494d9e7ad1d83cd6",
      "0xc7ae40a9f4204fa8bf6e5bfc961d088fd232c9ff34a329588c9f27cd8acaa271",
      "0xd4dc61819dc3cd5bb15215e13bfb92ebad94328fb24080e6a903c7e3c12b0574",
      "0xd9fa7d1960d8f7cf8fdaf7f53931f8feb5313a4173459272dba61934129e2787",
      "0xbfc3285f4c7158eb87eebfae5ca1bbc09bccfb8fa5ae2f453ffbf1ecd3876bb0",
      "0xe4bb733e809419c55ac54036bd4891c35f85b57183942a18f4ba0c1f635116e3",
      "0x3d8caefc50b9f978febb0083cf922993724c3cf73d4411664e65e202d496ee3e",
      "0x86244c4f0a6a69179c1f4631431248f3b758e1be1bdf5f6eaebc932896b95d9c",
      "0x99c1f2edb22e9f03ac45a67dda3200e85de62301b4eb7804bb0d9fca14726a30",
      "0xda998bfd6e231cc13b0749dcd5ee62f8592a1e82adb5ca795b9d6c94f40f9215",
      "0x96611cf04740f7e4cc662010e971968a74d237b8bb0e33c2c0ae8e4bb23ed98e",
      "0x2825bea80bb91d00d0a52e48aa4880c2a1a862f811713625b865fffa7b614c94",
      "0x0f7813db691d55228df91999b43dd7872adbc77e9d1480c78b84530aa7b84c82",
      "0x1d99a6104c9f96663ae286f4cc3fd07196fe722007048b9bd081443d32b20cd1",
      "0xd86fc2f8a3ec3dbf650c78e0915820ac920b199f977f3fd28116deb057017c69",
      "0x3ecb08f0aa2d9b22c36dc7715041cbf0b21c5cb943dde28c7406c3e9365bdd9a",
      "0xda589822e8da50bd4a3524efd66f92cf6a523d12c4c208c5247d8b667a06cb59",
      "0x0e38230dbb0cc421f57a798e6eaef18e3c9ea921f6041817ce0e1a40c54df9bb",
      "0x847209fc78834106ae095d1b8fc8a4794740fcfb0b52e29df6dba8a914ef4879",
      "0x52555075e33f1a4fe8fd3ee0fb35218fc33804d0aeb048ced4b63a83f10d4cf6",
      "0xe32a6e4a2547d6761c333bc2dc768eb5d22861beb32f1faee345c7ac07312132",
      "0xc06306cc8f28f1240f60c4af102d0cd591e32055fb3d95ae13742a103e975237",
      "0xb7cc2299dadbdf0bfa4b5951aeb57e21d9e699969540790db4186f3c8ff34713",
      "0x51252c6b4a33a8abc320861c8b31cf6c682be159a7688071c5a1b1845ea2d131",
      "0xeacda7af240a974f9e2dccb95be89f3aebaf7d7546734045d5749d78dce86e3d",
      "0xec79149b4c959cf1a073fb6fde78da92a84dfce63cb122069867cbaf14203bc0",
      "0x2d28f71f84955c7ab081469ea52cba0e4140c7ca1a84283a468a2181a59668df",
      "0x4be52f902c3e1760d74149b66804f690518fbfa1fd9477af031e0ff4a8e1e92a",
      "0x76a73093ad523a6bd8e5a05372bbbb5ca335284ddb9a02bce1a4b9451e89f515",
      "0x4caf333ad965bb9e6863cd88609869b7b781188745206f9441ef98f68fa4a736",
      "0x31aec7231e2f5ea7509bda9fec1edbfbb37e36fc4e1f650e07192bfc7fb58183",
      "0x3cbb550b047f1685cabe67d2401b0693c826200126bc5043dc4d3d1126d862f1",
      "0x3f63a806ad40f85471381976b09823fd5dea26ee80c28d562be12518880f054a",
      "0x0a0e7d17d6f87b12b9a4d46239320eaa50ad90facd994a779904ac3c888e5de8",
      "0x5d37ba0da5eff8cd00de97b06ecf3da17a6076ddaa644ea701071008152c148d",
      "0x217e6f62317d9355048bfb67488618bf626c8ab0765c0d71b3e56e431851c7e5",
      "0x79c4dd1fe23ed52b40cb303bcf2d5d840da1faeb7b58d31d4ff403b5f7695e95",
      "0x9ffdf32a79a404983125f3f8333f43cc72fa6a87fe2ffd6d288b910df036787a",
      "0x07484072182d16c9b10c92f53a889883d5c5134f76afed9f66f3e599bab4b802",
      "0xce29ba3c39b8ee50f27c421fe8660d30cf4da08ba9dab79951a1e02a866d2b27",
      "0x34a32e8f9b25b0f52e10fdf850a481e0c3d9830b1cff31d3599411b23252834a",
      "0xeb4dd580dda01cf018fa967e32dd3e60c23e4fed465fdc8216b38bade828963d",
      "0x2aff5890d2e31e64f09f02b245bd3b545373e54bd429b8636ca339df745f4712",
      "0x6419ee8534eddd330e3853c3304eb6a9b2692957c0f58070c97bd12f6603dd40",
      "0x4a480419b3e23ea287022c9561273ef1784d4e36535af6be85e5a2c3acdf807d",
      "0xae02a6b666f763e3918ded3519f9128c5c69e93558d3111c8055a5adef3af714",
      "0xc0d079d0efb570fb48d87526a768d4204aeffd0f0e5b236a49a028e973afd60c",
      "0x3bb88a0c838d23a5ea9fa44989980200f8d5591d3215d0a3a4861bd79ea9c3b0",
      "0x3477a50f3acd568bbf028a0b7f751dbfe6e8ad79c39c6e226596744257f331b1",
      "0x61d08f9f2d34a0329d530c4aafdef73c3b4419211a394d36bf9c14de1e0f07d0",
      "0x3281da562e8f332d69aeb8660900bd3302a2e62a85414bc1e7bba7dd6b0150c8",
      "0xa931886fdec0d55851ccd02af9c24da73894e2e27a6d73bd975489090fd9dac7",
      "0x1d67661a9a3e749796a4c01f76a8d8eef05d06e1fcbc629adf4bd867bafb8823",
      "0x53fdc5f70a57700a75762659e99a7c911db219b484d3f198ed16b7b370b4c14c",
      "0x8fe769d0133f799fbfce3a1f03bb197f1e979b598be0df258ecd594af8644832",
      "0xa57337b3b79c7c662425860ae5c5a49dbeef9d67aab8043f6fc3c4e2eb3ebfd5",
      "0xcdc7a687f8a8f68ca71ee95fece932bc294064b2d6d291c78df8f7a6e07ef103"
    ],
    "difficulty": "0x0",
    "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
    "gasLimit": "0x1c9c380",
    "gasUsed": "0x1699c83",
    "logsBloom": "0x1c243c7f96541e048c0cc481b0ac333461c12804d880990dfe1980c41c2a49aca538425bc4030022419e3fe80ce6a1819e0c8cbccaec3511034bc7c75a6424b148b3809049eb1a8b6a088bc9629304fa84666835856e23084c00b81191002810d6710c00834290e38544008cba206a7bf4891881609a144000d000b00c896c90b21805320683810d20c90c0810064069f4001911c10a0409400c615e0a34316d8b29c9d4298d7b191a6819811f118c01801021715096405280cbaa4326b1460ca46c66432390d05001c0341a2c82305750c027f4d2ae10971254a94321a9f2132090a00e1f0110b18567920180818fc6b1100e8af2e84040a0408c144015d213",
    "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
    "mixHash": "0xe8ad228f6a0f7c79bd2f8273f717a06f47b271f41d748718699bb966f710fc9b",
    "nonce": "0x0000000000000000",
    "parentHash": "0xbef5b480684b03c0c3ff58deec762cf6650de5b71da431e85d908cca221a10b2",
    "receiptsRoot": "0xce65ddb737ae93370c63077c742ba190d917fbe0876a9a1f9d793d5b125fa04a",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x9684",
    "stateRoot": "0xc57cf792e5cdff63c582e03084a7d21748196f1c6a97171d2b4e07417fa5df2e",
    "timestamp": "0x63b15d3b",
    "totalDifficulty": "0xc70d815d562d3cfa955",
    "transactionsRoot": "0x0cf6abfa0c1f1f8e031dad7a314c5b130099dcf340d39d840accc778cb623f64",
    "uncles": [],
    "baseFeePerGas": "0x2f99b1dd0"
  }
}
```


---

# eth_getBlockByNumber - Astar


eth_getBlockByNumber - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
Parameters
QUANTITY|TAG - integer of a block number, or the string "earliest", "latest" or "pending", as in the default block parameter.
Boolean - If true it returns the full transaction objects, if false only the hashes of the transactions.
JavaScript
params: [
    '0x1b4', 
    true
]
Returns
See eth_getBlockByHash
Request
cURL
Postman
SDK
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
Result
JavaScript
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
📘
NOTE
You can test out this method live from your browser using our composer tool.
LANGUAGE
Shell
JavaScript
Python
```
params: [
    '0x1b4', 
    true
]
```


```
curl https://eth-mainnet.g.alchemy.com/v2/${apiKey} \
-X POST \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":0}'
```


```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "number": "0x1b4",
    "difficulty": "0x4ea3f27bc",
    "extraData": "0x476574682f4c5649562f76312e302e302f6c696e75782f676f312e342e32",
    "gasLimit": "0x1388",
    "gasUsed": "0x0",
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "miner": "0xbb7b8287f3f0a933474a79eae42cbca977791171",
    "mixHash": "0x4fffe9ae21f1c9e15207b1f472d5bbdd68c9595d461666602f2be20daf5e7843",
    "nonce": "0x689056015818adbe",
    "parentHash": "0xe99e022112df268087ea7eafaf4790497fd21dbeeb6bd7a1721df161a6657a54",
    "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x220",
    "stateRoot": "0xddc8b0234c2e0cad087c8b389aa7ef01f7d79b2570bccb77ce48648aa61c904d",
    "timestamp": "0x55ba467c",
    "totalDifficulty": "0x78ed983323d",
    "transactions": [],
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "uncles": []
  }
}
```


---

# eth_getBlockTransactionCountByHash - Astar


eth_getBlockTransactionCountByHash - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - Astar


eth_getBlockTransactionCountByNumber - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - Astar


eth_getCode - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getStorageAt - Astar


eth_getStorageAt - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - Astar


eth_getTransactionByBlockHashAndIndex - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - Astar


eth_getTransactionByBlockNumberAndIndex - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - Astar


eth_getTransactionByHash - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - Astar


eth_getTransactionCount - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - Astar


eth_getUncleByBlockNumberAndIndex - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - Astar


eth_sendRawTransaction - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - Astar


eth_getLogs - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getFilterChanges - Astar


eth_getFilterChanges - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - Astar


eth_getFilterLogs - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - Astar


eth_newFilter - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - Astar


eth_newPendingTransactionFilter - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - Astar


eth_uninstallFilter - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - Astar


eth_newBlockFilter - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - Astar


eth_estimateGas - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getBlockReceipts - Astar


eth_getBlockReceipts - Astar
POST
https://astar-mainnet.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on Astar.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_subscribe


eth_subscribe
Subscribe to different Astar event types like newHeads, logs using WebSockets.
Creates a new subscription for desired events. Sends data as soon as it occurs.
Parameters
Event types- specifies the type of event to listen to (ex: new pending transactions, logs, etc.)
Optional params - optional parameters to include to describe the type of event to listen to (ex: address)
Returns
While the subscription is active, you will receive events formatted as an object described below:
Event Object:
jsonrpc: Always "2.0"
method: Always "eth_subscription"
params: An object with the following fields:
subscription: The subscription ID returned by the eth_subscribe call which created this subscription. This ID will be attached to all received events and can also be used to cancel the subscription using eth_unsubscribe
result: An object whose contents vary depending on the event type.
Event types
The following event types are accepted in all eth_subscribe WebSocket requests through your Alchemy endpoint. You can view the individual docs for example requests and responses.
Subscription Type Description
newHeads Emits new blocks that are added to the blockchain.
(logs)[ref:logs] Emits logs attached to a new block that match certain topic filters.
Request
wscat
alchemy-sdk
// initiate websocket stream first
wscat -c wss://astar-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
Result
results
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
WebSocket Limits
There is a limit of 20,000 WebSocket connections per API Key as well as 1,000 parallel WebSocket subscriptions per WebSocket connection, creating a maximum of 20 million subscriptions per application.
The maximum size of a JSON-RPC batch request that can be sent over a WebSocket connection is 20
Free tier users will be limited to 10 concurrent requests per WebSocket connection.
TABLE OF CONTENTS
Parameters
Returns
Event types
Request
Result
WebSocket Limits
```
// initiate websocket stream first
wscat -c wss://astar-mainnet.g.alchemy.com/v2/demo

// no param specification - return all mined txs  
{"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_minedTransactions"]}
```


```
{"id":1,"result":"0xf13f7073ddef66a8c1b0c9c9f0e543c3","jsonrpc":"2.0"}

// hashesOnly = true
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}


// hashesOnly = false
{
  "jsonrpc": "2.0",
  "method": "eth_subscription",
  "params": {
    "result": {
   "removed": false
   "transaction": {
       "blockHash":"0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43",
    "blockNumber":"0x5b8d80",
    "hash":"0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",
    "from":"0x2a9847093ad514639e8cdec960b5e51686960291",
    "gas":"0x4f588",
    "gasPrice":"0xc22a75840",
    "input":"0x000101d521928b4146",
    "nonce":"0x9a2",
    "r":"0xb5889c55a0ebbf86627524affc9c4fdedc4608bee7a0f9880b5ec965d58e4264",
    "s":"0x2da32e817e2483ec2199ec0121b93384ac820049a75e11b40d152fc7558a5d72",
    "to":"0xc7ed8919c70dd8ccf1a57c0ed75b25ceb2dd22d1",
    "transactionIndex":"0x14",
    "type":"0x0",
    "v":"0x1c",
    "value":"0x0"
   }
    },
    "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
  }
}
```


| Subscription Type | Description |
| --- | --- |
| newHeads | Emits new blocks that are added to the blockchain. |
| (logs)[ref:logs] | Emits logs attached to a new block that match certain topic filters. |


---

# eth_unsubscribe


eth_unsubscribe
Unsubscribe from different Astar event types with a regular RPC call with eth_unsubscribe as the method and the subscriptionId as the first parameter. It returns a bool indicating if the subscription was canceled successfully.
Parameters
Subscription ID, as previously returned from an eth_subscribe call.
Returns
true if a subscription was successfully canceled, or false if no subscription existed with the given ID.
Example
Request
wscat
alchemy-sdk
wscat -c wss://astar-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
Result
JSON
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
TABLE OF CONTENTS
Parameters
Returns
Example
Request
Result
```
wscat -c wss://astar-mainnet.g.alchemy.com/v2/your-api-key

{"jsonrpc":"2.0", "id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```


```
{
    "jsonrpc":"2.0",
    "id":1,
    "result":true
}
```


---

# eth_accounts - zkSync


eth_accounts - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a list of addresses owned by client. Since Alchemy does not store keys, this will always return empty.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - zkSync


eth_blockNumber - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - zkSync


eth_call - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_chainId - zkSync


eth_chainId - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_createAccessList - zkSync


eth_createAccessList - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Ethereum API - Creates an EIP2930 type accessList based on a given Transaction object. Returns list of addresses and storage keys that are read and written by the transaction (except the sender account and precompiles), plus the estimated gas consumed when the access list is added.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - zkSync


eth_estimateGas - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_feeHistory - zkSync


eth_feeHistory - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns a collection of historical gas information.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_gasPrice - zkSync


eth_gasPrice - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBalance - zkSync


eth_getBalance - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - zkSync


eth_getBlockByHash - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBlockByNumber - zkSync


eth_getBlockByNumber - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getBlockTransactionCountByHash - zkSync


eth_getBlockTransactionCountByHash - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - zkSync


eth_getBlockTransactionCountByNumber - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - zkSync


eth_getCode - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterChanges - zkSync


eth_getFilterChanges - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Polling method for a filter, which returns an array of logs which occurred since last poll.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getFilterLogs - zkSync


eth_getFilterLogs - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching filter with given id. Can compute the same results with an eth_getLogs call.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - zkSync


eth_getLogs - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getProof - zkSync


eth_getProof - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
---

# eth_getStorageAt - zkSync


eth_getStorageAt - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - zkSync


eth_getTransactionByBlockHashAndIndex - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - zkSync


eth_getTransactionByBlockNumberAndIndex - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - zkSync


eth_getTransactionByHash - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - zkSync


eth_getTransactionCount - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - zkSync


eth_getTransactionReceipt - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - zkSync


eth_getUncleByBlockHashAndIndex - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - zkSync


eth_getUncleByBlockNumberAndIndex - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - zkSync


eth_getUncleCountByBlockHash - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - zkSync


eth_getUncleCountByBlockNumber - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newBlockFilter - zkSync


eth_newBlockFilter - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when a new block arrives.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_newFilter - zkSync


eth_newFilter - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter object, based on filter options, to notify when the state changes (logs).
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` (Not available on Ethereum) - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_newPendingTransactionFilter - zkSync


eth_newPendingTransactionFilter - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a filter in the node, to notify when new pending transactions arrive. To check if the state has changed, call eth_getFilterChanges.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_protocolVersion - zkSync


eth_protocolVersion - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Returns the current ethereum protocol version.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - zkSync


eth_sendRawTransaction - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_uninstallFilter - zkSync


eth_uninstallFilter - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additionally, Filters timeout when they aren’t requested with eth_getFilterChangesfor a period of time.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockReceipts - zkSync


eth_getBlockReceipts - zkSync
POST
https://{network}.g.alchemy.com/v2/{apiKey}
Get all transaction receipts for a given block on zkSync.
LANGUAGE
Shell
Node
Ruby
PHP
Python
URL
Base URL
https://
zksync-mainnet
.g.alchemy.com/v2
/{apiKey}
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_blockNumber - BNB


eth_blockNumber - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of the most recent block.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_call - BNB


eth_call - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Executes a new message call immediately without creating a transaction on the block chain.
LANGUAGE
Shell
JavaScript
Python
---

# eth_chainId - BNB


eth_chainId - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the currently configured chain ID, a value used in replay-protected transaction signing as introduced by EIP-155.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_estimateGas - BNB


eth_estimateGas - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain.
LANGUAGE
Shell
JavaScript
Python
---

# eth_gasPrice - BNB


eth_gasPrice - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the current price per gas in wei.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getBalance - BNB


eth_getBalance - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the balance of the account of a given address.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockByHash - BNB


eth_getBlockByHash - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a block by block hash.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getBlockByNumber - BNB


eth_getBlockByNumber - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a block by block number.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getBlockTransactionCountByHash - BNB


eth_getBlockTransactionCountByHash - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getBlockTransactionCountByNumber - BNB


eth_getBlockTransactionCountByNumber - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getCode - BNB


eth_getCode - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns code at a given address.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getLogs - BNB


eth_getLogs - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns an array of all logs matching a given filter object.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


```
* `pending` - A sample next block built by the client on top of latest and containing the set of transactions usually taken from local mempool. Intuitively, you can think of these as blocks that have not been mined yet.
* `latest` - The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions.
* `safe` - The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is “unlikely” to be re-orged.
* `finalized` - The most recent crypto-economically secure block, that has been accepted by >2/3 of validators. Cannot be re-orged outside of manual intervention driven by community coordination. Intuitively, this block is very unlikely to be re-orged.
* `earliest` - The lowest numbered block the client has available. Intuitively, you can think of this as the first block created.
```


---

# eth_getProof - BNB


eth_getProof - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the account and storage values of the specified account including the Merkle-proof. This call can be used to verify that the data you are pulling from is not tampered with.
LANGUAGE
Shell
JavaScript
Python
---

# eth_getStorageAt - BNB


eth_getStorageAt - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the value from a storage position at a given address, or in other words, returns the state of the contract's storage, which may not be exposed via the contract's methods.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockHashAndIndex - BNB


eth_getTransactionByBlockHashAndIndex - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block hash and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByBlockNumberAndIndex - BNB


eth_getTransactionByBlockNumberAndIndex - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about a transaction by block number and transaction index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionByHash - BNB


eth_getTransactionByHash - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the information about a transaction requested by transaction hash. In the response object, blockHash, blockNumber, and transactionIndex are null when the transaction is pending.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionCount - BNB


eth_getTransactionCount - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of transactions sent from an address.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getTransactionReceipt - BNB


eth_getTransactionReceipt - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the receipt of a transaction by transaction hash.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockHashAndIndex - BNB


eth_getUncleByBlockHashAndIndex - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by hash and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleByBlockNumberAndIndex - BNB


eth_getUncleByBlockNumberAndIndex - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns information about an uncle of a block by number and uncle index position.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockHash - BNB


eth_getUncleCountByBlockHash - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block hash.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_getUncleCountByBlockNumber - BNB


eth_getUncleCountByBlockNumber - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Returns the number of uncles in a block matching the given block number.
LANGUAGE
Shell
Node
Ruby
PHP
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# eth_sendRawTransaction - BNB


eth_sendRawTransaction - BNB
POST
https://bnb-mainnet.g.alchemy.com/v2/{apiKey}
Creates a new message call transaction or a contract creation for signed transactions.
LANGUAGE
Shell
JavaScript
Python
RESPONSE
Click Try It! to start a request and see the response here!
---

# Sonic Chain API Quickstart


Sonic Chain API Quickstart
Get started building on Sonic and using the JSON-RPC API
To use the Sonic Chain API you'll need to create a free Alchemy account first!
Introduction
Sonic Chain is an EVM-compatible, high-performance, scalable, and secure layer-1 blockchain. With over 10,000 TPS, one-second confirmation times, and low-cost transactions, it provides a robust platform for decentralized applications (dApps) and Ethereum-based deployments.
What is the Sonic API?
The Sonic API allows interaction with the Sonic network through a set of JSON-RPC methods. Its design is familiar to developers who have worked with Ethereum's JSON-RPC APIs, making it intuitive and straightforward to use.
Getting Started Instructions
1. Choose a Package Manager (npm or yarn)
Select a package manager to manage your project's dependencies. Choose between npm and yarn based on your preference or project requirements.
npm yarn
Begin with npm by following the npm documentation. For yarn, refer to yarn's installation guide.
2. Set Up Your Project
Open your terminal and execute the following commands to create and initialize your project:
mkdir sonic-api-quickstart
cd sonic-api-quickstart
npm init --yes
mkdir sonic-api-quickstart
cd sonic-api-quickstart
yarn init --yes
This creates a new directory named sonic-api-quickstart and initializes a Node.js project within it.
3. Make Your First Request
Install Axios, a popular HTTP client, to make API requests:
Bash
npm install axios
# Or with yarn
# yarn add axios
Create an index.js file in your project directory and paste the following code:
JavaScript
const axios = require('axios');

const url = 'https://sonic-mainnet.g.alchemy.com/v2/${your-api-key}';

const payload = {
  jsonrpc: '2.0',
  id: 1,
  method: 'eth_blockNumber',
  params: []
};

axios.post(url, payload)
  .then(response => {
    console.log('Latest Block:', response.data.result);
  })
  .catch(error => {
    console.error(error);
  });
Remember to replace your-api-key with your actual Alchemy API key that you can get from your Alchemy dashboard.
4. Run Your Script
Execute your script to make a request to the Sonic mainnet:
Bash
node index.js
You should see the latest block information from Sonic's mainnet outputted to your console:
Latest Block: 0x...
Next Steps
Congratulations! You've made your first request to the Sonic network. You can now explore the various JSON-RPC methods available on Sonic and start building your dApps on this innovative platform.
TABLE OF CONTENTS
Introduction
What is the Sonic API?
Getting Started Instructions
1. Choose a Package Manager (npm or yarn)
2. Set Up Your Project
3. Make Your First Request
4. Run Your Script
Next Steps
```
mkdir sonic-api-quickstart
cd sonic-api-quickstart
npm init --yes
```


```
mkdir sonic-api-quickstart
cd sonic-api-quickstart
yarn init --yes
```


```
npm install axios
# Or with yarn
# yarn add axios
```


```
const axios = require('axios');

const url = 'https://sonic-mainnet.g.alchemy.com/v2/${your-api-key}';

const payload = {
  jsonrpc: '2.0',
  id: 1,
  method: 'eth_blockNumber',
  params: []
};

axios.post(url, payload)
  .then(response => {
    console.log('Latest Block:', response.data.result);
  })
  .catch(error => {
    console.error(error);
  });
```


```
node index.js
```


```
Latest Block: 0x...
```


| npm | yarn |
| --- | --- |
| Begin with npm by following the npm documentation. | For yarn, refer to yarn's installation guide. |


---

# Sonic Chain API FAQ


Sonic Chain API FAQ
Frequently asked questions about the Sonic Chain API
What is Sonic Chain?
Sonic Chain is a cutting-edge layer-1 blockchain platform offering high performance, scalability, and robust security. With transaction speeds exceeding 10,000 TPS and one-second confirmation times, it is purpose-built to support decentralized applications (dApps) and digital assets. It aims to provide fast transaction speeds, low costs, and high throughput, making it an attractive option for developers and users alike.
What is the Sonic Chain API?
The Sonic Chain API facilitates interaction with the Sonic Chain network through a collection of JSON-RPC methods. It provides developers with tools to interact with the blockchain, enabling functionalities such as transactions, smart contract deployment, and data retrieval.
How can I get started using the Sonic Chain API?
Explained in Sonic Chain API Quickstart.
Is Sonic Chain EVM compatible?
Yes, Sonic Chain is fully compatible with the Ethereum Virtual Machine (EVM). This compatibility allows Ethereum developers to port their projects to Sonic Chain with minimal changes, benefiting from the chain's high performance and low transaction fees.
What API does Sonic Chain use?
Sonic Chain uses the JSON-RPC API standard for blockchain interactions. This is the same standard used by Ethereum.
What is a Sonic Chain API key?
When accessing the Sonic Chain network via a node provider like Alchemy, developers use an API key to send transactions and retrieve data from the network.
For the best development experience, we recommend that you sign up for a free API key!
Which libraries support Sonic Chain?
Given Sonic Chain's EVM compatibility, popular Ethereum libraries like ethers.js and web3.js are fully compatible with Sonic Chain. This allows for seamless development and integration for those familiar with Ethereum's development ecosystem.
What programming languages work with Sonic Chain?
Similar to Ethereum, Sonic Chain supports a range of programming languages for blockchain interaction and smart contract development, including Solidity for smart contracts, as well as JavaScript and TypeScript for dApp development and off-chain interactions.
What does Sonic Chain use for gas?
Sonic Chain uses the S Token, its native cryptocurrency, for transaction fees, gas, and other network activities.
What methods does Alchemy support for the Sonic Chain API?
You can find the list of all the methods Alchemy supports for the Sonic Chain API on Sonic Chain API Endpoints page.
My question isn't here, where can I get help?
Don't worry, we got you. Check out our discord and feel free to post any questions you have!
TABLE OF CONTENTS
What is Sonic Chain?
What is the Sonic Chain API?
How can I get started using the Sonic Chain API?
Is Sonic Chain EVM compatible?
What API does Sonic Chain use?
What is a Sonic Chain API key?
Which libraries support Sonic Chain?
What programming languages work with Sonic Chain?
What does Sonic Chain use for gas?
What methods does Alchemy support for the Sonic Chain API?
My question isn't here, where can I get help?
---

# Sonic Chain API Endpoints


Sonic Chain API Endpoints
All Supported Endpoints for Sonic Chain API
API Endpoints by Use Case
Getting Blocks
Reading Transactions
Writing Transactions & EVM Execution
Account Information
Event Logs
Chain Information
Gas Estimation
Web3
Debug API
Getting Blocks
Retrieves information from a particular block in the blockchain.
eth_getBlockByHash
eth_blockNumber
eth_getBlockByNumber
eth_getBlockTransactionCountByHash
eth_getBlockTransactionCountByNumber
Reading Transactions
Retrieves information on the state data for addresses regardless of whether it is a user or a smart contract.
eth_getTransactionByHash
eth_getTransactionByBlockHashAndIndex
eth_getTransactionByBlockNumberAndIndex
eth_getTransactionReceipt
eth_getTransactionCount
Writing Transactions & EVM Execution
Allows developers to write data on-chain, and interact with smart contracts.
eth_sendRawTransaction
eth_call
Account Information
Returns information regarding an address's stored on-chain data.
eth_getCode
eth_getBalance
eth_getStorageAt
eth_getProof
Event Logs
Returns logs which are records that denote/provide context on specific events within a smart contract, like a token transfer or a change of ownership, for example.
eth_getLogs
Chain Information
Returns information on the network and internal settings.
eth_chainId
net_version
Gas Estimation
Returns information on the network gas estimates.
eth_estimateGas
eth_gasPrice
Web3
Returns network configuration information.
web3_clientVersion
web3_sha3
Debug API
The Debug API provides deeper insights into transaction processing and on-chain activity.
debug_traceCall
debug_traceTransaction
debug_traceBlockByNumber
debug_traceBlockByHash
TABLE OF CONTENTS
API Endpoints by Use Case
Getting Blocks
Reading Transactions
Writing Transactions & EVM Execution
Account Information
Event Logs
Chain Information
Gas Estimation
Web3
Debug API
---

