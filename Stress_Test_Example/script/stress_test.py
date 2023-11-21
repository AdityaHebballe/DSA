# main_script.py
import random
import sys
import os

# Accept the number of tests as a command line parameter
tests = int(sys.argv[1])
# Accept the parameter for the tests as a command line parameter
n = int(sys.argv[2])

for i in range(tests):
    print("Test #" + str(i))
    # Run the generator gen.py with parameter n and the seed i
    os.system("python3 gen.py " + str(n) + " " + str(i) + " > input.txt")
    # Run the model solution model.py
    os.system("python3 model.py <input.txt >model.txt")
    # Run the main solution
    os.system("python3 main.py <input.txt >main.txt")

    # Read the output of the model solution
    with open('model.txt') as f:
        model = f.read()
    print("Model:", model)

    # Read the output of the main solution
    with open('main.txt') as f:
        main = f.read()
    print("Main:", main)

    if model != main:
        break
