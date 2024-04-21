# Hardhat 
- To deploy any dapp we need to do some several work give as follow:
    * Setting up your Node.js environment for Ethereum development
    * Creating and configuring a Hardhat project
    * The basics of a Solidity smart contract that implements a token
    * Writing automated tests for your contract using Hardhat
    * Debugging Solidity with console.log() using Hardhat Network
    * Deploying your contract to Hardhat Network and Ethereum testnets

## 1. Setting up the environment
   ### Installing Node.js
   - You can skip this section if you already have a working Node.js >=18.0 installation. If not, here's how to install it on Ubuntu, MacOS and Windows.
        ### Ubuntu
        - Copy and paste these commands in a terminal:
        ```sh
        sudo apt update
        sudo apt install curl git
        curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
        sudo apt-get install -y nodejs
        ```
        ### MacOS
        - ***Make sure you have git installed.***
        - Copy and paste these commands in a terminal:
        ```sh
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
        nvm install 20
        nvm use 20
        nvm alias default 20
        npm install npm --global  # Upgrade npm to the latest version
        ```
   
   ### Upgrading your Node.js installation
   - If your version of Node.js is older and not supported by Hardhat follow the instructions below to upgrade.
        ### Ubuntu
        - Remove older version to run follow cmd:
        ```sh
        sudo apt remove nodejs
        ```

        ### MacOS
        - You can change your Node.js version using nvm. To upgrade to Node.js 20.x run these in a terminal:
        ```sh
        nvm install 20
        nvm use 20
        nvm alias default 20
        npm install npm --global # Upgrade npm to the latest version
        ```
