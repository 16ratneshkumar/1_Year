<h1 align=center>HOW TO INSTALL DOCKER ON UBUNTU(AWS)</h1>


<br/>

#### What you’ll need (Required)
```
- 2 CPUs or more
- 2 GB of free memory
- 20 GB of free disk space
- Internet connection

NOTE : "t3.small" perfect for docker on aws.
```
<br/>

### STEP-1

<b>STEP-1 IS NOT MANDATORY</b>

#### Switch to root user & change hostname

```
$ sudo -i

$ hostnamectl set-hostname docker

$ bash
```

<br/>

### STEP-2

#### Uninstall old versions

```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

<br/>

### STEP-3

#### Set up the repository
```
$ sudo apt-get update

$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

<br/>

### STEP-4

#### Add Docker’s official GPG key
<h4>Full Form Of GPG=“GnuPrivacy Guard”</h4>
<p>why use GPG? because we don’t want to install unauthenticated packages to our Linux machine and risk our Linux machine and also to make sure users can communicate securely. GPG, or GNU Privacy Guard, is a public key cryptography implementation. This allows for the secure transmission of information between parties and can be used to verify that the origin of a message is genuine</p>

```
$ sudo mkdir -p /etc/apt/keyrings

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

<br/>

### STEP-5

#### Use the following command to set up the repository
```
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

<br/>

### STEP-6

#### Install Docker Engine
```
$ sudo apt-get update

$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

<br/>

### STEP-7

#### Start Docker service
```
$ systemctl start docker

$ systemctl enable docker

$ systemctl status docker
```

<br/>

### STEP-8

#### Check docker version

```
$ docker version

$ docker --version
```

<br/>

### STEP-9

#### Run demo sample container
```
$ docker container ls

$ docker image ls

$ docker run -itd httpd

$ docker container ls

$ docker image ls
```
