# Field_mapper_robot

# Overview
Design of modular, cost-effective field mapper robot

# Requirements


# Part list 

| **Component**                          | **Quantity** | **Price (USD)** | **Product Link**                                                                                                                                       |  
|-----------------------------------------|-------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  
| Z Axis-300mm, XY-300mm-12mm Pitch       | 1           | 338.54           | [Link](https://www.aliexpress.us/item/3256805348651313.html?spm=a2g0o.order_detail.order_detail_item.3.5fa4f19cjVbIP4&gatewayAdapt=glo2usa)             |  
| Stepper Motor Driver TB6600             | 3           | 5.60             | [Link](https://www.aliexpress.us/item/3256805781393725.html?spm=a2g0o.order_detail.order_detail_item.2.1ed6f19cobQnNT&gatewayAdapt=glo2usa)             |  
| Arduino UNO R4 Minima                   | 1           | 16.00            | [Link](https://thepihut.com/products/arduino-uno-r4-minima)                                               
| Gaussmeter Model GM2                    | 1           | 902.00           | [Link](https://www.alphalabinc.com/products/gm2/?srsltid=AfmBOor0p2l-VF9fIRODsZqY854WaDDNnBIFsOJ6kHjN2p6iCgCOzTLX)                                      |  
| **TOTAL**                               |             | **1262.14$**      |                                                                                                        


# Recommended hardware tools and assembly tips
## Tip 1. Attaching printed ruler to the axes
![Diagram](Attachments/tip1.jpg)
Having a ruler attached to the axes would minimize calibration efforts and ensure precise measurements for each step

## Tip 2. Mounting the robot on a wooden panel
Screwing down the robot on a wooden panel (recommended minimum size 40 x 60 x 1.5 cm) would increase stability and aid in calibration

## Tip 3. Using a variable DC power supply 
Buying a variable DC power supply would ease the power supply process. They are readily available and relatively cheap (~15$)
![Diagram](Attachments/tip3.jpg)

## Tip 4. Setting right switches on Stepper motor driver 
For code to work as expected (with right calibrations) and to avoid burning stepper motors with high current, follow the order of switches as shown in the image. (S1-OFF,S2-OFF,S3-OFF,S4-OFF,S5-OFF,S6-OFF)
![Diagram](Attachments/tip4.jpg)

# 3D printable files


# Flowcharts 

![Diagram](Attachments/draw1.png)

![Diagram](Attachments/draw2.png)
