# Coffee Shop Sales & Expenses Tracker

This application helps track coffee sales and business expenses, and provides visualizations for monthly financial overviews.

## Features

*   Record individual sales transactions (item, quantity, price).
*   Record business expenses (description, category, amount).
*   Data is stored locally in CSV files (`data/sales.csv`, `data/expenses.csv`).
*   Generate and view bar charts for:
    *   Total monthly sales for a given year.
    *   Total monthly expenses for a given year.
*   Command-line interface (CLI) for easy interaction.

## Project Structure

```
coffee_tracker/
├── data/                 # Stores sales.csv and expenses.csv
│   ├── sales.csv
│   └── expenses.csv
├── src/                  # Source code
│   ├── __init__.py
│   ├── main.py           # Main application logic and CLI
│   ├── models.py         # Data models (Sale, Expense classes)
│   ├── data_manager.py   # Handles reading/writing data
│   └── visualizer.py     # Generates charts
├── tests/                # Unit tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_data_manager.py
├── plots/                # Directory where generated charts are saved
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <repository_url>
    # cd coffee_tracker_project_directory
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Navigate to the `coffee_tracker` directory (if you cloned it, you might be in `coffee_tracker_project_directory/coffee_tracker`). The application is run from the `src` directory using Python's module execution flag (`-m`).

From the directory containing the `coffee_tracker` folder (e.g., your project's root if `coffee_tracker` is the main app folder):

```bash
python -m coffee_tracker.src.main
```

Or, if your current directory is `coffee_tracker/src/`:
```bash
python main.py
```
(Note: The first method using `-m` is generally more robust for handling Python's package imports.)

Upon running, you will see a command-line menu to interact with the application.

## How to Run Unit Tests

To run the unit tests, navigate to the project root directory (the one containing the `coffee_tracker` folder and this README). Then run:

```bash
python -m unittest discover tests
```
or more specifically:
```bash
python -m unittest tests.test_models
python -m unittest tests.test_data_manager
```

This will discover and run all tests located in the `tests` directory.

## Dependencies

*   `matplotlib` (for generating charts)

## Future Enhancements (Possible Ideas)

*   More detailed reports (e.g., profit/loss).
*   Data export/import in different formats.
*   GUI instead of CLI.
*   Support for different users or shops.
*   More advanced data analysis and filtering.