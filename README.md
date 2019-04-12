[![PyPI version](https://badge.fury.io/py/avm.svg)](https://badge.fury.io/py/avm)
[![Build Status](https://travis-ci.org/ror6ax/avm.svg?branch=master)](https://travis-ci.org/ror6ax/avm)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
# avm

A tool for managing AWS default account, rvm-style.

Usage:

* `avm --add -f ~/Downloads/another_random_AWS_keypair.csv -a alias_that_makes_sense` to pull a profile into ~/.aws/credentials
* `avm --use your-profile-name` to set a profile as default
* `avm` to choose default profile from the list:

![list](list.png)

Installation:

* `pip install avm`
