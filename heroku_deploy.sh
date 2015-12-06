git clone https://github.com/javiergarridomellado/IV_javiergarridomellado.git
cd IV_javiergarridomellado
heroku keys:add
heroku git:clone -a prueba
heroku ps:scale web=1 --app prueba
heroku open --app prueba
