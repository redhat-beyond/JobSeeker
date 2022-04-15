
<p align="center">
    <a href="https://github.com/redhat-beyond">
        <img alt="Red Hat" src="https://img.shields.io/badge/Red%20Hat-EE0000?style=flat&logo=redhat&logoColor=white">
    </a>
    <a href="https://git-scm.com/">
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white">
    </a>
    <a href="https://www.vagrantup.com/">
        <img alt="Vagrant" src="https://img.shields.io/badge/vagrant-%231563FF.svg?style=flat&logo=vagrant&logoColor=white">
    </a>
    <a href="https://www.djangoproject.com/">
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white">
    </a>
    <a href="https://slack.com/">
        <img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white">
    </a>
    <a href="https://github.com/redhat-beyond/JobSeeker/blob/main/LICENSE">
        <img alt="LICENSE" src="https://img.shields.io/github/license/redhat-beyond/JobSeeker?style=flat">
    </a>
    <a href="https://github.com/redhat-beyond/JobSeeker/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/redhat-beyond/JobSeeker?style=flat">
    </a>
    <a href="https://github.com/redhat-beyond/JobSeeker/issues">
        <img alt="GitHub issues" src="https://img.shields.io/github/issues/redhat-beyond/JobSeeker?style=flat">
    </a>
</p>

<p align="center">
    <img src='https://svgshare.com/i/fFV.svg' height="130"/>
</p>


**Job Seeker** is a web platform, built for people to post and find jobs.
It might serve students, freelancers or organizations.

---

## :runner: How To Run The Project

### Prerequisites

You should install the following programs before proceeding:

- #### Git (*Advised For Downloading This Project*)
    > Git is a Version Control System (VCS) - the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time.

    We will use Git to download this project in the steps below.
    [Download Git Here!](https://git-scm.com/downloads)

- #### VirtualBox
    > VirtualBox is a hypervisor, which lets us create and run virtual machines.

    During the installation process, Windows might pop-up some warning windows about installing device driver software, please confirm for it that the software should be installed.
    VirtualBox supports various OS to host virtual machines.
    [Download VirtualBox Here!](https://www.virtualbox.org/wiki/Downloads)

- #### Vagrant
    > Vagrant is a tool for using virtual machines to share development environments.
    > Learn more about it [here](https://www.vagrantup.com/).
    
    Please make sure you have Vagrant installed on your computer, if not then install the latest version of Vagrant for your current operating system.
    [Download Vagrant Here!](https://www.vagrantup.com/downloads)

#### **ATTENTION:**
Ensure **virtualization hardware** is enabled in BIOS settings. An explanation on how to do it can be found [here](https://www.virtualmetric.com/blog/how-to-enable-hardware-virtualization).

---

### Run The Project

#### Download The Project
```sh
git clone https://github.com/redhat-beyond/JobSeeker
cd JobSeeker
``` 

#### Run The Application
```sh
vagrant up
```
This will bring up Vagrant and Virtualbox, to start the application.
> **ATTENTION:** If this is the first time you run this command, then a network connection is essential.

Afterwards, the web application will be presented on http://localhost:8000

---

## How To Remove The Project

- #### Destroy The Vagrant VM
    Run the command:
    ```sh
    vagrant destroy
    ```
    After running the last command, the terminal will prompt the following:
    ```sh
    default: Are you sure you want to destroy the 'default' VM? [y/N]
    ```
    Type: ` y `

- #### Delete The Project Root Directory
    Locate the project root directory on your computer and delete it.
---

## :memo: Documentation
More can be found [here!](docs)

