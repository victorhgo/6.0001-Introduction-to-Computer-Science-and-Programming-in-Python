import time

# perf_counter instead of time

def CelsiusToFahrenheit(c):
    """
    Assumes c is temperature measured in Celsius degrees
    Converts it to Fahrenheit """
    return c * 9/5 + 32

# Start clock
time0 = time.perf_counter()
CelsiusToFahrenheit(100000)
time1 = time.perf_counter() - time0
print("t =", time0, ":", time1, "s,")