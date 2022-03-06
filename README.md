# Beyond-07-team-4

**Prerequisite:**

VirtualBox: VirtualBox is a hypervisor, which lets us create and run virtual machines.
The page below include links for downloading VirtualBox for various OS:
https://www.virtualbox.org/wiki/Downloads. 
During the installation process, Windows might pop-up some warning windows about installing 
device driver software, please confirm for it that the software should be installed.

Vagrant: Vagrant is a tool for using virtual machines to share development environments.
Learn more about it at:
https://www.vagrantup.com/. 
Please make sure you have Vagrant installed on your computer, if not then install the latest version of the Vagrant for your current operating system:
https://www.vagrantup.com/downloads. 

In order for it all to work, please enable virtualization hardware on your computer. An explanation on how to do it can be found here:
https://www.virtualmetric.com/blog/how-to-enable-hardware-virtualization. 

**How to run a project in VagrantBox:**

Create a folder in which the project will be placed.
Open the terminal and cd to the relevant directory:

*On Windows the commands to do so would be:

C: 

cd \src\placement_of_relevant_directory

*On Linux/Mac:

cd ~/src/placement_of_relevant_directory

Run the following commands:

1) vagrant init fedora/34-cloud-base - created the initial vagrantfile that marks the root directory of your project and 
   describes the machine and resources you need to run your project.
   
3) vagrant up - brings up the VM 

Now that the Vagrant is up, we can verify everything is working by accessing it with the command: 

vagrant ssh

Now the prompt should show: [vagrant@localhost]

**git clone project-url:**

In order to make modifications to the repository files and clone your copy of
the repository to your local machine, please use the following command (after cd to the relevant project's directory):

git clone https://github.com/redhat-beyond/Beyond-07-team-4.git

