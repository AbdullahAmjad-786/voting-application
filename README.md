# Voting App with Vagrant and Ansible
This is a simple web application that allows users to vote for their favorite animal (cats or dogs). The votes are stored in a database and displayed on the results page. This version of the application uses Vagrant and Ansible to automate the deployment process.

Getting Started
Prerequisites
Before you can run the voting application, you will need to install the following software:

VirtualBox
Vagrant
Ansible

Clone the repository:
git clone https://github.com/AbdullahAmjad-786/voting-app.git
cd voting-app

Create and provision the Vagrant virtual machine:
vagrant up


SSH into the virtual machine:
vagrant ssh

Change to the voting-app directory:
cd /vagrant

Build the Docker images:
docker-compose build

Start the Docker containers:
docker-compose up

Access the voting application by going to http://localhost:5000 in your web browser.

Usage
To vote for a cat, click the "Vote for Cats" button.
To vote for a dog, click the "Vote for Dogs" button.
To view the results of the vote, click the "Results" button.
Scaling the Application
If you need to scale the application to handle increased loads, you can use the docker-compose up command with the --scale option to specify the number of replicas to run. For example, to run 3 replicas of the web service:

docker-compose up --scale web=3
