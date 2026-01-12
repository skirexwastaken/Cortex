# Cortex: A symbol based language

Cortex is a simple esoteric programming language, inspired by Brain Fuck, written in python. 

The syntax is quite similar to Brain Fuck, however it has more features and some features from Brain Fuck work differently.

Cortex works with a total amount of 1024 cells, where each cell can hold a value of 1 Byte.

## Example Usage

python cortex.py main.cor

## Syntax

| Symbol | Description |
|------:|-------------|
| > | Moves the cell pointer by 1 to the right |
| < | Moves the cell pointer by 1 to the left |
| + | Adds the value 1 to the current cell |
| - | Subtracts the value 1 from the current cell |
| . | Prints the numerical value of the current cell |
| * | Prints the ASCII character of the current cell |
| % | Jumps to a token based on the value of the current cell |
| ( | If condition — code inside () is skipped if the current cell value is 0 |
| ) | End of If condition |
| [ | If > 0 condition — sets currentFlow to 1 if current cell value is greater than 0 |
| ] | End of If > 0 condition — sets currentFlow to -1 if current cell value is greater than 0 |
| { | If == 0 condition — sets currentFlow to 1 if current cell value equals 0 |
| } | End of If == 0 condition — sets currentFlow to -1 if current cell value equals 0 |
| # | If this symbol is at the start of the code, debug mode is enabled |
| / | Adds the value from user input to the current cell |
