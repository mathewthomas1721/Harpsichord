#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Generates .wav files of all scales based on starting frequency

from MeanTone import meantone
from KarplusStrong import Generate
from EvenTempered import ET
from PythagDodec import dodec
from Ptolemy import ptolemy

ETfilenameDict = { 0 :"EvenTemperedScale/C.wav", 1 : "EvenTemperedScale/C#.wav", 2 : "EvenTemperedScale/D.wav", 3 : "EvenTemperedScale/D#.wav", 4 : "EvenTemperedScale/E.wav", 5 : "EvenTemperedScale/F.wav", 6 : "EvenTemperedScale/F#.wav", 7 :"EvenTemperedScale/G.wav", 8 : "EvenTemperedScale/G#.wav", 9 : "EvenTemperedScale/A.wav", 10 : "EvenTemperedScale/A#.wav", 11 : "EvenTemperedScale/B.wav"  }
ETfilenameOctave1Dict = { 0 :"EvenTemperedScale/Octave1C.wav", 1 : "EvenTemperedScale/Octave1C#.wav", 2 : "EvenTemperedScale/Octave1D.wav", 3 : "EvenTemperedScale/Octave1D#.wav", 4 : "EvenTemperedScale/Octave1E.wav", 5 : "EvenTemperedScale/Octave1F.wav", 6 : "EvenTemperedScale/Octave1F#.wav", 7 :"EvenTemperedScale/Octave1G.wav", 8 : "EvenTemperedScale/Octave1G#.wav", 9 : "EvenTemperedScale/Octave1A.wav", 10 : "EvenTemperedScale/Octave1A#.wav", 11 : "EvenTemperedScale/Octave1B.wav"  }
ETfilenameOctave2Dict = { 0 :"EvenTemperedScale/Octave2C.wav", 1 : "EvenTemperedScale/Octave2C#.wav", 2 : "EvenTemperedScale/Octave2D.wav", 3 : "EvenTemperedScale/Octave2D#.wav", 4 : "EvenTemperedScale/Octave2E.wav", 5 : "EvenTemperedScale/Octave2F.wav", 6 : "EvenTemperedScale/Octave2F#.wav", 7 :"EvenTemperedScale/Octave2G.wav", 8 : "EvenTemperedScale/Octave2G#.wav", 9 : "EvenTemperedScale/Octave2A.wav", 10 : "EvenTemperedScale/Octave2A#.wav", 11 : "EvenTemperedScale/Octave2B.wav"  }
ETfilenameOctave3Dict = { 0 :"EvenTemperedScale/Octave3C.wav", 1 : "EvenTemperedScale/Octave3C#.wav", 2 : "EvenTemperedScale/Octave3D.wav", 3 : "EvenTemperedScale/Octave3D#.wav", 4 : "EvenTemperedScale/Octave3E.wav", 5 : "EvenTemperedScale/Octave3F.wav", 6 : "EvenTemperedScale/Octave3F#.wav", 7 :"EvenTemperedScale/Octave3G.wav", 8 : "EvenTemperedScale/Octave3G#.wav", 9 : "EvenTemperedScale/Octave3A.wav", 10 : "EvenTemperedScale/Octave3A#.wav", 11 : "EvenTemperedScale/Octave3B.wav"  }
ETfilenameOctave4Dict = { 0 :"EvenTemperedScale/Octave4C.wav", 1 : "EvenTemperedScale/Octave4C#.wav", 2 : "EvenTemperedScale/Octave4D.wav", 3 : "EvenTemperedScale/Octave4D#.wav", 4 : "EvenTemperedScale/Octave4E.wav", 5 : "EvenTemperedScale/Octave4F.wav", 6 : "EvenTemperedScale/Octave4F#.wav", 7 :"EvenTemperedScale/Octave4G.wav", 8 : "EvenTemperedScale/Octave4G#.wav", 9 : "EvenTemperedScale/Octave4A.wav", 10 : "EvenTemperedScale/Octave4A#.wav", 11 : "EvenTemperedScale/Octave4B.wav"  }


