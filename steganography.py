import cv2
import os

# Load the image
image_path = C:\Users\GOWTHAM M\Downloads\Gowtham Photo.jpeg  # Replace with your image path
img = cv2.imread(image_path)

# Check if image loaded successfully
if img is None:
    print(f"Error: Could not load image at {image_path}")
    exit()

# Get image dimensions
height, width, _ = img.shape

# Input secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Check if the message fits in the image
if len(msg) > (height * width):
    print("Error: Message too long for this image. Use a larger image or shorter message.")
    exit()

# Create dictionaries for character-to-ASCII and ASCII-to-character mapping
d = {chr(i): i for i in range(255)}  # char -> ASCII
c = {i: chr(i) for i in range(255)}  # ASCII -> char

# Embed the message into the image
n, m, z = 0, 0, 0  # n: row, m: col, z: channel (R, G, B)
for char in msg:
    img[n, m, z] = d[char]  # Replace pixel value with ASCII value of character
    m += 1  # Move horizontally
    if m >= width:  # If end of row, move to next row
        m = 0
        n += 1
    z = (z + 1) % 3  # Cycle through R, G, B channels

# Save and open the encrypted image
output_path = "encryptedImage.jpg"
cv2.imwrite(output_path, img)
os.system(f"start {output_path}")  # Opens image on Windows

# Decrypt the message
message = ""
n, m, z = 0, 0, 0  # Reset coordinates
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]  # Extract character from pixel value
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT auth")
