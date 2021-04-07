"""
sensor.py

"""


def read_sensor():
    data = 10.4
    result = {
        "source": "voltage sensor",
        "value": data,
    }
    return result