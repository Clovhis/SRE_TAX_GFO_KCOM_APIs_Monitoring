from datetime import datetime

# ---------------------------------------------------------------------------
# Date Utilities
# Provides reusable helpers for formatting dates in log entries and requests.
# ---------------------------------------------------------------------------

def today():
    return str(datetime.now().strftime("%Y-%m-%d"))
