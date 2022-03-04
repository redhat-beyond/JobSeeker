# Beyond-07-team-4

**Reqirements:**

Adding a Vagrantfile for spinning up a development VM.

Vagrant is a tool for using virtual machines to share development environments.
Learn more about it at:
https://www.vagrantup.com/

Please make sure you have Vagrant installed on your computer, if not then you can download from here:
https://www.vagrantup.com/downloads

Also, make sure that you have VirtualBox installed. VirtualBox is a hypervisor, which lets us create and run virtual machines.
The page below include links for downloading VirtualBox for various OS:
https://www.virtualbox.org/wiki/Downloads

In order for it all to work, please enable virtualization hardware on your computer. An explanation on how to do it can be found here:
https://www.virtualmetric.com/blog/how-to-enable-hardware-virtualization

Then, when you have all those you can bring up the VM by using the command: vagrant up.

Now that the Vagrant is up, we can verify everything is working by accessing it with the command: vagrant ssh
Now the prompt should show: [vagrant@localhost]$
