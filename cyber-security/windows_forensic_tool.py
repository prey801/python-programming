import win32evtlog
import datetime
import os

# Log source and investigator details
log_type = "Application"  # Changed to Application to detect malware simulator
investigator = "Investigator_1"
report_file = "forensic_report.txt"
custody_log = []

def log_chain_of_custody(action):
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "investigator": investigator
    }
    custody_log.append(entry)


def parse_event_logs():
    log_chain_of_custody("Started parsing Windows event logs")

    server = 'localhost'
    hand = win32evtlog.OpenEventLog(server, log_type)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    print(f"[*] Reading {total} events from '{log_type}' log...\n")
    suspicious = []

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    while events:
        for event in events:
            timestamp = event.TimeGenerated.Format()
            source = str(event.SourceName)
            event_id = str(event.EventID)
            category = str(event.EventCategory)
            description = event.StringInserts

            if description:
                description = " ".join(description)
                # Check for suspicious patterns including malware simulator
                suspicious_patterns = [
                    "failed", "unauthorized", "malware", "simulation", 
                    "harmlessmalwaresim", "suspicious files", "crashed",
                    "user info", "collection", "scan found"
                ]
                
                # Also check for specific Event ID used by malware simulator
                is_suspicious = any(pattern in description.lower() for pattern in suspicious_patterns)
                is_malware_sim = (event_id == "1337" and source == "HarmlessMalwareSim")
                
                if is_suspicious or is_malware_sim:
                    suspicious.append({
                        "timestamp": timestamp,
                        "source": source,
                        "event_id": event_id,
                        "description": description
                    })
        events = win32evtlog.ReadEventLog(hand, flags, 0)

    log_chain_of_custody("Finished parsing logs and collected suspicious entries")
    return suspicious


def generate_report(suspicious_entries):
    with open(report_file, "w", encoding='utf-8') as f:
        f.write("FORENSIC REPORT\n")
        f.write("========================\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Investigator: {investigator}\n\n")

        f.write("TOOLS USED:\n")
        f.write("- pywin32 (Windows Event Log Parser)\n\n")

        f.write("EVIDENCE COLLECTED:\n")
        for entry in suspicious_entries:
            f.write(f"{entry['timestamp']} - EventID: {entry['event_id']} - Source: {entry['source']}\n")
            f.write(f"Description: {entry['description']}\n\n")

        f.write("CHAIN OF CUSTODY:\n")
        for entry in custody_log:
            f.write(f"{entry['timestamp']} - {entry['action']} by {entry['investigator']}\n")

    print(f"[+] Report generated: {report_file}")


if __name__ == "__main__":
    print("=== Windows Forensic Investigation Tool ===\n")
    log_chain_of_custody("Started forensic investigation")

    suspicious_logs = parse_event_logs()
    generate_report(suspicious_logs)

    print("[*] Done. Check 'forensic_report.txt' for analysis results.\n")
