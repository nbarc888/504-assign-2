Video Link: 

Hello Everyone this is a tutorial on how to create a VM instance on Google Cloud with Flask Deployment


# First step is to get code set up and pre-upload code to github repo 
Code we are using for flask application is flaskapp.py

# Second step is to set up Google Cloud VM instance
Machine configuration settings for this instance used: 
Series: E2 , Preset machine type: e2=micro(2 vCPU, 1 core, 1GB memory) 
OS: Ubuntu ,Version Ubuntu 25.04 , Size 10GB
Ensure HTTP Traffic and HTTPS Traffic is allowed under networking category

# Launch VM then go to SHH
Insert following codes
Sudo apt update 
sudo apt install python3 python3-pip python3-venv
Git clone (insert link for flask template git repo) 
Ls -l to list down files within repo
Then cd (file) and repear ls -l
python -m venv venv
source venv/bin/activate
python flaskapp.py

# Firewall edit
Go into fire wall box to create a general rule to enable general public access rather than default access to 433. 
Scroll down to protocols and ports to TCP type in number then create. 
For Source ivp4 insert 0.0.0.0
