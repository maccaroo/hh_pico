hh_pico
=======
This repo contains projects using the Raspberry Pi Pico hardware as sensors.

# Pico Temperature Sensor
I used [this tutorial](https://www.halvorsen.blog/documents/technology/iot/pico/pico_temperature_sensor_builtin.php) as a source.  This code was developed and deployed to the Pico from Thonny.  I aim to get a VSCode environment working soon.

This project uses a built-in temperature sensor on the Pico to report an approximation of the ambient temperature.  The temperature sensor itself is located on the RP2040 microcontroller chip, and so may report slightly higher than the actual ambient temperature.  The sensor checks the temperature periodically and sends the reading to the Home Historan API.
