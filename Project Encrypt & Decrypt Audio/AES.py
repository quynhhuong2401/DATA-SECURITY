from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

import random
import string
from Crypto.Cipher import AES

# Taking input
fs, data = wavfile.read('alo.wav')
plt.plot(data)  # fs = sampling frequency = 44.1kHz
plt.title("Original Audio Plot")

with open('alo.wav', 'rb') as fd:
    contents = fd.read()
# Playing that sound

sd.play(data, fs)

# Getting ready with AES

AES_KEY = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))

AES_IV = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

print("AES Key is ", AES_KEY)
print("AES Initialization vector is ", AES_IV)

# Encrpytion of audio file
encryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
encrypted_audio = encryptor.encrypt(contents)

# Saving the encrypted file
with open('encrypted_audio_file.wav', 'wb') as fd:
    fd.write(encrypted_audio)
print("A file titled 'encrypted_audio_file.wav' is generated which is the encrypted audio to be communicated")

# Loading
with open('encrypted_audio_file.wav', 'rb') as fd:
    contents1 = fd.read()

# Decryption of data
decryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
decrypted_audio = decryptor.decrypt(contents1)

with open('decrypted_audio_file.wav', 'wb') as fd:
    fd.write(decrypted_audio)

fs, data1 = wavfile.read('decrypted_audio_file.wav')
plt.plot(data1)  # fs = sampling frequency = 44.1kHz
plt.title("Original Audio Plot")
data_1 = np.asarray(data1, dtype=np.int32)
sd.play(data_1, fs)
