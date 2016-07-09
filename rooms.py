from constants import REST_URL
import requests
import home

# TODO change to emum model
# TODO add docstrings
'''
https://rest.ambiclimate.com/IrDeployment
button: power
device_id
fan: high
mode: cool
power: off
swing: off
temperature: 27
'''

class Modes(object):
    # I imagine there are other modes.. I just haven't seen them yet.
    COOL = "Cool"

class Fan(object):
    HIGH = "High"
    LOW = "Low"
    AUTO = "Auto"

class Swing(object):
    AUTO = "Auto"
    OFF = "Off"

class Power(object):
    OFF = "Off"
    ON = "On"

'''
Ambipy :: raw :: [{u'louver': None, u'power': u'Off', u'created_on': u'2016-07-09T05:46:48+00:00', u'fan': u'High', u'mode': u'Cool', u'swing': u'Off', u'temperature': 26}]
Ambipy :: raw :: [{u'louver': u'Off', u'power': u'Off', u'created_on': u'2016-07-09T05:46:52+00:00', u'fan': u'Auto', u'mode': u'Cool', u'swing': u'Auto', u'temperature': 19}]
Ambipy :: Payload :: {'temperature': 26, 'power': 'On', 'button': 'power', 'fan': 'High', 'mode': 'Cool', 'swing': u'Off', 'device_id': u'05D8FF393131573257198218'}
'''

class Room(object):
    def __init__(self, rawDeviceData, headers):
        self.__deviceDict = rawDeviceData

        home.log("raw :: {0}".format(self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')]))
        self.__headers = headers
        self.__setup()

    def __setup(self):
        self.__name = self.__deviceDict[unicode("room_name")]
        self.__deviceId = self.__deviceDict[unicode("device_id")]
        self.__powerState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0][unicode('power')]

        rawMode = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['mode']
        rawFan = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['fan']

        if rawFan == "Auto":
            self.__fanState = Fan.AUTO
        elif rawFan == "High":
            self.__fanState = Fan.HIGH

        if rawMode == "Cool":
            self.__modeState = Modes.COOL

        self.__swingState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['swing']
        self.__temperature = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['temperature']

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

        data = {'button': 'power', 'power': self.__powerState, 'device_id': self.__deviceId, 'fan': self.__fanState, 'mode': self.__modeState, 'swing': self.__swingState, 'temperature': self.__temperature}
        home.log("Payload :: {0}".format(data))
        home.log("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)

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
        elif stateIn == Swing.AUTO:
            self.__swingState = Swing.AUTO

        data = {'button': 'swing', 'device_id': self.__deviceId, 'fan': self.__fanState, 'mode': self.__modeState, 'swing': self.__swingState, 'temperature': self.__temperature}
        home.log("Payload ::", data)
        home.log("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)


    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperatureIn):
        if isinstance(temperatureIn, float) != True:
            raise ValueError
        else:
            print("this is correct")

    @property
    def fan(self):
        return self.__fanState

    @fan.setter
    def fan(self):
        pass
