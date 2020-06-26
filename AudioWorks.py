import wave

def getAudioData(audio='test.wav'):
    obj = wave.open(audio, 'r')
    channels = obj.getnchannels()
    samplewidth = obj.getsampwidth()
    framerate = obj.getframerate()
    nframes = obj.getnframes()
    params = obj.getparams()
    data = obj.readframes(obj.getnframes())
    obj.close()
    return [data, channels, samplewidth, framerate, nframes, params, audio]


def createAudioFile(audioData, AFname='GeneratedAudioFile.wav'):
    obj2 = wave.open(AFname, 'w')
    obj2.setnchannels(audioData[1])
    obj2.setsampwidth(audioData[2])
    obj2.setframerate(audioData[3])
    obj2.setnframes(audioData[4])
    obj2.setparams(audioData[5])
    obj2.writeframes(audioData[0])
    obj2.close()
    return 0

# createAudioFile(getAudioData())