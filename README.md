# sleepcycle-mqtt
a bridge between the Sleepcycle App's PartnerLink and MQTT

## What does it do?
Sleepcycle offers on iOS the possibility to link with other people. They call this feature PartnerLink.

PartnerLink works by first publishing the iPhone/iPad's device name under the mdns service `_sleepcycle_ald._tcp.local.`.
So if your phone is called `Klaernie iPhone`the resulting mdns announcement would be for `Klaernie iPhone._sleepcycle_ald._tcp.local.`

This script now listens for these announcements, and when they are detected pushes a message with the value `ON` to an mqtt topic,
and also publishes a Homeassistant compatible autodiscovery entry.

## Configuration
As I intended to start this script via systemd I wanted to maintain the configuration in the systemd unit file as well.

Hence script requires two environment variables:
- `MQTT_SERVER` - the MQTT server it connects to
- `MQTT_TOPIC` - the base topic, under which it's status topics will apprear

## Limitations
- As this only runs locally, I did not feel the need to support TLS on the MQTT connection.
- Homeassistant discovery is non-configurable. I was just too lazy, so if you want it please send a PR.
- I bet there is a nice way to make the information pushed to Homeassistant more fleshed out.
- The environment variables don't have defaults in the code, only in the shipped service file
- A requirement is the `python3-zeroconf` package used. When I wrote this first it did not accept the mdns service name due to the disallowed `_` in the name. This may have changed by now.

## License
MIT License

Copyright (c) 2020 Andre Klärner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
