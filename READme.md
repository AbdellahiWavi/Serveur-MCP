# IA Agentique pour la Cyberdéfense avec MCP

## Description

Ce projet implémente une architecture de cyberdéfense agentique basée sur le protocole MCP (Model Context Protocol).

Le système utilise :

* Un LLM local : Ollama + Mistral
* Des serveurs MCP spécialisés
* MCP Inspector pour les tests
* Python + FastMCP

Le projet contient deux serveurs MCP :

* `network_server.py` : surveillance réseau
* `log_server.py` : analyse de logs

---

# Prérequis

Avant d’exécuter le projet, assurez-vous d’avoir installé :

## 1. Python 3.11+

Téléchargement :

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Vérification :

```bash
python --version
```

---

## 2. Node.js

Nécessaire pour MCP Inspector.

Téléchargement :

[https://nodejs.org/](https://nodejs.org/)

Vérification :

```bash
node -v
npm -v
```

---

## 3. Ollama

Téléchargement :

[https://ollama.com/](https://ollama.com/)

Installer ensuite le modèle Mistral :

```bash
ollama pull mistral
```

---

## 4. Installer Nmap

Téléchargement :

[https://nmap.org/download.html](https://nmap.org/download.html)

⚠ Important :
Ajouter Nmap au PATH Windows durant l’installation.

Vérification :

```bash
nmap --version
```

---

# Installation du projet

## 1. Cloner le dépôt GitHub

```bash
git clone https://github.com/AbdellahiWavi/Serveur-MCP.git
```

---

## 2. Entrer dans le dossier du projet

```bash
cd Serveur-MCP
```

---

## 3. Créer un environnement virtuel

```bash
python -m venv venv
```

---

## 4. Activer l’environnement virtuel

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
venv\Scripts\activate
```

---

## 5. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

Ou manuellement :

```bash
pip install mcp fastmcp
```

---

# Exécution des serveurs MCP

⚠ IMPORTANT :

Les deux serveurs MCP ne doivent pas être exécutés en même temps avec `mcp dev`.

Exécutez uniquement un serveur à la fois ou bien changer le port du serveur et le port du client.

---

# Lancer le serveur réseau

Le serveur `network_server.py` contient les outils de surveillance réseau :

* scan_ports()
* ping_host()
* check_connections()
* get_network_stats()

Commande :

```bash
mcp dev network_server.py
```

Après le lancement, MCP Inspector ouvrira automatiquement une interface web.

Par défaut :

```text
http://localhost:6274
```

---

# Lancer le serveur d’analyse de logs

Le serveur `log_server.py` contient les outils d’analyse de logs :

* read_logs()
* detect_bruteforce()
* analyze_errors()
* get_security_summary()

Commande :

```bash
mcp dev log_server.py
```

---

# Important

Ne lancez PAS les deux commandes simultanément :

****Mauvaise pratique :****

```bash
mcp dev network_server.py
mcp dev log_server.py
```

Cela peut provoquer :

* des conflits de ports
* des erreurs MCP Inspector
* des problèmes de communication STDIO

Mais vous pouvez executer le deux commandes simultanément en donnant à chaque serveur un port différent
***exemple :***
$env:CLIENT_PORT=8080; $env:SERVER_PORT=9000; npx @modelcontextprotocol/inspector python network_server.py
$env:CLIENT_PORT=9090; $env:SERVER_PORT=7070; npx @modelcontextprotocol/inspector python log_server.py


---

# Bonne pratique

Fermer le premier serveur avant de lancer le second.

Exemple :

1. Tester `network_server.py`
2. Fermer le terminal
3. Lancer ensuite `log_server.py`

---

# Validation avec MCP Inspector

MCP Inspector permet :

* de visualiser les outils MCP
* d’exécuter les fonctions
* de tester les paramètres
* de voir les réponses retournées

Exemple :

* tester `ping_host()`
* tester `scan_ports()`
* tester `detect_bruteforce()`

---

# Structure du Projet

```text
Serveur-MCP/
│
├── network_server.py
├── log_server.py
├── fake_logs.txt
├── requirements.txt
├── README.md
└── venv/
```

---

# Technologies Utilisées

| Composant           | Technologie      |
| ------------------- | ---------------- |
| Langage             | Python 3.11+     |
| LLM Local           | Ollama + Mistral |
| SDK MCP             | MCP Python SDK   |
| Framework MCP       | FastMCP          |
| Outil de test       | MCP Inspector    |
| Surveillance réseau | Nmap + Netstat   |
| Transport           | STDIO            |

---

# Auteurs

* Elwavi Abdellahi

---

# Dépôt GitHub

[https://github.com/AbdellahiWavi/Serveur-MCP](https://github.com/AbdellahiWavi/Serveur-MCP)
