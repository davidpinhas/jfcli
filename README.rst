jfcli
========

CLI for running basic requests to Artifactory Cloud.

Preparing the Development
-------------------------

1. Ensure ''pip'' and ''pipenv'' are installed.
2. Clone repository: ''git clone git@github.com:example/jfcli''
3. ''cd'' into the repository.
4. Fetch development dependencies ''make install''
5. Activate vrtualenv: ''pipenv shell''

Usage
-----

Pass in the Artifactory server name, user credentials and action to run.

Ping example:

::

    $ jfcli testart --user david --password password --ping

System version example:

::

    $ jfcli testart --user david --password password --version

Running Tests
-------------

Run tests locally using ''make'' if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make
