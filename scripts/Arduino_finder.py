import serial.tools.list_ports as lp

ports = list(lp.comports())
arduino_port = None

for p in ports:
    print(p)  # Debug output
    if "USB Serial Device" in p.description or "Arduino" in p.description:
        arduino_port = p.device
        break

if not arduino_port:
    print("❌ Arduino UNO R4 Minima not found.")
else:
    print(f"✅ Found Arduino on port: {arduino_port}")
    with open("arduino_port.txt", "w") as f:
        f.write(arduino_port)
