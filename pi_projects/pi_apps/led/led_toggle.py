import gpiozero
import time
import sys

class BlinkLed:
    def __init__(self, pin, onoff_time=.5):
        self.led = gpiozero.LED(pin)
        self.onoff_time = onoff_time
    
    def blink_forever(self):
        while True:
            self.led.on()
            time.sleep(1)
            self.led.off()
            time.sleep(1)
    
    def blink(self, numer_of_times=-1):
        MAX_ = 100
        if (numer_of_times != -1):
            print("blink %d times" % numer_of_times)
            self.led.blink(on_time=self.onoff_time, off_time=self.onoff_time, n=numer_of_times, background=True)
#           This doesn't work 
#            while (self.led._blink_thread is not None):
            while (self.led._blink_thread.is_alive() ):
                time.sleep(.5)
#            print ("Blink thread alive = %s" % (self.led._blink_thread is None))
        else:
            print("blink %d times" % MAX_)
            self.led.blink(n=MAX_, background=False)

def main():
    pin_ = 4
    on_off_time = .25
    blink_num = 10
    print("Blink LED: BCM%d" % pin_)
    blink_led = BlinkLed(pin=pin_, onoff_time=on_off_time)
#    blink_led.blink()
    blink_led.blink(blink_num)
    return 1

if __name__ == '__main__':
    main()
    sys.exit()

