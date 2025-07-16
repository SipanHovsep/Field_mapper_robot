#!/usr/bin/env python
# Field‑mapper runner – freeze‑proof & correct byte extraction

import csv, serial, time, sys
from pathlib import Path

# ─── USER SETTINGS ────────────────────────────────────────────────────────────
INPUT_CSV   = "path.csv"
OUTPUT_CSV  = "data.csv"
CMD_DELAY   = 0.25
DWELL_S     = 5
ARDUINO_BAUD = 9600
SENSOR_PORT  = "COM6"

FRAME_LEN   = 13
INIT_CMD_1  = b"\x14"*6
INIT_CMD_2  = b"\xff"*6
INIT_CMD_3  = b"\x01"*6
START_STREAM_CMD = b"\x04"*6
ACK_CMD     = b"\x03"*6
# ──────────────────────────────────────────────────────────────────────────────

def init_sensor(port: serial.Serial) -> None:
    """Full wake‑up sequence."""
    print("[INFO] (re)initialising probe …")
    port.baudrate, port.bytesize = 1200, serial.SEVENBITS
    port.dtr, port.rts = True, True
    time.sleep(0.1)
    port.baudrate, port.bytesize = 115200, serial.EIGHTBITS
    port.rts = False
    for cmd in (INIT_CMD_1, INIT_CMD_2, INIT_CMD_3):
        port.write(cmd)
    time.sleep(0.5)
    port.read(port.in_waiting or 1)
    port.write(START_STREAM_CMD)
    print("[INFO] probe ready")

# ─── Ports ────────────────────────────────────────────────────────────────────
ARDUINO_PORT = Path("arduino_port.txt").read_text().strip() \
    if Path("arduino_port.txt").exists() else sys.exit("arduino_port.txt missing")

try:
    ser_motion = serial.Serial(ARDUINO_PORT, ARDUINO_BAUD, timeout=1)
    time.sleep(2)
    print(f"[INFO] motion link on {ARDUINO_PORT}")

    ser_sensor = serial.Serial(SENSOR_PORT, timeout=2)
    init_sensor(ser_sensor)

except serial.SerialException as e:
    sys.exit(f"Serial error: {e}")

# ─── Motion helpers ───────────────────────────────────────────────────────────
def step_axis(axis, delta):
    if delta == 0: return
    cmd = (axis + ('+\n' if delta > 0 else '-\n')).encode()
    for _ in range(abs(delta)):
        ser_motion.write(cmd)
        time.sleep(CMD_DELAY)

def goto(target, current):
    dx, dy, dz = (t - c for t, c in zip(target, current))
    step_axis('X', dx); step_axis('Y', dy); step_axis('Z', dz)
    return target

# ─── Sensor read (correct bytes) ──────────────────────────────────────────────
def read_sensor() -> float:
    frame = ser_sensor.read(FRAME_LEN)
    if len(frame) != FRAME_LEN:
        print("[WARN] timeout – resetting probe")
        init_sensor(ser_sensor)
        frame = ser_sensor.read(FRAME_LEN)
        if len(frame) != FRAME_LEN:
            print("[ERROR] probe silent after re‑init")
            return float('nan')
    ser_sensor.write(ACK_CMD)                         # queue next frame
    raw = int.from_bytes(frame[-2:], "big")           # *** last 2 bytes ***
    return raw / 100.0

# ─── Load path.csv ────────────────────────────────────────────────────────────
path = []
with open(INPUT_CSV, newline='') as f:
    for r in csv.reader(f, delimiter=' '):
        if not r or any(not c.strip() for c in r): continue
        if any(not c.lstrip('-').isdigit() for c in r[:3]): continue
        path.append(tuple(map(int, r[:3])))

if not path: sys.exit("Path is empty!")
print(f"[INFO] {len(path)} points loaded from {INPUT_CSV}")

# ─── Scan loop ────────────────────────────────────────────────────────────────
with open(OUTPUT_CSV, 'w', newline='') as fout:
    wr = csv.writer(fout, delimiter=' ')
    wr.writerow(["x","y","z","reading"])
    current = (0,0,0)
    for i,tgt in enumerate(path,1):
        current = goto(tgt,current); time.sleep(DWELL_S)
        val = read_sensor()
        wr.writerow([*tgt,f"{val:.2f}"]); fout.flush()
        if i%100==0 or i==len(path): print(f"[INFO] {i}/{len(path)} V={val:.2f}")

# ─── Cleanup ──────────────────────────────────────────────────────────────────
ser_motion.close(); ser_sensor.close()
print(f"[INFO] finished – data in {OUTPUT_CSV}")
