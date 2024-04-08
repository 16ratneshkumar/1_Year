# How To Use Slither For Auditing Smart Contracts
![audit](https://github.com/16ratneshkumar/1_Year/assets/142919875/33703d7f-0772-4190-8851-723bae699117)

## What is Slither ?
- Slither is a Solidity static analysis framework based on Python 3. It is one of the most popular tools for smart contracts auditing. Slither has a wide range of vulnerability detectors, printers for visualization of the contract details, and API for custom analyses. It supports Solidity 0.4+ contracts and the audit time is fewer than 1 second per contract.

## Why Are Smart Contract Audits Important ?
- While blockchain technology is secure, blockchain applications have security vulnerabilities. One of the most famous security incidents involving smart contracts was the theft of $50 million in 2016. Hackers took advantage of vulnerable code in The DAO, a blockchain investment fund controlled through smart contracts. A smart contract security audit team can help mitigate such risks.

## How To Install Slither

```
sudo apt install software-properties-common
```

```
sudo add-apt-repository ppa:ethereum/ethereum
```

```
sudo apt install solc
```

- You should also install the solc-select. It is used for quick installation and switching between Solidity compiler versions.

```
pip3 install solc-select
```

```
solc-select use [VERSION] --always-install
```
- After the solc and solc-select are installed with no errors, we can proceed to the Slither installation. It can be done in three ways:

- ### Using Pip ( Recommended ):

```
pip3 install slither-analyzer
```

- ### Using GitHub:

```
git clone <https://github.com/crytic/slither.git> && cd slither python3 setup.py install
```

- ### Using Docker

```
docker pull trailofbits/eth-security-toolbox
```

***We can check the installation by running slither --version***

## How to check a smart contract using Slither
- After you defined a contract that you want to check, the easiest way is just to run slither [target]. The target can be specified in several ways:

    * Local copy of a contract file. 
    Example: slither SecureContract.sol

    * Project directory. 
    Example: slither /path/to/the/project/SecureProject

    * Mainnet contract address.
    Example: slither 0xf34960d9d60be18cC1D5Afc1A6F012A723a28811
