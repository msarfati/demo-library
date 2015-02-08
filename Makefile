# Michael Sarfati
# Demo-Library project

SHELL=/bin/bash
PROJECT_NAME=Demo-Library
MOD_NAME=demo_library
CONFIG=etc/dev.conf

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	rm -rf build dist *.egg-info
	rm -rf docs/source/auto docs/build

server:
	SETTINGS=$$PWD/$(CONFIG) bin/manage.py runserver

shell:
	SETTINGS=$$PWD/$(CONFIG) bin/manage.py shell
	

.PHONY: clean install server db shell dbshell