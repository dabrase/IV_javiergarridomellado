from fabric.api import run, local, hosts, cd
from fabric.contrib import django



def install_run():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull javiergarridomellado/iv_javiergarridomellado:apuestas')
	run('sudo docker run -i -t javiergarridomellado/iv_javiergarridomellado:apuestas /bin/bash')
