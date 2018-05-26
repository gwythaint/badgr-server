# Badgr Server
*Digital badge management for issuers, earners, and consumers*

Badgr-server is the Python/Django API backend for issuing [Open Badges](http://openbadges.org). In addition to a powerful Issuer API and browser-based user interface for issuing, Badgr offers integrated badge management and sharing for badge earners. Free accounts are hosted by Concentric Sky at [Badgr.io](http://info.badgr.io), but for complete control over your own issuing environment, Badgr Server is available open source as a Python/Django application.

See also [badgr-ui](https://github.com/concentricsky/badgr-ui-prerelease), the Angular front end that serves as users' interface for this project.

### About the Badgr Project
Badgr was developed by [Concentric Sky](https://concentricsky.com), starting in 2015 to serve as an open source reference implementation of the Open Badges Specification. It provides functionality to issue portable, verifiable Open Badges as well as to allow users to manage badges they have been awarded by any issuer that uses this open data standard. Since 2015, Badgr has grown to be used by hundreds of educational institutions and other people and organizations worldwide. See [Project Homepage](https://badgr.org) for more details about contributing to and integrating with Badgr.

## How to get started on your local development environment.
Prerequisites:

* git
* python 2.7.x
* virtualenv
* mysql
* [cairo](https://www.cairographics.org/download/) (SVG utility)

#### Optional extras:

* memcached
* amqp broker (e.g. RabbitMQ)

#### System-specific requirements:
* OS X: [XCode Command line tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)
* Ubuntu 12.04 (install packages with apt-get): git, git-core, python-virtualenv, gcc, python-pip, python-devel, libjpeg-turbo, libjpeg-turbo-devel, zlib-devel, mariadb-devel, openldap-devel, cyrus-sasl-devel, swig, libxslt-devel, automake, autoconf, libtool, libffi-devel
* CentOS 7.x (install packages with yum): git, git-core, python-virtualenv, gcc, python-pip, python-devel, libjpeg-turbo, libjpeg-turbo-devel, zlib-devel, mariadb-devel, openldap-devel, cyrus-sasl-devel, swig, libxslt-devel, automake, autoconf, libtool, libffi-devel

Note: some of these packages would introduce additional security considerations if left installed on a server used in production.

### Create project directory and environment

* `mkdir badgr && cd badgr`
* `virtualenv env`
* `source env/bin/activate` *Activate the environment (each time you start a session working with the code)*

*Obtain source code and clone into code directory*

* `git clone https://github.com/concentricsky/badgr-server-prerelease.git code`
* `cd code`

*Your Directory structure will look like this with default logs and mediafiles locations:*
```
badgr
├── code
│   ├── apps
│   ├── docs
├── env
```

### Install requirements
*from within code directory*

* `pip install -r requirements.txt`

### Customize local settings to your environment
* `cp apps/mainsite/settings_local.py.example apps/mainsite/settings_local.py`
* Edit the settings_local.py file and insert local credentials for DATABASES and email, then run the following from within the `code` directory:

### Migrate databases, build front-end components
* `./manage.py migrate` - set up database tables
* `./manage.py dist` - generate docs swagger file(s)
* `./manage.py createsuperuser` - follow prompts to create your first admin user account

### Run a server locally for development
* `./manage.py runserver`
* Navigate to http://localhost:8000/staff
* login as your superuser you created above

API documentation is viewable at `/docs`

### Additional configuration options
Set these values in your settings_local.py file to configure the application to your specific needs. Required options are listed in bold.
* *HELP_EMAIL* (Required)
  - An email address for your support staff.
* BADGR_APPROVED_ISSUERS_ONLY:
  - If you choose to use the BADGR_APPROVED_ISSUERS_ONLY flag, this means new user accounts will not be able to define new issuers (though they can be added as staff on issuers defined by others) unless they have the Django user permission 'issuer.add_issuer'. The recommended way to grant users this privilege is to create a group that grants it in the `/staff` admin area and addthe appropriate users to that group.
* GOOGLE_ANALYTICS_ID:
  - Google Analytics code will be inserted into your pages if this is set to your account tracking code, e.g. 'UA-3929083373-2'. See https://support.google.com/analytics/answer/1008080
* PINGDOM_MONITORING_ID:
  - If you use Pingdom to monitor site performance, including this setting will embed Pingdom tracking script into the header.
* CELERY_ALWAYS_EAGER = True
  - Celery is an asynchronous task runner built into Django and Badgr. Advanced deployments may separate celery workers from web nodes for improved performance. For development environments where Celery tasks should run synchronously, set this flag to true. Very few tasks are part of this repository, and eager is a safe setting for most production deploys.
* OPEN_FOR_SIGNUP = True
  - This defaults to True, but allows you to turn off signup if you would like to use Badgr for only single-account use or to manually create all users in `/staff`.
* PAGINATION_SECRET_KEY:
  - Key used for symmetrical encryption of pagination cursors.  If not defined, encryption is disabled.  Must be 32 byte, base64-encoded random string.  For example: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
