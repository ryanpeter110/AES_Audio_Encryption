import AudioWorks as aw
import AES

audioData = aw.getAudioData('test.wav')

AES.enc.encrypt_file(audioData[6])
AES.enc.decrypt_file(audioData[6] + '.enc')