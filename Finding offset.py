from music21 import stream, note, base
import pickle

##n = note.Note('C#4')
##p = stream.Part()
##p.insert(20.0, n)
##print(n.activeSite) is p
##
##print(n.offset)

stream1 = stream.Stream()

#load the notes used to train the model
with open('Dataset/Acoustic guitar/Notes/notes', 'rb') as filepath:
    notes = pickle.load(filepath)

##noteList = []
##
##for elem in range(0, len(notes)):
##        noteList.append(notes[elem])

##notesLength = len(notes)
##notes = note.Note()

##for elem in range(0,len(noteList)):
##    stream1.append(notes)

for thisNote in stream1.getElementsByClass(note.Note(notes)):
    print(thisNote, thisNote.offset)

##with open('C:/Users/hshah/Desktop/Notes.txt', 'w') as f:
##    for item in noteList:
##            f.write("%s\n" % item)


##
##for offset in range(0, notesLength):
##    stream1.insert(offset, base.ElementWrapper(notes))
##    notes.activeSite() is stream1
##
##print(stream1.highestOffset)
