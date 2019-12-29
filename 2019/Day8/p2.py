
# Read the image data.
with open("i1.txt") as input:
    image = input.read()

# Initialize the image.
decodedImage = [["2"] * 25 for _ in range(6)]

# Decode the image.
for i, p in enumerate(image):
    
    offset = i % 150
    row = offset // 25
    col = offset % 25

    val = decodedImage[row][col]

    if val == "2":
        pixel = " " if p == "0" else p
        decodedImage[row][col] = pixel

# Print the image.
for row in decodedImage:
    print("".join(row))
