sudo apt-get install wget
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
cd ..
heroku login
heroku create
git add .
git commit -m "heroku deploy"
git push heroku master
heroku run python manage.py syncdb --noinput
heroku ps:scale web=1
heroku apps:rename ejemplodeploy
heroku open
