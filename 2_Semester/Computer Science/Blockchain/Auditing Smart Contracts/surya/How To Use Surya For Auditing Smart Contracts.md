# How To Use Surya For Auditing Smart Contracts.....
![Image](src/Global.png)
## What Is Surya ?
- Surya is a specific blockchain auditing tool.

## How To Install Surya ?
***Optional Step***

![Image](<src/Screenshot from 2024-04-14 16-21-48.png>)
```
mkdir surya && cd surya 
```

***Mandatory Step***
```
sudo su
```
![Image](<src/Screenshot from 2024-04-14 16-25-11.png>)
```
npm install -g surya
```
![alt text](<src/Screenshot from 2024-04-14 16-42-03.png>)
![alt text](<src/Screenshot from 2024-04-14 16-42-10.png>)
![alt text](<src/Screenshot from 2024-04-14 16-34-33.png>)
![alt text](<src/Screenshot from 2024-04-14 16-42-24.png>)
![alt text](<src/Screenshot from 2024-04-14 16-42-17.png>)
```
surya graph Contracts/Library.sol | dot -Tpng > Library.png
```
***Output***
+ ***Library***

![Image](src/Library.png)
+ ***Generic***

![Image](src/Generic.png)
+ ***Global***

![Image](src/Global.png)
+ ***Inheritance***

![Image](src/Inheritance.png)
+ ***V060***

![Image](src/V060.png)


## Flatten
- The flatten command outputs a flattened version of the source code, with all import statements replaced by the corresponding source code. Import statements that reference a file that has already been imported, will simply be commented out.
![alt text](<src/Screenshot from 2024-04-14 16-46-43.png>)
![alt text](<src/Screenshot from 2024-04-14 16-47-20.png>)
![alt text](<src/Screenshot from 2024-04-14 16-47-38.png>)
![alt text](<src/Screenshot from 2024-04-14 16-48-02.png>)
```
surya flatten Contracts/Library.sol
```


## Describe
- The describe command shows a summary of the contracts and methods in the files provided.
![alt text](<src/Screenshot from 2024-04-14 16-49-15.png>)
![alt text](<src/Screenshot from 2024-04-14 16-49-33.png>)
```
surya describe Contracts/Library.sol
```


## Inheritance
- The inheritance command outputs a DOT-formatted graph of the inheritance tree. For Windows machines, the > should be replaced with -o.

![alt text](<src/Screenshot from 2024-04-14 17-56-05.png>)
```
surya inheritance Contracts/Library.sol | dot -Tpng > Library1.png
```
***Output***
+ ***Library***

![alt text](src/Library1.png)
+ ***Generic***

![alt text](src/Generic1.png)
+ ***Global***

![alt text](src/Global1.png)
+ ***Inheritance***

![alt text](src/Inheritance1.png)
+ ***V060***

![alt text](src/V0601.png)
## Parse
- The parse command outputs a treefied AST object coming from the parser.
![alt text](<src/Screenshot from 2024-04-14 16-53-24.png>)
![alt text](<src/Screenshot from 2024-04-14 16-53-54.png>)
![alt text](<src/Screenshot from 2024-04-14 16-54-27.png>)
```
surya parse Contracts/Library.sol
```
***Output***



## Mdreport
- The mdreport command creates a Markdown description report with tables comprising information about the system's files, contracts and their functions. Much like describe but outputting to a nicely formatted Markdown file.
```
surya mdreport report_outfile.md Contracts/Library.sol
```
[Report File](report_outfile.md)

[For More Information Go Through..](https://github.com/Consensys/surya?tab=readme-ov-file)