MTfilenameDict = {0 : 'MeanToneScale/C.wav', 1 : 'MeanToneScale/C#.wav', 2 : 'MeanToneScale/Db.wav', 3 : 'MeanToneScale/D.wav', 4 : 'MeanToneScale/D#.wav', 5 : 'MeanToneScale/Eb.wav', 6 : 'MeanToneScale/E.wav', 7 : 'MeanToneScale/F.wav', 8 : 'MeanToneScale/F#.wav', 9 : 'MeanToneScale/Gb.wav', 10 : 'MeanToneScale/G.wav', 11 : 'MeanToneScale/G#.wav', 12 : 'MeanToneScale/Ab.wav', 13 : 'MeanToneScale/A.wav', 14 : 'MeanToneScale/A#.wav', 15 : 'MeanToneScale/Bb.wav', 16 : 'MeanToneScale/B.wav'}
MTfilenameOctave1Dict = {0 : 'MeanToneScale/Octave1C.wav', 1 : 'MeanToneScale/Octave1C#.wav', 2 : 'MeanToneScale/Octave1Db.wav', 3 : 'MeanToneScale/Octave1D.wav', 4 : 'MeanToneScale/Octave1D#.wav', 5 : 'MeanToneScale/Octave1Eb.wav', 6 : 'MeanToneScale/Octave1E.wav', 7 : 'MeanToneScale/Octave1F.wav', 8 : 'MeanToneScale/Octave1F#.wav', 9 : 'MeanToneScale/Octave1Gb.wav', 10 : 'MeanToneScale/Octave1G.wav', 11 : 'MeanToneScale/Octave1G#.wav', 12 : 'MeanToneScale/Octave1Ab.wav', 13 : 'MeanToneScale/Octave1A.wav', 14 : 'MeanToneScale/Octave1A#.wav', 15 : 'MeanToneScale/Octave1Bb.wav', 16 : 'MeanToneScale/Octave1B.wav'}
MTfilenameOctave2Dict = {0 : 'MeanToneScale/Octave2C.wav', 1 : 'MeanToneScale/Octave2C#.wav', 2 : 'MeanToneScale/Octave2Db.wav', 3 : 'MeanToneScale/Octave2D.wav', 4 : 'MeanToneScale/Octave2D#.wav', 5 : 'MeanToneScale/Octave2Eb.wav', 6 : 'MeanToneScale/Octave2E.wav', 7 : 'MeanToneScale/Octave2F.wav', 8 : 'MeanToneScale/Octave2F#.wav', 9 : 'MeanToneScale/Octave2Gb.wav', 10 : 'MeanToneScale/Octave2G.wav', 11 : 'MeanToneScale/Octave2G#.wav', 12 : 'MeanToneScale/Octave2Ab.wav', 13 : 'MeanToneScale/Octave2A.wav', 14 : 'MeanToneScale/Octave2A#.wav', 15 : 'MeanToneScale/Octave2Bb.wav', 16 : 'MeanToneScale/Octave2B.wav'}
MTfilenameOctave3Dict = {0 : 'MeanToneScale/Octave3C.wav', 1 : 'MeanToneScale/Octave3C#.wav', 2 : 'MeanToneScale/Octave3Db.wav', 3 : 'MeanToneScale/Octave3D.wav', 4 : 'MeanToneScale/Octave3D#.wav', 5 : 'MeanToneScale/Octave3Eb.wav', 6 : 'MeanToneScale/Octave3E.wav', 7 : 'MeanToneScale/Octave3F.wav', 8 : 'MeanToneScale/Octave3F#.wav', 9 : 'MeanToneScale/Octave3Gb.wav', 10 : 'MeanToneScale/Octave3G.wav', 11 : 'MeanToneScale/Octave3G#.wav', 12 : 'MeanToneScale/Octave3Ab.wav', 13 : 'MeanToneScale/Octave3A.wav', 14 : 'MeanToneScale/Octave3A#.wav', 15 : 'MeanToneScale/Octave3Bb.wav', 16 : 'MeanToneScale/Octave3B.wav'}
MTfilenameOctave4Dict = {0 : 'MeanToneScale/Octave4C.wav', 1 : 'MeanToneScale/Octave4C#.wav', 2 : 'MeanToneScale/Octave4Db.wav', 3 : 'MeanToneScale/Octave4D.wav', 4 : 'MeanToneScale/Octave4D#.wav', 5 : 'MeanToneScale/Octave4Eb.wav', 6 : 'MeanToneScale/Octave4E.wav', 7 : 'MeanToneScale/Octave4F.wav', 8 : 'MeanToneScale/Octave4F#.wav', 9 : 'MeanToneScale/Octave4Gb.wav', 10 : 'MeanToneScale/Octave4G.wav', 11 : 'MeanToneScale/Octave4G#.wav', 12 : 'MeanToneScale/Octave4Ab.wav', 13 : 'MeanToneScale/Octave4A.wav', 14 : 'MeanToneScale/Octave4A#.wav', 15 : 'MeanToneScale/Octave4Bb.wav', 16 : 'MeanToneScale/Octave4B.wav'}

