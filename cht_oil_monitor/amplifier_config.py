import board
import digitalio
import adafruit_max31855

amplifiers = {
    "Cyl 1": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D5),
    },
    "Cyl 3": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D6),
    },
    "Oil": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D13),
    },
}