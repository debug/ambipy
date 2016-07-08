from constants import REST_URL
import requests

# TODO change to emum model
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
    HIGH = "high"
    LOW = "low"
    AUTO = "auto"

class Room(object):
    def __init__(self, rawDeviceData, headers):
        self.__deviceDict = rawDeviceData

        print(self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')])
        self.__headers = headers
        self.__setup()

    def __setup(self):
        self.__name = self.__deviceDict[unicode("room_name")]
        self.__deviceId = self.__deviceDict[unicode("device_id")]
        self.__powerState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0][unicode('power')]

        self.__fanState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['fan']
        self.__modeState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0]['mode']
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
        data = {'button': 'power', 'device_id': self.__deviceId, 'fan': self.__fanState, 'mode': self.__modeState, 'swing': self.__swingState, 'temperature': self.__temperature}
        if stateIn == False:
            data['power'] = "off"
        elif stateIn == True:
            data['power'] = "on"

        print("{0}/IrDeployment".format(REST_URL))
        response = requests.put("{0}/IrDeployment".format(REST_URL), data=data, verify=False, headers=self.__headers)

    @property
    def mode(self):
        pass

    @mode.setter
    def mode(self, modeIn):
        pass

    @property
    def swing(self):
        return self.__swingState

    @swing.setter
    def swing(self):
        pass

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self):
        pass

    @property
    def fan(self):
        return self.__fanState

    @fan.setter
    def fan(self):
        pass
