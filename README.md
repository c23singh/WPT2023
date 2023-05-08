# WPT2023

README

Signature Analysis Script:
This script will display the manufacturer, serial number, battery status, and power received of a device given a series of qi messages. These qi messages can currently only be obtained by hand copying them from the qi sniffer’s software to a text file. One good area to place effort would be automating the process of placing qi messages read by the sniffer into a text file. The  graph of the power received by the phone can be used to predict which applications are running on the device. 

Waveform Generator Script:
This script allows you to enter a specific 	qi message in binary form, and generate a waveform that can be injected via the waveform generator. The Qi Wireless Power Transfer System Power Class 0 Specification defines the structure of various qi messages that you can craft with this code. The ones we explored but have not been 100% successful with were control error packets and stop charge packets. These can potentially be used to stop a device from charging. This script also generates a .csv file that can be used by the waveform generator. 

Waveform Generator:
The waveform generator can be used to inject your newly crafted waveform across the adversarial coil. This is accomplished by loading your waveform onto a usb drive and sticking it in the back of the waveform generator. From the UI on the waveform generator, the .csv can be selected as a waveform to be used. The waveform generator can then be connected to the adversarial coil to send your packet across it. 

Qi Sniffer Software:
The Qi Sniffer and its software can e used in tandem to collect several important pieces of information from the communication between a device a the power transmitter. The Qi Sniffer must be placed in very close proximity to the transmitter. We tended to place the sniffer under the transmitter with the phone on top of everything. Once this is complete, the software can start recording by pressing the play button. To stop the recording, press the stop button. These snapshots can be saved as a .qid file. These files can only be opened by the sniffer software. The hex for these files can be explored using hexed.it, however, no useful information was found within. This may be worth exploring to automate the data collection process. 

