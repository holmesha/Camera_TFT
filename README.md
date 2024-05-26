Camera_TFT

Display a Raspberry Pi Camera Module 3 Feed on a TFT Screen

Raspberry Pi Display Project

Description

This project demonstrates how to display a camera feed on an ST7789 TFT display using a Raspberry Pi. It includes handling button inputs to control the display’s backlight, providing an interactive way to manage the display power. Additionally, it shows how to display the camera feed on a larger desktop window using Tkinter.

Components

	•	Raspberry Pi 5: The central computing unit that processes the camera feed and controls the display.
	•	ST7789 TFT Display: A 240x320 2” Adafruit pixel display used to show the camera output. This particular screen had an EyeSpy connector, which made it much easier to connect without all the wires.
	•	EyeSpy Beret: Provides easy connection ports for the TFT display and a couple of buttons. Able to be mounted above the active cooler.
	•	Camera Module 3: Captures real-time video feed displayed on the TFT.
	•	Optional: Pimoroni NVMe Hat: Used to potentially improve the computing power of the Raspberry Pi.

Hardware Setup

	1.	Connect the Display: Wire the ST7789 display to the Raspberry Pi via the SPI interface.
	2.	Attach the Camera: Connect the camera module to the CSI port of the Raspberry Pi.
	3.	Power Setup: Ensure the Raspberry Pi and all components are properly powered.

Software Setup

Dependencies

Ensure all required libraries are installed. The Adafruit libraries are used to simplify the use of the EyeSpy beret/screen. You can find more (including sample test code) on the Adafruit EYESPI Beret here: https://learn.adafruit.com/eyespi-pi-beret

```bash
sudo pip3 install adafruit-circuitpython-rgb-display pillow picamera2 spidev adafruit-blinka
```

Code Overview

The provided Python script initializes the hardware, configures the camera, and sets up the display. It also uses Tkinter to create a window on the desktop to show the camera feed at a larger size.

Using Tkinter

Tkinter is a standard GUI (Graphical User Interface) toolkit in Python. It provides a fast and easy way to create GUI applications. In this project, Tkinter is used to create a window on the Raspberry Pi’s desktop that displays the camera feed.

Here is an overview of how Tkinter is used in the script:

	1.	Initialize Tkinter: Create the main window (root) and set its title and size.
	2.	Create a Label: A Tkinter Label widget is used to display the camera feed.
	3.	Update Function: A function is defined to capture frames from the camera, resize them, and update the label. This function is called periodically using root.after.
	4.	Main Loop: The Tkinter main loop (root.mainloop()) is started, which keeps the window open and responsive.