## 2. Creating a new Hardhat project
   - ***we suggest you use npm 7 or higher for this.***
   - Open a new terminal and run these commands to create a new folder:
   ```sh
   mkdir hardhat-tutorial && cd hardhat-tutorial
   ```
   - Then initialize an npm project using following cmd:
   ```sh
   npm init
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-56-10.png>)
   - Now we can install Hardhat:
   ```sh
   npm install --save-dev hardhat
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-51-10.png>)
   - In the same directory where you installed Hardhat run:
   ```sh
   npx hardhat init
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-51-26.png>)
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-52-37.png>)
   - Select Create an empty hardhat.config.js with your keyboard and hit enter.

   ***When Hardhat is run, it searches for the closest hardhat.config.js file starting from the current working directory. This file normally lives in the root of your project and an empty hardhat.config.js is enough for Hardhat to work. The entirety of your setup is contained in this file.***
   ### Plugins
   - Hardhat is unopinionated in terms of what tools you end up using, but it does come with some built-in defaults. All of which can be overridden. Most of the time the way to use a given tool is by consuming a plugin that integrates it into Hardhat.
   ```sh
   npm install --save-dev @nomicfoundation/hardhat-toolbox
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-55-37.png>)
   - Add this line to your hardhat.config.js so that it looks like this:
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-57-11.png>)
   ```solidity
    require("@nomicfoundation/hardhat-toolbox");

    /** @type import('hardhat/config').HardhatUserConfig */
    module.exports = {
    solidity: "0.8.24",
    };
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 17-57-55.png>)
## 3. Writing and compiling smart contracts
- We're going to create a simple smart contract that implements a token that can be transferred. Token contracts are most frequently used to exchange or store value. 
   ### Writing smart contracts
   - Start by creating a new directory called contracts and create a file inside the directory called Token.sol.
   ```sh
   mkdir contracts && cd contracts
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-00-10.png>)
   ```sh
   touch Token.sol && nano Token.sol
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-01-06.png>)
   
   ***Paste the code below into the file and take a minute to read the code. It's simple and it's full of comments explaining the basics of Solidity.***
   ```solidity
    //SPDX-License-Identifier: UNLICENSED

    // Solidity files have to start with this pragma.
    // It will be used by the Solidity compiler to validate its version.
    pragma solidity ^0.8.0;


    // This is the main building block for smart contracts.
    contract Token {
        // Some string type variables to identify the token.
        string public name = "My Hardhat Token";
        string public symbol = "MHT";

        // The fixed amount of tokens, stored in an unsigned integer type variable.
        uint256 public totalSupply = 1000000;

        // An address type variable is used to store ethereum accounts.
        address public owner;

        // A mapping is a key/value map. Here we store each account's balance.
        mapping(address => uint256) balances;

        // The Transfer event helps off-chain applications understand
        // what happens within your contract.
        event Transfer(address indexed _from, address indexed _to, uint256 _value);

        /**
        * Contract initialization.
        */
        constructor() {
            // The totalSupply is assigned to the transaction sender, which is the
            // account that is deploying the contract.
            balances[msg.sender] = totalSupply;
            owner = msg.sender;
        }

        /**
        * A function to transfer tokens.
        *
        * The `external` modifier makes a function *only* callable from *outside*
        * the contract.
        */
        function transfer(address to, uint256 amount) external {
            // Check if the transaction sender has enough tokens.
            // If `require`'s first argument evaluates to `false` then the
            // transaction will revert.
            require(balances[msg.sender] >= amount, "Not enough tokens");

            // Transfer the amount.
            balances[msg.sender] -= amount;
            balances[to] += amount;

            // Notify off-chain applications of the transfer.
            emit Transfer(msg.sender, to, amount);
        }

        /**
        * Read only function to retrieve the token balance of a given account.
        *
        * The `view` modifier indicates that it doesn't modify the contract's
        * state, which allows us to call it without executing a transaction.
        */
        function balanceOf(address account) external view returns (uint256) {
            return balances[account];
        }
    }
    ```
   ### Compiling contracts
   - To compile the contract run following cmd in your terminal.
   ```sh
   npx hardhat compile
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-08-26.png>)
## 4. Testing contracts
- To test our contract, we are going to use Hardhat Network, a local Ethereum network designed for development. It comes built-in with Hardhat, and it's used as the default network. You don't need to setup anything to use it.
   ### Writing tests
   - For testing we are using chai library of javascript.
   - Create a new directory called test inside our project root directory and create a new file in there called Token.js.
   ```sh
   mkdir test && cd test
   ```
   ```sh
   touch Token.js && nano Token.js
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-09-59.png>)
   
   ***Paste this line into Token.js***
   ```js
    const { expect } = require("chai");

    describe("Token contract", function () {
    it("Deployment should assign the total supply of tokens to the owner", async function () {
        const [owner] = await ethers.getSigners();

        const hardhatToken = await ethers.deployContract("Token");

        const ownerBalance = await hardhatToken.balanceOf(owner.address);
        expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
    });
    });
    ```
    - After this run this cmd in your terminal.
    ```sh
    npx hardhat test
    ```
    ![Image](<../src tutorial/Screenshot from 2024-04-17 18-10-37.png>)
    ### Using a different account(Optional)
    - If you need to test your code by sending a transaction from an account (or Signer in ethers.js terminology) other than the default one, you can use the connect() method on your ethers.js Contract object to connect it to a different account, like this:
    - ***Paste this code in your test/Token.js file***
    ```js
    const { expect } = require("chai");

    describe("Token contract", function () {
    // ...previous test...

    it("Should transfer tokens between accounts", async function() {
        const [owner, addr1, addr2] = await ethers.getSigners();

        const hardhatToken = await ethers.deployContract("Token");

        // Transfer 50 tokens from owner to addr1
        await hardhatToken.transfer(addr1.address, 50);
        expect(await hardhatToken.balanceOf(addr1.address)).to.equal(50);

        // Transfer 50 tokens from addr1 to addr2
        await hardhatToken.connect(addr1).transfer(addr2.address, 50);
        expect(await hardhatToken.balanceOf(addr2.address)).to.equal(50);
        });
    });
    ```
    - After this run this cmd in your terminal.
    ```sh
    npx hardhat test
    ```
    ### Reusing common test setups with fixtures (Optional)
    - The two tests that we wrote begin with their setup, which in this case means deploying the token contract. In more complex projects, this setup could involve multiple deployments and other transactions. Doing that in every test means a lot of code duplication. Plus, executing many transactions at the beginning of each test can make the test suite much slower.
    - You can avoid code duplication and improve the performance of your test suite by using fixtures. A fixture is a setup function that is run only the first time it's invoked. On subsequent invocations, instead of re-running it, Hardhat will reset the state of the network to what it was at the point after the fixture was initially executed.
    - ***Paste this code in your test/Token.js file.***
    ```js
    const {
    loadFixture,
    } = require("@nomicfoundation/hardhat-toolbox/network-helpers");
    const { expect } = require("chai");

    describe("Token contract", function () {
    async function deployTokenFixture() {
        const [owner, addr1, addr2] = await ethers.getSigners();

        const hardhatToken = await ethers.deployContract("Token");

        // Fixtures can return anything you consider useful for your tests
        return { hardhatToken, owner, addr1, addr2 };
    }

    it("Should assign the total supply of tokens to the owner", async function () {
        const { hardhatToken, owner } = await loadFixture(deployTokenFixture);

        const ownerBalance = await hardhatToken.balanceOf(owner.address);
        expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
    });

    it("Should transfer tokens between accounts", async function () {
        const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
        deployTokenFixture
        );

        // Transfer 50 tokens from owner to addr1
        await expect(
        hardhatToken.transfer(addr1.address, 50)
        ).to.changeTokenBalances(hardhatToken, [owner, addr1], [-50, 50]);

        // Transfer 50 tokens from addr1 to addr2
        // We use .connect(signer) to send a transaction from another account
        await expect(
        hardhatToken.connect(addr1).transfer(addr2.address, 50)
        ).to.changeTokenBalances(hardhatToken, [addr1, addr2], [-50, 50]);
    });
    });
    ```
    - After this run this cmd in your terminal.
    ```sh
    npx hardhat test
    ```
    ### Full coverage
    - Now that we've covered the basics that you'll need for testing your contracts, here's a full test suite for the token with a lot of additional information about Mocha and how to structure your tests. We recommend reading it thoroughly.
    - ***Paste this code in your test/Token.js file.***
    ```js
    // This is an example test file. Hardhat will run every *.js file in `test/`,
    // so feel free to add new ones.

    // Hardhat tests are normally written with Mocha and Chai.

    // We import Chai to use its asserting functions here.
    const { expect } = require("chai");

    // We use `loadFixture` to share common setups (or fixtures) between tests.
    // Using this simplifies your tests and makes them run faster, by taking
    // advantage of Hardhat Network's snapshot functionality.
    const {
    loadFixture,
    } = require("@nomicfoundation/hardhat-toolbox/network-helpers");

    // `describe` is a Mocha function that allows you to organize your tests.
    // Having your tests organized makes debugging them easier. All Mocha
    // functions are available in the global scope.
    //
    // `describe` receives the name of a section of your test suite, and a
    // callback. The callback must define the tests of that section. This callback
    // can't be an async function.
    describe("Token contract", function () {
    // We define a fixture to reuse the same setup in every test. We use
    // loadFixture to run this setup once, snapshot that state, and reset Hardhat
    // Network to that snapshot in every test.
    async function deployTokenFixture() {
        // Get the Signers here.
        const [owner, addr1, addr2] = await ethers.getSigners();

        // To deploy our contract, we just have to call ethers.deployContract and await
        // its waitForDeployment() method, which happens once its transaction has been
        // mined.
        const hardhatToken = await ethers.deployContract("Token");

        await hardhatToken.waitForDeployment();

        // Fixtures can return anything you consider useful for your tests
        return { hardhatToken, owner, addr1, addr2 };
    }

    // You can nest describe calls to create subsections.
    describe("Deployment", function () {
        // `it` is another Mocha function. This is the one you use to define each
        // of your tests. It receives the test name, and a callback function.
        //
        // If the callback function is async, Mocha will `await` it.
        it("Should set the right owner", async function () {
        // We use loadFixture to setup our environment, and then assert that
        // things went well
        const { hardhatToken, owner } = await loadFixture(deployTokenFixture);

        // `expect` receives a value and wraps it in an assertion object. These
        // objects have a lot of utility methods to assert values.

        // This test expects the owner variable stored in the contract to be
        // equal to our Signer's owner.
        expect(await hardhatToken.owner()).to.equal(owner.address);
        });

        it("Should assign the total supply of tokens to the owner", async function () {
        const { hardhatToken, owner } = await loadFixture(deployTokenFixture);
        const ownerBalance = await hardhatToken.balanceOf(owner.address);
        expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
        });
    });

    describe("Transactions", function () {
        it("Should transfer tokens between accounts", async function () {
        const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
            deployTokenFixture
        );
        // Transfer 50 tokens from owner to addr1
        await expect(
            hardhatToken.transfer(addr1.address, 50)
        ).to.changeTokenBalances(hardhatToken, [owner, addr1], [-50, 50]);

        // Transfer 50 tokens from addr1 to addr2
        // We use .connect(signer) to send a transaction from another account
        await expect(
            hardhatToken.connect(addr1).transfer(addr2.address, 50)
        ).to.changeTokenBalances(hardhatToken, [addr1, addr2], [-50, 50]);
        });

        it("Should emit Transfer events", async function () {
        const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
            deployTokenFixture
        );

        // Transfer 50 tokens from owner to addr1
        await expect(hardhatToken.transfer(addr1.address, 50))
            .to.emit(hardhatToken, "Transfer")
            .withArgs(owner.address, addr1.address, 50);

        // Transfer 50 tokens from addr1 to addr2
        // We use .connect(signer) to send a transaction from another account
        await expect(hardhatToken.connect(addr1).transfer(addr2.address, 50))
            .to.emit(hardhatToken, "Transfer")
            .withArgs(addr1.address, addr2.address, 50);
        });

        it("Should fail if sender doesn't have enough tokens", async function () {
        const { hardhatToken, owner, addr1 } = await loadFixture(
            deployTokenFixture
        );
        const initialOwnerBalance = await hardhatToken.balanceOf(owner.address);

        // Try to send 1 token from addr1 (0 tokens) to owner.
        // `require` will evaluate false and revert the transaction.
        await expect(
            hardhatToken.connect(addr1).transfer(owner.address, 1)
        ).to.be.revertedWith("Not enough tokens");

        // Owner balance shouldn't have changed.
        expect(await hardhatToken.balanceOf(owner.address)).to.equal(
            initialOwnerBalance
        );
        });
    });
    });
    ```
    - After this run this cmd in your terminal.
    ```sh
    npx hardhat test
    ```
    ![Image](<../src tutorial/Screenshot from 2024-04-17 18-13-02.png>)
## 5. Debugging with Hardhat Network
   ### Solidity console.log
   - When running your contracts and tests on Hardhat Network you can print logging messages and contract variables calling console.log() from your Solidity code. To use it you have to import hardhat/console.sol in your contract code.
   ```s
    pragma solidity ^0.8.0;

    import "hardhat/console.sol";

    contract Token {
    //...
    }
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-15-59.png>)
   - Then you can just add some console.log calls to the transfer() function as if you were using it in JavaScript:
   ```solidity
    function transfer(address to, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Not enough tokens");

        console.log(
            "Transferring from %s to %s %s tokens",
            msg.sender,
            to,
            amount
        );

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-23-32.png>)
   - After pasteing this line to run following command:
   ```sh
    npx hardhat test
   ```
## 6. Deploying to a live network
- Once you're ready to share your dApp with other people, you may want to deploy it to a live network. This way others can access an instance that's not running locally on your system.
- The "mainnet" Ethereum network deals with real money, but there are separate "testnet" networks that do not. These testnets provide shared staging environments that do a good job of mimicking the real world scenario without putting real money at stake, and Ethereum has several, like Sepolia and Goerli. We recommend you deploy your contracts to the Sepolia testnet.
- At the software level, deploying to a testnet is the same as deploying to mainnet. The only difference is which network you connect to. Let's look into what the code to deploy your contracts using Hardhat Ignition would look like.
- In Hardhat Ignition, deployments are defined through Ignition Modules. These modules are abstractions to describe a deployment; that is, JavaScript functions that specify what you want to deploy.
- Ignition modules are expected to be within the ./ignition/modules directory.So now create this.
```sh
mkdir ignition && cd ignition
```
```sh
mkdir modules && cd modules
```
![Image](<../src tutorial/Screenshot from 2024-04-17 18-30-16.png>)
- ***Paste the following into a Token.js file in that directory:***
    ```js
    const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

    const TokenModule = buildModule("TokenModule", (m) => {
    const token = m.contract("Token");

    return { token };
    });

    module.exports = TokenModule;
    ```
    ![Image](<../src tutorial/Screenshot from 2024-04-17 18-30-30.png>)
- To tell Hardhat to connect to a specific Ethereum network, you can use the --network parameter when running any task, like this:
    ```sh
    npx hardhat ignition deploy ./ignition/modules/Token.js --network <network-name>
    ```
    ![Image](<../src tutorial/Screenshot from 2024-04-17 18-33-52.png>)
- With our current configuration, running it without the --network parameter would cause the code to run against an embedded instance of Hardhat Network. In this scenario, the deployment actually gets lost when Hardhat finishes running, but it's still useful to test that our deployment code works:
   ### Deploying to remote networks
   - To deploy to a remote network such as mainnet or any testnet, you need to add a network entry to your hardhat.config.js file. We’ll use Sepolia for this example, but you can add any network. For key storage, utilize the configuration variables.
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-38-12.png>)
   - ***If you use infura API key***
    ```js
    require("@nomicfoundation/hardhat-toolbox");

    // Ensure your configuration variables are set before executing the script
    const { vars } = require("hardhat/config");

    // Go to https://infura.io, sign up, create a new API key
    // in its dashboard, and add it to the configuration variables
    const INFURA_API_KEY = vars.get("INFURA_API_KEY");

    // Add your Sepolia account private key to the configuration variables
    // To export your private key from Coinbase Wallet, go to
    // Settings > Developer Settings > Show private key
    // To export your private key from Metamask, open Metamask and
    // go to Account Details > Export Private Key
    // Beware: NEVER put real Ether into testing accounts
    const SEPOLIA_PRIVATE_KEY = vars.get("SEPOLIA_PRIVATE_KEY");

    module.exports = {
    solidity: "0.8.24",
    networks: {
        sepolia: {
        url: `https://sepolia.infura.io/v3/${INFURA_API_KEY}`,
        accounts: [SEPOLIA_PRIVATE_KEY],
        },
    },
    };
    ```
    - ***If you use alchemy API key***
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
    solidity: "0.8.24",
    networks: {
        sepolia: {
        url: `https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}`,
        accounts: [SEPOLIA_PRIVATE_KEY]
        }
    }
    };
    ```
    ![Image](<../src tutorial/Screenshot from 2024-04-17 18-38-32.png>)

