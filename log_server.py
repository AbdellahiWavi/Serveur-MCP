from mcp.server import MCPServer, tool
from collections import Counter
import re
from pathlib import Path
from datetime import datetime

server = MCPServer(name="log-analysis")

# Créer un fichier de logs simulé si on n'est pas sous Linux
LOG_FILE = Path("simulated_auth.log")

if not LOG_FILE.exists():
    with open(LOG_FILE, "w") as f:
        f.write("""Jan 15 10:23:45 sshd[1234]: Failed password for invalid user admin from 192.168.1.45 port 445
Jan 15 10:23:50 sshd[1235]: Failed password for invalid user root from 192.168.1.45 port 445
Jan 15 10:24:01 sshd[1236]: Failed password for invalid user admin from 10.0.0.23 port 22
Jan 15 10:24:05 sshd[1237]: Accepted password for user yassine from 192.168.1.100
Jan 15 10:25:10 sshd[1245]: Failed password for invalid user root from 172.16.0.7 port 22
""")

@server.tool()
def parse_auth_logs(n_lines: int = 50) -> dict:
    """Lit les dernières lignes du log d'authentification."""
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()[-n_lines:]
    return {"last_lines": lines, "count": len(lines)}

@server.tool()
def detect_bruteforce(threshold: int = 5) -> dict:
    """Détecte les attaques par force brute."""
    ip_counter = Counter()
    failed_pattern = re.compile(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)")
    
    with open(LOG_FILE, "r") as f:
        for line in f:
            match = failed_pattern.search(line)
            if match:
                ip_counter[match.group(1)] += 1
                
    suspects = {ip: count for ip, count in ip_counter.items() if count >= threshold}
    
    return {
        "suspects": suspects,
        "total_suspects": len(suspects),
        "threshold": threshold,
        "timestamp": datetime.now().isoformat()
    }

@server.tool()
def get_failed_logins() -> dict:
    """Retourne les tentatives de connexion échouées."""
    return detect_bruteforce(threshold=1)

@server.tool()
def search_log_pattern(pattern: str, logfile: str = "simulated_auth.log") -> dict:
    """Recherche un motif regex dans un fichier de log."""
    try:
        with open(logfile, "r") as f:
            content = f.read()
        matches = re.findall(pattern, content)
        return {"pattern": pattern, "matches": matches, "count": len(matches)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    server.run(transport="stdio")