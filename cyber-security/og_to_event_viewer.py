import win32evtlogutil
import win32evtlog
import win32event
import win32api
import win32con
import servicemanager

APP_NAME = "CustomAppFailureSimulator"
EVENT_ID = 1001  # Custom event ID (between 1000–9999 for applications)

def log_failure_to_event_viewer():
    try:
        # Simulated crash (division by zero)
        print("Simulating application crash...")
        _ = 1 / 0
    except ZeroDivisionError as e:
        # Log error to Windows Event Viewer
        message = f"{APP_NAME} encountered an error: {str(e)}"
        print(f"[!] Logging error to Windows Event Viewer: {message}")
        
        win32evtlogutil.ReportEvent(
            APP_NAME,
            EVENT_ID,
            eventType=win32con.EVENTLOG_ERROR_TYPE,
            strings=[message],
            data=b"CrashTrace"
        )

if __name__ == "__main__":
    log_failure_to_event_viewer()
