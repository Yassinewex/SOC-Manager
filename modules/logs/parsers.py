import re

SSH_FAIL = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")
SSH_OK = re.compile(r"Accepted \S+ for (\S+) from (\d+\.\d+\.\d+\.\d+)")

def parse_auth_line(line):
    if m := SSH_FAIL.search(line):
        return {"source": "ssh", "event_type": "auth_failure",
                "utilisateur": m[1], "ip_source": m[2], "message": line.strip()}
    if m := SSH_OK.search(line):
        return {"source": "ssh", "event_type": "auth_success",
                "utilisateur": m[1], "ip_source": m[2], "message": line.strip()}
    return None

def parse_wazuh_alert(a):
    d = a.get("data", {})
    win = d.get("win", {}).get("eventdata", {})
    return {
        "source": "wazuh",
        "utilisateur": d.get("dstuser") or win.get("targetUserName"),
        "ip_source": d.get("srcip") or win.get("ipAddress"),
        "event_type": "auth_failure" if "authentication_failed" in a["rule"].get("groups", []) else "alert",
        "message": a["rule"]["description"],
        "raw": a,
    }