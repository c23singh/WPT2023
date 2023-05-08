% Define the LSFR parameters
lsfr_length = 8; % Length of the LSFR
lsfr_taps = [8 6 5 4]; % Taps of the LSFR polynomial
lsfr_seed = [0 1 0 1 0 0 1 1]; % Seed of the LSFR

% define the message to encrypt
message = 'tza';
cipherArray = [];
% convert the character to a binary string
ciphertext = dec2bin(message, 8); 
disp(ciphertext)
disp(cipherArray)

% Load the ciphertext message
% ciphertext = [0 1 0 1 1 0 1 1 0 1 1 1 0 0 1 1];

% Initialize the LSFR state
lsfr_state = lsfr_seed;

% Generate the pseudorandom sequence used for decryption
for i = 1:length(ciphertext)
    % Compute the next LSFR output bit
    output_bit = mod(sum(lsfr_state(lsfr_taps)), 2);
    
    % Update the LSFR state
    lsfr_state = [output_bit lsfr_state(1:end-1)];
    
    % Save the LSFR output bit for decryption
    decryption_key(i) = output_bit;
end

% Decrypt the ciphertext message
plaintext = xor(ciphertext, decryption_key);

% Display the decrypted message
disp(char(bin2dec(char(reshape(char('0'+plaintext), 8, [])')))');
