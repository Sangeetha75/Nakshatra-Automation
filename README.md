# Nakshatra Automation – Home Assistant Assignment
### **Student Name:** Sangeetha Kodadhala  
### **Register Number:** 42732041  
### **MQTT Topic Used:** `home/sangeetha-2025/sensor`

---

## 📌 Assignment Overview
This project demonstrates integration between **Python → MQTT → Home Assistant**.  
Sensor values are published using a Python script and displayed on the Home Assistant dashboard through MQTT sensors.

This repository contains:
- Python MQTT publisher script  
- Home Assistant YAML configuration  
- Screenshots (if added)  
- PDF summary  
- Video link (if added)

---

## 📁 Files in Repository

| File Name | Description |
|----------|-------------|
| `publisher.py` | Python script to publish temperature, humidity, and light intensity values via MQTT |
| `configuration.yaml` | Home Assistant MQTT configuration for displaying the sensors |
| `Nakshatra_Assignment_Summary_Sangeetha_42732041.pdf` | One-page assignment summary |
| `README.md` | Documentation for the assignment |


---

## 🧪 Python → MQTT Publishing

The Python script publishes:
- Temperature = **25°C**
- Humidity = **60%**
- Light Intensity = **350 lx**  
- Student Info:
  - `student_name = "Sangeetha Kodadhala"`
  - `unique_id = "42732041"`

The message is sent as JSON format to the topic:  
`home/sangeetha-2025/sensor`

Run the script:

```bash
python3 publisher.py

