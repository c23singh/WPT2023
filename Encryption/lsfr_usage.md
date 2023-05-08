# Linear Shift Feedback Register (LFSR)

Source: Lt Col Jason McGinthy

Included is a very basic example simulating lsfr encryption using MATLAB and Simulink

Required Dependencies
- MATLAB
- Simulink
- Communications Toolbox (which will install other dependencies)

The linear_shift_feedback_register_demo file is comprised of 2 53-bit LFSRs, one that represents the stream cipher, and the other is a random data stream.  These streams are then XOR’d to create a ciphertext and then the original stream cipher is XOR’d with the cipher text to show the original data stream. 


To run the file, just click the green run button at the top of the Simulink window.  The Scope window should open and display 4 plots: the stream cipher, the data stream, the ciphertext, and the decrypted data stream.  In theory you can change the data waveform and as long as you have the correct timing for the XOR, you can use any wave.