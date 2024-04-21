# Blockchain-Based Voting System

## Overview
The Blockchain-Based Voting System is a secure and transparent approach to conducting elections using blockchain technology. This project aims to ensure the integrity, security, and transparency of the voting process by leveraging the decentralized nature of blockchain networks.

## Benefits
- **Security**: Utilizes cryptographic techniques and decentralization to prevent tampering and ensure the integrity of the voting process.
- **Transparency**: All voting transactions are recorded on the blockchain, providing an auditable and transparent trail of every vote cast.
- **Immutability**: Once a vote is recorded on the blockchain, it becomes immutable and cannot be altered, ensuring the reliability of the voting data.
- **Accessibility**: Enables voters to securely cast their votes from anywhere with an internet connection, promoting inclusivity and accessibility.
- **Anonymity**: Protects the identity of voters while ensuring their votes are accurately recorded and counted, preserving privacy.

## Prerequisites
- Ubuntu install in your machine.
- [Node.js](<../../how to install node js.md>) (version 18 and above) installed on your machine
- Hardhat for Ethereum smart contract development
- Account on Alchemy  or Infura for API 
- Metamask account and their browser extension installed on your browser

## Installation By Itself
#### Step 1
- Create a new repository
```sh
mkdir voting-dapp && voting-dapp
```
![Image](<../voting src/Screenshot from 2024-04-20 09-05-40.png>)


#### Step 2
- Then initialize an npm project and fill required details.
```sh
npm init
```
![Image](<../voting src/Screenshot from 2024-04-20 09-09-29.png>)


#### Step 3
- Create a file package.json and paste following code.
```sh
nano package.json
```
```json
{
  "name": "blockchain-based-voting-system",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@nomicfoundation/hardhat-toolbox": "^2.0.2",
    "@nomiclabs/hardhat-ethers": "^2.2.2",
    "dotenv": "^16.0.3",
    "hardhat": "^2.13.0",
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "ethers": "^5.7.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4",
    "@babel/plugin-proposal-private-property-in-object": "^7.22.5"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```


#### Step 4
- Now we can install Hardhat:
```
npm install --save-dev hardhat
```
![Image](<../voting src/Screenshot from 2024-04-20 09-17-14.png>) 


#### Step 5
- Then initialize an hardhat project,select create a JavaScript project and fill other details.
```sh
npx hardhat init
```
![Image](<../voting src/Screenshot from 2024-04-20 09-24-52.png>)


#### Step 6
- Now edit hardhat.config.js file with following lines.
```sh
nano hardhat.config.js
```
**Use this line if you have alchemy API.**
```js
require("@nomicfoundation/hardhat-toolbox");

// Ensure your configuration variables are set before executing the script
const { vars } = require("hardhat/config");

// Go to https://alchemy.com, sign up, create a new App in
// its dashboard, and add its key to the configuration variables
const ALCHEMY_API_KEY = vars.get("ALCHEMY_API_KEY");

// Add your Sepolia account private key to the configuration variables
// To export your private key from Coinbase Wallet, go to
// Settings > Developer Settings > Show private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Beware: NEVER put real Ether into testing accounts
const SEPOLIA_PRIVATE_KEY = vars.get("SEPOLIA_PRIVATE_KEY");

module.exports = {
  solidity: "0.8.11",
  networks: {
    sepolia: {
      url: `https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}`,
      accounts: [SEPOLIA_PRIVATE_KEY]
    }
  }
};
```

#### Step 7
- Create .env file in which you can add following details.
```
API_URL = "your api"
PRIVATE_KEY = "metamask private key"
CONTRACT_ADDRESS = ""
```


#### Step 8
- Go to contracts folder and edit filename(lock.sol to Voting.sol) and paste following code.
```sh
cd contracts
```
![Image](<../voting src/Screenshot from 2024-04-20 09-27-26.png>) 

**Voting.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Candidate {
        string name;
        uint256 voteCount;
    }

    Candidate[] public candidates;
    address owner;
    mapping(address => bool) public voters;

    uint256 public votingStart;
    uint256 public votingEnd;

