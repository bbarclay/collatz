# Rules for Creating Tests

*   **Odd/Even Number Rule:** Test cases should only use odd numbers as starting values. Even numbers should be excluded.
*   **Read Before Overwriting:** Before overwriting any test file, carefully read its contents to understand the existing test case and avoid unintended data loss.

# Test Framework Instructions

## Overview

The test framework allows for the generation of test files based on hypotheses and past hypotheses. It ensures context tracking and data collection in a reusable format (JSON).

## Generating Tests

1. **Prepare Hypotheses File:** Create a file containing hypotheses, each on a new line.
2. **Run Test Framework:** Execute the `test_framework.py` script with the hypotheses file as input.
3. **Generated Test Files:** The framework will generate test files based on the provided hypotheses.

## Validating Hypotheses

1. **Run Tests:** Execute the generated test files to validate the hypotheses.
2. **Collect Results:** The framework will store the results in a flat file format (JSON) for easy analysis.

## Storing Results

1. **Results File:** The results will be stored in a specified results file in JSON format.
2. **Context Tracking:** The framework will track context and past hypotheses to ensure systematic testing.

## Example Usage

```python
from test_framework import TestFramework

# Initialize the test framework with hypothesis and results files
framework = TestFramework('hypotheses.txt', 'results.json')

# Generate test cases based on hypotheses
test_cases = framework.generate_test_cases()

# Run tests and collect results
results = framework.run_tests()

# Store results in a flat file format (JSON)
framework.store_results(results)
```

## Notes

- **Hypotheses Format:** Each hypothesis should be a single line in the hypotheses file.
- **Results Format:** Results will be stored in JSON format for easy analysis and consolidation.
