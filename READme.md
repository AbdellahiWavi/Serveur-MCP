# IA Agentique pour la Cyberdéfense avec MCP

## Description

Ce projet implémente une architecture de cyberdéfense agentique basée sur le protocole MCP (Model Context Protocol).

Le système utilise :

- Un LLM local : Ollama + Mistral
- Des serveurs MCP spécialisés
- MCP Inspector pour les tests
- Python + FastMCP

Le projet contient deux serveurs MCP :

- `network_server.py` : surveillance réseau
- `log_server.py` : analyse de logs

---

# Prérequis

Avant d’exécuter le projet, assurez-vous d’avoir installé les composants suivants.

---

## 1. Python 3.11+

Téléchargement :

https://www.python.org/downloads/

Vérification :

```bash
python --version
```

---

## 2. Node.js

Nécessaire pour MCP Inspector.

Téléchargement :

https://nodejs.org/

Vérification :

```bash
node -v
npm -v
```

---

## 3. Ollama

Téléchargement :

https://ollama.com/

Installer ensuite le modèle Mistral :

```bash
ollama pull mistral
```

---

## 4. Installer Nmap

Téléchargement :

https://nmap.org/download.html

⚠ Important :

Ajouter Nmap au PATH Windows durant l’installation.

Vérification :

```bash
nmap --version
```

---

# Installation du Projet

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

# Exécution des Serveurs MCP

## Important

Les deux serveurs MCP utilisent par défaut les mêmes ports MCP Inspector.

Par conséquent, exécuter les deux commandes simultanément avec `mcp dev` peut provoquer :

- des conflits de ports ;
- des erreurs MCP Inspector ;
- des problèmes de communication STDIO.

---

# Option 1 — Exécuter un seul serveur à la fois (Recommandé)

## Lancer le serveur réseau

Le serveur `network_server.py` contient les outils :

- `scan_ports()`
- `ping_host()`
- `check_connections()`
- `get_network_stats()`

Commande :

```bash
mcp dev network_server.py
```

---

## Lancer le serveur d’analyse de logs

Le serveur `log_server.py` contient les outils :

- `parse_auth_logs()`
- `detect_bruteforce()`
- `get_failed_logins()`
- `search_log_pattern()`

Commande :

```bash
mcp dev log_server.py
```

---

## Bonne pratique

1. Tester `network_server.py`
2. Fermer le terminal ou arrêter le serveur
3. Lancer ensuite `log_server.py`

---

# Option 2 — Exécuter les deux serveurs simultanément

Il est possible d’exécuter les deux serveurs en même temps à condition d’utiliser des ports différents pour chaque instance MCP Inspector.

---

## Exemple : serveur réseau

### PowerShell

```powershell
$env:CLIENT_PORT=8080
$env:SERVER_PORT=9000

npx @modelcontextprotocol/inspector python network_server.py
```

Interface MCP Inspector :

```text
http://localhost:8080
```

---

## Exemple : serveur logs

### PowerShell

```powershell
$env:CLIENT_PORT=9090
$env:SERVER_PORT=7070

npx @modelcontextprotocol/inspector python log_server.py
```

Interface MCP Inspector :

```text
http://localhost:9090
```

---

# Validation avec MCP Inspector

MCP Inspector permet :

- de visualiser les outils MCP ;
- d’exécuter les fonctions ;
- de tester les paramètres ;
- de visualiser les réponses retournées.

Exemples de tests :

- `ping_host()`
- `scan_ports()`
- `detect_bruteforce()`
- `search_log_pattern()`

---

# Structure du Projet

```text
Serveur-MCP/
│
├── network_server.py
├── log_server.py
├── simulated_auth.log
├── requirements.txt
├── README.md
└── venv/
```

---

# Technologies Utilisées

| Composant | Technologie |
|---|---|
| Langage | Python 3.11+ |
| LLM Local | Ollama + Mistral |
| SDK MCP | MCP Python SDK |
| Framework MCP | FastMCP |
| Outil de test | MCP Inspector |
| Surveillance réseau | Nmap + Netstat |
| Analyse de logs | Regex + Python |
| Transport MCP | STDIO |

---

# Auteurs

- Elwavi Abdellahi

---

# Dépôt GitHub

https://github.com/AbdellahiWavi/Serveur-MCP