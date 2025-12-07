# Home Assistant MQTT Sensor Integration

## Student Details
- **Name:** Sangeetha Kodadhala
- **Register Number:** 42732041
- **MQTT Topic Used:** home/sangeetha-2025/sensor

## Overview
This project demonstrates publishing temperature data to an MQTT broker using Python and displaying it in Home Assistant.

## Sensor
- Temperature: 25°C

## Requirements
- Python 3.x
- paho-mqtt library (`pip install paho-mqtt`)
- Mosquitto MQTT broker
- Home Assistant

## Steps to Run
1. Ensure Mosquitto broker is running.
2. Update `mqtt_publish.py` with your register number.
3. Run Python script: `python mqtt_publish.py`
4. Configure Home Assistant to subscribe to MQTT topic: `home/akhilaboni-2025/sensor`
5. Observe live temperature values on the HA dashboard.

## Notes
- Topic is unique per student.
- Video demonstration includes face verification, timestamp, HA dashboard, MQTT publish, and Python script execution.
