tugger
======

Simple tool for running `Docker` based development environments with `Chef` and `Berkshelf` based provisioning.

Reads config from the `Tuggerfile` in your project's root folder and uses use a `tugger-stack` from another git
repository which contains the provisioning config for your development container.

You can find a Debian based LAMP `tugger-stack` here: https://github.com/joschi127/tugger-stack-lamp

To create your own provisioning config, just fork the repository of the `tugger-stack` and use the Git URL of your
own repository in your `Tuggerfile`.

Credits
-------

* Inspired by `Vagrant` and the `vagrant up` command - just run `tugger start` from your project folder and you're
ready to go
* `Chef` and `Berkshelf` based provisioning, originally based on the `Vagrant-LAMP-Stack` by MiniCodeMonkey
* And of course also thanks a lot to all the guys from `Docker`, `Chef`, `Berkshelf` and all the other great tools
we're using for this

Features
--------

* Should be as easy to use as `Vagrant` (having less features but being more lightweight)
* Should work out of the box on Linux and Mac (only `Docker` and standard tools lile `bash` or `git` are required)
* Faster and using less memory and disk space than `Vagrant` or other virtual machines, thanks to the power of
`Docker` containers (at least on Linux hosts)
* Automatic provisioning and reprovisioning
* Allows using a shared `Docker` image if you create several containers from the same `tugger-stack` to save disk
space and to allow creating new containers faster
* Automatically shares your project source files with the container
* Automatically shares your `~/.git` and `~/.ssh` settings folders with the container so you can use git and your
existing SSH keys from within the container
* Avoids nasty permission issues (e.g. by automatically running Apache and PHP with your own user's user id in
the `tugger-stack-lamp`)
* Automatically updates your `/etc/hosts` file so you can access your containers by using a fixed host name
* Automatically allocates mapped ports (required on Mac for direct access e.g. to the webserver running in the
container)
* Allows to override settings predefined in the `tugger-stack`'s chef.json file by setting extra chef.json data
in your Tuggerfile

Prerequisites
-------------

`Docker` has to be installed and your own user account has to be allowed to use it. (For most systems, add yourself
to the `docker` group and re-login.)

On Macs you have to use `boot2docker` in addition.

Quick start - using tugger for your project
-------------------------------------------

Install tugger if not already installed:

    git clone https://github.com/joschi127/tugger /some/target/path/tugger

Make it available as a global command: (optional)

    sudo ln -s /some/target/path/tugger/bin/tugger /usr/local/bin/tugger

Add a `Tuggerfile` to your project:

    cp /some/target/path/tugger/Tuggerfile.example /path/to/your/project/Tuggerfile
    # edit the file with your favorite text editor
    # feel free to add the file to your project's version control system

Start docker container by using `tugger`:

    tugger start

For more information have a look at the command reference:

    tugger --help
