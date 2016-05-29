from brewapp import app
from brewapp.base.hardwareswitch import SwitchBase
from brewapp.base.model import *

try:
    import RPi.GPIO as GPIO
    app.logger.info("SETUP GPIO Module Loaded")
except Exception as e:
    app.logger.error("SETUP GPIO Module " + str(e))
    pass

class BrewGPIO(SwitchBase):

    def init(self):
        app.logger.info("INIT GPIO")
        try:
            GPIO.setmode(GPIO.BCM)

            for h in app.brewapp_hardware_config:
                g = self.translateDeviceName(h)
                print g

                if(g != None):
                    app.logger.info("SETUP HARDWARE: " + h + " GPIO: " + str(g))
                    GPIO.setup(g, GPIO.OUT)
                    if(self.getConfigValue(h, "inverted", False)):
                        GPIO.output(g, 1)
                    else:
                        GPIO.output(g, 0)
            '''
            hw = Hardware.query.all()
            for h in hw:
                g = self.translateDeviceName(h.switch)
                if(g != None):
                    app.logger.info("SETUP HARDWARE: " + h.name + " GPIO: " + str(g))
                    GPIO.setup(g, GPIO.OUT)
                    GPIO.output(g, 0)

            kettles = Kettle.query.all()
            for k in kettles:
                heater_gpio = self.translateDeviceName(k.heater)
                if(heater_gpio != None and heater_gpio != ""):
                    app.logger.info("SETUP GPIO HEATER: " + str(heater_gpio))
                    GPIO.setup(heater_gpio, GPIO.OUT)
                    GPIO.output(heater_gpio, 0)

                ## Init agitator
                agitator_gpio = self.translateDeviceName(k.agitator)
                if(agitator_gpio != None and agitator_gpio != ""):
                    app.logger.info("SETUP GPIO AGITATOR" + str(agitator_gpio))
                    GPIO.setup(agitator_gpio, GPIO.OUT)
                    GPIO.output(agitator_gpio, 0)
            '''
            app.brewapp_gpio = True
            self.state = True
            app.logger.info("ALL GPIO INITIALIZED")

        except Exception as e:
            app.logger.error("SETUP GPIO FAILD " + str(e))
            app.brewapp_gpio = False
            self.state = False

    def cleanup(self):
        try:
            GPIO.cleanup()
        except Exception as e:
            app.logger.error("CLEAN UP OF GPIO FAILD " + str(e))

    def getDevices(self):
        gpio = []
        for i in range(2, 27):
            gpio.append("GPIO"+str(i))
        return gpio

    def translateDeviceName(self, name):
        if(name == None or name == ""):
            return None
        return int(name[4:])

    def switchON(self, device):
        app.logger.info("GPIO ON" + str(device))
        if(app.brewapp_gpio == True):
            gpio = self.translateDeviceName(device)
            #GPIO.output(gpio, 1)
            if(self.getConfigValue(device, "inverted", False)):
                GPIO.output(g, 0)
            else:
                GPIO.output(g, 1)
            pass
        else:
            app.logger.warning("GPIO TEST MODE ACTIVE. GPIO is not switched on" + str(device))

    def switchOFF(self, device):
        app.logger.info("GPIO OFF" + str(device))
        if(app.brewapp_gpio == True):
            gpio = self.translateDeviceName(device)
            if(self.getConfigValue(device, "inverted", False)):
                GPIO.output(g, 1)
            else:
                GPIO.output(g, 0)
            #GPIO.output(gpio, 0)
            pass
        else:
            app.logger.warning("GPIO TEST MODE ACTIVE. GPIO is not switched off" + str(device))
