import time
import os
import glob
from datetime import datetime
import random
import re

LOG_DIR = "logs/log-2018-06-10"
TARGET_LOG = "logs/live_firefox.log"
DELAY_SECONDS = 0.1  # faster simulation

LOG_PATTERN = re.compile(r'^\d{2}:\d{2}:\d{2}\s+(INFO|DEBUG|WARN|WARNING|ERROR)')

log_files = sorted(glob.glob(os.path.join(LOG_DIR, "*.txt")))
if not log_files:
    print(f"No log files found in {LOG_DIR}")
    exit(1)

# remove old live log
if os.path.exists(TARGET_LOG):
    os.remove(TARGET_LOG)

print("🚀 Starting faster real-time log streaming simulation...")

# --- simulation loop ---
while True:
    # pick a random file
    file_path = random.choice(log_files)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # pick a random line
    line = random.choice(lines).strip()
    if line and LOG_PATTERN.match(line):
        now = datetime.now().strftime("%H:%M:%S")
        parts = line.split(None, 1)
        new_line = f"{now} {parts[1]}\n" if len(parts) == 2 else f"{now} {line}\n"

        with open(TARGET_LOG, "a", encoding="utf-8") as target:
            target.write(new_line)
            target.flush()

    time.sleep(DELAY_SECONDS)
