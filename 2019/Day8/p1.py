
# Read the image data.
with open("i1.txt") as input:
    image = input.read()

minZero = float("inf")
minZeroChecksum = 0
zero = one = two = 0

# Find the layer with the least amount of zeros.
for i, p in enumerate(image):
    
    if p == "0":
        zero += 1

    elif p == "1":
        one += 1
    
    elif p == "2":
        two += 1

    if (i + 1) % 150 == 0:
        if zero < minZero:
            minZero = zero
            minZeroChecksum = one * two
        
        zero = one = two = 0

# Print the checksum.
print(minZeroChecksum)
