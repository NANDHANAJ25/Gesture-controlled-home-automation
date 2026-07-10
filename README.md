# 🖐️ Gesture Control Home Automation using ESP32

## 📌 Overview
Gesture Control Home Automation is a touch-free smart automation system that enables users to control devices using hand gestures. The system uses **Python**, **OpenCV**, and **MediaPipe** to detect hand landmarks and identify finger movements. The detected finger states are transmitted to an **ESP32** through serial communication, where each finger controls a dedicated LED. This project demonstrates a simple, efficient, and contactless approach to home automation using computer vision and embedded systems.

---

## 🚀 Features
- Touch-free home automation
- Real-time hand and finger detection
- Five independent LED controls
- One LED assigned to each finger
- Fast gesture recognition using MediaPipe
- Serial communication between Python and ESP32
- Easy to expand for controlling real appliances

---

## 🛠️ Technologies Used
- Python
- OpenCV
- MediaPipe
- ESP32
- Arduino IDE
- PySerial

---

## ⚙️ Working Principle
1. The laptop camera captures live hand movements.
2. MediaPipe detects 21 hand landmarks.
3. Finger positions are analyzed to determine which fingers are raised.
4. A 5-bit binary command is generated based on the detected fingers.
5. The command is transmitted to the ESP32 via serial communication.
6. The ESP32 processes the received data and controls the corresponding LEDs.

---

## ✋ Finger Mapping

| Finger | LED |
|--------|-----|
| 👍 Thumb | LED 1 |
| ☝️ Index | LED 2 |
| 🖕 Middle | LED 3 |
| 💍 Ring | LED 4 |
| 🤏 Little | LED 5 |

---

## 📂 Project Structure

```
Gesture-Control-Home-Automation/
│── ESP32_Code/
│── Python_Code/
│── README.md
│── hand_landmarker.task
│── requirements.txt
```

---

## 🔧 Hardware Components
- ESP32 Development Board
- 5 LEDs
- 5 × 220Ω Resistors
- Breadboard
- Jumper Wires

---

## 💻 Software Requirements
- Python 3.12
- Arduino IDE
- OpenCV
- MediaPipe
- PySerial

Install the required Python libraries:

```bash
pip install opencv-python mediapipe pyserial
```

---

## 🎯 Applications
- Smart Home Automation
- Contactless Device Control
- Human-Computer Interaction
- IoT-Based Systems
- Educational Embedded Projects

---

## 🔮 Future Enhancements
- Replace LEDs with relay modules to control household appliances.
- Add Wi-Fi or Bluetooth communication.
- Integrate with IoT platforms such as Blynk or MQTT.
- Support custom hand gestures and voice commands.
- Develop a standalone embedded vision system without a computer.

---

## 👨‍💻 Author
**Nandhana J**  
B.Tech Electronics and Communication Engineering
