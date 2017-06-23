#### Note: Generally vagrant files are gitignore'd, but are not in this case to allow transfer to new projects.

### 1. Install basic requirements

* [Virtualbox] (https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/)

### 2. Start repo

Either fork this or create a new repo on github.

### 3. In repo, copy
    Vagrantfile
    vagrant.sh
    requirements.txt

These are the files that will be used to make the vagrant machine.

    Vagrantfile      - configures the machine
    vagrant.sh       - sets up the environment after the vm is configured. Installs mysql,
      sets un/ps to root/root, sets up a vritualenv, and installs requirements.txt
    requirements.txt - list of python packages installed with pip, callled by vagrant.sh, during configuration.

### 4. Create the machien and ssh in
	vagrant up
	vagrant ssh
	cd /vagrant
	source venv/bin/activate -- enter shell of virtualenv

### 5. Ensure requirements are configured, install any necessary
    pip freeze 
    pip install -r requirements.txt

### 6. If using this vm for just this project, can bypass the virtualenv and install requirements locally.

This also lets you sync the vagrant machine with pycharm (thus not requiring all dependencies to be installed locally for pycharm to not complain). You can sync pycharm by doing the following steps. Guide is [here](https://developer.rackspace.com/blog/a-tutorial-on-application-development-using-vagrant-with-the-pycharm-ide/):

1. Preferences > Project: XXX > Project Interpreter
1. Press gear button by the project interpreter text box and click **Add Remote**
1. Select Vagrant and navigate to vagrant machine
1. Click ok and it will do some ssh voodoo

### 7. Files are shared between local and vagrant machine, so develop locally and deploy on vagrant machine.

Can hit the deployed site on whatever port you exposed in Vagrantfile.