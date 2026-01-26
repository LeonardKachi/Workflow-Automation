# daily_commit.py
import os
from datetime import datetime
import random

def make_daily_commit():
    # Create a log file if it doesn't exist
    log_file = "daily_log.txt"
    
    # Add a random activity entry
    activities = [
        "Updated documentation",
        "Fixed minor bugs",
        "Code refactoring",
        "Added new feature",
        "Performance improvements",
        "Test updates",
        "Security patches",
        "Dependency updates"
    ]
    
    with open(log_file, "a") as f:
        activity = random.choice(activities)
        f.write(f"{datetime.now()}: {activity}\n")
        print(f"Added: {datetime.now()}: {activity}")
    
    # Git operations
    os.system("git add .")
    commit_message = f"Daily update: {datetime.now().strftime('%Y-%m-%d')}"
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin main")

if __name__ == "__main__":
    make_daily_commit()
