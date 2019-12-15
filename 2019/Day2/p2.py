import c

# Run the program until the correct inputs are found.
for i in range(99):
    for j in range (99):
        output = c.runProgram(i, j)

        if (output == 19690720):
            print(100 * i + j)


print("Finished.")
