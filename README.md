# Camera_TFT
Display a Raspberry Pi Camera Module 3 Feed on a TFT Screen

# Raspberry Pi Display Project

## Description
This project demonstrates how to display a camera feed on an ST7789 TFT display using a Raspberry Pi. It includes handling button inputs to control the display's backlight, providing an interactive way to manage the display power.

## Components
- **Raspberry Pi 5**: The central computing unit that processes the camera feed and controls the display.
- **ST7789 TFT Display**: A 240x320 2" Adafruit pixel display used to show the camera output. This particular screen had an eye spi connector, which made it much easier to connect without all the wires.
- **EyeSpy Beret**: Provides easy connection ports for the TFT display and a couple buttons. Able to be mounted above the active cooler
- **Camera Module**: Captures real-time video feed displayed on the TFT.
- Optional: **Pimoroni NVMe Hat**: I just wanted to see if this improved the computing power of the Raspberry Pi.

## Hardware Setup
1. **Connect the Display**: Wire the ST7789 display to the Raspberry Pi via the SPI interface.
2. **Attach the Camera**: Connect the camera module to the CSI port of the Raspberry Pi.
3. **Power Setup**: Ensure the Raspberry Pi and all components are properly powered.

## Software Setup
### Dependencies
Ensure all required libraries are installed. Mainly I used the Adafruit libraries to make it easy to use the Eyespi beret/screen.

sudo pip3 install adafruit-circuitpython-rgb-display pillow picamera2 spidev adafruit-blinka