constructor(string[] memory _candidateNames, uint256 _durationInMinutes) {
    for (uint256 i = 0; i < _candidateNames.length; i++) {
        candidates.push(Candidate({
            name: _candidateNames[i],
            voteCount: 0
        }));
    }
    owner = msg.sender;
    votingStart = block.timestamp;
    votingEnd = block.timestamp + (_durationInMinutes * 1 minutes);
}

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function addCandidate(string memory _name) public onlyOwner {
        candidates.push(Candidate({
                name: _name,
                voteCount: 0
        }));
    }

    function vote(uint256 _candidateIndex) public {
        require(!voters[msg.sender], "You have already voted.");
        require(_candidateIndex < candidates.length, "Invalid candidate index.");

        candidates[_candidateIndex].voteCount++;
        voters[msg.sender] = true;
    }

    function getAllVotesOfCandiates() public view returns (Candidate[] memory){
        return candidates;
    }

    function getVotingStatus() public view returns (bool) {
        return (block.timestamp >= votingStart && block.timestamp < votingEnd);
    }

    function getRemainingTime() public view returns (uint256) {
        require(block.timestamp >= votingStart, "Voting has not started yet.");
        if (block.timestamp >= votingEnd) {
            return 0;
    }
        return votingEnd - block.timestamp;
    }
}
```


#### Step 9
- Then compile the project.
```sh
npx hardhat compile
```
![Image](<../voting src/Screenshot from 2024-04-20 09-28-26.png>) 


#### Step 10
- After compile your project you have to check error in your project.For that go inside the test folder and edit the code in lock.js file.
```js
const {
  time,
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { anyValue } = require("@nomicfoundation/hardhat-chai-matchers/withArgs");
const { expect } = require("chai");

describe("Lock", function () {
  // We define a fixture to reuse the same setup in every test.
  // We use loadFixture to run this setup once, snapshot that state,
  // and reset Hardhat Network to that snapshot in every test.
  async function deployOneYearLockFixture() {
    const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
    const ONE_GWEI = 1_000_000_000;

    const lockedAmount = ONE_GWEI;
    const unlockTime = (await time.latest()) + ONE_YEAR_IN_SECS;

    // Contracts are deployed using the first signer/account by default
    const [owner, otherAccount] = await ethers.getSigners();

    const Lock = await ethers.getContractFactory("Lock");
    const lock = await Lock.deploy(unlockTime, { value: lockedAmount });

    return { lock, unlockTime, lockedAmount, owner, otherAccount };
  }

  describe("Deployment", function () {
    it("Should set the right unlockTime", async function () {
      const { lock, unlockTime } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.unlockTime()).to.equal(unlockTime);
    });

    it("Should set the right owner", async function () {
      const { lock, owner } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.owner()).to.equal(owner.address);
    });

    it("Should receive and store the funds to lock", async function () {
      const { lock, lockedAmount } = await loadFixture(
        deployOneYearLockFixture
      );

      expect(await ethers.provider.getBalance(lock.target)).to.equal(
        lockedAmount
      );
    });

    it("Should fail if the unlockTime is not in the future", async function () {
      // We don't use the fixture here because we want a different deployment
      const latestTime = await time.latest();
      const Lock = await ethers.getContractFactory("Lock");
      await expect(Lock.deploy(latestTime, { value: 1 })).to.be.revertedWith(
        "Unlock time should be in the future"
      );
    });
  });

  describe("Withdrawals", function () {
    describe("Validations", function () {
      it("Should revert with the right error if called too soon", async function () {
        const { lock } = await loadFixture(deployOneYearLockFixture);

        await expect(lock.withdraw()).to.be.revertedWith(
          "You can't withdraw yet"
        );
      });

      it("Should revert with the right error if called from another account", async function () {
        const { lock, unlockTime, otherAccount } = await loadFixture(
          deployOneYearLockFixture
        );

        // We can increase the time in Hardhat Network
        await time.increaseTo(unlockTime);

        // We use lock.connect() to send a transaction from another account
        await expect(lock.connect(otherAccount).withdraw()).to.be.revertedWith(
          "You aren't the owner"
        );
      });

      it("Shouldn't fail if the unlockTime has arrived and the owner calls it", async function () {
        const { lock, unlockTime } = await loadFixture(
          deployOneYearLockFixture
        );

        // Transactions are sent using the first signer by default
        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).not.to.be.reverted;
      });
    });

    describe("Events", function () {
      it("Should emit an event on withdrawals", async function () {
        const { lock, unlockTime, lockedAmount } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw())
          .to.emit(lock, "Withdrawal")
          .withArgs(lockedAmount, anyValue); // We accept any value as `when` arg
      });
    });

    describe("Transfers", function () {
      it("Should transfer the funds to the owner", async function () {
        const { lock, unlockTime, lockedAmount, owner } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).to.changeEtherBalances(
          [owner, lock],
          [lockedAmount, -lockedAmount]
        );
      });
    });
  });
});
```
- Then run test cmd for test.
```sh
npx hardhat test
```


#### Step 11
- Create a folder(scripts) and in that create a file(depoly.js).Also add this line in file.
```sh
mkdir scripts && cd scripts
```
![Image](<../voting src/Screenshot from 2024-04-20 10-07-41.png>) 
```sh 
nano depoly.js
```
```js
async function main() {
  const Voting = await ethers.getContractFactory("Voting");

  // Start deployment, returning a promise that resolves to a contract object
  const Voting_ = await Voting.deploy(["Ratnesh Kumar", "Rajnish", "Chandan", "Pushpendra"], 90);
  console.log("Contract address:", Voting_.address);


}

