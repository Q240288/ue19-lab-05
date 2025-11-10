# \# ue19-lab-05 : Client API Public - Chuck Norris Jokes

# 

# \## 📝 Description du Programme

# 

# Ce programme Python utilise la librairie `requests` pour interroger l'\*\*API publique Chuck Norris Jokes\*\* (`https://api.chucknorris.io/jokes/random`). Il récupère une blague aléatoire au format JSON et l'affiche dans la console. L'objectif est de démontrer l'utilisation de `requests` et la conteneurisation via Docker.

# 

# \## ⚙️ Installation et Exécution

# 

# Vous pouvez exécuter ce programme de deux manières : directement avec Python ou via un conteneur Docker.

# 

# \### 1. Exécution Locale (avec Python)

# 

# 1\.  \*\*Prérequis :\*\* Assurez-vous d'avoir Python 3 et `pip` installés.

# 2\.  \*\*Cloner le repository :\*\*

# &nbsp;   ```bash

# &nbsp;   git clone \[https://github.com/Q240288/ue19-lab-05.git](https://github.com/Q240288/ue19-lab-05.git)

# &nbsp;   cd ue19-lab-05

# &nbsp;   ```

# 3\.  \*\*Installer les dépendances :\*\*

# &nbsp;   ```bash

# &nbsp;   pip install -r requirements.txt

# &nbsp;   ```

# 4\.  \*\*Lancer le programme :\*\*

# &nbsp;   ```bash

# &nbsp;   python app.py

# &nbsp;   ```

# 

# \### 2. Exécution avec Docker

# 

# 1\.  \*\*Prérequis :\*\* Avoir Docker installé et en cours d'exécution sur votre système.

# 2\.  \*\*Cloner le repository :\*\* (Si ce n'est pas déjà fait)

# &nbsp;   ```bash

# &nbsp;   git clone \[https://github.com/Q240288/ue19-lab-05.git](https://github.com/Q240288/ue19-lab-05.git)

# &nbsp;   cd ue19-lab-05

# &nbsp;   ```

# 3\.  \*\*Construire l'image\*\* à l'aide du `Dockerfile` :

# &nbsp;   ```bash

# &nbsp;   docker build -t ue19-lab-05-joke .

# &nbsp;   ```

# 4\.  \*\*Lancer le conteneur\*\* :

# &nbsp;   ```bash

# &nbsp;   docker run --rm ue19-lab-05-joke

# &nbsp;   ```

# &nbsp;   (L'option `--rm` supprime le conteneur après son exécution pour un nettoyage automatique.)

