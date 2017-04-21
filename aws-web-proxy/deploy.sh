#!/bin/bash
setenforce 0
yum install epel-release -y && yum install git htop ansible -y
git clone https://github.com/mjaxolotl/aws-test-task.git
cd aws-test-task
ansible-playbook web-server.yml
