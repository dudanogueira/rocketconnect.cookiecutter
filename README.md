# Rocket Connect Cookie Cutter
Cookie cutter for Rocket.Connect

This is a simple script to define how to deploy our connectings

WARNING!
======================
This is an under development structre. Feel free to create an issue or contribute with improvements.


Running
======================
on a regular, modern linux distro (Tested always on Ubuntu latest LTS), 

issue the folowing commands:

Install dependencies
======================
sudo apt-get install git docker docker-compose python3-pip

Install Cookiecutter
====================
pip install cookiecutter

Cut a cookie from this repo
===========
cookiecutter https://github.com/dudanogueira/rocketconnect_cookiecutter

Select your cookie flavours
===========

    me@mycompany.com.br:~/dev/v2$ cookiecutter rc_cookiecutter/
    project_name [My Company]: 
    project_slug [mycompany]: 
    domain [mycompany.localhost]: mycompany.com.br
    use_portainer [y]: 
    use_traefik [y]: 
    use_letsencrypt [y]: 
    add_traefik_labels [y]: 
    email_for_letsencrypt [your@email.com]: 
    use_phpweb [y]: 
    use_rocketchat [y]: 
    use_rocketconnect [y]: 
    use_waautomate [y]: 
    use_metabase [y]: 
    use_nextcloud [y]: 
    use_odoo [y]: 
    use_mautic [y]: 
    use_limesurvey [y]: 
    use_glpi [y]: 

    ####### TAKE NOTE!!!! #######
    Master User/Password:  admin / XXXXXXXXXX

    #
    # Website at: http://www.mycompany.com.br
    #

    Use the master password at: http://traefik.mycompany.com.br/dashboard/
    Use the master password at: http://chat.mycompany.com.br

    # RocketConnect, run the following commands inside deploy folder
    docker-compose run --rm rocketconnect python manage.py migrate
    docker-compose run --rm rocketconnect python manage.py createsuperuser

    Use the created user at:  http://rc.mycompany.com.br/adminRANDOMSTUFF
    Use the created user at: http://rc.mycompany.com.br
    Use the master password at: http://rc.mycompany.com.br/flowerRANDOMSTUFF
    Configure a new user at: http://metabase.mycompany.com.br
    Use the master password at: http://cloud.mycompany.com.br
    Configure a new user at: http://odoo.mycompany.com.br
    Configure a new user at: http://m.mycompany.com.br
    Configure a new user at: http://glpi.mycompany.com.br
    ######################

Point your domain at it
===========
If you deployed at a server with public up, point mycompany.com.br and *.mycompany.com.br to the server ip.

if you are deploying locally, or to test, do not choose lets encript, and set the domain to myclient.localhost.
