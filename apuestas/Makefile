#Makefile FJGM segundo hito

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;

install: clean
	python setup.py install
	
test: clean
	python manage.py test
	
run:
	python manage.py runserver