PDfilenameDict = { 0 :'PythagDodecScale/C.wav', 1 : 'PythagDodecScale/C#.wav', 2 : 'PythagDodecScale/D.wav', 3 : 'PythagDodecScale/D#.wav', 4 : 'PythagDodecScale/E.wav', 5 : 'PythagDodecScale/F.wav', 6 : 'PythagDodecScale/F#.wav', 7 :'PythagDodecScale/F#2.wav', 8 :'PythagDodecScale/G.wav', 9 : 'PythagDodecScale/G#.wav', 10 : 'PythagDodecScale/A.wav', 11 : 'PythagDodecScale/A#.wav', 12 : 'PythagDodecScale/B.wav'}
PDfilenameOctave1Dict = { 0 :'PythagDodecScale/Octave1C.wav', 1 : 'PythagDodecScale/Octave1C#.wav', 2 : 'PythagDodecScale/Octave1D.wav', 3 : 'PythagDodecScale/Octave1D#.wav', 4 : 'PythagDodecScale/Octave1E.wav', 5 : 'PythagDodecScale/Octave1F.wav', 6 : 'PythagDodecScale/Octave1F#.wav', 7 :'PythagDodecScale/Octave1F#2.wav', 8 :'PythagDodecScale/Octave1G.wav', 9 : 'PythagDodecScale/Octave1G#.wav', 10 : 'PythagDodecScale/Octave1A.wav', 11 : 'PythagDodecScale/Octave1A#.wav', 12 : 'PythagDodecScale/Octave1B.wav'}
PDfilenameOctave2Dict = { 0 :'PythagDodecScale/Octave2C.wav', 1 : 'PythagDodecScale/Octave2C#.wav', 2 : 'PythagDodecScale/Octave2D.wav', 3 : 'PythagDodecScale/Octave2D#.wav', 4 : 'PythagDodecScale/Octave2E.wav', 5 : 'PythagDodecScale/Octave2F.wav', 6 : 'PythagDodecScale/Octave2F#.wav', 7 :'PythagDodecScale/Octave2F#2.wav', 8 :'PythagDodecScale/Octave2G.wav', 9 : 'PythagDodecScale/Octave2G#.wav', 10 : 'PythagDodecScale/Octave2A.wav', 11 : 'PythagDodecScale/Octave2A#.wav', 12 : 'PythagDodecScale/Octave2B.wav'}
PDfilenameOctave3Dict = { 0 :'PythagDodecScale/Octave3C.wav', 1 : 'PythagDodecScale/Octave3C#.wav', 2 : 'PythagDodecScale/Octave3D.wav', 3 : 'PythagDodecScale/Octave3D#.wav', 4 : 'PythagDodecScale/Octave3E.wav', 5 : 'PythagDodecScale/Octave3F.wav', 6 : 'PythagDodecScale/Octave3F#.wav', 7 :'PythagDodecScale/Octave3F#2.wav', 8 :'PythagDodecScale/Octave3G.wav', 9 : 'PythagDodecScale/Octave3G#.wav', 10 : 'PythagDodecScale/Octave3A.wav', 11 : 'PythagDodecScale/Octave3A#.wav', 12 : 'PythagDodecScale/Octave3B.wav'}
PDfilenameOctave4Dict = { 0 :'PythagDodecScale/Octave4C.wav', 1 : 'PythagDodecScale/Octave4C#.wav', 2 : 'PythagDodecScale/Octave4D.wav', 3 : 'PythagDodecScale/Octave4D#.wav', 4 : 'PythagDodecScale/Octave4E.wav', 5 : 'PythagDodecScale/Octave4F.wav', 6 : 'PythagDodecScale/Octave4F#.wav', 7 :'PythagDodecScale/Octave4F#2.wav', 8 :'PythagDodecScale/Octave4G.wav', 9 : 'PythagDodecScale/Octave4G#.wav', 10 : 'PythagDodecScale/Octave4A.wav', 11 : 'PythagDodecScale/Octave4A#.wav', 12 : 'PythagDodecScale/Octave4B.wav'}

