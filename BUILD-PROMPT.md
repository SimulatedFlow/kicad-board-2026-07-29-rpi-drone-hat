```json
{
  "board_name": "RPi-DroneRover-HAT",
  "one_liner": "Raspberry-Pi-HAT mit 40-pin Pi-Header, IMU-Modulsockel, 4x ESC/Servo-PWM-Ausgaengen, BEC-5V-Einspeisung, Buzzer und Status-LED.",
  "confidence": "medium",
  "price_eur": 21
}
```

## BUILD-PROMPT

### 1. Board-Spezifikation & DFM
* **Abmessungen:** 65,0 mm × 56,0 mm (Raspberry-Pi-HAT-Format), 4-lagig (F.Cu/B.Cu Signal, In1.Cu GND, In2.Cu +5V), FR4 1,6 mm.
* **Nur THT.** IMU als aufsteckbares Modul (GY-521). Keine SMD-ICs. Pi-GPIO ist 3,3 V — ESC-Signale werden von 3,3 V direkt getrieben (uebliche Praxis).
* **Spurbreiten:** Signal ≥ 0,4 mm; +5V/GND ≥ 1,0 mm. Clearance ≥ 0,3 mm.

### 2. Mechanik (HAT-Standard)
* Nullpunkt (0,0) unten links, 65×56 mm. **4× M2,5-Bohrung** (Ø 2,75 mm) an den HAT-Standardpositionen (3,5 / 3,5), (61,5 / 3,5), (3,5 / 52,5), (61,5 / 52,5); 3,0 mm Keepout. Der 40-pin-Header liegt am Rand wie beim HAT-Standard.

### 3. Bauteilliste (Standard-KiCad-Bibliotheken)
1. **J_PI (40-pin Pi-GPIO):** 1× Buchsenleiste **2x20** (Stacking-faehig). `Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical`
2. **J_IMU (GY-521-Sockel):** 1× Buchsenleiste 1x08. `Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical`
3. **J_M1..J_M4 (ESC/Servo):** 4× Stiftleiste 1x03 (SIG, +5V, GND). `Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical`
4. **J_BEC (5V-Einspeisung):** 1× Schraubklemme 2-polig. `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal`
5. **D_PWR:** 1× 1N5819. `Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal`
6. **C_BULK:** 1× Elko 470 µF/16 V. `Capacitor_THT:CP_Radial_D8.0mm_P3.50mm`  **C_DEC:** 1× 100 nF. `Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm`
7. **R_SDA, R_SCL:** 2× 4,7 kΩ I2C-Pullups nach +3V3. `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal`
8. **BZ:** 1× Stiftleiste 1x02 (aktiver Buzzer). `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`
9. **LED1 + R_LED (330 Ω):** Status. `LED_THT:LED_D5.0mm`, `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal`

### 4. Netze (Raspberry-Pi-40-pin-Nummerierung)
* **Versorgung:** J_BEC.1 → Anode D_PWR; Kathode → **+5V** → J_PI Pin2 & Pin4 (5V), J_IMU.VCC, J_M1..4 Pin2, C_BULK(+), C_DEC(+). Alle GND (J_PI Pin6/9/14/20/25/30/34/39, J_BEC.2, C(−), J_IMU.GND, J_M1..4 Pin3, BZ.2) → **GND**. +3V3 = J_PI Pin1 → R_SDA/R_SCL Pullup-Versorgung.
* **I2C (IMU):** J_PI **Pin3 (GPIO2/SDA1)** → J_IMU.SDA + R_SDA; **Pin5 (GPIO3/SCL1)** → J_IMU.SCL + R_SCL. J_IMU.INT → J_PI **Pin7 (GPIO4)**. J_IMU.AD0 → GND.
* **ESC-PWM (hardware-PWM-faehige GPIOs):** J_PI **Pin32 (GPIO12) → J_M1.1**, **Pin33 (GPIO13) → J_M2.1**, **Pin12 (GPIO18) → J_M3.1**, **Pin35 (GPIO19) → J_M4.1**.
* **Buzzer:** J_PI **Pin37 (GPIO26) → BZ.1**. **Status-LED:** J_PI **Pin36 (GPIO16) → R_LED → LED1** → GND.

### 5. Layout
* J_PI (2x20) an die lange Unterkante (HAT-konform). IMU-Sockel zentral. Die 4 ESC-Header an den gegenueberliegenden Rand, beschriftet M1..M4. J_BEC an eine kurze Kante (dicke +5V-Bahn zum Pi-5V). Silk beschriften: 5V, GND, SDA, SCL, M1-M4, Buzzer.

### 6. Workflow (MCP)
1. Schaltplan (Net-Labels + Footprints, Pi-Pinnummern als Kommentar). 2. PCB Edge.Cuts 65×56, 4× M2,5 an HAT-Position. 3. 4 Lagen: In1.Cu GND + In2.Cu +5V ZUERST. 4. Weiträumig platzieren. 5. Freerouting (Signal 0,4 / +5V 1,0 mm) nur F/B. 6. DRC 0. 7. Gerber+Drill → ./gerbers. 8. Ehrliche Zusammenfassung.
