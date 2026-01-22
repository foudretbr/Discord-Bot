# Discord-Bot

Un bot Discord simple écrit en Python, conçu comme projet d'apprentissage et démonstration. Il fournit des commandes de modération (kick, ban, clear) et une commande utilitaire pour récupérer des images depuis l'API Pexels.

## Caractéristiques

- Commandes de modération : kick, ban, clear
- Commande d'image : `img` (récupère des images depuis l'API Pexels)
- Architecture en cogs (extensible)

## Prérequis

- Python 3.8+
- Un token de bot Discord (DISCORD_TOKEN)
- Une clé API Pexels (PEXELS_API_KEY) si vous souhaitez utiliser la commande `img`

Les dépendances du projet se trouvent dans `requirements.txt`.

## Installation

1. Clonez le dépôt (ou copiez les fichiers dans un dossier local).
2. Créez et activez un environnement virtuel (recommandé) :

	 python -m venv .venv
	 source .venv/bin/activate

3. Installez les dépendances :

	 pip install -r requirements.txt

4. Créez un fichier `.env` à la racine du projet et ajoutez les variables d'environnement nécessaires :

	 DISCORD_TOKEN=votre_token_discord
	 PEXELS_API_KEY=votre_cle_pexels  # optionnel — requis seulement pour la commande img

Ne partagez jamais votre token Discord publiquement.

## Configuration

Le bot lit le token et la clé Pexels depuis les variables d'environnement (via `python-dotenv`). Assurez-vous que `.env` contient correctement ces valeurs avant de lancer le bot.

## Utilisation

Lancer le bot :

	 python main.py

Le bot charge les cogs situés dans le dossier `cogs/`.

# Discord-Bot

Un bot Discord écrit en Python. Fournit des commandes de modération et une commande utilitaire pour récupérer des images depuis l'API Pexels.

## Caractéristiques

- Commandes de modération : `kick`, `ban`, `clear`
- Commande d'image : `img` (récupère des images depuis l'API Pexels)
- Conception modulaire avec cogs

## Prérequis

- Python 3.8 ou supérieur
- Un token de bot Discord (variable d'environnement `DISCORD_TOKEN`)
- (Optionnel) Clé API Pexels (`PEXELS_API_KEY`) pour la commande `img`

Les dépendances sont listées dans `requirements.txt`.

## Installation

1. Créez et activez un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

3. Créez un fichier `.env` à la racine du projet en copiant `.env.example` et en renseignant vos valeurs :

```text
DISCORD_TOKEN=your_discord_bot_token_here
PEXELS_API_KEY=your_pexels_api_key_here
```

## Exécution

Lancer le bot :

```bash
python main.py
```

Le bot charge les cogs présents dans le dossier `cogs/`.

## Commandes

- `kick <user> [reason]` — Exclut un utilisateur du serveur.
  - Permissions requises : `kick_members` (pour l'utilisateur) et pour le bot.

- `ban <user> [reason]` — Bannit un utilisateur du serveur.
  - Permissions requises : `ban_members` (pour l'utilisateur) et pour le bot.

- `clear <amount>` — Supprime un nombre spécifié de messages dans le canal.
  - Permissions requises : `manage_messages` (pour l'utilisateur) et pour le bot.

- `img <keyword> <amount>` — Renvoie des images depuis Pexels.
  - Paramètres : `keyword` (mot-clé), `amount` (nombre d'images, maximum 4)

## Structure du projet

```
.
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .env.example
└── cogs/
    ├── moderation.py
    └── troll.py
```

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE`.
