# confirm our vagrant-docker-compose plugin is installed https://github.com/leighmcculloch/vagrant-docker-compose
%x(vagrant plugin install vagrant-docker-compose) unless Vagrant.has_plugin?('vagrant-docker-compose')

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/ubuntu-16.04"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 8000, host: 28000
  config.vm.network "forwarded_port", guest: 5432, host: 25432
  config.vm.network "forwarded_port", guest: 8024, host: 28024

  config.vm.provision :docker

  config.vm.provision :docker_compose,
                      yml: "/vagrant/development.yml",
                      rebuild: true,
                      run: "always"

end
