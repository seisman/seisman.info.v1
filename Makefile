PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

BRANCH = blog

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for SeisMan Blog Powered by Pelican						   '
	@echo '																	   '
	@echo 'Usage:															   '
	@echo '   make html                   (re)generate the web site			   '
	@echo '   make clean                  remove the generated files		   '
	@echo '   make regenerate             regenerate files upon modification   '
	@echo '   make publish                generate using production settings   '
	@echo '   make serve [PORT=8000]      serve site at http://localhost:8000  '
	@echo '   make devserver [PORT=8000]  start/restart develop_server.sh	   '
	@echo '   make stopserver             stop local server					   '
	@echo '   make github                 upload the web site via gh-pages	   '
	@echo '   make gitcafe                upload the web site via gitcafe-pages'
	@echo '   make import                 import output to blog branch		   '
	@echo '   make pdf                    convert updated rST to PDF		   '
	@echo '   make all                    upload web site to GitHub and Gitcafe'
	@echo '																	   '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	[ ! -d cache		] || rm -rf cache
	[ ! -d __pycache__	] || rm -rf __pycache__
	[ ! -e *.pyc		] || rm -rf *.pyc

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

pdf:
	python makepdf.py --update
	qrsync ~/.qiniu.conf

github:
	git push github $(BRANCH):master --force

gitcafe:
	git push gitcafe $(BRANCH):gitcafe-pages --force

import:
	ghp-import -b $(BRANCH) $(OUTPUTDIR) -m "`date +'%Y-%m-%d %H:%M:%S'`"

all: publish pdf import gitcafe github

.PHONY: html help clean regenerate serve devserver publish github gitcafe import all
