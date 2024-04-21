# Hardhat Boilerplate

This repository presents an exemplary project suitable as the initial framework for your Ethereum endeavor. It's also highly conducive to grasping the fundamentals of smart contract development.


This repository offers a model project to kickstart your Ethereum venture. It's designed to be an ideal resource for learning the foundational aspects of smart contract development.


## Quick start

The first things you need to do are cloning this repository and installing its
dependencies:

```sh
git clone https://github.com/NomicFoundation/hardhat-boilerplate.git
cd hardhat-boilerplate
npm install
```

Once installed, let's run Hardhat's testing network:

```sh
npx hardhat node
```

Then, on a new terminal, go to the repository's root folder and run this to
deploy your contract:

```sh
npx hardhat run scripts/deploy.js --network localhost
```

Finally, we can run the frontend with:

```sh
cd frontend
npm install
npm start
```

Open [http://localhost:3000/](http://localhost:3000/) to see your Dapp. You will
need to have [Metamask](https://metamask.io) installed and listening to `localhost 8545`.

## User Guide

You can find detailed instructions on using this repository and many tips in his [tutorial](../hardhat-tutorial/README.md).

- [Hardhat's full documentation](https://hardhat.org/docs/)

**Happy _building_!**
