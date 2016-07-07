# ambipy
Ambi-Climate Python API Bindings

Wholley unsupported by Ambi-Climate (as it was reversed engineered after packeting sniffing and SSL spoofing). More of a proof of concept until the official API is released.

###
Requires:
  - requests (http://docs.python-requests.org/)

###
Known Limitations:
  - Currently only supports one appliance per room, this will be an API breaking change if I update this.
  - Doesn't support all functions.

###
Usage:
  - Create an auth.json file in package root with two keys email and password that is associated with your account. Alternatively you can set the properties directly on the User class.
