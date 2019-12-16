import c as common

valid = 0
pw = common.Password([2, 4, 5, 5, 5, 5], [7, 8, 9, 9, 9, 9])

# Part 1: Look for passwords with any two of the same digits in a row.
while pw.inRange():
    if pw.hasDouble():
        valid += 1

    pw.increment()

print (valid)