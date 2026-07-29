#!/usr/bin/env python3
"""
RPi-DroneRover-HAT — Beispiel-Software (Raspberry Pi, pigpio)
Simulated Flow UG · MIT-Lizenz · github.com/SimulatedFlow

Liest die MPU-6050 (I2C /dev/i2c-1) und gibt 4 ESC/Servo-PWM-Signale (1000-2000us,
50 Hz) auf GPIO12/13/18/19 aus. Einfacher Rate-Mode-P-Mixer als edukative Basis.

  sudo apt install python3-smbus pigpio && sudo systemctl enable --now pigpiod
  python3 drone_hat.py

⚠️ KEIN zertifizierter Flugcontroller. Nur mit abgenommenen Propellern testen.
"""
import time
import smbus2 as smbus
import pigpio

MPU = 0x68
ESC = {"M1": 12, "M2": 13, "M3": 18, "M4": 19}   # BCM
LED, BUZZ = 16, 26

pi = pigpio.pi()
bus = smbus.SMBus(1)


def mpu_init():
    bus.write_byte_data(MPU, 0x6B, 0x00)   # wake
    bus.write_byte_data(MPU, 0x1B, 0x08)   # gyro +/-500 dps


def _s16(h, l):
    v = (h << 8) | l
    return v - 65536 if v > 32767 else v


def gyro():
    d = bus.read_i2c_block_data(MPU, 0x43, 6)
    return (_s16(d[0], d[1]) / 65.5, _s16(d[2], d[3]) / 65.5, _s16(d[4], d[5]) / 65.5)


def esc_us(pin, us):
    pi.set_servo_pulsewidth(pin, max(1000, min(2000, int(us))))


def main():
    for p in ESC.values():
        esc_us(p, 1000)
    pi.set_mode(LED, pigpio.OUTPUT)
    pi.set_mode(BUZZ, pigpio.OUTPUT)
    mpu_init()
    time.sleep(2)   # ESC-Arming

    # Demo: fester Schwebe-Sollwert (im echten Betrieb: RC/MAVLink-Eingang)
    throttle, roll_sp, pitch_sp, yaw_sp = 1200, 0, 0, 0
    Kp = 0.9
    t0 = time.time()
    try:
        while True:
            gx, gy, gz = gyro()
            u_roll = roll_sp * 0.5 - Kp * gx
            u_pitch = pitch_sp * 0.5 - Kp * gy
            u_yaw = yaw_sp * 0.5 - Kp * gz
            esc_us(ESC["M1"], throttle - u_roll - u_pitch - u_yaw)   # vorne rechts
            esc_us(ESC["M2"], throttle - u_roll + u_pitch + u_yaw)   # hinten rechts
            esc_us(ESC["M3"], throttle + u_roll + u_pitch - u_yaw)   # hinten links
            esc_us(ESC["M4"], throttle + u_roll - u_pitch + u_yaw)   # vorne links
            pi.write(LED, int(time.time() * 2) & 1)
            time.sleep(0.005)   # ~200 Hz
    except KeyboardInterrupt:
        pass
    finally:
        for p in ESC.values():
            pi.set_servo_pulsewidth(p, 0)
        pi.stop()
        print("\nMotoren aus, beendet. Zeit:", round(time.time() - t0, 1), "s")


if __name__ == "__main__":
    main()
