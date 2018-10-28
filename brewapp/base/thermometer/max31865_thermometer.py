import os
from subprocess import Popen, PIPE, call
from random import randint, uniform
from brewapp import app
from decimal import Decimal, ROUND_HALF_UP
from subprocess import call

class MAX31865Thermometer(object):

    def init(self):
        try:
            app.logger.warning("MAX31865 initialization not implemented")
            # Get control of SPI bus
        except Exception as e:
            app.logger.error("Failed to initialize 1 wire thermometer ERROR: " + str(e))

    def getSensors(self):
        try:
            arr = []
            app.logger.warning("MAX31865 Sensor Check not implemented")
            # Poll all SPI SS lines for MAX31865 Devices
        except:
            return ["MAX31865DummySensor1","MAX31865DummySensor2"]

    def readTemp(self, tempSensorId):

        try:
            if(tempSensorId == None or tempSensorId == ""):
                return -1
            if (app.testMode == True):
                temp_C = 22.2
            else:
                app.logger.warning("MAX31865 readTemp not implemented")
                # Get temp from sensor
                temp_C = 11.1
        except Exception as e:
            app.logger.warning("Error" + str(e))
            return None

        return float(format(temp_C, '.2f'))