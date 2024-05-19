 import digitalio
 import board
 from PIL import Image
 from picamera2 import Picamera2
 from adafruit_rgb_display import st7789 as adafruit_st7789
 
 # Define pins according to the EyeSpy HAT
 cs_pin = digitalio.DigitalInOut(board.CE0)  # Chip select
 dc_pin = digitalio.DigitalInOut(board.D25)  # Data/command
reset_pin = digitalio.DigitalInOut(board.D27)  # Reset

# Define button pins
button_on = digitalio.DigitalInOut(board.D5)  # Button to turn on the backli>
button_off = digitalio.DigitalInOut(board.D6)  # Button to turn off the back>
button_on.switch_to_input(pull=digitalio.Pull.UP)
button_off.switch_to_input(pull=digitalio.Pull.UP)

# Backlight setup
backlight = digitalio.DigitalInOut(board.D18)
backlight.switch_to_output()

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

# Display loop
try:
    while True:
        # Check button state
        if not button_on.value:  # Button is pressed, turn on the backlight
            backlight.value = True
        if not button_off.value:  # Button is pressed, turn off the backlight
            backlight.value = False

        frame = picam2.capture_array()
        image = Image.fromarray(frame).convert('RGB')
        image = image.resize((display.width, display.height), Image.BILINEAR>

        # Display the image only if backlight is on
        if backlight.value:
            display.image(image)

except KeyboardInterrupt:
    print("Stream stopped")

finally:
    picam2.stop()
    backlight.value = False  # Turn off backlight when done
