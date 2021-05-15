from __future__ import print_function

import os
import random
import string
import base64 
import hashlib

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

def generate_random_string(
    length, using_digits=False, using_ascii_letters=False, using_punctuation=False
):
    """
    Example:
        opting out for 50 symbol-long, [a-z][A-Z][0-9] string
        would yield log_2((26+26+50)^50) ~= 334 bit strength.
    """
    if not using_sysrandom:
        return None

    symbols = []
    if using_digits:
        symbols += string.digits
    if using_ascii_letters:
        symbols += string.ascii_letters
    if using_punctuation:
        all_punctuation = set(string.punctuation)
        # These symbols can cause issues in environment variables
        unsuitable = {"'", '"', "\\", "$"}
        suitable = all_punctuation.difference(unsuitable)
        symbols += "".join(suitable)
    return "".join([random.choice(symbols) for _ in range(length)])


def set_flag(file_path, flag, value=None, formatted=None, *args, **kwargs):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your system. "
                "Please, make sure to manually {} later.".format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value

def main():
    compose_file = os.path.join("docker-compose.yml")
    django_secret_key = set_flag(
        compose_file,
        "!!!SET DJANGO_SECRET_KEY!!!",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    DJANGO_ADMIN_URL = set_flag(
        compose_file,
        "!!!SET DJANGO_ADMIN_URL!!!",
        length=5,
        using_digits=True,
        using_ascii_letters=True,
    )
    master_admin_password = set_flag(
        compose_file,
        "!!!SET MASTER_ADMIN_PASSWORD!!!",
        length=10,
        using_digits=True,
        using_ascii_letters=True,
    )
    master_admin_password_pash = set_flag(
        compose_file,
        "!!!SET MASTER_ADMIN_PASSWORD_HASH!!!",
        value = '{SHA}'+base64.b64encode(hashlib.sha1(master_admin_password.encode('utf-8')).digest()).decode()
    )
    
    print("")
    print("####### TAKE NOTE!!!! #######")
    print("Master User/Password:  admin / {0}".format(master_admin_password))
    
    use_traefik = '{{ cookiecutter.use_traefik}}'
    if use_traefik == "y":
        print("Use the master password at: http://traefik.{{ cookiecutter.domain}}/dashboard/")

    use_rocketchat = '{{ cookiecutter.use_rocketchat}}'
    if use_rocketchat == "y":
        print("Use it at: http://chat.{{ cookiecutter.domain}}")

    use_rocketconnect = '{{ cookiecutter.use_rocketconnect}}'
    if use_rocketconnect == "y":
        print("for RocketConnect, run the following commands inside deploy folder")
        print("docker-compose run --rm rocketconnect python manage.py migrate")
        print("docker-compose run --rm rocketconnect python manage.py createsuperuser")
        print("")
        print("Use the created user at:  http://rc.{{ cookiecutter.domain}}/admin"+DJANGO_ADMIN_URL)
        print("Use the created user at: http://rc.{{ cookiecutter.domain}}")
        print("Use the master password at: http://rc.{{ cookiecutter.domain}}/flower"+DJANGO_ADMIN_URL)

    use_metabase = '{{ cookiecutter.use_metabase}}'
    if use_metabase == "y":
        print("Configure a new user at: http://metabase.{{ cookiecutter.domain}}")

    use_nextcloud = '{{ cookiecutter.use_nextcloud}}'
    if use_nextcloud == "y":
        print("Use the master password at: http://cloud.{{ cookiecutter.domain}}")

    use_odoo = '{{ cookiecutter.use_odoo}}'
    if use_odoo == "y":
        print("Configure a new user at: http://odoo.{{ cookiecutter.domain}}")

    use_mautic = '{{ cookiecutter.use_mautic}}'
    if use_mautic == "y":
        print("Configure a new user at: http://m.{{ cookiecutter.domain}}")

    use_glpi = '{{ cookiecutter.use_glpi}}'
    if use_glpi == "y":
        print("Configure a new user at: http://glpi.{{ cookiecutter.domain}}")

    print("######################")

    set_flag(
        compose_file,
        "!!!SET POSTGRES_USER!!!",
        length=8,
        using_digits=True,
        using_ascii_letters=True,
    )
    set_flag(
        compose_file,
        "!!!SET POSTGRES_PASSWORD!!!",
        length=8,
        using_digits=True,
        using_ascii_letters=True,
    )

if __name__ == "__main__":
    main()