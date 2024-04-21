# How To Install Latest Version Of Node js In Ubuntu...
## What Is NPM (Node Package Manager) ?
- NPM (Node Package Manager) Is Bundled With Node.Js And Automates Package And Dependency Management For Node.Js Projects. By Running “Npm Install,” Users Can Instantly Fetch And Install Project Dependencies. It Enables Version Control To Prevent Project Disruptions And Ensures Seamless Onboarding For New Contributors.

## Installing Default Or Latest Node.js.....
- 1. Install Node.js:
    ```
    sudo apt install -y nodejs
    ```
- 2. Once the install is complete, verify your Node.js installation:
    ```
    node -v
    ```
- 3. ***Optional:*** Enter the following command to install the Node Package Manager (NPM), which provides additional flexibility for Node.js management:
    ```
    sudo apt install -y npm
    ```
- 4. ***Optional:*** Verify your NPM version:
    ```
    npm -v
    ```


## Installing a Specific Version Of Node.js ....
- 1. For updating to the latest versions of all the relevant packages, use
    ```
    sudo apt update
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-40-33.png>)
- 2. Now use This to upgrade all the upgradable packages.
    ```
    sudo apt upgrade -y
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-41-10.png>)
- 3. Install CURL
    - First, you'll need to install curl if it's not installed on your system already. You can install curl by using the command below:
    ```
    sudo apt install curl -y
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-41-25.png>)
***Note: Now you'll need to follow these steps in order to ensure that you've installed Node.js successfully on your system.***
- 4. Obtain the Node.js source:
    - Version 16
    ```
    curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
    ```
    - Version 18
    ```
    curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    ```
    - Version 19
    ```
    curl -sL https://deb.nodesource.com/setup_19.x | sudo -E bash -
    ```
    - Version 20
    ```
    curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    ```
    - Version 21
    ```
    curl -sL https://deb.nodesource.com/setup_21.x | sudo -E bash -
    ```
- 5. Install the selected version of Node.js:
    ```
    sudo apt-get install -y nodejs
    ```
- 6. Verify that the correct version of Node.js is installed:
    ```
    node -v
    ```
- 7. Ensure that the most current version of NPM is installed:
    ```
    sudo npm install -g npm@latest
    ```
    ***Place Of Latest You Also Specify The Version***
- 8. Check the NPM version:
    ```
    npm -v
    ```

## Another Way To Install Specific Version Of Node Js After Install Curl...
- Install the Node Version Manager (NVM) by using the following command:
    ```
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-41-37.png>)
- Activate the NVM using the command below:
    ```
    source ~/.bashrc
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-45-36.png>)
- Now, you can ask NVM which versions of Node are available:
    ```
    nvm list-remote
    ```
- Install the latest Long Term Support version of Node by using the command below:
    ```
    nvm install --lts
    ```
    or
    ```
    nvm install v[version]
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-42-22.png>)
- Make the default LTS version as NVM
    - We have installed the latest LTS version of Node, but we also need to set the default version of NVM so that it gets used by default whenever we need it. You can use the command below to do that. 
    ```
    nvm alias default 20.12.2
    ```
- Confirm that Node was installed
    - Use the command below to check whether the default version is the exact version you just installed:
    ```
    node -v npm -v
    ```
    ![Image](<src/Screenshot from 2024-04-17 16-42-41.png>)

## For install or update npm use
```sh
npm install -g npm@[version]