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
        ```
        sudo apt update
        sudo apt install curl git
        curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
        sudo apt-get install -y nodejs
        ```
        ### MacOS
        - ***Make sure you have git installed.***
        - Copy and paste these commands in a terminal:
        ```
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
        nvm install 20
        nvm use 20
        nvm alias default 20
        npm install npm --global # Upgrade npm to the latest version
        ```
   
   ### Upgrading your Node.js installation
   - If your version of Node.js is older and not supported by Hardhat follow the instructions below to upgrade.
        ### Ubuntu
        - Remove older version to run follow cmd:
        ```
        sudo apt remove nodejs
        ```

        ### MacOS
        - You can change your Node.js version using nvm. To upgrade to Node.js 20.x run these in a terminal:
        ```
        nvm install 20
        nvm use 20
        nvm alias default 20
        npm install npm --global # Upgrade npm to the latest version
        ```
## 2. Creating a new Hardhat project
   - ***we suggest you use npm 7 or higher for this.***
   - Open a new terminal and run these commands to create a new folder:
   ```
   mkdir hardhat-tutorial && cd hardhat-tutorial
   ```
   - Then initialize an npm project using following cmd:
   ```
   npm init
   ```
   - Now we can install Hardhat:
   ```
   npm install --save-dev hardhat
   ```
   - In the same directory where you installed Hardhat run:
   ```
   npx hardhat init
   ```
   - Select Create an empty hardhat.config.js with your keyboard and hit enter.

   ***When Hardhat is run, it searches for the closest hardhat.config.js file starting from the current working directory. This file normally lives in the root of your project and an empty hardhat.config.js is enough for Hardhat to work. The entirety of your setup is contained in this file.***

      ### Plugins




## 3. Writing and compiling smart contracts
- We're going to create a simple smart contract that implements a token that can be transferred. Token contracts are most frequently used to exchange or store value. 
   ### Writing smart contracts
   - Start by creating a new directory called contracts and create a file inside the directory called Token.sol.
   ```
   mkdir contracts && cd contracts
   ```
   ```
   touch Token.sol && nano Token.sol
   ```
   ***Paste the code below into the file and take a minute to read the code. It's simple and it's full of comments explaining the basics of Solidity.***
   ```
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
   ```
   npx hardhat compile
   ```
## 4. Testing contracts
- To test our contract, we are going to use Hardhat Network, a local Ethereum network designed for development. It comes built-in with Hardhat, and it's used as the default network. You don't need to setup anything to use it.
   ### Writing tests
   - For testing we are using chai library of javascript.
   - Create a new directory called test inside our project root directory and create a new file in there called Token.js.
   ```
   mkdir test && cd test
   ```
   ```
   touch Token.js && nano Token.js
   ```
   ***Paste this line into Token.js***
   ```
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
    ```
    npx hardhat test
    ```
    ### Using a different account(Optional)
    - If you need to test your code by sending a transaction from an account (or Signer in ethers.js terminology) other than the default one, you can use the connect() method on your ethers.js Contract object to connect it to a different account, like this:
    - ***Paste this code in your test/Token.js file***
    ```
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
    ```
    npx hardhat test
    ```
    ### Reusing common test setups with fixtures (Optional)
    - The two tests that we wrote begin with their setup, which in this case means deploying the token contract. In more complex projects, this setup could involve multiple deployments and other transactions. Doing that in every test means a lot of code duplication. Plus, executing many transactions at the beginning of each test can make the test suite much slower.
    - You can avoid code duplication and improve the performance of your test suite by using fixtures. A fixture is a setup function that is run only the first time it's invoked. On subsequent invocations, instead of re-running it, Hardhat will reset the state of the network to what it was at the point after the fixture was initially executed.
    - ***Paste this code in your test/Token.js file.***
    ```
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
    ```
    npx hardhat test
    ```
    ### Full coverage
    - Now that we've covered the basics that you'll need for testing your contracts, here's a full test suite for the token with a lot of additional information about Mocha and how to structure your tests. We recommend reading it thoroughly.
    - ***Paste this code in your test/Token.js file.***
    ```
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
    ```
    npx hardhat test
    ```
## 5. Debugging with Hardhat Network
   ### Solidity console.log
   - When running your contracts and tests on Hardhat Network you can print logging messages and contract variables calling console.log() from your Solidity code. To use it you have to import hardhat/console.sol in your contract code.
    ```
    pragma solidity ^0.8.0;

    import "hardhat/console.sol";

    contract Token {
    //...
    }
    ```





    ```
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
    - After pasteing this line to run following command:
    ```
    npx hardhat test
    ```
## 6. Deploying to a live network
