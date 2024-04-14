## Sūrya's Description Report

### Files Description Table


|  File Name  |  SHA-1 Hash  |
|-------------|--------------|
| Contracts/Library.sol | [object Promise] |


### Contracts Description Table


|  Contract  |         Type        |       Bases      |                  |                 |
|:----------:|:-------------------:|:----------------:|:----------------:|:---------------:|
|     └      |  **Function Name**  |  **Visibility**  |  **Mutability**  |  **Modifiers**  |
||||||
| **Tester** | Implementation |  |||
| └ | useLib1 | Public ❗️ |   |NO❗️ |
| └ | useLib2 | Public ❗️ |   |NO❗️ |
| └ | useLib3 | Public ❗️ |   |NO❗️ |
||||||
| **Lib1** | Library |  |||
| └ | returnMe | Public ❗️ |   |NO❗️ |
| └ | returnMe2 | Internal 🔒 |   | |
||||||
| **Lib2** | Library |  |||
| └ | returnMe | Public ❗️ |   |NO❗️ |
||||||
| **Lib3** | Library |  |||
| └ | returnMe | Public ❗️ |   |NO❗️ |
||||||
| **Tester2** | Implementation |  |||
| └ | useInternalOnly | Public ❗️ |   |NO❗️ |
| └ | usePublic | Public ❗️ |   |NO❗️ |
||||||
| **testShort** | Library |  |||
| └ | something | Internal 🔒 |   | |
| └ | something2 | Public ❗️ |   |NO❗️ |


### Legend

|  Symbol  |  Meaning  |
|:--------:|-----------|
|    🛑    | Function can modify state |
|    💵    | Function is payable |
