from ping import Poll,PingService
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__ == "__main__":
                    
    import traceback
    import types
    led = 4
    GPIO.setup(led, GPIO.OUT)



    ping_svc = PingService("www.sonera.fi")
    #ping_svc.delay=10

    def my_online(self):
        self.log(self.host + " is up")
        GPIO.output(led, 1)
        time.sleep(0.5)
        GPIO.output(led, 0)



    ping_svc.online = types.MethodType(my_online, ping_svc)

    def my_offline(self):
        self.log(self.host + " is down")
        GPIO.output(led, 1)


    ping_svc.offline = types.MethodType(my_offline, ping_svc)


    try:

        ping_svc.start()

        while len(Poll.thread_list()) > 0:
            time.sleep(0.2)

            while len(PingService.msgs) > 0:
                print PingService.msgs.pop(0)


    except KeyboardInterrupt:
    # note: all threads must be stopped before python will exit!
        ping_svc.stop()
        GPIO.cleanup()
        sys.exit(0)
        pass


    except:
        t, v, tb = sys.exc_info()
        traceback.print_exception(t, v, tb)
        ping_svc.stop()
        GPIO.cleanup()
        sys.exit(0)


