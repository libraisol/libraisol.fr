# Site vitrine de l'association LIBRaiSOL

Le thème est adapté du thème *html5-dopetrope* disponible sous la [licence] CCA 3.0 sur **html5up.net**.

Le site est généré via le moteur d'intégration continue de Gitlab-CE et
hébergé sur les pages de framagit.

## Installation

Après avoir téléchargé ou cloné le projet, vous pouvez installer le site statique de plusieurs façons.

### Dans un environnement virtuel Python
Lancez d'abord la commande :
```
pip install -r requirements.txt
```
Exécutez ensuite le serveur de développement :
```
make devserver
```
Le site est alors disponible à l'adresse `http://localhost:8000/`.

### Sur une distribution GNU/Linux
Il est nécessaire d'installer le paquet **Pelican**, par exemple sur une distribution Debian, en exécutant la commande :
```
apt install pelican
```
Exécutez ensuite le serveur de développement :
```
make devserver
```
Le site est alors disponible à l'adresse `http://localhost:8000/`.

### Dans un environnement Docker
Vous pouvez construire l'image à l'aide du fichier `Dockerfile` :
```
docker build -t debian-pelican .
```
Puis, vous exécutez cette image dans un conteneur :
```
docker run -d -p 80:80 debian-pelican
```
Le site est alors disponible à l'adresse `http://localhost`.

[licence]: https://html5up.net/license