main()
 .then(() => process.exit(0))
 .catch(error => {
   console.error(error);
   process.exit(1);
 });
```


#### Step 12
- After that deploy you project with following cmd you will get a contract address paste it in your .env file.
```sh
npx hardhat run --network sepolia scripts/depoly.js
```
![Image](<../voting src/Screenshot from 2024-04-20 11-49-34.png>) 


#### Step 13
- Now we create a react app using following cmd:
```sh
npx create-react-app voting-system
```
![Image](<../voting src/Screenshot from 2024-04-20 12-11-41.png>) 
![Image](<../voting src/Screenshot from 2024-04-20 12-12-08.png>) 


#### Step 14
- Now start your server to see your depolyment with following cmd:
```sh
npm start
```
![Image](<../voting src/Screenshot from 2024-04-20 12-13-04.png>) 
![Image](<../voting src/Screenshot from 2024-04-20 12-14-03.png>) 

**if every thing is alright you will see this**
![Image](<../voting src/Screenshot from 2024-04-20 12-14-13.png>)

#### Step 15
- Now install ethers.js library for you project.
```sh
npm install ethers@5.7.1
```
![Image](<../voting src/Screenshot from 2024-04-20 12-33-33.png>) 


#### Step 16
- Now stop your server with ctrl + c and move src and public folder from voting-system to your root folder.
- Also edit app.css,app.js with this lines.

**App.css**
```css
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f1f1f1;
}

.welcome-message {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
}

.login-button {
  background-color: #007bff;
  color: #fff;
  font-size: 1.2rem;
  border: none;
  border-radius: 0.3rem;
  padding: 1rem 2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #0069d9;
}


.connected-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f1f1f1;
}

.connected-header {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 2rem;
}

.connected-account {
  font-size: 1.2rem;
  text-align: center;
  margin-bottom: 2rem;
}

.connected-button {
  background-color: #007bff;
  color: #fff;
  font-size: 1.2rem;
  border: none;
  border-radius: 0.3rem;
  padding: 1rem 2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: 2rem;
}

.connected-button:hover {
  background-color: #0069d9;
}

.connected-contract-address {
  font-size: 1.2rem;
  text-align: center;
}


.candidates-table {
  border-collapse: collapse;
  width: 50%;
  text-align:center;
}

.candidates-table th, .candidates-table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.candidates-table th {
  background-color: #f2f2f2;
}

input[type=number] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 16px;
  margin-bottom: 10px;
}
```
**App.js**
```js
import { useState, useEffect } from 'react';
import {ethers} from 'ethers';
import {contractAbi, contractAddress} from './Constant/constant';
import Login from './Components/Login';
import Finished from './Components/Finished';
import Connected from './Components/Connected';
import './App.css';

