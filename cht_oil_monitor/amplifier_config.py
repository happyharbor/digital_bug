import board
import digitalio
import adafruit_max31855

amplifiers = {
    "Cyl 1": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D5),
        "nickname": "C1",
        "column": 0,
        "row": 0,
    },
    "Cyl 3": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D6),
        "nickname": "C3",
        "column": 9,
        "row": 0,
    },
    "Oil": {
        "board": adafruit_max31855.MAX31855,
        "spi": board.SPI(),
        "cs": digitalio.DigitalInOut(board.D13),
        "nickname": "Oil",
        "column": 4,
        "row": 1,
    },
}