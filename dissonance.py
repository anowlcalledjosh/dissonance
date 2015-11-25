#!/usr/bin/env python3

"""dissonance - a bot framework for Discord, written in Python using discord.py.

Copyright 2015 Josh Holland

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# http://semver.org
# 0.x.x versions are development, so API is to be considered unstable
__version__ = "0.1.0"


import logging
logging.basicConfig()

import discord
client = discord.Client()


class DissonanceError(Exception):
    pass


# This is function:expr, where function is called if bool(expr()).
# expr() should probably return a match object. We could accept a string and do
# re.match() on that, but we use functions for flexibility.
commands = {}

def register_command(condition):
    def wrap(command):
        commands[command] = condition
    return wrap


@client.event
def on_message(message):
    for command in commands:
        # The tntended usecase is that this returns a match object (for later
        # use in the actual command function).
        ret = commands[command](message)
        if ret:
            command(message, client, ret)


def main(email=None, password=None, ready="Connected to Discord!"):
    if email is None:
        email = input("Email: ")
    else:
        print("Email is " + email)  # Useful if password is input by hand.
    if password is None:
        import getpass
        password = getpass.getpass("Password: ")
    client.login(email, password)
    if not client.is_logged_in:
        raise DissonanceError("Discord login failed!")

    @client.event
    def on_ready():
        print(ready)

    try:
        client.run()
    except KeyboardInterrupt:
        client.logout()
        print()  # Give prompt on a new line.
        exit()  # Exit cleanly, don't give a massive stack trace for a Ctrl-C.
    except:
        client.logout()
        raise
