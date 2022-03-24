jfcli
========

CLI for running basic requests to Artifactory Cloud.

Preparing the Development
-------------------------

1. Ensure ''pip'' and ''pipenv'' are installed.
2. Clone repository: ''git clone https://github.com/davidpinhas/jfcli.git''
3. ''cd'' into the repository.
4. Fetch development dependencies ''make install''
5. Activate vrtualenv: ''pipenv shell''

Usage
-----

Pass in the Artifactory server name, user credentials and action to run.

Ping example:

::

    $ python3 jfcli -s server -u david -p password -a ping

System version example:

::

    $ python3 jfcli -s server -u david -p password -a version

Storage info example:

::

    $ python3 jfcli -s server -u david -p password -a storage_info

Running Tests
-------------

Run tests locally using ''make'' if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make
