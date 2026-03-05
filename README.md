# 🚀 CI Introduction Project

This project serves as my hands-on introduction to **Continuous Integration (CI)** using GitHub Actions and Pytest. The goal is to demonstrate how automated testing can ensure code quality and reliability before merging changes.



## 🛠 Project Components

* **`app.py`**: Contains the core logic functions for mathematical power calculations.
* **`_test.py`**: A dedicated testing suite using the `pytest` framework to validate the logic.
* **`.github/workflows/main.yml`**: The CI configuration file that automates the testing process on every push.

## 🧪 Testing Logic

The project includes unit tests for several mathematical operations:
* **Square/Cube/Power Calculations**: Ensures basic math remains accurate.
* **Zero & Negative Handling**: Validates edge cases.
* **Type Validation**: Uses `pytest.raises(TypeError)` to ensure the system handles invalid inputs (like strings) gracefully.

## ⚙️ How the CI Works

Every time code is pushed to the `main` branch or a Pull Request is opened, the following automated steps occur:

1.  **Virtual Environment**: GitHub spins up a fresh `ubuntu-latest` runner.
2.  **Dependency Installation**: Python 3.12 is configured, and libraries (`pytest`, `streamlit`) are installed via `pip`.
3.  **Automated Execution**: The command `pytest _test.py` is executed.
4.  **Gatekeeping**: 
    * ✅ If tests pass, the build turns green, allowing the merge.
    * ❌ If any test fails, the build turns red, preventing broken code from entering the main branch.



