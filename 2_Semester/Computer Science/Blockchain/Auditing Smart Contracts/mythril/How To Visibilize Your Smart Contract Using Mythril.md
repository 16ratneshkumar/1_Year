# How To Visibilize Your Smart Contract Using Mythril.....
![Image](<src/Screenshot from 2024-04-14 18-57-37.png>)

## What Is Mythril ?
- Mythril is a security analysis tool for Ethereum smart contracts. It was introduced at HITBSecConf 2018.

+ Mythril detects a range of security issues, including integer underflows, owner-overwrite-to-Ether-withdrawal, and others. Note that Mythril is targeted at finding common vulnerabilities, and is not able to discover issues in the business logic of an application. 

## How To Install Slither....
***Optional Step***
![](<src/Screenshot from 2024-04-14 18-40-39.png>)
```
mkdir mythril && cd mythril 
```
***Mandatory Step***
```
sudo apt update
```
![Image](<src/Screenshot from 2024-04-14 18-41-00.png>)
```
sudo apt install software-properties-common
```
![Image](<src/Screenshot from 2024-04-14 18-41-30.png>)
```
sudo add-apt-repository ppa:ethereum/ethereum
```
![Image](<src/Screenshot from 2024-04-14 18-42-44.png>)
```
sudo apt install solc
```
![Image](<src/Screenshot from 2024-04-14 18-43-30.png>)
```
solc-select use [VERSION] --always-install
```
![Image](<src/Screenshot from 2024-04-14 18-57-05.png>)
```
sudo apt install libssl-dev python3-dev python3-pip
```
![Image](<src/Screenshot from 2024-04-14 18-43-56.png>)
```
pip3 install mythril
```
![Image](<src/Screenshot from 2024-04-14 18-45-28.png>)

#### Use To Check The Version Of Mythril

![Image](<src/Screenshot from 2024-04-14 18-48-29.png>)
```
myth version
```

## How to analyze a smart contract using mythril....
```
touch MyContract.sol && nano MyContract.sol
```
![Image](<src/Screenshot from 2024-04-14 18-49-37.png>)
```
myth analyze <file_path>
```
![alt text](<src/Screenshot from 2024-04-14 18-57-37.png>)
![alt text](<src/Screenshot from 2024-04-14 18-58-12.png>)
```
myth analyze <file_path> -o json
```
![Image](<src/Screenshot from 2024-04-14 19-01-29.png>)

[For More Information Go Through....](https://mythril-classic.readthedocs.io/en/master/about.html)