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

# Instructions for Using the New Test Framework

## Overview

The new test framework is designed to create a structured environment for generating, validating, and storing test results based on hypotheses. It ensures systematic testing and context tracking.

## Generating Tests

1. **Prepare Hypotheses File:** Create a file named `hypotheses.txt` containing hypotheses, each on a new line.
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

# Flow Loop for AI to Solve the Goal

## Overview

This section explains the flow loop that AI must follow to solve the goal. The goal is to create test files, validate hypotheses, and store results in JSON format.

## Flow Loop Steps

1. **Read Goal File:** The AI should read the `goal.txt` file to get context and understand the primary objective and critical rules.
2. **Generate Test Files:** The AI should create `test_1`, `test_2`, and `test_3` directories, each containing core files: `test.py`, `raw.json`, and `results.json`.
3. **Fill Core Files:** The AI should fill out the core files based on the rules and context from the `goal.txt` file.
4. **Enforce Conditions:** The AI should enforce conditions like not allowing Collatz for even numbers or for 1.
5. **Create Tests:** The AI should create 3 tests based on the line file and what might help solve the goal.
6. **Store Raw Data:** The AI should store raw data in `raw.json` in each test folder.
7. **Execute Tests:** The AI should execute the tests and fill out `results.json` with high-level overview information.
8. **Analyze Results:** The AI should analyze the results and store them in a specified results file in JSON format.
9. **Track Context:** The AI should track context and past hypotheses to ensure systematic testing.
10. **Repeat Loop:** The AI should repeat the flow loop to continuously improve and solve the goal.

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

# Micro Test Framework

## Overview

The micro test framework emphasizes the importance of not biting off more than can be proven in a single iteration. Tests should be logical and simple, just like the truths.

## Guidelines

1. **Small Iterations:** Focus on small, manageable iterations for each test.
2. **Logical Tests:** Ensure that each test is logical and straightforward.
3. **Simple Truths:** Base tests on simple, foundational truths.

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
