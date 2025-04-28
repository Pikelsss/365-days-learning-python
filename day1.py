print ("Hello World")
print ("Its me James")
print ("hey this is me testing and laerning python for 365 days of code")
print ("I am learning python")
print ("I am learning python")
print ("This is greate i mean")

print("Hello", "World", sep="-")  # Output: Hello-World

print("Hello", end=" ")  # Output: Hello (stays on the same line)
print("World!")          # Output: World! (printed on the same line)

with open("output.txt", "w") as f:
    print("Hello, File!", file=f)  # This will write to 'output.txt'

import time
print("Hello", end="", flush=True)
time.sleep(2)
print(" James!")
