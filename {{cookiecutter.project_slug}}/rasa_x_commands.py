#!/bin/python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import argparse
import subprocess

logger = logging.getLogger(__name__)


def create_argparser():
    parser = argparse.ArgumentParser(description="runs the bot.")

    subparsers = parser.add_subparsers(help="sub-command help")

    create_user = subparsers.add_parser("create", help="creates a new Rasa X user")
    create_user.add_argument(
        "role",
        choices=["admin", "annotator", "tester"],
        help="Role of the user that gets created.",
    )
    create_user.add_argument("username", help="Name of the user to create")
    create_user.add_argument("password", help="Password to use for the user")
    create_user.add_argument(
        "--update", action="store_true", help="Update the password of an existing user"
    )
    create_user.set_defaults(func=create_rasa_x_user)

    create_saml_user = subparsers.add_parser(
        "create-saml", help="creates a new Rasa X SAML user"
    )
    create_saml_user.add_argument(
        "role",
        choices=["admin", "annotator", "tester"],
        help="Role of the user that gets created.",
    )
    create_saml_user.add_argument(
        "name_id", help="Name ID of the SAML user to be created"
    )
    create_saml_user.set_defaults(func=create_rasa_x_saml_user)

    delete_user = subparsers.add_parser("delete", help="delete a Rasa X user")
    delete_user.add_argument("username", help="Name of the user to delete")
    delete_user.add_argument(
        "--delete-created-conversations",
        action="store_true",
        help=(
            "Whether to delete interactive learning conversations created by "
            "this user."
        ),
    )
    delete_user.set_defaults(func=delete_rasa_x_user)

    return parser


def run_manage_users_command(command, success_log_message, error_log_message):
    """Run `manage_users.py` `command`.

    Args:
        command: `manage_users.py` command to run.
        success_log_message: Message to be printed on success.
        error_log_message: Message to obe printed on error.

    """
    create_cmd = "/app/scripts/manage_users.py {}".format(command)

    return_code = subprocess.call(
        "docker-compose exec rasa-x bash " '-c "python {}"'.format(create_cmd),
        shell=True,
    )

    if return_code == 0:
        logger.info(success_log_message)
    else:
        logger.error(error_log_message)
        exit(return_code)


def create_rasa_x_user(args):
    command = "create {} {} {} ".format(args.username, args.password, args.role)

    if args.update:
        command += " --update"

    run_manage_users_command(command, "Created user.", "Failed to create user.")


def create_rasa_x_saml_user(args):
    command = "create-saml {} {}".format(args.name_id, args.role)

    run_manage_users_command(
        command, "Created SAML user.", "Failed to create SAML user."
    )


def delete_rasa_x_user(args):
    command = "delete {}".format(args.username)
    if args.delete_created_conversations:
        command += " --delete-created-conversations"

    run_manage_users_command(command, "Deleted user.", "Failed to delete user.")


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")

    parsed = create_argparser().parse_args()
    # call the function associated with the sub parser (set_defaults)
    parsed.func(parsed)
