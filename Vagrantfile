Vagrant.configure("2") do |config|
    config.vm.network "public_network"
    config.vm.box = "utm/debian11"

    config.vm.provider "utm" do |vb|
        vb.memory = "2048"
        vb.cpus = 2
    end

    config.vm.network "forwarded_port", guest:8080, host:8080
    config.vm.network "forwarded_port", guest:8081, host:8081
    config.vm.network "forwarded_port", guest:8082, host:8082
    config.vm.network "forwarded_port", guest:5432, host:5432
    config.vm.provision "shell", path: "provision.sh"
end
