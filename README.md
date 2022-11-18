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
curl -L https://get.docker.com | sh
sudo apt-get install git python3-pip

Install Cookiecutter
====================
pip install cookiecutter

Cut a cookie from this repo
===========
cookiecutter https://github.com/dudanogueira/rocketconnect_cookiecutter

Select your cookie flavours
===========

Above is the "form" you will need to answer to cut this cookie.

At the end of it, you get simple cmomands on how to manage the stack.
This content will be available at a how_to_use.txt inside your project.

**The master password** is at the first line of your docker-compose.yml

    root@mycompany.com.br:~$ cookiecutter https://github.com/dudanogueira/rocketconnect_cookiecutter
    project_name [My Company]: 
    project_slug [mycompany]: 
    domain [mycompany.localhost]: mycompany.com.br
    use_portainer [y]: 
    use_traefik [y]: 
    expose_ports [n]: 
    use_letsencrypt [y]: 
    add_traefik_labels [y]: 
    email_for_letsencrypt [your@email.com]: 
    use_phpweb [y]: 
    use_rocketchat [y]: 
    use_rocketconnect [y]: 
    use_waautomate [y]: 
    use_wppconnect [y]: 
    use_metabase [y]: 
    use_nextcloud [y]: 
    use_odoo [y]: 
    use_mautic [y]: 
    use_limesurvey [y]: 
    use_glpi [y]: 
    use_moodle [y]:
    use_openproject [y]: 

    ####### TAKE NOTE!!!! #######
    Master User/Password:  admin / XXXXXXXXXX

    #
    # Website at: http://www.mycompany.com.br
    #
    # Use the master password at: http://traefik.mycompany.com.br/dashboard/
    # Use the master password at. ADMIN is adminrc: http://chat.mycompany.com.br
    # RocketConnect, run the following commands inside deploy folder
    docker-compose run --rm rocketconnect python manage.py migrate
    docker-compose run --rm rocketconnect python manage.py createsuperuser
    #
    # Use the created user at:  http://rc.mycompany.com.br/adminL32yP
    # Use the created user at: http://rc.mycompany.com.br
    # Use the master password at: http://rc.mycompany.com.br/flowerL32yP
    Configure a new user at: http://metabase.mycompany.com.br
    Use the master password at: http://cloud.mycompany.com.br
    Configure a new user at: http://odoo.mycompany.com.br
    Configure a new user at: http://m.mycompany.com.br
    Configure a new user at: http://glpi.mycompany.com.br
    User master password at: http://ead.mycompany.com.br
    User master password at: http://bot.mycompany.com.br
    ######################
    # MANAGEMENT AND BACKUP/RESTORE

    # enter the project folder
    cd mycompany

    # create a public, attachable network:
    docker network create --attachable traefik-public

    # Run base containers
    # some containers may encounter problems if postgres is not uphttps://github.com/dudanogueira/rocketconnect.cookiecutter
    # lets start them first and wait a little bit for the first run
    docker-compose up -d traefik postgres

    # Run other service
    # * after waiting a little bit.
    docker-compose up -d rocketchat
    docker-compose up -d rocketconnect
    docker-compose up -d metabase
    docker-compose up -d nextcloud
    docker-compose up -d ....

    # After the initial run, you can start all
    docker-compose up -d

    # Or stop all containers
    docker-compose stop

    # watch all logs
    docker-compose logs -f --tail=10

    # or only a few
    docker-compose logs -f --tail=10 traefik postgres rocketchat rocketconnect

    # list all VOLUMES used in this project
    docker volume ls | grep mycompany_

    # REMOVE all containers
    docker-compose rm

    # REMOVE all VOLUMES used in this project - WARNING!!!
    docker volume rm $(docker volume ls | grep mycompany_ | awk '{print $2}')



Point your domain at it
===========
If you deployed at a server with public ip, point mycompany.com.br and *.mycompany.com.br to the server ip.

if you are deploying locally, or to test, do not choose lets encript, and set the domain to myclient.localhost.

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

Proposed new open source
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