function App() {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [votingStatus, setVotingStatus] = useState(true);
  const [remainingTime, setremainingTime] = useState('');
  const [candidates, setCandidates] = useState([]);
  const [number, setNumber] = useState('');
  const [CanVote, setCanVote] = useState(true);


  useEffect( () => {
    getCandidates();
    getRemainingTime();
    getCurrentStatus();
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', handleAccountsChanged);
    }

    return() => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      }
    }
  });


  async function vote() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract (
        contractAddress, contractAbi, signer
      );

      const tx = await contractInstance.vote(number);
      await tx.wait();
      canVote();
  }


  async function canVote() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract (
        contractAddress, contractAbi, signer
      );
      const voteStatus = await contractInstance.voters(await signer.getAddress());
      setCanVote(voteStatus);

  }

  async function getCandidates() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract (
        contractAddress, contractAbi, signer
      );
      const candidatesList = await contractInstance.getAllVotesOfCandiates();
      const formattedCandidates = candidatesList.map((candidate, index) => {
        return {
          index: index,
          name: candidate.name,
          voteCount: candidate.voteCount.toNumber()
        }
      });
      setCandidates(formattedCandidates);
  }


  async function getCurrentStatus() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract (
        contractAddress, contractAbi, signer
      );
      const status = await contractInstance.getVotingStatus();
      console.log(status);
      setVotingStatus(status);
  }

  async function getRemainingTime() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contractInstance = new ethers.Contract (
        contractAddress, contractAbi, signer
      );
      const time = await contractInstance.getRemainingTime();
      setremainingTime(parseInt(time, 16));
  }

  function handleAccountsChanged(accounts) {
    if (accounts.length > 0 && account !== accounts[0]) {
      setAccount(accounts[0]);
      canVote();
    } else {
      setIsConnected(false);
      setAccount(null);
    }
  }

  async function connectToMetamask() {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        setProvider(provider);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        console.log("Metamask Connected : " + address);
        setIsConnected(true);
        canVote();
      } catch (err) {
        console.error(err);
      }
    } else {
      console.error("Metamask is not detected in the browser")
    }
  }

  async function handleNumberChange(e) {
    setNumber(e.target.value);
  }

  return (
    <div className="App">
      { votingStatus ? (isConnected ? (<Connected 
                      account = {account}
                      candidates = {candidates}
                      remainingTime = {remainingTime}
                      number= {number}
                      handleNumberChange = {handleNumberChange}
                      voteFunction = {vote}
                      showButton = {CanVote}/>) 
                      
                      : 
                      
                      (<Login connectWallet = {connectToMetamask}/>)) : (<Finished />)}
      
    </div>
  );
}
export default App;
```


#### Step 17
- Create a new folder(Components) in src folder and add this files.
**Connected.jsx**
```jsx
import React from "react";

