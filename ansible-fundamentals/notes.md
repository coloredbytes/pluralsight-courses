<h1 align="center">Ansible Fundamentals </h1>

<h2 align="center"> :link: Table of Contents </h2>

+ [Introduction to Ansible](#%69%6E%74%72%6F%64%75%63%74%69%6F%6E%2D%74%6F%2D%61%6E%73%69%62%6C%65)
  + [What is Ansible?](#%77%68%61%74%2D%69%73%2D%61%6E%73%69%62%6C%65%3F)
+ [Setting up Ansible](#%73%65%74%74%69%6E%67%2D%75%70%2D%61%6E%73%69%62%6C%65)
  + [Ansible Architecture](#%61%6E%73%69%62%6C%65%2D%61%72%63%68%69%74%65%63%74%75%72%65)
  + [Installing Ansible](#%69%6E%73%74%61%6C%6C%69%6E%67%2D%61%6E%73%69%62%6C%65)
  + [Two Distributions](#%74%77%6F%2D%64%69%73%74%72%69%62%75%74%69%6F%6E%73)
  + [Ansible Project Structure.](#%61%6E%73%69%62%6C%65%2D%70%72%6F%6A%65%63%74%2D%73%74%72%75%63%74%75%72%65%2E)
  + [Demo: Installing Ansible using `pip`](#%64%65%6D%6F%3A%2D%69%6E%73%74%61%6C%6C%69%6E%67%2D%61%6E%73%69%62%6C%65%2D%75%73%69%6E%67%2D%60%70%69%70%60)


## Introduction to Ansible

**Overview**

- What is Ansible?
- Why Ansible?
- Understanding IaC

### What is Ansible?

**Congiuration Managment (CM)**
- Process of systematically managing, organizing and controlling changes in the system. Helps in establishing and maintaining consistency of the systems's performance and its functional and physical attributes.

**Some History**

- Free and open-source CM automation platform
- Written by Michael DeHaan in 2012; acquired by Red Hat in 2015

**Other Info**

Can Deploy to bare metal, virtual, and cloud hosts running **Linux, macOS, and Windows**.

## Setting up Ansible

### Ansible Architecture

- `Control Node`: Node that has Ansible installed.
- `Managed Node`: Node that is in the Ansible inventory.

### Installing Ansible
<details>
<summary> Click Here </summary>

- Ubuntu

```bash
sudo apt update
sudo apt install ansible
```

- RHEL

```bash
sudo yum install ansible
```
- Python Pip

```bash
pip install ansible
```
- Source

```bash
git clone https://github.com/ansible/ansible.git
cd ansible
source hacking/env-setup
```
</details>


### Two Distributions

- `ansible-core`: Just the essentials: command-line tools and essential modules.
-  `ansible`: "**Batteries included**" and provides a collection of modules, plugins and roles.

> [!NOTE]
> Installation method depends on your Linux distribution.
> - Windows control nodes require WSL.
> - **Think in terms of python!**

### Ansible Project Structure.

<details>
<summary> Click Here </summary>

```
ansible-project/
├── ansible.cfg
├── inventory/
│   ├── development
│   └── production
├── playbooks/
│   ├── webservers.yml
│   └── dbservers.yml
├── roles/
│   ├── common/
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── templates/
│   │   ├── files/
│   │   ├── vars/
│   │   │   └── main.yml
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── meta/
│   │   │   └── main.yml
│   ├── webserver/
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── templates/
│   │   │   └── httpd.conf.j2
│   │   ├── files/
│   │   ├── vars/
│   │   │   └── main.yml
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── meta/
│   │   │   └── main.yml
└── group_vars/
    ├── all.yml
    └── webservers.yml
```
</details>

### Demo: Installing Ansible using `pip`

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
```
- Add this to your `.bashrc`

```bash
export PATH=$PATH:$HOME/.local/bin
exec bash
```
- Installing ansible with pip

```bash
python3 -m pip install --user ansible
```


