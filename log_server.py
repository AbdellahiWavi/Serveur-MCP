from mcp.server.fastmcp import FastMCP
from collections import Counter
from pathlib import Path
from datetime import datetime
import re

server = FastMCP("log-analysis")

# ==================================================
# Création du fichier de logs simulé
# ==================================================

LOG_FILE = Path("simulated_auth.log")

if not LOG_FILE.exists():
    LOG_FILE.write_text(
        """Jan 15 10:23:45 sshd[1234]: Failed password for invalid user admin from 192.168.1.45 port 445
Jan 15 10:23:50 sshd[1235]: Failed password for invalid user root from 192.168.1.45 port 445
Jan 15 10:24:01 sshd[1236]: Failed password for invalid user admin from 10.0.0.23 port 22
Jan 15 10:24:05 sshd[1237]: Accepted password for user yassine from 192.168.1.100
Jan 15 10:25:10 sshd[1245]: Failed password for invalid user root from 172.16.0.7 port 22
""",
        encoding="utf-8"
    )

# ==================================================
# Lire les logs
# ==================================================

@server.tool()
def parse_auth_logs(n_lines: int = 50) -> dict:
    """Lit les dernières lignes du fichier de logs."""

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-n_lines:]

        return {
            "count": len(lines),
            "last_lines": [line.strip() for line in lines]
        }

    except Exception as e:
        return {"error": str(e)}

# ==================================================
# Détection brute-force
# ==================================================

@server.tool()
def detect_bruteforce(threshold: int = 2) -> dict:
    """Détecte les attaques brute-force."""

    try:
        ip_counter = Counter()

        failed_pattern = re.compile(
            r"Failed password .* from (\d+\.\d+\.\d+\.\d+)"
        )

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                match = failed_pattern.search(line)

                if match:
                    ip_counter[match.group(1)] += 1

        suspects = {
            ip: count
            for ip, count in ip_counter.items()
            if count >= threshold
        }

        return {
            "suspects": suspects,
            "total_suspects": len(suspects),
            "threshold": threshold,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        return {"error": str(e)}

# ==================================================
# Tentatives échouées
# ==================================================

@server.tool()
def get_failed_logins() -> dict:
    """Retourne toutes les tentatives échouées."""

    return detect_bruteforce(threshold=1)

# ==================================================
# Recherche regex
# ==================================================

@server.tool()
def search_log_pattern(
    pattern: str,
    logfile: str = "simulated_auth.log"
) -> dict:
    """Recherche un pattern regex dans un fichier de log."""

    try:
        with open(logfile, "r", encoding="utf-8") as f:
            content = f.read()

        matches = re.findall(pattern, content)

        return {
            "pattern": pattern,
            "matches": matches,
            "count": len(matches)
        }

    except Exception as e:
        return {"error": str(e)}

# ==================================================
# Main
# ==================================================

if __name__ == "__main__":
    print("[+] MCP Log Server started...")
    server.run(transport="stdio")