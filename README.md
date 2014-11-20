tugger
======

Simple tool for running Docker based development environments with Chef and Berkshelf based provisioning. Reads config
from the `Tuggerfile` in your project's root folder.

Will use a tugger-stack from another git repository which contains the provisioning config for your development
container.

You can find a Debian based LAMP tugger-stack here: https://github.com/joschi127/tugger-stack-lamp

To create your own provisioning config, just fork the repository of the tugger-stack and use the Git URL of your own
repository in your `Tuggerfile`.

Prerequisites
-------------

Docker has to be installed and your own user account has to be allowed to use it. (For most systems, add yourself to
the `docker` group and re-login.) 

Quick start - using tugger for your project
-------------------------------------------

Install tugger if not already installed:

    git clone https://github.com/joschi127/tugger /some/target/path/tugger

Make it available as a global command: (optional)

    sudo ln -s /some/target/path/tugger/bin/tugger /usr/local/bin/tugger

Add a `Tuggerfile` to your project:

    cp /some/target/path/tugger/Tuggerfile.example /path/to/your/project/
    # edit the file with your favorite text editor
    # feel free to add the file to your project's version control system

Start docker container by using `tugger`:

    tugger start

For more information have a look at the command reference:

    tugger --help
