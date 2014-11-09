tugger
======

Simple tool for running Docker based development environments with Chef and Berkshelf based provisioning. Reads config
from the 'Tuggerfile' in your project's root folder.

Will use a tugger-stack from another git repository which contains the provisioning config for your development container.

You can find a Debian based LAMP stack here:

https://github.com/joschi127/tugger-stack-lamp

To create your own provisioning config, just fork the repository and use the Git URL of your own tugger-stack in your 'Tuggerfile'.