PtolemyfilenameDict = { 0 :'PtolemyScale/C.wav', 1 : 'PtolemyScale/C#.wav', 2 : 'PtolemyScale/D.wav', 3 : 'PtolemyScale/D#.wav', 4 : 'PtolemyScale/E.wav', 5 : 'PtolemyScale/F.wav', 6 : 'PtolemyScale/F#.wav', 7 :'PtolemyScale/F#2.wav', 8 :'PtolemyScale/G.wav', 9 : 'PtolemyScale/G#.wav', 10 : 'PtolemyScale/A.wav', 11 : 'PtolemyScale/A#.wav', 12 : 'PtolemyScale/B.wav'}
PtolemyfilenameOctave1Dict = { 0 :'PtolemyScale/Octave1C.wav', 1 : 'PtolemyScale/Octave1C#.wav', 2 : 'PtolemyScale/Octave1D.wav', 3 : 'PtolemyScale/Octave1D#.wav', 4 : 'PtolemyScale/Octave1E.wav', 5 : 'PtolemyScale/Octave1F.wav', 6 : 'PtolemyScale/Octave1F#.wav', 7 :'PtolemyScale/Octave1F#2.wav', 8 :'PtolemyScale/Octave1G.wav', 9 : 'PtolemyScale/Octave1G#.wav', 10 : 'PtolemyScale/Octave1A.wav', 11 : 'PtolemyScale/Octave1A#.wav', 12 : 'PtolemyScale/Octave1B.wav'}
PtolemyfilenameOctave2Dict = { 0 :'PtolemyScale/Octave2C.wav', 1 : 'PtolemyScale/Octave2C#.wav', 2 : 'PtolemyScale/Octave2D.wav', 3 : 'PtolemyScale/Octave2D#.wav', 4 : 'PtolemyScale/Octave2E.wav', 5 : 'PtolemyScale/Octave2F.wav', 6 : 'PtolemyScale/Octave2F#.wav', 7 :'PtolemyScale/Octave2F#2.wav', 8 :'PtolemyScale/Octave2G.wav', 9 : 'PtolemyScale/Octave2G#.wav', 10 : 'PtolemyScale/Octave2A.wav', 11 : 'PtolemyScale/Octave2A#.wav', 12 : 'PtolemyScale/Octave2B.wav'}
PtolemyfilenameOctave3Dict = { 0 :'PtolemyScale/Octave3C.wav', 1 : 'PtolemyScale/Octave3C#.wav', 2 : 'PtolemyScale/Octave3D.wav', 3 : 'PtolemyScale/Octave3D#.wav', 4 : 'PtolemyScale/Octave3E.wav', 5 : 'PtolemyScale/Octave3F.wav', 6 : 'PtolemyScale/Octave3F#.wav', 7 :'PtolemyScale/Octave3F#2.wav', 8 :'PtolemyScale/Octave3G.wav', 9 : 'PtolemyScale/Octave3G#.wav', 10 : 'PtolemyScale/Octave3A.wav', 11 : 'PtolemyScale/Octave3A#.wav', 12 : 'PtolemyScale/Octave3B.wav'}
PtolemyfilenameOctave4Dict = { 0 :'PtolemyScale/Octave4C.wav', 1 : 'PtolemyScale/Octave4C#.wav', 2 : 'PtolemyScale/Octave4D.wav', 3 : 'PtolemyScale/Octave4D#.wav', 4 : 'PtolemyScale/Octave4E.wav', 5 : 'PtolemyScale/Octave4F.wav', 6 : 'PtolemyScale/Octave4F#.wav', 7 :'PtolemyScale/Octave4F#2.wav', 8 :'PtolemyScale/Octave4G.wav', 9 : 'PtolemyScale/Octave4G#.wav', 10 : 'PtolemyScale/Octave4A.wav', 11 : 'PtolemyScale/Octave4A#.wav', 12 : 'PtolemyScale/Octave4B.wav'}

def genscale(bf):
	meantonescale = meantone(float(bf)/8,MTfilenameDict) + meantone(float(bf)/4,MTfilenameOctave1Dict) + meantone(float(bf)/2,MTfilenameOctave2Dict) + meantone(float(bf),MTfilenameOctave3Dict) + meantone(2*float(bf),MTfilenameOctave4Dict)
	etscale = ET(float(bf)/8,ETfilenameDict) + ET(float(bf)/4,ETfilenameOctave1Dict) + ET(float(bf)/2,ETfilenameOctave2Dict) + ET(float(bf),ETfilenameOctave3Dict) + ET(2*float(bf),ETfilenameOctave4Dict)
	pythagdodecscale = dodec(float(bf)/8,PDfilenameDict) + dodec(float(bf)/4,PDfilenameOctave1Dict) + dodec(float(bf)/2,PDfilenameOctave2Dict) + dodec(float(bf),PDfilenameOctave3Dict) + dodec(2*float(bf),PDfilenameOctave4Dict)
	ptolemyscale = ptolemy(float(bf)/8,PtolemyfilenameDict) + ptolemy(float(bf)/4,PtolemyfilenameOctave1Dict) + ptolemy(float(bf)/2,PtolemyfilenameOctave2Dict) + ptolemy(float(bf),PtolemyfilenameOctave3Dict) + ptolemy(2*float(bf),PtolemyfilenameOctave4Dict)

	for i in range(len(meantonescale)):
		Generate(meantonescale[i].finfreq, 44100//1, meantonescale[i].filename)
	
	for i in range(len(etscale)):
		Generate(etscale[i].finfreq, 44100//1, etscale[i].filename)

	for i in range(len(pythagdodecscale)):
		Generate(pythagdodecscale[i].finfreq, 44100//1, pythagdodecscale[i].filename)

	for i in range(len(ptolemyscale)):
		Generate(ptolemyscale[i].finfreq, 44100//1, ptolemyscale[i].filename)