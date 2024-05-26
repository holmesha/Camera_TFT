import digitalio
import board
from PIL import Image, ImageTk
from picamera2 import Picamera2
from adafruit_rgb_display import st7789 as adafruit_st7789
import tkinter as tk
import os

# Ensure DISPLAY variable is set
os.environ['DISPLAY'] = ':0'

# Function to initialize the pin and handle errors
def initialize_pin(pin):
    try:
        pin_object = digitalio.DigitalInOut(pin)
        return pin_object
    except OSError as e:
        if e.errno == 16:  # Device or resource busy
            print(f"Pin {pin} is busy, trying another pin...")
            return None
        else:
            raise e

# Define pins according to the EyeSpy HAT
cs_pin = initialize_pin(board.CE0)
if cs_pin is None:
    cs_pin = initialize_pin(board.CE1)  # Fallback pin

dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)

# Define button pins
button_on = digitalio.DigitalInOut(board.D5)  # Button to turn on the backlight
button_off = digitalio.DigitalInOut(board.D6)  # Button to turn off the backlight
button_on.switch_to_input(pull=digitalio.Pull.UP)
button_off.switch_to_input(pull=digitalio.Pull.UP)

# Backlight setup
backlight = digitalio.DigitalInOut(board.D18)
backlight.switch_to_output()
backlight.value = True  # Ensure the backlight is on initially

# SPI configuration
spi = board.SPI()
display = adafruit_st7789.ST7789(
    spi,
    height=320,  # Adjusted dimensions based on rotation
    width=240,
    rotation=0,  # Adjusted rotation
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=32000000  # Adjusted SPI speed for stability
)

# Initialize Picamera2
picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()

# Initialize Tkinter
root = tk.Tk()
root.title("Camera Feed")
root.geometry("800x600")  # Set the size of the Tkinter window

# Create a label to display the camera feed
label = tk.Label(root)
label.pack(expand=True)

# Function to update the Tkinter window with the camera feed
def update_frame():
    frame = picam2.capture_array()
    image = Image.fromarray(frame).convert('RGB')
    image_tft = image.resize((display.width, display.height), Image.BILINEAR)
    
    # Display the image on the physical display
    if backlight.value:
        display.image(image_tft)

    # Resize the image for the larger Tkinter window
    image_tk = image.resize((800, 600), Image.BILINEAR)

    # Convert the image to a format Tkinter can use and display it in the Tkinter window
    tk_image = ImageTk.PhotoImage(image_tk)
    label.config(image=tk_image)
    label.image = tk_image
    
    # Schedule the next frame update
    root.after(100, update_frame)

# Start the frame update loop
update_frame()

# Handle button presses to control the backlight
def check_buttons():
    if not button_on.value:  # Button is pressed, turn on the backlight
        backlight.value = True
    if not button_off.value:  # Button is pressed, turn off the backlight
        backlight.value = False

    root.after(100, check_buttons)

# Start checking the buttons
check_buttons()

# Start the Tkinter main loop
root.mainloop()

# Stop the camera and turn off the backlight when the program is closed
picam2.stop()
backlight.value = False  # Turn off backlight when done
