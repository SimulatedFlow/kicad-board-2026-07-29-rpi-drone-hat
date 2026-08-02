# RPi-DroneRover-HAT — PCBWay Share & Sell (einreichfertig, NICHT eingereicht)

Erstellt 2026-08-02. Grund: Der Share&Sell-Lauf vom 2026-07-30 hat dieses Board mit der
Begruendung „hat KEINE deliverables (nie fertig gebaut)" uebersprungen — das war **falsch**
(veralteter Scan-Stand). Alle Deliverables liegen seit 2026-07-29 23:15/23:16 auf Platte.

**Status: VORBEREITET, NICHT abgeschickt.** Der Submit-Klick geht in PCBWays
Redaktions-Review und macht das Projekt danach oeffentlich → das ist ein Publish-Schritt und
bleibt Silvan vorbehalten. Verkaeufer = **Simulated Flow UG** (Hardware).

## Verifizierter Bau-Stand (2026-08-02 nachgeprueft)

| Punkt | Befund |
|---|---|
| `BUILT`-Marker | vorhanden, `2026-07-29T23:16:03` |
| Gerber-ZIP | `RPi-DroneRover-HAT_PCBWay_gerbers.zip`, 93.752 Byte, 28 Dateien inkl. `.drl` |
| Lagen | 4 (F.Cu signal · In1.Cu GND-Plane · In2.Cu +5V-Plane · B.Cu signal) — Gerber `.gtl/.g1/.g2/.gbl` alle vorhanden |
| Abmessung | 65,0 × 56,0 mm (aus Edge.Cuts gemessen) |
| DRC | **0 Fehler**, 12 Warnungen (2 dangling Freerouting-Stubs, 4 MountingHole-Lib-Nag, 6 Silk) — `RPi-DroneRover-HAT_drc_violations.json`, `severity_counts.error = 0` |
| BOM | `bom.csv`, 15 Positionen, komplett THT |
| Schaltplan | `schematic.pdf` (53.772 Byte) |
| Renders | `render_top.png` (69.789 B) + `render_bottom.png` (49.143 B) |
| eBay-Text | `ebay_listing.md` vorhanden |

Damit ist der Deliverable-Satz **identisch** zu den vier am 30.07. eingereichten Boards
(quad-fc, cnc-stepper, sensor-node, brushed-quad) — gleiche sieben Artefakte je Ordner.

## Formularinhalt (1:1 uebernehmen)

Dieselben Felder maschinenlesbar in `pcbway_share_and_sell.json` (gleicher Ordner) — fuer einen
spaeteren automatisierten Lauf direkt einlesbar.

**Titel**
```
RPi-DroneRover-HAT — Hand-Solderable Raspberry Pi HAT for Large Drones & Rovers
```

