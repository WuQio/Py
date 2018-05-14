# coding:utf-8
# !/usr/bin/python3
from midiutil import MIDIFile

c4  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
c3 = []
c2 = []
c5 = []
for i in c4:
    c3.append(i-12)
    c2.append(i-24)
    c5.append(i+12)

track1    = 0
track2    = 1
channel  = 0
time     = 0    # In beats
duration = 4    # In beats
tempo    = 70   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track1, time, tempo)

melody1 = [[c4[6], 0], [c5[5], 0.5], [c5[3], 1], [c5[1], 1.75], [c5[2], 2], [c4[5], 4], [c5[5], 4.5], [c5[3], 5], [c4[5], 5.75], [c5[1], 6], [c4[6], 8], [c5[5], 8.5], [c5[3], 9], [c5[1], 9.5], [c4[7], 10], [c5[1], 11.25], [c5[2], 11.75], [c5[4], 12], [c5[3], 13.75], [c5[3], 14], [c4[6], 16], [c5[5], 16.5], [c5[3], 17], [c5[1], 17.75], [c5[2], 18], [c4[5], 20], [c5[5], 20.5], [c5[3], 21], [c4[5], 21.75], [c5[1], 22], [c4[6], 24], [c5[5], 24.5], [c5[3], 25], [c5[1], 25.5], [c4[7], 26], [c5[1], 27.5], [c5[1], 28]]
melody2 = [[c2[4], 0], [c3[1], 0.5], [c3[4], 1], [c2[5], 2], [c3[2], 2.5], [c3[5], 3], [c2[3], 4], [c2[7], 4.5], [c3[3], 5], [c2[6], 6], [c3[3], 6.5], [c3[6], 7], [c2[4], 8], [c3[1], 8.5], [c3[4], 9], [c2[5], 10], [c3[2], 10.5], [c3[5], 11], [c3[1], 12], [c3[5], 12.5], [c4[1], 13], [c4[2], 13.5], [c4[3], 14], [c2[4], 16], [c3[1], 16.5], [c3[4], 17], [c2[5], 18], [c3[2], 18.5], [c3[5], 19], [c2[3], 20], [c2[7], 20.5], [c3[3], 21], [c2[6], 22], [c3[3], 22.5], [c3[6], 23], [c2[4], 24], [c3[1], 24.5], [c3[4], 25], [c2[5], 26], [c3[2], 26.5], [c3[5], 27], [c3[1], 28], [c3[5], 28.5], [c4[1], 29]]

MyMIDI.addTempo(track1, time, tempo)
for note in melody1:
    MyMIDI.addNote(track1, channel, note[0]+12, note[1], duration, volume)

MyMIDI.addTempo(track2, time, tempo)
for note in melody2:
    MyMIDI.addNote(track2, 1, note[0], note[1], duration, volume-40)

# MyMIDI.addTempo(track1, time, tempo)
# MyMIDI.addTempo(track2, time, tempo)
#
# for i, pitch in enumerate(degrees1):
#     MyMIDI.addNote(track1, channel, pitch, time + i, duration, volume)
#
# for i, pitch in enumerate(degrees2):
#     MyMIDI.addNote(track2, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)