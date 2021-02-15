# Pico with OLED screen and BME280 sensor
MicroPython script to display the air temperature, humidity and pressure on the OLED screen using Raspberry Pi Pico microcontroller.

![Project image](img/project_img.jpg?raw=true)

## Detailed description
Schematic of the connections can be found in the connections.pdf file. OLED screen with SH1106 driver was used. It will not work if screen has different driver chip. Documentation on how to use MicroPython on the Raspberry Pi Pico can be found [here](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).

## Dependencies
You need two libraries to run this script:

[SH1106](https://github.com/robert-hh/SH1106)

[BME280](https://github.com/catdog2/mpy_bme280_esp8266)

sh1106.py and bme280.py files should be copied into the /lib directory crated in the main directory of the microcontroller.
