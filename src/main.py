import RPi.GPIO as GPIO
from dynamic_resist import DynamicResist
from sensor_sound import SensorSound

def main():
    print('Start program!')

    dynamic_resist = DynamicResist()
    sensor_sound = SensorSound()

    dynamic_resist.run()
    sensor_sound.run()

    while True:
        try:
            pass

        except KeyboardInterrupt:
            print('main KeyboardInterrupt')


if __name__ == '__main__':
    main()
    GPIO.cleanup(0)
