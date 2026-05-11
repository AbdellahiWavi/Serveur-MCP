# Configuration du Serveur MCP - Network Security

Ce répertoire contient la configuration pour intégrer le serveur MCP de sécurité réseau avec Continue.

## Fichiers de Configuration

- **config.json** - Configuration principale de Continue avec le serveur MCP
- **config.yaml** - Configuration alternative en YAML
- **mcpServers/new-mcp-server.yaml** - Définition détaillée du serveur MCP
- **agents/new-config.yaml** - Configuration de l'agent

## Outils Disponibles

Le serveur MCP expose les outils suivants:

1. **scan_ports** - Scanne les ports ouverts sur un hôte
   - Paramètres: host (string), port_range (string, optional)
   
2. **ping_host** - Vérifie la disponibilité d'un hôte
   - Paramètres: host (string)
   
3. **check_connections** - Vérifie les connexions réseau actives
   
4. **get_network_stats** - Récupère les statistiques réseau

## Utilisation avec Continue

Le serveur MCP est automatiquement découvert par Continue via le fichier config.json.
Les outils peuvent être utilisés via les commandes slash:
- `/scan` - Scanner les ports d'un hôte
- `/network-check` - Vérifier l'état du réseau
