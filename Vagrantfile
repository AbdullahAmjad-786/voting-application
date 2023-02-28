Vagrant.configure("2") do |config|
  # Set the box to Ubuntu 20.04
  config.vm.box = "ubuntu/focal64"

  # Configure the virtual machine
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = "2"
  end

  # Set up a private network
  config.vm.network "private_network", ip: "192.168.33.10"

  # Provision the virtual machine with Ansible
  config.vm.provision "ansible" do |ansible|
    # Specify the Ansible playbook
    ansible.playbook = "ansible/playbook.yml"
    # Specify the inventory file
    ansible.inventory_path = "ansible/inventory"
    # Specify any extra variables required for the playbook
    ansible.extra_vars = {
      db_password: "admin",
      db_name: "votes",
      db_user: "admin"
    }
  end
end
