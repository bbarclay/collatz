import json
import os
import re

class TestFramework:
   def __init__(self, hypothesis_file, results_file):
       self.hypothesis_file = hypothesis_file 
       self.results_file = results_file
       self.context = []
       self.load_context()

   def load_context(self):
       if os.path.exists(self.results_file):
           with open(self.results_file, 'r') as file:
               self.context = json.load(file)
       else:
           self.context = []

   def save_context(self):
       with open(self.results_file, 'w') as file:
           json.dump(self.context, file, indent=4)

   def read_hypotheses(self):
       with open(self.hypothesis_file, 'r') as file:
           hypotheses = file.readlines()
       return [hypothesis.strip() for hypothesis in hypotheses]

   def generate_test_cases(self):
       hypotheses = self.read_hypotheses()
       test_cases = []
       for hypothesis in hypotheses:
           # Generate test cases based on the hypothesis
           # This is a placeholder for the actual test case generation logic
           test_cases.append(f"Test case for hypothesis: {hypothesis}")
       return test_cases

   def store_results(self, results):
       self.context.append(results)
       self.save_context()

   def run_tests(self):
       test_cases = self.generate_test_cases()
       results = []
       for test_case in test_cases:
           # Execute the test case and collect results
           # This is a placeholder for the actual test execution logic
           result = f"Result for {test_case}"
           results.append(result)
       self.store_results(results)
       return results

   def get_next_test_number(self):
       # Find all existing test directories
       existing_dirs = [d for d in os.listdir() if os.path.isdir(d) and d.startswith('test_')]
       if not existing_dirs:
           return 1
           
       # Extract numbers from directory names
       numbers = []
       for dir_name in existing_dirs:
           match = re.match(r'test_(\d+)', dir_name)
           if match:
               numbers.append(int(match.group(1)))
               
       # Return the next sequential number
       return max(numbers) + 1 if numbers else 1

   def create_test_files(self):
       # Get the next test number
       next_num = self.get_next_test_number()
       test_dir = f'test_{next_num}'
       
       # Create the new test directory
       os.makedirs(test_dir, exist_ok=True)
       
       # Create test files in the new directory
       with open(os.path.join(test_dir, 'test.py'), 'w') as file:
           file.write(f"# Test file for {test_dir}\n")
       
       with open(os.path.join(test_dir, 'raw.json'), 'w') as file:
           json.dump({}, file)
           
       with open(os.path.join(test_dir, 'results.json'), 'w') as file:
           json.dump({}, file)
           
       with open(os.path.join(test_dir, 'hypothesis.tex'), 'w') as file:
           file.write(f"Hypothesis for {test_dir}\n")
           
       return test_dir

   def enforce_conditions(self, number):
       if number == 1 or number % 2 == 0:
           raise ValueError("Collatz sequence cannot start with 1 or an even number.")
       return number

   def create_hypothesis_files(self):
       # Get the latest test directory
       next_num = self.get_next_test_number() - 1  # Get current (last created) number
       test_dir = f'test_{next_num}'
       
       if os.path.exists(test_dir):
           with open(os.path.join(test_dir, 'hypothesis.tex'), 'w') as file:
               file.write(f"Hypothesis for {test_dir}\n")
       else:
           raise FileNotFoundError(f"Test directory {test_dir} does not exist")
