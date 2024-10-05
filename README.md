# Simple Python Tip-Calculator

A basic python tip calculator that calculates how much a person should pay, including tip, based on the total bill.

## Features
- Simple text-based user interface for input/output

## Installation
### Prerequisites
Make sure you have python installed on your machine. You can download it from the official website: [Python.org](https://www.python.org/).

### Steps:
1. Clone the repository: 
    ```bash
    git clone https://github.com/shafayat666/tip-calculator.git
    ```
2. Navigate into the project directory:
    ```bash
    cd tip-calculator
    ```
3. (*Optional*) Create a virtual environment and activate it:
    - For Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - For Windows:
        ```bash
        python -m venv venv
        venv/Scripts/activate
        ```
4. Install dependencies (*if any*):
    ```bash
    pip install -r requirements.txt
    ```
    (*Note: This project doesn't use any external libraries, you can skip this step*)

## Usage
1. Run the calculator script:
    ```bash
    python main.py
    ```
2. Input numbers and choose an operation:
    - The program will ask you to input the bill, tip percentage and the number of people.
    - The program will output the result based on your inputs.

## Example of Usage
```
Welcome to the tip calculator!
What was the total bill? $324
How much tip would you like to give? 10, 12, or 15? 23
How many people to split the bill? 4
Each person should pay: $99.63
```
## Error Handling
- Doesn't handle division by zero with an error message.
- Invalid input types (like entering text instead of numbers) are not managed with appropriate error prompts.

## Contributing
Contributions are welcome! If you have any ideas for improving this calculator, feel free to fork the repository, make your changes and submit a pull request.

1. Fork the repo
2. Create a new branch (``` git checkout -b feature-branch ```)
3. Commit your changes (``` git commit -m "Add new feature" ```)
4. Pusj to the branch (``` git push origin feature-branch ```)
5. Open an Pull Request
