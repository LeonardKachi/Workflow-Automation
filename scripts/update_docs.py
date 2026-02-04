#!/usr/bin/env python3
"""
Process project data and generate analytics
"""
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from pathlib import Path

def generate_data_analytics():
    """Generate meaningful data analytics"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Generate or update dataset
    dataset_path = data_dir / "dataset.json"
    
    if dataset_path.exists():
        with open(dataset_path, 'r') as f:
            data = json.load(f)
    else:
        # Initial dataset
        data = {
            "created": datetime.now().isoformat(),
            "metrics": [],
            "statistics": {}
        }
    
    # Add new metric entry
    new_metric = {
        "timestamp": datetime.now().isoformat(),
        "random_metric": np.random.randint(1, 100),
        "performance_score": round(np.random.uniform(0.5, 1.0), 3)
    }
    data["metrics"].append(new_metric)
    
    # Calculate statistics
    if data["metrics"]:
        df = pd.DataFrame(data["metrics"])
        data["statistics"] = {
            "total_entries": len(df),
            "avg_random_metric": round(df["random_metric"].mean(), 2),
            "avg_performance": round(df["performance_score"].mean(), 3),
            "last_updated": datetime.now().isoformat()
        }
    
    # Save updated data
    with open(dataset_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Generate analytics markdown
    analytics_md = f"""# Project Analytics Report

## 📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### 📊 Current Statistics
- **Total Data Points**: {data['statistics'].get('total_entries', 0)}
- **Average Metric**: {data['statistics'].get('avg_random_metric', 0)}
- **Performance Score**: {data['statistics'].get('avg_performance', 0)}

### 📈 Recent Metrics
"""
    
    # Add recent entries
    for metric in data["metrics"][-5:]:  # Last 5 entries
        ts = datetime.fromisoformat(metric["timestamp"])
        analytics_md += f"- **{ts.strftime('%m/%d %H:%M')}**: Metric={metric['random_metric']}, Score={metric['performance_score']}\n"
    
    # Save analytics
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    with open(docs_dir / "analytics.md", 'w') as f:
        f.write(analytics_md)
    
    print(f"✅ Generated analytics with {len(data['metrics'])} data points")

if __name__ == "__main__":
    generate_data_analytics()