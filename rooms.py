
#{u'room_name': u'Living Room', u'mac': u'00:9A:D5:52:1A:AA', u'created_on': u'2015-08-21T02:42:55+00:00', u'role': u'Admin', u'location': {u'location_id': u'1c29020c-ac1e-4602-9fcb-965533645e97'}, u'appliances': [{u'irprofile_id': 297, u'appliance_id': u'1fa2bbcc-da78-42e8-bbf7-422303725ed9', u'name': None, u'appliance_state': {u'limit': 1, u'appliance_id': u'1fa2bbcc-da78-42e8-bbf7-422303725ed9', u'data': [{u'louver': u'Auto', u'power': u'On', u'created_on': u'2016-07-07T04:52:55+00:00', u'fan': u'Auto', u'mode': u'Cool', u'swing': u'Off', u'temperature': 25}], u'offset': 0}, u'series': None, u'ircode_profile_id': 622, u'model': None, u'type': u'AirConditioner', u'manufacturer': u'FUJITSU GENERAL'}], u'sensors': {u'temperature': {u'limit': 1, u'device_id': u'05E1FF393131573257198116', u'data': [{u'created_on': u'2016-07-07T05:58:05+00:00', u'value': 25.139999389648438}], u'offset': 0}, u'humidity': {u'limit': 1, u'device_id': u'05E1FF393131573257198116', u'data': [{u'created_on': u'2016-07-07T05:58:05+00:00', u'value': 75.41999816894531}], u'offset': 0}}, u'type': u'IRBlaster', u'device_id': u'05E1FF393131573257198116'}

class Room(object):
    def __init__(self, rawDeviceData):
        self.__deviceDict = rawDeviceData
        self.__setup()

    def __setup(self):
        pass
        self.__name = self.__deviceDict[unicode("room_name")]

    def __name__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def power(self):
        pass

    @power.setter
    def power(self, stateIn):
        pass
