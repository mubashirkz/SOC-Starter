import json
import re
from pathlib import Path

LOG_DIR = Path("logs")
OUTPUT_FILE = Path("alerts.json")

pattern = re.compile(
    r"^(?P<timestamp>.*?) \| "
    r"SRC_IP=(?P<source_ip>.*?) \| "
    r"EVENT=(?P<event_type>.*?) \| "
    r"SEVERITY=(?P<severity>.*?)$"
)


def parse_log(file_path):
    """Parse one SOC log file and return a normalized alert."""

    content = file_path.read_text(encoding="utf-8").strip()
    match = pattern.match(content)

    if not match:
        print(f"[WARNING] Could not parse {file_path.name}")
        return None

    return {
        "timestamp": match.group("timestamp"),
        "source_ip": match.group("source_ip"),
        "event_type": match.group("event_type"),
        "severity": match.group("severity"),
    }


def main():
    alerts = []

    for log_file in sorted(LOG_DIR.glob("*.log")):
        alert = parse_log(log_file)

        if alert:
            alerts.append(alert)

    OUTPUT_FILE.write_text(
        json.dumps(alerts, indent=4),
        encoding="utf-8"
    )

    print(f"Successfully normalized {len(alerts)} alerts.")
    print(f"Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()