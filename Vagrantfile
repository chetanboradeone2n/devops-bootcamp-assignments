Vagrant.configure("2") do |config|
    config.vm.box = "utm/debian11"

    config.vm.provider "utm" do |vb|
        vb.memory = "2048"
        vb.cpus = 2
    end

    config.vm.network "forwarded_port", guest:80, host:8080
end