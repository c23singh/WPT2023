% LFSR Encryption in MATLAB

% define the message to encrypt
message = 'secret_stuff';

% define the polynomial coefficients for the LFSR
poly = [1 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1];

% define the initial state of the LFSR
state = [1 0 1 0 0 1 1 1 1 0 1 0 0 0 1 1];

% calculate the length of the LFSR
n = length(poly);

% initialize the encrypted message
encrypted_message = [];

% loop through each character in the message
for i = 1:length(message)  
    % convert the character to a binary string
    binary_string = dec2bin(message(i), 8); 
    % loop through each bit in the binary string
    for j = 1:8
        % shift the LFSR by one position
        feedback_bit = mod(state(poly == 1)*ones(sum(poly),1),2);
        state = [feedback_bit state(1:n-1)];
        % store feedback_bit to constuct decryption key
        decryption_key(j) = feedback_bit;
        % encrypt the bit by XORing it with the LFSR output
        encrypted_bit = xor(str2double(binary_string(j)), state(1));
        % add the encrypted bit to the encrypted message
        encrypted_message = [encrypted_message encrypted_bit];
    end
end

% display the encrypted message
disp('Encrypted message:');
disp(encrypted_message);

% Decrypt the ciphertext message
plaintext = xor(encrypted_message, decryption_key);

% Display the decrypted message
disp(char(bin2dec(char(reshape(char('0'+plaintext), 8, [])')))');
