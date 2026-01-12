# --- Importing needed libraries ---
import sys
import os
import time

# --- Cortex ---
def cortex():

    # --- Checking if there's a filename in sys.argv ---
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        # --- Checking if this filename exists ---
        if os.path.exists(filename):

            # --- Loading code ---
            with open(filename,"r") as file:
                code = "".join(line.replace("\n","").replace(" ","") for line in file.readlines())
            
            # --- Checking if debug mode should be activated ---
            if code[0] == "#":
                debug = True
                code = code[1:]

            else:
                debug = False
            
            # --- Code and its length ---
            codeLength = len(code)
            currentToken = 0

            workspace = []

            # --- Generating cell workspace ---
            for cell in range(1024):
                workspace.append(0)
            
            # --- Pointer that points to the current cell in workspace ---
            currentCell = 0

            # --- Current flow = 1 -> Code is being executed from left to right, Current flow = -1 -> Code is being executed from right to left ---
            currentFlow = 1

            execute = True

            # --- Main execution loop ---
            while currentToken < codeLength and currentToken >= 0:

                # --- If debug is turned on, current token and current cell value is printed at the beginning of every cycle ---
                if debug:
                    print([code[currentToken],workspace[currentCell]])
                    time.sleep(1)
                    
                # --- Checkinf if code should be executed ---   
                if execute == True:
                    match code[currentToken]:
                        # --- Moves the cell pointer by 1 to the right ---
                        case ">":
                            currentCell += 1

                        # --- Moves the cell pointer by 1 to the left ---
                        case "<":
                            currentCell -= 1

                        # --- Adds the value 1 to the current cell ---
                        case "+":
                            cell = workspace[currentCell]

                            if cell + 1 > 255:
                                cell = 0

                            else:
                                cell += 1

                            workspace[currentCell] = cell
                        
                        # --- Subtracts the value 1 from the current cell ---
                        case "-":
                            cell = workspace[currentCell]

                            if cell - 1 < 0:
                                cell = 255

                            else:
                                cell -= 1

                            workspace[currentCell] = cell

                        # --- Prints the numerical value of the current cell ---
                        case ".":
                            print(workspace[currentCell])

                        # --- Prints the ASCII character of the current cell ---
                        case "*":    
                            print(chr(workspace[currentCell]))

                        # --- Jumps to a token based on the value of the current cell ---
                        case "%":
                            jumpValue = workspace[currentCell]

                            if jumpValue >= codeLength:
                                currentToken = jumpValue - codeLength
                                
                            else: 
                                currentToken = jumpValue - 1

                        # --- If > 0 condition — sets currentFlow to 1 if current cell value is greater than 0 ---
                        case "[":
                            if workspace[currentCell] > 0:
                                currentFlow = 1

                        # --- End of If > 0 condition — sets currentFlow to -1 if current cell value is greater than 0 ---
                        case "]":
                            if workspace[currentCell] > 0:
                                currentFlow = -1
                                execute = False

                        # --- If == 0 condition — sets currentFlow to 1 if current cell value equals 0 ---
                        case "{":
                            if workspace[currentCell] == 0:
                                currentFlow = 1

                        # --- End of If == 0 condition — sets currentFlow to -1 if current cell value equals 0 ---
                        case "}":
                            if workspace[currentCell] == 0:
                                currentFlow = -1
                                execute = False
                        
                        # --- If condition — code inside () is skipped if the current cell value is 0 ---
                        case "(":
                            if workspace[currentCell] == 0:
                                execute = False

                        # --- Adds the value from user input to the current cell ---
                        case "/":
                            inputValue = input("$ ")[0]

                            if not inputValue.isnumeric():
                                inputValue = ord(inputValue)

                            inputValue = int(inputValue)

                            cell = workspace[currentCell]

                            if cell + inputValue > 255:
                                cell = (cell + inputValue) - 255

                            else:
                                cell = inputValue

                            workspace[currentCell] = cell

                else:
                    match code[currentToken]:

                        # --- End of If condition ---
                        case ")":
                            execute = True

                currentToken += currentFlow

                # --- If currentCell points to a cell that's out of range, it flips ---
                match currentCell:
                    case 1024:
                        currentCell = 0
                    
                    case -1:
                        currentCell = 1023

        # --- Invalid filename ---
        else:
            print("Invalid filename.")

    # --- Invalid sys.argv ---
    else:
        print("Invalid system arguments.")

# --- Launching cortex ---        
try:
    cortex()

except:
    exit()