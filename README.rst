======================
Cookiecutter Carol Online App
======================

.. image:: https://badge.buildkite.com/422ebd0246ac3ba16af48eb9d45fccf79452e5c739be48e187.svg
    :target: https://buildkite.com/totvslabs/cookiecutter-carol-app-online

Cookiecutter_ template for a Totvs Carol Online App.

* GitHub repo: https://github.com/totvslabs/cookiecutter-carol-app-online/

Features
--------

* Create batch, online and frontend features
* Simple initial config

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/totvslabs/cookiecutter-carol-app-online.git

Then:

* Initialize your Git local repository
* Create a repo and put it there.
* Check if your are running Python 3.6+ ``python --version``
* Install a virtualenv by running ``make venv``
* Activate your new Python Virtual Env: ``source .venv/bin/activate``
* Install all development required libs using: ``make dev``

Just run ``make`` to see all options you have.

Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
