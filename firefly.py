
import board
import busio
import adafruit_apds9960.apds9960
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True

while True:
    # change the color integration time of sensor
    sensor.color_integration_time = 40
    r, g, b, c = sensor.color_data
    print("Red: {0}, Green: {1}, Blue: {2}, Clear: {3}".format(r, g, b, c))
    pixels.fill((int(c), int(c), int(c)))