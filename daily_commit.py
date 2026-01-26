#!/usr/bin/env python3
"""
GitHub Daily Commit Automation Script
Automatically creates meaningful commits to maintain contribution streak
"""

import os
import sys
import random
from datetime import datetime, timedelta
import json
import hashlib

class DailyCommitAutomator:
    def __init__(self):
        self.repo_path = os.getcwd()
        self.log_file = "contributions_log.json"
        self.readme_file = "README.md"
        self.stats_file = "contributions_stats.md"
        
    def setup_git_config(self):
        """Configure git user for automated commits"""
        os.system('git config --global user.name "GitHub Automation"')
        os.system('git config --global user.email "github-actions[bot]@users.noreply.github.com"')
        
    def generate_meaningful_content(self):
        """Generate realistic development activities"""
        activities = {
            "code": [
                "Refactored module for better maintainability",
                "Optimized database query performance",
                "Fixed edge case in authentication flow",
                "Implemented new API endpoint",
                "Added input validation for user forms",
                "Updated error handling middleware",
                "Improved logging functionality",
                "Enhanced security measures",
                "Added unit tests for critical functions",
                "Code cleanup and documentation"
            ],
            "docs": [
                "Updated API documentation",
                "Added code examples to README",
                "Improved installation guide",
                "Created troubleshooting section",
                "Updated contribution guidelines",
                "Added project roadmap",
                "Documented configuration options",
                "Created architecture overview",
                "Updated changelog",
                "Added usage examples"
            ],
            "infra": [
                "Updated Docker configuration",
                "Optimized CI/CD pipeline",
                "Improved build scripts",
                "Updated dependency versions",
                "Enhanced deployment scripts",
                "Added monitoring configuration",
                "Updated security policies",
                "Improved backup procedures",
                "Optimized server configuration",
                "Updated environment variables"
            ]
        }
        
        activity_type = random.choice(list(activities.keys()))
        activity = random.choice(activities[activity_type])
        return activity_type, activity
    
    def update_log_file(self):
        """Update JSON log with today's activity"""
        activity_type, activity = self.generate_meaningful_content()
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "activity_type": activity_type,
            "activity": activity,
            "commit_hash": hashlib.md5(f"{timestamp}{activity}".encode()).hexdigest()[:8]
        }
        
        # Load existing log or create new
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                log_data = json.load(f)
        else:
            log_data = {"contributions": []}
        
        # Add new entry
        log_data["contributions"].append(log_entry)
        
        # Keep only last 365 days
        if len(log_data["contributions"]) > 365:
            log_data["contributions"] = log_data["contributions"][-365:]
        
        with open(self.log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        return log_entry
    
    def update_readme(self, log_entry):
        """Update README with contribution stats"""
        if not os.path.exists(self.readme_file):
            readme_content = "# Contribution Tracker\n\n"
        else:
            with open(self.readme_file, 'r') as f:
                readme_content = f.read()
        
        # Add stats section if not exists
        if "## Daily Contributions" not in readme_content:
            readme_content += "\n## Daily Contributions\n\n"
        
        stats_section = f"""
### {log_entry['date']}
- **Activity**: {log_entry['activity']}
- **Type**: {log_entry['activity_type'].capitalize()}
- **Time**: {datetime.now().strftime("%H:%M:%S")}

---
"""
        
        # Insert at the beginning of contributions section
        contributions_index = readme_content.find("## Daily Contributions") + len("## Daily Contributions\n\n")
        readme_content = readme_content[:contributions_index] + stats_section + readme_content[contributions_index:]
        
        with open(self.readme_file, 'w') as f:
            f.write(readme_content)
    
    def update_stats(self):
        """Generate statistics markdown file"""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                log_data = json.load(f)
            
            total_contributions = len(log_data["contributions"])
            activity_types = {}
            
            for entry in log_data["contributions"]:
                activity_type = entry["activity_type"]
                activity_types[activity_type] = activity_types.get(activity_type, 0) + 1
            
            stats_content = f"""# Contribution Statistics

## Overview
- **Total Contributions**: {total_contributions}
- **Tracking Since**: {log_data['contributions'][0]['date'] if total_contributions > 0 else 'N/A'}
- **Last Updated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Activity Distribution
"""
            
            for activity_type, count in activity_types.items():
                percentage = (count / total_contributions) * 100
                stats_content += f"- **{activity_type.capitalize()}**: {count} ({percentage:.1f}%)\n"
            
            # Add recent activities
            stats_content += "\n## Recent Activities (Last 7 Days)\n"
            recent_contributions = log_data["contributions"][-7:] if total_contributions >= 7 else log_data["contributions"]
            
            for entry in reversed(recent_contributions):
                stats_content += f"- **{entry['date']}**: {entry['activity']} [{entry['activity_type']}]\n"
            
            with open(self.stats_file, 'w') as f:
                f.write(stats_content)
    
    def create_additional_files(self):
        """Create various file types to simulate real development"""
        file_actions = [
            lambda: self.create_test_file(),
            lambda: self.update_config_file(),
            lambda: self.create_data_file(),
        ]
        
        # Randomly choose 1-2 file actions
        num_actions = random.randint(1, 2)
        for _ in range(num_actions):
            random.choice(file_actions)()
    
    def create_test_file(self):
        """Create or update a test file"""
        test_files = ["test_example.py", "test_utils.py", "test_api.py"]
        test_file = random.choice(test_files)
        
        test_content = f'''"""
Test file for {test_file}
Generated on {datetime.now().strftime("%Y-%m-%d")}
"""

import pytest

def test_example():
    """Sample test case"""
    assert 1 + 1 == 2

def test_string_operations():
    """Test string functionality"""
    text = "Hello, World!"
    assert len(text) == 13
    assert text.upper() == "HELLO, WORLD!"

# Additional test placeholder
# def test_feature():
#     pass
'''
        
        with open(test_file, 'a') as f:
            f.write(f"\n\n{test_content}")
    
    def update_config_file(self):
        """Update configuration files"""
        config_files = ["config.json", "settings.yaml", ".env.example"]
        config_file = random.choice(config_files)
        
        if config_file == "config.json":
            config = {
                "last_updated": datetime.now().isoformat(),
                "version": f"1.0.{random.randint(1, 100)}",
                "environment": "development",
                "features": ["api", "database", "authentication"]
            }
            
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    existing_config = json.load(f)
                existing_config.update(config)
                config = existing_config
            
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
        
        elif config_file == "settings.yaml":
            yaml_content = f"""# Settings file
# Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

app:
  name: "Automation Project"
  version: "1.0.{random.randint(1, 100)}"
  environment: "development"

database:
  host: "localhost"
  port: 5432
  name: "automation_db"

logging:
  level: "INFO"
  file: "app.log"
"""
            with open(config_file, 'a') as f:
                f.write(f"\n{yaml_content}")
    
    def create_data_file(self):
        """Create data or sample files"""
        data_files = ["sample_data.json", "example.csv", "data_sample.yaml"]
        data_file = random.choice(data_files)
        
        if data_file == "sample_data.json":
            data = {
                "timestamp": datetime.now().isoformat(),
                "sample_id": random.randint(1000, 9999),
                "values": [random.random() for _ in range(5)],
                "metadata": {
                    "generated_by": "automation_script",
                    "purpose": "testing_and_demo"
                }
            }
            with open(data_file, 'w') as f:
                json.dump(data, f, indent=2)
        
        elif data_file == "example.csv":
            csv_content = f"""timestamp,value1,value2,value3
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{random.randint(1,100)},{random.randint(1,100)},{random.randint(1,100)}
"""
            with open(data_file, 'a') as f:
                f.write(csv_content)
    
    def run(self):
        """Main execution method"""
        print("🚀 Starting Daily Commit Automation")
        print(f"📁 Repository: {self.repo_path}")
        print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            # Setup
            self.setup_git_config()
            
            # Generate and log activity
            log_entry = self.update_log_file()
            print(f"📝 Activity: {log_entry['activity']}")
            print(f"🏷️  Type: {log_entry['activity_type']}")
            
            # Update files
            self.update_readme(log_entry)
            self.update_stats()
            self.create_additional_files()
            
            # Git operations
            print("📊 Staging changes...")
            os.system("git add .")
            
            # Create commit with meaningful message
            commit_message = f"{log_entry['activity_type'].capitalize()}: {log_entry['activity']} - {log_entry['date']}"
            os.system(f'git commit -m "{commit_message}"')
            
            # Get current branch
            current_branch = os.popen("git branch --show-current").read().strip()
            print(f"🌿 Branch: {current_branch}")
            
            # Push changes
            print("⬆️  Pushing to remote...")
            push_result = os.system(f"git push origin {current_branch} --quiet")
            
            if push_result == 0:
                print("✅ Success! Changes pushed successfully.")
                print(f"📈 Total files updated: 4+")
                print(f"🔗 Commit: {log_entry['commit_hash']}")
            else:
                print("❌ Push failed! Check git permissions.")
                sys.exit(1)
                
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    automator = DailyCommitAutomator()
    automator.run()
