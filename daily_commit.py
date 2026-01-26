# daily_commit.py
import os
from datetime import datetime
from github import Github

def make_daily_commit():
    # Add your changes here
    with open("daily_log.txt", "a") as f:
        f.write(f"Update: {datetime.now()}\n")
    
    # Git commands
    os.system("git add daily_log.txt")
    os.system(f'git commit -m "Daily commit: {datetime.now().date()}"')
    os.system("git push")

if __name__ == "__main__":
    make_daily_commit()