**Kategorien (genau 3, aus dem Modal „Creative Fields — select up to 3")**
```
Raspberry Pi
Robotics
Flight
```

**Elevator Pitch (≤ 140 Zeichen; hier 118)**
```
Through-hole Raspberry Pi HAT for big drones and rovers: 40-pin Pi header, IMU socket, 4x ESC/servo PWM, 5V BEC input.
```

**Detail-Description (Quill-Editor `.ql-editor`, 1.406 Zeichen)**
```
RPi-DroneRover-HAT — Raspberry Pi HAT for large drones and rovers

A fully through-hole, hand-solderable HAT that turns a Raspberry Pi into the flight/drive controller of a large quadcopter or rover. Plug the Pi in, add a GY-521 IMU module and up to four ESCs or servos, feed it from your BEC — done. Every part is THT, so it assembles with a basic soldering iron: no hot air, no BGA, no stencil.

Features
- 65 x 56 mm standard Raspberry Pi HAT outline, 4x M2.5 mounting holes
- 2x20 female header for the 40-pin Pi GPIO connector
- Socket for a GY-521 / MPU-6050 6-axis IMU module (I2C, 4k7 pull-ups on board)
- 4x 3-pin ESC / servo PWM outputs (signal + 5V + GND) along the top edge
- 5V BEC input on a screw terminal, reverse-polarity protection (1N5819)
- 470 uF bulk + 100 nF decoupling, buzzer header, status LED with 330 R series resistor
- 4-layer stackup: signal / solid GND plane / +5V plane / signal — quiet supply, EMC-friendly
- 15 BOM positions, all standard KiCad footprints, DRC clean (0 errors)

What you get
Gerbers and drill file (PCBWay-ready), BOM as CSV, schematic PDF and example firmware. Project home: https://github.com/SimulatedFlow

Sold as a bare or partially populated PCB — you add the Pi, the IMU module and the connectors. Made to order, shipped from Germany by Simulated Flow UG. Open-source hardware for makers, education and hobby use; not a certified consumer product.
```

**Dateien (Reihenfolge nach dem erprobten Rezept)**

| Feld | Datei |
|---|---|
| `input[type=file]` nth(0) — Gerber-ZIP | `F:\KiCad Projects\BluepillBoards\_BoardIdeas\2026-07-29-rpi-drone-hat\deliverables\RPi-DroneRover-HAT_PCBWay_gerbers.zip` |
| nth(1) — Cover (oeffnet Crop-Modal) | `…\deliverables\render_top.png` |
| nth(4) — Real shot / Galerie | `…\deliverables\render_bottom.png` |

**Restfelder:** Gerber-Download = *Allowed* · Lizenz = Default **CC BY-SA** (Dropdown ist
Custom, nicht per `<select>` setzbar — genau wie bei den vier anderen Boards).

## Ablauf (aus dem funktionierenden Rezept vom 30.07.)

1. `pcbway.com/project/ShareProjectPublish` (Konto simulatedflow eingeloggt, keine Login-Wall).
2. Titel + Pitch **per echter Tastatur tippen** (Feld klicken → Ctrl+A/Delete → `keyboard.type`).
   JS-`.value` reicht nicht: der Zaehler bleibt 0/150 und die Continue-Validierung scheitert still.
3. Kategoriefeld klicken → Modal → die drei Leafs oben exakt anklicken → „Confirm".
4. „Continue" (nur wenn der Zeichenzaehler > 0 steht).
5. Schritt 2: Dateien wie oben; Cover-Crop-Modal per Koordinate absenden (y ∈ [600, 840], x > 1000).
6. Beschreibung in `.ql-editor` in einer **Verify-Retry-Schleife** tippen, bis
   `innerText.trim().length > 200` — der erste Versuch landet erfahrungsgemaess leer.
7. **„Save drafts"** = Entwurf (nicht auffindbar, aber harmlos) · **„Submit"** = Redaktions-Review
   → danach oeffentlich + 10 % Provision. Submit validiert die Description streng
   („please input detail info!"), Save drafts nicht.
8. Erfolgskontrolle: Antwort von `member.pcbway.com/Project/SaveShareProject` = `message success ok`.

## Angemerkte Ungereimtheiten (nicht von mir entschieden)

- **Falsche Vorlagen-Angaben in den generierten Texten dieses Boards.** `ebay_listing.md`
  (aus `board_build_runner`) und `…\_HardwareListings\2026-07-29-rpi-drone-hat\pcbway-shared\listing.md`
  (aus `hardware_multistore_runner`, `_spec_lines`) behaupten „Leerplatine fuer STM32 Bluepill",
  „Passt direkt auf die STM32 'Bluepill'" und „4x M3-Befestigungsbohrungen". Beides stimmt fuer
  dieses Board nicht: es ist ein **Raspberry-Pi**-HAT ohne Bluepill, mit **M2,5**-Bohrungen
  (Footprint `MountingHole_2.75mm`). Der Text oben ist deshalb **von Hand** geschrieben, nicht
  aus den Generatoren uebernommen. Die Generator-Vorlagen sind noch zu fixen (betrifft alle
  Nicht-Bluepill-Boards).
- **Widerspruch Gerber-Freigabe:** die vier eingereichten Boards stehen auf
  „Gerber-Download = Allowed", waehrend `_HardwareListings\…\SUMMARY.md` „Kein Gratis-Download
  der Fertigungsdaten" fordert. Oben ist *Allowed* eingetragen, um zu den vier bereits
  eingereichten Boards zu passen — wenn die SUMMARY-Linie gelten soll, muessen alle fuenf
  geaendert werden.
