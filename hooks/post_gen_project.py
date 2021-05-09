from __future__ import print_function

import os
import random
import shutil
import string

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
    print("Master User/Password:  admin/{0}".format(master_admin_password))
    
    print("Use it at: http://{{ cookiecutter.domain}}/admin"+DJANGO_ADMIN_URL)
    print("Use it at: http://{{ cookiecutter.domain}}/flower"+DJANGO_ADMIN_URL)

    include_rocketchat = '{{ cookiecutter.include_rocketchat}}'
    if include_rocketchat == "y":
        print("Use it at: http://chat.{{ cookiecutter.domain}}")

    include_metabase = '{{ cookiecutter.include_metabase}}'
    if include_metabase == "y":
        print("Use it at: http://metabase.{{ cookiecutter.domain}}")


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