## **Image for creating Alchemy API**
![Image](<../src tutorial/Screenshot from 2024-04-17 19-16-01.png>)
![Image](<../src tutorial/Screenshot from 2024-04-17 19-16-06.png>)
![Image](<../src tutorial/Screenshot from 2024-04-17 19-16-54.png>)


   - Before final depolyment
   - You have to set ALCHEMY API and SEPOLIA PRIVATE KEY.
   - To check you have already set or not alchemy api key and sepolia private key. 
   ```sh
   npx hardhat vars setup
   ```
   
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-55-16.png>)
   - To set alchemy api key cmd as follow.
   ```sh
   npx hardhat vars set ALCHEMY_API_KEY
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 19-34-35.png>)
   - To set sepolia private key cmd as follow.
   ```sh
   npx hardhat vars set SEPOLIA_PRIVATE_KEY
   ```
   ![Image](<../src tutorial/Screenshot from 2024-04-17 18-54-46.png>)



   - Finally, run to depoly:
   ```bash
   npx hardhat ignition deploy ./ignition/modules/Token.js --network sepolia
   ```
    
![Image](<../src tutorial/Screenshot from 2024-04-17 19-02-14.png>)
![Image](<../src tutorial/Screenshot from 2024-04-17 19-03-36.png>)

***If everything went well, you should see the deployed contract address.***

## **API request on alchemy**
![Image](<../src tutorial/Screenshot from 2024-04-17 19-12-40.png>)
![Image](<../src tutorial/Screenshot from 2024-04-17 19-13-11.png>)


**Thank you!!**

[For More Information Go Through..](https://hardhat.org/tutorial)