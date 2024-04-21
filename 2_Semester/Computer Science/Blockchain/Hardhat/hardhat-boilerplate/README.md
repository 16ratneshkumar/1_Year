# Hardhat Boilerplate :: A Project Transaction Of ethereum Token

This repository presents an exemplary project suitable as the initial framework for your Ethereum endeavor. It's also highly conducive to grasping the fundamentals of smart contract development.


This repository offers a model project to kickstart your Ethereum venture. It's designed to be an ideal resource for learning the foundational aspects of smart contract development.


## Quick start

The first things you need to do are cloning this repository and installing its
dependencies:

```sh
git clone https://github.com/NomicFoundation/hardhat-boilerplate.git
```
![Image](<../src boiler/Screenshot from 2024-04-17 19-53-33.png>) 
```sh
cd hardhat-boilerplate
```
![Image](<../src boiler/Screenshot from 2024-04-17 20-39-30.png>) 
```sh
npm install
```
![Image](<../src boiler/Screenshot from 2024-04-17 20-40-32.png>) 

Once installed, let's run Hardhat's testing network:

```sh
npx hardhat node
```
![Image](<../src boiler/Screenshot from 2024-04-17 21-32-18.png>)
Then, on a new terminal, go to the repository's root folder and run this to
deploy your contract:

```sh
npx hardhat run scripts/deploy.js --network localhost
```
![Image](<../src boiler/Screenshot from 2024-04-17 20-43-08.png>) 

Finally, we can run the frontend with:

```sh
cd frontend
```

```sh
npm install
```
![Image](<../src boiler/Screenshot from 2024-04-17 19-44-24.png>) 

_Use this if you will see vulnerabilities_
```sh
npm audit fix
```
![Image](<../src boiler/Screenshot from 2024-04-17 20-40-13.png>) 
```sh
npm run start
```
![Image](<../src boiler/Screenshot from 2024-04-17 21-40-26.png>) 
![Image](<../src boiler/Screenshot from 2024-04-17 20-59-24.png>) 
![Image](<../src boiler/Screenshot from 2024-04-17 21-00-30.png>) 

or 

You can also use different way to start server.
```sh
npm run bulid
```
 
![Image](<../src boiler/Screenshot from 2024-04-17 22-02-08.png>)
```sh
npm install -g server 
server -s build
```
![Image](<../src boiler/Screenshot from 2024-04-17 22-02-49.png>)  
![Image](<../src boiler/Screenshot from 2024-04-17 22-03-10.png>)

Open [http://localhost:3000/](http://localhost:3000/) to see your Dapp. You will
need to have [Metamask](https://metamask.io) installed and listening to `localhost 8545`.

## Performance of Dapp
### **Starting Interface Without Metamask Extension**
![Image](<../src boiler/Screenshot from 2024-04-17 21-00-57.png>)
### **After Connect Metamask Extansion**
![Image](<../src boiler/Screenshot from 2024-04-17 21-06-58.png>) 
### **Connect With Metamask Wallet**
<div>
    <img src="../src boiler/Screenshot from 2024-04-17 21-08-06.png" alt="Image"/> 
    <img src="../src boiler/Screenshot from 2024-04-17 21-08-15.png" alt="Image"/> 
</div>

### **Genrate Token For Transaction**
![Image](<../src boiler/Screenshot from 2024-04-17 21-24-10.png>) 
![Image](<../src boiler/Screenshot from 2024-04-17 21-25-56.png>)

   **Image of metamask after token genrated**
   ![Image](<../src boiler/Screenshot from 2024-04-17 21-26-27.png>)

### **Doing Transaction** 
![Image](<../src boiler/Screenshot from 2024-04-17 21-29-17.png>)
![Image](<../src boiler/Screenshot from 2024-04-17 22-05-51.png>)

   **Image of metamask after transaction** 

   ![Image](<../src boiler/Screenshot from 2024-04-17 21-29-56.png>) 
   ![Image](<../src boiler/Screenshot from 2024-04-17 21-30-12.png>)
   
   **Image of terminal after transaction**

   ![Image](<../src boiler/Screenshot from 2024-04-17 22-09-38.png>)
  
  **Image of request analytics on alchemy**
  ![Image](<../src boiler/Screenshot from 2024-04-17 20-52-33.png>)

## _After Terminating The Server_
![Image](<../src boiler/Screenshot from 2024-04-17 22-11-34.png>)


# **Happy _building_!**
