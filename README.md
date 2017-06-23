1. Start repo

2. In repo, copy
    Vagrantfile
    vagrant.sh
    requirements.txt

   These are the files that will be used to make the vagrant machine. 
   Vagrantfile      - configures the machine  
   vagrant.sh       - sets up the environment after the vm is configured. Installs mysql, 
   				        sets un/ps to root/root, sets up a vritualenv, and installs requirements.txt
   requirements.txt - list of python packages installed with pip, callled by vagrant.sh, during configuration.

3. Create the machien and ssh in
	vagrant up
	vagrant ssh
	  cd /vagrant
	source venv/bin/activate -- enter shell of virtualenv

4. Ensure requirements are configured, install any necessary
    pip freeze 
    pip install -r requirements.txt

5. If using this vm for just this project, can bypass the virtualenv and install requirements locally.
    This also lets you sync the vagrant machine with pycharm (thus not requiring all dependencies to be
    installed locally for pycharm to not complain). You can sync pycharm by:
      a. Preferences > Project: XXX > Project Interpreter
      b. Press gear button by the project interpreter text box and click ADD REMOTE
      c. Select Vagrant and navigate to vagrant machine
      d. Click ok and it will do some ssh voodoo but voila you're there*

6. Files are shared between local and vagrant machine, so develop locally and deploy on vagrant machine. 
     Can hit the deployed site on whatever port you exposed in Vagrantfile. 



* https://developer.rackspace.com/blog/a-tutorial-on-application-development-using-vagrant-with-the-pycharm-ide/