const Connected = (props) => {
    return (
        <div className="connected-container">
            <h1 className="connected-header">You are Connected to Metamask</h1>
            <p className="connected-account">Metamask Account: {props.account}</p>
            <p className="connected-account">Remaining Time: {props.remainingTime}</p>
            { props.showButton ? (
                <p className="connected-account">You have already voted</p>
            ) : (
                <div>
                    <input type="number" placeholder="Entern Candidate Index" value={props.number} onChange={props.handleNumberChange}></input>
            <br />
            <button className="login-button" onClick={props.voteFunction}>Vote</button>

                </div>
            )}
            
            <table id="myTable" className="candidates-table">
                <thead>
                <tr>
                    <th>Index</th>
                    <th>Candidate name</th>
                    <th>Candidate votes</th>
                </tr>
                </thead>
                <tbody>
                {props.candidates.map((candidate, index) => (
                    <tr key={index}>
                    <td>{candidate.index}</td>
                    <td>{candidate.name}</td>
                    <td>{candidate.voteCount}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            
        </div>
    )
}

export default Connected;
```
**Finished.jsx**
```jsx
import React from "react";

const Finished = (props) => {
    return (
        <div className="login-container">
            <h1 className="welcome-message">Voting is Finished</h1>
        </div>
    )
}

export default Finished;
```
**Login.jsx**
```jsx
import React from "react";

const Login = (props) => {
    return (
        <div className="login-container">
            <h1 className="welcome-message">Welcome to decentralized voting application</h1>
            <button className="login-button" onClick = {props.connectWallet}>Login Metamask</button>
        </div>
    )
}

export default Login;
```


#### Step 18
- Create a new folder(Constant) in src folder and add constant.js file.
```js
const contractAddress = "your contract address";

const contractAbi = your abi ;
//This abi is in your artigacts/contracts/Voting.sol/Voting.json file

export {contractAbi, contractAddress};

```


#### Step 19
- Your project is done.Its time to run your project.
- Before run your project you have to bulid your project .
```sh
npm serve build
```
![Image](<../voting src/Screenshot from 2024-04-20 14-05-32.png>) 
![Image](<../voting src/Screenshot from 2024-04-20 14-09-20.png>) 

- Now start your server and see your output in your local host(10.0.2.15:3000)
```sh
server -s build
```
![Image](<../voting src/Screenshot from 2024-04-20 14-04-32.png>) 


## Installation By Github
### Step 1
- Clone this project repository.
```bash
git clone https://github.com/16ratneshkumar/blockchain-voting-system.git 
```
### Step 2
- Navigate to the project directory:
```bash
cd blockchain-voting-system/voting-dapp
```
### Step 3
- Now create .env file with this details.
```
API_URL = "your api"
PRIVATE_KEY = "metamask private key"
CONTRACT_ADDRESS = ""
```
### Step 4
- After that deploy you project with following cmd you will get a contract address paste it in your .env file.
```sh
npx hardhat run --network sepolia scripts/depoly.js
```
### Step 5
- go to src/Constant folder and edit constant.js file with your Contract Address and Contract Abi.
```js
const contractAddress = "your contract address";

const contractAbi = your abi ;
//This abi is in your artigacts/contracts/Voting.sol/Voting.json file

export {contractAbi, contractAddress};

```
### Step 6
- Your project is done.Its time to run your project.
- Before run your project you have to bulid your project .
```sh
npm serve build
```
![Image](<../voting src/Screenshot from 2024-04-20 14-05-32.png>) 
![Image](<../voting src/Screenshot from 2024-04-20 14-09-20.png>) 

- Now start your server and see your output in your local host(10.0.2.15:3000)
```sh
npm install -g server && server -s build
```
![Image](<../voting src/Screenshot from 2024-04-20 14-04-32.png>) 


### **Image Of Result**
**1.First Interface**
![Image](<../voting src/Screenshot from 2024-04-20 12-21-05.png>) 

**2.Login Into metamask**
![Image](<../voting src/Screenshot from 2024-04-20 13-58-16.png>)

**3.Start Voting**
![Image](<../voting src/Screenshot from 2024-04-20 14-10-41.png>)

**4.Voting**
![Image](<../voting src/Screenshot from 2024-04-20 14-10-50.png>) 

**5.Voted**
![Image](<../voting src/Screenshot from 2024-04-20 14-11-32.png>) 

### **Image of Metamask during voting**
<div>
  <img src="../voting src/Screenshot from 2024-04-20 14-12-49.png" alt="Image" /> 
  <img src="../voting src/Screenshot from 2024-04-20 14-12-57.png" alt="Image" /> 
  <img src="../voting src/Screenshot from 2024-04-20 14-13-19.png" alt="Image" />
  <img src="../voting src/WhatsApp Image 2024-04-21 at 11.51.54_533e58a7.jpg" alt="Image" />
  <img src="../voting src/WhatsApp Image 2024-04-21 at 11.51.54_bb403983.jpg" alt="Image" />
</div> 

### **Image of Alchemy(Api request)**
<div>
<img src="../voting src/Screenshot 2024-04-20 143345.jpg" alt="Image" />
<img src="../voting src/Screenshot 2024-04-20 143431.jpg" alt="Image" /> 
<img src="../voting src/Screenshot 2024-04-20 143511.jpg" alt="Image" /> 
<img src="../voting src/Screenshot 2024-04-20 143533.jpg" alt="Image" /> 
<img src="../voting src/Screenshot 2024-04-20 143620.jpg" alt="Image" /> 
<img src="../voting src/Screenshot 2024-04-20 143726.jpg" alt="Image" />
</div> 
 

### Usage
1. Install and configure Metamask on your browser.
2. Connect Metamask to the Ethereum network and authorize the application to interact with your account.
3. Access the online interface to securely cast your vote during the specified voting period.
4. Each vote is encrypted and recorded on the blockchain, ensuring its immutability and integrity.
5. After each vote, the system transparently counts and tallies the votes, producing election results that can be publicly verified.


**Thank You**
