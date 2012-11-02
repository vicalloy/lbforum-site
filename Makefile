MGP = 
PY = ./env/bin/python
PIP = ./env/bin/pip
MG = $(PY) ./lbforum_site/manage.py

mg: 
	$(MG) $(MGP) 
init:
	python ./scripts/create_env.py
installreq:
	$(PIP) install -r requirements.txt
run:
	$(MG) runserver
test:
	$(MG) test dpress
rmpyc: 
	find ./lbforum_site/ -type f -name "*.pyc"|xargs rm -rf
