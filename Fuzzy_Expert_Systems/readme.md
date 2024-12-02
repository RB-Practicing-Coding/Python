# Simple Fuzzy Expert System
- Define Fuzzy Variables: I define temperature (input) and fan_speed (output) as fuzzy variables with their respective ranges.

- Define Membership Functions: I create membership functions for temperature (cold, warm, hot) and fan_speed (low, medium, high) using triangular membership functions.

- Define Fuzzy Rules: I define rules to control the fan speed based on temperature:
    + If the temperature is cold, the fan speed is low.

    + If the temperature is warm, the fan speed is medium.

    + If the temperature is hot, the fan speed is high.

- Create Control System: I create and simulate the control system using the defined rules.

- Test the System: I test the fuzzy system with an example temperature (e.g., 15°C) and compute the fan speed.

# How to run
- Need to install requirement.txt first
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```
- Run
```bash
python3 ./demo.py
```