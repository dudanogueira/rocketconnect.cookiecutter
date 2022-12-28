# Rocket Connect Cookie Cutter
Cookie cutter for Rocket.Connect

This is a simple script that guides you into deploying some nice open source projects.

Whats is [Cookiecutter](https://github.com/cookiecutter/cookiecutter)?
What is [Rocket.Connect](https://github.com/dudanogueira/rocket.connect/)?

WARNING!
======================
This is an under development structre. Feel free to create an issue or contribute with improvements.


Running
======================
on a regular, modern linux distro (Tested always on Ubuntu latest LTS), 

issue the folowing commands:

Install dependencies
======================
```
sudo apt-get install git python3-pip curl
curl -L https://get.docker.com | sh
```

Install Cookiecutter
====================
```
pip install cookiecutter
```


Point your domain at it
===========
If you are deploying on a server with public ip, point mycompany.com.br and *.mycompany.com.br to the server ip.

if you are deploying locally, or to test, do not choose lets encrypt, and set the domain to `mycompany.localhost` or just follow with defaults. You cal also expose ports when using it locally.

Cut a cookie from this repo
===========
```
cookiecutter https://github.com/dudanogueira/rocketconnect_cookiecutter
```

Select your cookie flavours
===========

Bellow is the "form" you will need to answer to cut this cookie.

At the end of it, you get simple commands on how to manage the stack.
This content will be available at a how_to_use.txt inside your project.

**The master password** is at the first line of your docker-compose.yml file, as well as at the how_to_use.txt
```
root@mycompany.com.br:~$ cookiecutter https://github.com/dudanogueira/rocketconnect_cookiecutter
project_name [My Company]: 
project_slug [mycompany]: 
domain [mycompany.localhost]:  mycompany.com.br
use_portainer [y]: 
use_traefik [y]: 
expose_ports [n]: 
use_letsencrypt [y]: 
add_traefik_labels [y]: 
email_for_letsencrypt [your@email.com]: 
use_rocketchat [y]: 
use_rocketconnect [y]: 
use_rocketchat_metrics [y]: 
use_wppconnect [y]: 
use_botpress [y]: 
######################

#
# INITIAL
#

MASTER ADMIN PASSWORD: admin / UHIuoHCR2C

# enter the project folder
cd mycompany

# create a public, attachable network:
docker network create --attachable traefik-public

# Run containers
docker compose up -d

# watch all logs
docker compose logs -f --tail=10

# access services
Complete the Wizard at: http://chat.mycompany.localhost
Use the master password at: http://traefik.mycompany.localhost/dashboard/
# RocketConnect, run the following commands inside deployment folder
docker compose run --rm rocketconnect python manage.py migrate
docker compose run --rm rocketconnect python manage.py createsuperuser --username admin

Use the created user at: http://rc.mycompany.localhost
Use the master password at: http://rc.mycompany.localhost/flower"+DJANGO_ADMIN_URL

    Use the master password at: http://grafana.mycompany.localhost
    Go to Dashboard > Manage > Rocket.Chat Metrics
# Or stop all containers
docker compose stop

# or only a few
docker compose logs -f --tail=10 traefik rocketchat rocketconnect

# list all VOLUMES used in this project
docker volume ls | grep mycompany_

# REMOVE all containers
docker compose rm

# REMOVE all VOLUMES used in this project - WARNING!!!
docker volume rm $(docker volume ls | grep mycompany_ | awk '{print $2}')
```

RoadMap
===========
- Create tests
- Create Terraform and Ansible options
- Support K8s (?)
- Add some more cool open source softwares
- Use LDAP
- Optionally Integrate with LDAP
- Optionally use docker swarm
- Security Check
- Call it 1.0

Proposed new open source (will not included directly, but on separate compose)
===========
- GroupOffice
- Magento
- Prestashop
- Wordpress
- ELK - Grafana, Prometheus
- Drupal / Joomla
- SuiteCRM
- Pentaho / Webspoon
- Orange HRM
- Wekan
- Gitlab
- cAdvisor
- Ansible Tower
- Jellyfin
- PenPot
