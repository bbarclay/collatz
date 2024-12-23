import json

def collatz_sequence(n):
    if n == 1 or n % 2 == 0:
        raise ValueError("Collatz sequence cannot start with 1 or an even number.")
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def run_test():
    test_data = {
        "test_name": "test_1",
        "description": "Test for odd starting number",
        "starting_value": 7,
        "expected_sequence": [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    }

    try:
        result_sequence = collatz_sequence(test_data["starting_value"])
        test_data["result_sequence"] = result_sequence
        test_data["status"] = "Passed" if result_sequence == test_data["expected_sequence"] else "Failed"
    except ValueError as e:
        test_data["status"] = "Error"
        test_data["error_message"] = str(e)

    with open("raw.json", "w") as raw_file:
        json.dump(test_data, raw_file, indent=4)

    high_level_results = {
        "test_name": test_data["test_name"],
        "status": test_data["status"]
    }

    with open("results.json", "w") as results_file:
        json.dump(high_level_results, results_file, indent=4)

if __name__ == "__main__":
    run_test()
