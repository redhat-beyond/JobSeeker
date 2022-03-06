# Job Seeker

**Job Seeker** is a web platform, built for people to post and find jobs.
It might serve students, freelancers or organzations.

## How To Run The Project

> NOTE: Depending on your OS, the commands in this README should be run with the following shells:
> - *Windows:* on **cmd** or **Powershell**.
> - *Linux:* on **terminal**.

### Prerequisites

You should install the following programs before proceeding:

- #### VirtualBox
    > VirtualBox is a hypervisor, which lets us create and run virtual machines.

    During the installation process, Windows might pop-up some warning windows about installing device driver software, please confirm for it that the software should be installed.
    VirtualBox supports various OS to host virtual machines.
    [Download VirtualBox Here!](https://www.virtualbox.org/wiki/Downloads)

- #### Vagrant
    > Vagrant is a tool for using virtual machines to share development environments.
    > Learn more about it [here](https://www.vagrantup.com/).
    > 
    Please make sure you have Vagrant installed on your computer, if not then install the latest version of Vagrant for your current operating system.
    [Download Vagrant Here!](https://www.vagrantup.com/downloads)

#### **ATTENTION:**
In order for it all to work, please enable **virtualization hardware** on your computer. An explanation on how to do it can be found [here](https://www.virtualmetric.com/blog/how-to-enable-hardware-virtualization).

---

### Run The Project

#### Download The Project

On your computer:
1. Navigate to the folder you wish to place the project at.

2. Download the project, and enter its folder.
   - In case you have [Git](https://git-scm.com/downloads) installed on your computer, then simply run:
     ```sh
     git clone https://github.com/redhat-beyond/Beyond-07-team-4
     ```
     Afterwards, enter the folder of the project by running:
     ```sh
     cd Beyond-07-team-4
     ```
   - Else, you can download the project like so:
     1. Press the green "Code" button.
     2. Press "Download ZIP".
     ![](https://i.imgur.com/t6VtSva.png)

#### Run The Application

Run the command:
```sh
vagrant up
```
This will bring up Vagrant and Virtualbox, to start the application.
> **ATTENTION:** If this is the first time you run this command, then a network connection is essential.

