wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
heroku login
heroku create
git add .
git commit -m "heroku deploy"
git push heroku master
heroku ps:scale web=1
heroku apps:rename ejemplo_deploy
heroku open
