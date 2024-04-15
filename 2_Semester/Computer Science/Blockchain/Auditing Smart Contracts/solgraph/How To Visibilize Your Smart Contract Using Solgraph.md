# How To Visibilize Your Smart Contract Using Solgraph.....
![OutputImage](src/MyContract.png)
## What Is Solgraph ?
- Solgraph is a tool used for visualizing the control flow of Solidity smart contracts. It can be helpful for analyzing the security of smart contracts by providing a visual representation of the control flow within the contract's code. This can assist in identifying potential vulnerabilities and understanding the overall structure of the contract.

***Legend:***
   * Red: Send to external address
   * Blue: Constant function
   * Yellow: View
   * Green: Pure
   * Orange: Call
   * Purple: Transfer
   * Lilac: Payable
## How To Install Solgraph ?
***Optional Step***

![Image](<src/Screenshot from 2024-04-14 10-44-08.png>)

```
mkdir solgraph 
```
```
cd solgraph
```
***Mandatory Step***
```
sudo su
```
![Image](<src/Screenshot from 2024-04-14 11-11-25.png>)
```
touch MyContract.sol
```
```
nano MyContract.sol
```
***This is the contant of a MyContract.sol file***
![Image](<src/Screenshot from 2024-04-14 11-10-24.png>)
```
touch MyContract.dot
```
```
touch MyContract.dot
```
***This is the contant of a MyContract.dot file***
![Image](<src/Screenshot from 2024-04-14 11-17-24.png>)

![Image](<src/Screenshot from 2024-04-14 10-48-04.png>)
```
sudo apt install npm
```
![Image](<src/Screenshot from 2024-04-14 11-12-16.png>)
```
npm install -g solgraph
```
Depending on your permissions, you may need to add the unsafe-perm flag:
![Image](<src/Screenshot from 2024-04-14 11-12-49.png>)
```
sudo npm install -g solgraph --unsafe-perm=true --allow-root
```
You have to have graphviz installed to render the DOT file as an image:
![Image](<src/Screenshot from 2024-04-14 11-13-15.png>)
```
apt install graphviz
```
![Image](<src/Screenshot from 2024-04-14 11-17-50.png>)
```
dot -Tpng MyContract.dot -o MyContract.png
```

[For More Information Go Through..](https://github.com/raineorshine/solgraph)