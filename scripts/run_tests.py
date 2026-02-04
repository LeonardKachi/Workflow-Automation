#!/usr/bin/env python3
"""
Run automated tests and generate reports
"""
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path

def run_tests():
    """Execute test suite and generate reports"""
    test_dir = Path("tests")
    test_dir.mkdir(exist_ok=True)
    
    # Create sample test if none exists
    sample_test = test_dir / "test_sample.py"
    if not sample_test.exists():
        with open(sample_test, 'w') as f:
            f.write('''"""
Sample tests for the project
"""
import pytest
import random

def test_addition():
    """Test basic arithmetic"""
    assert 1 + 1 == 2

def test_list_operations():
    """Test list manipulation"""
    items = [1, 2, 3]
    items.append(4)
    assert len(items) == 4
    assert items[-1] == 4

def test_random_generation():
    """Test random number generation within bounds"""
    value = random.randint(1, 100)
    assert 1 <= value <= 100

def test_string_operations():
    """Test string methods"""
    text = "Hello, World!"
    assert text.startswith("Hello")
    assert text.endswith("!")
    assert "World" in text

class TestMathOperations:
    """Test class for math operations"""
    
    def test_multiplication(self):
        assert 3 * 4 == 12
    
    def test_division(self):
        assert 10 / 2 == 5
    
    def test_power(self):
        assert 2 ** 3 == 8

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
''')
    
    # Run tests
    print("Running test suite...")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"],
        capture_output=True,
        text=True
    )
    
    # Create results directory
    results_dir = Path("test_results")
    results_dir.mkdir(exist_ok=True)
    
    # Save test output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(results_dir / f"test_results_{timestamp}.txt", 'w') as f:
        f.write(result.stdout)
    
    # Generate summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "exit_code": result.returncode,
        "tests_run": None,
        "tests_passed": None,
        "tests_failed": None
    }
    
    # Parse test results
    lines = result.stdout.split('\n')
    for line in lines:
        if "passed" in line and "failed" in line and "errors" in line:
            parts = line.split()
            summary["tests_passed"] = parts[0]
            summary["tests_failed"] = parts[2]
            summary["tests_run"] = int(parts[0]) + int(parts[2])
            break
    
    # Save summary as JSON
    with open(results_dir / "latest_results.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nTest Execution Complete:")
    print(f"Exit Code: {result.returncode}")
    print(f"Results saved to: test_results/")
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(run_tests())