from constants import REST_URL
import requests
import home

# TODO add docstrings

class Modes(object):
    # I imagine there are other modes.. I just haven't seen them yet.
    COOL = "cool"

class Fan(object):
    HIGH = "high"
    LOW = "low"
    AUTO = "auto"

class Swing(object):
    AUTO = "auto"
    OFF = "off"

class Power(object):
    OFF = "off"
    ON = "on"

class Comfort(object):
    # Guesses at values probably wrong need more data points.
    HOT = 2.0
    TOO_WARM = 1.8
    A_BIT_WARM = 1.6
    COMFORTABLE = 1
    A_BIT_COLD = 0.8
    TOO_COLD = 0.6
    FREEZING = 0.4

class Room(object):
    def __init__(self, rawDeviceData, headers):
        self.__deviceDict = rawDeviceData

        home.log("raw :: {0}".format(self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')]))
        self.__headers = headers
        self.__setup()

    def __setup(self):
        self.__name = self.__deviceDict[unicode("room_name")]
        self.__deviceId = self.__deviceDict[unicode("device_id")]

        rawPower = self.__deviceDict[unicode("appliances")][0][unicode("appliance_state")][unicode("data")][0][unicode("power")]

        if rawPower == "On":
            self.__powerState = Power.ON
        if rawPower == "Off":
            self.__powerState = Power.OFF

        self.__temperature = self.__deviceDict[unicode("appliances")][0][unicode("appliance_state")][unicode("data")][0]["temperature"]

        rawMode = self.__deviceDict[unicode("appliances")][0][unicode("appliance_state")][unicode("data")][0]["mode"]
        rawFan = self.__deviceDict[unicode("appliances")][0][unicode("appliance_state")][unicode("data")][0]["fan"]
        rawSwing = self.__deviceDict[unicode("appliances")][0][unicode("appliance_state")][unicode("data")][0]["swing"]

        if rawFan == "Auto":
            self.__fanState = Fan.AUTO
        elif rawFan == "High":
            self.__fanState = Fan.HIGH
        elif rawFan == "Low":
            self.__fanState = Fan.LOW

        if rawMode == "Cool":
            self.__modeState = Modes.COOL

        if rawSwing == "Off":
            self.__swingState = Swing.OFF
        elif rawSwing == "Auto":
            self.__swingState = Swing.AUTO

    def __name__(self):
        return self.__name

    @property
    def deviceId(self):
        return self.__deviceId

    @property
    def name(self):
        return self.__name

    @property
    def power(self):
        return self.__powerState

    @power.setter
    def power(self, stateIn):
        if stateIn == Power.OFF:
            self.__powerState = Power.OFF
        elif stateIn == Power.ON:
            self.__powerState = Power.ON
        else:
            raise ValueError

        data = {"button": "power", "power": self.__powerState, "device_id": self.__deviceId, "fan": self.__fanState, "mode": self.__modeState, "swing": self.__swingState, "temperature": self.__temperature}
        home.log("Payload :: {0}".format(data))
        home.log("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)
        return True

    @property
    def mode(self):
        return self.__modeState

    @mode.setter
    def mode(self, modeIn):
        pass

    @property
    def swing(self):
        return self.__swingState

    @swing.setter
    def swing(self, swingStateIn):
        if swingStateIn == Swing.OFF:
            self.__swingState = Swing.OFF
        elif swingStateIn == Swing.AUTO:
            self.__swingState = Swing.AUTO

        data = {"button": "swing", "device_id": self.__deviceId, "fan": self.__fanState, "mode": self.__modeState, "swing": self.__swingState, "temperature": self.__temperature, "power": self.__powerState}
        home.log("Payload :: {0}".format(data))
        home.log("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)
        return True

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperatureIn):
        """
        Allows user to set temperature.

        Args:
            temperatureIn `float`.

        Returns:
            `bool` For success state.

        """
        if isinstance(temperatureIn, float) != True:
            raise ValueError
            return False
        else:
            data = {"quantity": "Temperature", "value": temperatureIn, "device_id": self.__deviceId}
            response = requests.put("{0}/AbsoluteApplianceControlTarget".format(REST_URL), data=data, verify=False, headers=self.__headers)
            return True

    @property
    def fan(self):
        return self.__fanState

    @fan.setter
    def fan(self, fanStateIn):
        if fanStateIn == Fan.HIGH:
            self.__fanState = Fan.HIGH
        elif fanStateIn == Fan.LOW:
            self.__fanState = Fan.LOW
        elif fanStateIn == Fan.AUTO:
            self.__fanState = Fan.AUTO
        else:
            raise ValueError

        data = {"button": "fan", "device_id": self.__deviceId, "fan": self.__fanState, "mode": self.__modeState, "swing": self.__swingState, "temperature": self.__temperature, "power": self.__powerState}
        home.log("Payload :: {0}".format(data))
        home.log("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)
        return True
