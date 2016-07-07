
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

class Room(object):
    def __init__(self, rawDeviceData):
        self.__deviceDict = rawDeviceData
        self.__setup()

        import pprint as pp
        #pp.pprint(self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')])

    def __setup(self):
        self.__name = self.__deviceDict[unicode("room_name")]
        self.__deviceId = self.__deviceDict[unicode("device_id")]
        self.__powerState = self.__deviceDict[unicode('appliances')][0][unicode('appliance_state')][unicode('data')][0][unicode('power')]
        #print(self.__powerState)

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
        pass

    @property
    def mode(self):
        pass

    @mode.setter
    def mode(self, modeIn):
        pass

    @property
    def swing(self):
        pass

    @swing.setter
    def swing(self):
        pass

    @property
    def temperature(self):
        pass

    @temperature.setter
    def temperature(self):
        pass
