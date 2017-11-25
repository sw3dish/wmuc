# wmuc

This repository is the source for WMUC Radio - College Park's website

It can be found at: [wmuc.umd.edu](https://wmuc.umd.edu)

## Getting started

To run a local copy of the site:

* Install Vagrant and VirtualBox
  * Install Vagrant's docker-compose plugin: `vagrant plugin install vagrant-docker-compose`
  * Install Vagrant's guest additions update: `vagrant plugin install vagrant-vbguest`
* Clone this repo (wmuc-site-docker)
  * `cd` into wmuc-site-docker
* Clone wmuc-site inside the wmuc-site-docker/app folder.
* Run `vagrant up`
* Run `vagrant ssh` to work in the Vagrant environment

When you're done:
* Run `vagrant halt`

### Prerequisites

Vagrant + VirtualBox
git
