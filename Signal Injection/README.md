# Signal Injection

### Waveform Generator Script:
This script allows you to enter a specific 	qi message in binary form, and generate a waveform that can be injected via the waveform generator. The Qi Wireless Power Transfer System Power Class 0 Specification defines the structure of various qi messages that you can craft with this code. The ones we explored but have not been 100% successful with were control error packets and stop charge packets. These can potentially be used to stop a device from charging. This script also generates a .csv file that can be used by the waveform generator.

### Waveform Generator ( Keysight 33500B Series Waveform Generator with an adversarial coil):
The waveform generator can be used to inject your newly crafted waveform across the adversarial coil. This is accomplished by loading your waveform onto a usb drive and sticking it in the back of the waveform generator. From the UI on the waveform generator, the .csv can be selected as a waveform to be used. The waveform generator can then be connected to the adversarial coil to send your packet across it.