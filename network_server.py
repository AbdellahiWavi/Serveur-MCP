from mcp.server.fastmcp import FastMCP
import subprocess
import socket
import json
from datetime import datetime

server = FastMCP(name="network-security")

@server.tool()
def scan_ports(host: str, port_range: str = "1-1024") -> dict:
    """Scanne les ports ouverts sur un hôte cible."""
    try:
        result = subprocess.run(['nmap', '-p', port_range, '-T4', host], 
                              capture_output=True, text=True, timeout=30)
        return {
            "host": host,
            "port_range": port_range,
            "output": result.stdout,
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e)}

@server.tool()
def ping_host(host: str) -> dict:
    """Vérifie si un hôte est joignable."""
    try:
        result = subprocess.run(['ping', '-n', '4', host], 
                              capture_output=True, text=True)
        return {
            "host": host,
            "output": result.stdout,
            "reachable": "temps" in result.stdout.lower() or "time" in result.stdout.lower()
        }
    except Exception as e:
        return {"error": str(e)}

@server.tool()
def check_connections() -> dict:
    """Liste les connexions réseau actives."""

    try:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if result.returncode != 0:
            return {
                "status": "error",
                "stderr": result.stderr
            }

        output = result.stdout or ""

        return {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "connections": output[:3000]
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


@server.tool()
def get_network_stats() -> dict:
    """Retourne les statistiques réseau."""

    try:
        result = subprocess.run(
            ["netstat", "-s"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if result.returncode != 0:
            return {
                "status": "error",
                "stderr": result.stderr
            }

        output = result.stdout or ""

        return {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "stats": output[:3000]
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    server.run(transport="stdio")