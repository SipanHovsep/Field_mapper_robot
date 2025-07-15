# Field Mapper Robot

## Overview
Design of a **modular, cost‑effective robot** for mapping magnetic fields within a defined volume.
<div align="center">
  <img src="Attachments/image1.jpg" width="450" alt="Ruler attached to linear stage" />
</div>
---

## Requirements
*Specify hardware/firmware requirements here.*

---

## Bill of Materials
| Component | Qty | Unit Price (USD) | Link |
|---|:---:|:---:|---|
| Linear stages (Z 300 mm, XY 300 mm – 12 mm pitch) | 1 | 338.54 | [Product](https://www.aliexpress.us/item/3256805348651313.html?spm=a2g0o.order_detail.order_detail_item.3.5fa4f19cjVbIP4&gatewayAdapt=glo2usa) |
| TB6600 stepper driver | 3 | 5.60 | [Product](https://www.aliexpress.us/item/3256805781393725.html?spm=a2g0o.order_detail.order_detail_item.2.1ed6f19cobQnNT&gatewayAdapt=glo2usa) |
| Arduino UNO R4 Minima | 1 | 16.00 | [Product](https://thepihut.com/products/arduino-uno-r4-minima) |
| Gaussmeter GM2 | 1 | 902.00 | [Product](https://www.alphalabinc.com/products/gm2/?srsltid=AfmBOor0p2l-VF9fIRODsZqY854WaDDNnBIFsOJ6kHjN2p6iCgCOzTLX) |
| **Total** |  | **1262.14** |  |

---

## Assembly Tips

### 1 · Axis Ruler for Quick Calibration
<div align="center">
  <img src="Attachments/tip1.jpg" width="450" alt="Ruler attached to linear stage" />
</div>
Attaching a printed ruler minimises calibration time and ensures precise step‑to‑millimetre mapping.

### 2 · Mount on a Rigid Base
<div align="center">
  <img src="Attachments/tip2.jpg" width="450" alt="Robot mounted on wooden panel" />
</div>
Secure the frame to a **≥ 40 × 60 × 1.5 cm** wooden panel for stability during operation.

### 3 · Variable DC Power Supply
<div align="center">
  <img src="Attachments/tip3.jpg" width="450" alt="Variable DC power supply" />
</div>
A low‑cost variable supply (~15 USD) simplifies testing different motor voltages and current limits.

### 4 · TB6600 DIP‑Switch Settings
<div align="center">
  <img src="Attachments/tip4.jpg" width="450" alt="TB6600 switch positions" />
</div>
Set switches **S1–S6 = OFF** to match the firmware micro‑stepping and protect the motors.

---

## 3‑D Printable Parts
*Upload STL/STEP files in this directory and list them here.*

---

## High‑Level Workflow
<div align="center">
  <img src="Attachments/draw1.png" width="500" alt="System flowchart 1" />
</div>
<div align="center">
  <img src="Attachments/draw2.png" width="500" alt="System flowchart 2" />
</div>

---

© 2025 Field Mapper Robot Project. Licensed under MIT.
