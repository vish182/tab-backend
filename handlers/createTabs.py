import traceback
import re
import time

class tabGenerator():

    
    def createChordMap():
        
        chordMap = {
            "achord": "-02220",
            "amaj7chord": "-02120",
            "a7chord": "-02020",
            "amchord": "-02210",
            "am7chord": "-02010",

            "bchord": "--4442",
            "bmaj7chord": "22130-",
            "b7chord": "-21202",
            "bmchord": "--4432",
            "bm7chord": "-20202",

            "cchord": "-32010",
            "cmaj7chord": "-32000",
            "c7chord": "-32310",
            "cmchord": "-310--",
            "cm7chord": "-313--",

            "dchord": "--0232",
            "dmaj7chord": "--0222",
            "d7chord": "--0212",
            "dmchord": "--0231",
            "dm7chord": "--0211",

            "echord": "022100",
            "emaj7chord": "021100",
            "e7chord": "020100",
            "emchord": "022000",
            "em7chord": "022030",

            "fchord": "--3211",
            "fmaj7chord": "--3210",
            "f7chord": "131211",
            "fmchord": "--3111",
            "fm7chord": "131111",

            "gchord": "320003",
            "gmaj7chord": "3-0002",
            "g7chord": "320001",
            "gmchord": "--0333",
            "gm7chord":"-13030"
        }

        return chordMap

    # create a readable list of reference guitar notes for
    # comparison and input validation
    guitarRangeOrig = ["E2", "F2", "F#2", "G2", "G#2",
        "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4",
        "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5",
        "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", ""]
    
    # create process-formatted list of reference guitar
    # notes for comparison
    # and input validation
    guitarRange = []

    # create map with possible chords and tabs in order of
    # Elow A D G B Ehigh in custom method
    chordMap = createChordMap()

    # create running record of notes from which to print out later
    eHighRecord = []
    bRecord = []
    gRecord = []
    dRecord = []
    aRecord = []
    eLowRecord = []

    # initialize running variable to record last chosen fret to calculate travel
    lastFret = 0.0

    # create reference note lists for guitar strings
    # where index of note corresponds to fret

    eHighString = ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5",
        "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6"]

    bString = ["B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5",
        "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5"]

    gString = ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4",
        "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5"]

    dString = ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4",
        "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5"]

    aString = ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3",
        "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4"]

    eLowString = ["E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3",
        "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4"]

    tunedStrings = ["e", "B", "G", "D", "A", "E"]

    
    
    @classmethod
    def assignTuningReference(cls, inputTuning="standard"):

        if inputTuning == "standard":
            return

        tuning = ""
        while True:
            tuning = input("Enter the guitar tuning as Standard, Open G, Open D, C6 or Dsus4: ")
            # remove all spaces
            tuning.replace(" ", "")
            # remove all commas
            tuning.replace(",", "")
            tuning = tuning.lower()
            tempList = ["standard", "openg", "opend", "c6", "dsus4"]
            if tuning == "" or tuning in tempList:
                break

        if tuning == "" or tuning == "standard":
            return
        
        elif tuning == "openg":
            cls.setOpenG()
        
        elif tuning == "opend":
            cls.setOpenD()
        
        elif tuning == "c6":
            cls.setC6()

        elif tuning == "dsus4":
            cls.setDsus4()

        return
        

    @classmethod
    def setOpenG(cls):
        cls.guitarRangeOrig = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
        "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4",
        "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5",
        "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", ""]

        cls.eHighString = ["D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5",
					"D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6"]
        cls.bString = ["B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",
                "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5"]
        cls.gString = ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4",
                "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5"]
        cls.dString = ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4",
                "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5"]
        cls.aString = ["G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3",
                "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4"]
        cls.eLowString = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
                "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"]
        cls.tunedStrings = ["d", "B", "g", "D", "G", "D"]  

    @classmethod
    def setOpenD(cls):
        cls.guitarRangeOrig = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", ""]
        cls.ehighString = ["D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5",
                "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6"]
        cls.bString = ["A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4",
                "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5"]
        cls.gString = ["F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4",
                "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5"]
        cls.dString = ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4",
                "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5"]
        cls.aString = ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3",
                "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4"]
        cls.elowString = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
                "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"]
        cls.tunedStrings = [" d", " a", "F#", " d", " A", " D"]

    @classmethod
    def setC6(cls):
        cls.guitarRangeOrig = ["C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
        "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4",
        "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5",
        "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", ""]
        cls.ehighString = ["E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5",
                "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6"]
        cls.bString = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5",
                "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C5"]
        cls.gString = ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4",
                "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5"]
        cls.dString = ["C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4",
                "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5"]
        cls.aString = ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3",
                "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4"]
        cls.elowString = ["C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
                "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4"]
        cls.tunedStrings = ["E", "c", "G", " C", " A", " C"]

    @classmethod
    def setDsus4(cls):
        cls.guitarRangeOrig = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
        "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4",
        "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5",
        "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", ""]
        cls.ehighString = ["D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5",
                "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6"]
        cls.bString = ["A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4",
                "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5"]
        cls.gString = ["G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4",
                "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5"]
        cls.dString = ["D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4",
                "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5"]
        cls.aString = ["A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3",
                "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4"]
        cls.elowString = ["D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2", "C3", "C#3",
                "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"]
        cls.tunedStrings = ["d", "a", "G", "D", "A", "D"]    

    
    @classmethod
    def readNoteGroups(cls, sourceFileName):
        
        for i in range(len(cls.guitarRangeOrig)):
            cls.guitarRange.append(cls.guitarRangeOrig[i].lower())

        noteGroups = []

        # read source file and split lines
        inputLines = []
        
        # change name of source file with list of notes
        try:
            with open(sourceFileName, 'r') as f:
                noteGroups.append(f.name)
                for line in f.readlines():
                    if line != None:
                        inputLines.append(line)
        except IOError:
            traceback.print_exc()

        # identify first line with "chord" or numbers (notes)
        firstNoteIndex = 0
        for i in range(len(inputLines)):
            if re.match(".*chord.*", inputLines[i].lower()):
                firstNoteIndex = i
                break

            if re.match(".*\\d.*", inputLines[i]):
                firstNoteIndex = i
                break

            elif i == len(inputLines)-1:
                print("No notes were found in the source file. Please double check that octave numbers are specified (ex: A#4)")
    
        # group notes without the numberless first lines
        noteGroups.extend(inputLines[firstNoteIndex:])

        print("Notes found in file: {0} \n".format(noteGroups))

        return noteGroups
    
    @classmethod
    def validateSource(cls, noteGroups):
        # clean up input for validation

        # make all notes lowercase
        noteGroups = [n.lower() for n in noteGroups]
        # remove all spaces
        noteGroups = [n.replace(" ", "") for n in noteGroups]
        # remove all commas
        noteGroups = [n.replace(",", "") for n in noteGroups]
        # remove all \n chars
        noteGroups = [n.replace("\n", "") for n in noteGroups]

        # change all flats to equivalent sharps for ease of processing
        noteGroups = [n.replace("gb", "f#") for n in noteGroups]
        noteGroups = [n.replace("ab", "g#") for n in noteGroups]
        noteGroups = [n.replace("bb", "a#") for n in noteGroups]
        noteGroups = [n.replace("db", "c#") for n in noteGroups]
        noteGroups = [n.replace("eb", "d#") for n in noteGroups]

        outOfRangeNotes = [ "a2","b2","c2","c#2", "d2","d#2"]

        noteGroups = [n for n in noteGroups if n not in outOfRangeNotes]

        # split up notes into different elements of new list for note validation
        allNotes = []
        for line in noteGroups:
            # chord names and strings less than 3 char (single notes) are grouped as their own units
            if re.match(".*chord.*", line) or len(line) <= 3:
                allNotes.append(line)
            
            # multiple note chords (not names) are broken up for note validation
            elif len(line) > 3:
                numIndices = []
                for i in range(len(line)):
                    if line[i].isdigit():
                        numIndices.append(i)
                allNotes.append(line[0:numIndices[0]+1])
                for i in range(len(numIndices)-1):
                    allNotes.append(line[numIndices[i]+1:numIndices[i+1]+1])

        # loop through all notes and validate by comparing with reference note list and chord map
        for i in range(len(allNotes)):
            matched = False
            if allNotes[i] in cls.chordMap.keys():
                matched = True

            elif allNotes[i] in cls.guitarRange:
                matched = True

            if matched == False:
                print("Note Range: ", cls.guitarRangeOrig)
                print("Chord Range: ", cls.chordMap.keys())
                print()
                print("Input: ", allNotes)
                print("Problematic Input: ", allNotes[i])
                print("Pitch mismatch! Please input pitches or chords within the range of a guitar with standard tuning as shown above")
                return
            
        print("All Notes okay: ", allNotes, "\n")
        return noteGroups

    @classmethod
    def recordChord(cls, noteGroups, i):
        # retrieve corresponding tab string for chord
        chordTab = cls.chordMap[noteGroups[i]]

        # add fret for each string to the string records
        cls.eLowRecord.append(chordTab[0])
        cls.aRecord.append(chordTab[1])
        cls.dRecord.append(chordTab[2])
        cls.gRecord.append(chordTab[3])
        cls.bRecord.append(chordTab[4])
        cls.eHighRecord.append(chordTab[5])

    @classmethod
    def recordSingleNote(cls, noteGroups, i):
        # default tab values for the six strings
        # order: eHigh B G D A eLow
        pitchStringFrets = [100, 100, 100, 100, 100, 100]

        fretDeltaArray = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        delta = 100.0
        measureBreak = False

        # loop through all frets and record positions where a pitch exists for each string
        for stringFret in range(len(cls.eHighString)):
            if noteGroups[i] == "":
                measureBreak = True

            if noteGroups[i] == cls.eHighString[stringFret].lower():
                pitchStringFrets[0] = stringFret

            if noteGroups[i] == cls.bString[stringFret].lower():
                pitchStringFrets[1] = stringFret

            if noteGroups[i] == cls.gString[stringFret].lower():
                pitchStringFrets[2] = stringFret

            if noteGroups[i] == cls.dString[stringFret].lower():
                pitchStringFrets[3] = stringFret

            if noteGroups[i] == cls.aString[stringFret].lower():
                pitchStringFrets[4] = stringFret
            
            if noteGroups[i] == cls.eLowString[stringFret].lower():
                pitchStringFrets[5] = stringFret

        # compare fret positions with lastFret to calculate delta i.e. travel aka spread of frets
        for stringIndex in range(len(pitchStringFrets)):
            delta = abs(cls.lastFret - pitchStringFrets[stringIndex])


            # easy to play open string
            if pitchStringFrets[stringIndex] != 0:
                fretDeltaArray[stringIndex] = delta

        # choose string that will play note based on lowest delta and record to string records
        if measureBreak == True:
            cls.eHighRecord.append("|")
            cls.bRecord.append("|")
            cls.gRecord.append("|")
            cls.dRecord.append("|")
            cls.aRecord.append("|")
            cls.eLowRecord.append("|")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 0:
            cls.eHighRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))
            cls.bRecord.append("-")
            cls.gRecord.append("-")
            cls.dRecord.append("-")
            cls.aRecord.append("-")
            cls.eLowRecord.append("-")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 1:
            cls.eHighRecord.append("-")
            cls.bRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))
            cls.gRecord.append("-")
            cls.dRecord.append("-")
            cls.aRecord.append("-")
            cls.eLowRecord.append("-")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 2:
            cls.eHighRecord.append("-")
            cls.bRecord.append("-")
            cls.gRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))
            cls.dRecord.append("-")
            cls.aRecord.append("-")
            cls.eLowRecord.append("-")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 3:
            cls.eHighRecord.append("-")
            cls.bRecord.append("-")
            cls.gRecord.append("-")
            cls.dRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))
            cls.aRecord.append("-")
            cls.eLowRecord.append("-")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 4:
            cls.eHighRecord.append("-")
            cls.bRecord.append("-")
            cls.gRecord.append("-")
            cls.dRecord.append("-")
            cls.aRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))
            cls.eLowRecord.append("-")

        elif fretDeltaArray.index(min(fretDeltaArray)) == 5:
            cls.eHighRecord.append("-")
            cls.bRecord.append("-")
            cls.gRecord.append("-")
            cls.dRecord.append("-")
            cls.aRecord.append("-")
            cls.eLowRecord.append(str(pitchStringFrets[fretDeltaArray.index(min(fretDeltaArray))]))

        # set new last fret to the current fret
        cls.lastFret = min(pitchStringFrets)
        if cls.lastFret == 100.0:
            cls.lastFret = 0.0

    @classmethod
    def recordMultiNote(cls, noteGroups, i):
        chordNotes = []
        allPlayableStrings = []
        allStringFrets = []

        # split up notes based on numbers
        numIndices = []
        for y in range(len(noteGroups[i])):
            if noteGroups[i][y].isdigit():
                numIndices.append(y)

        chordNotes.append(noteGroups[i][0:numIndices[0]+1])

        for y in range(len(numIndices)-1):
            chordNotes.append(noteGroups[i][numIndices[y]+1: numIndices[y+1]+1])

        # loop through all frets and record positions where a pitch exists for each string
        for y in range(len(chordNotes)):
            # order: e B G D A E
            pitchStringFrets = [100, 100, 100, 100, 100, 100]

            for stringFret in range(len(cls.eHighString)):
                if chordNotes[y] == cls.eHighString[stringFret].lower():
                    pitchStringFrets[0] = stringFret

                if chordNotes[y] == cls.bString[stringFret].lower():
                    pitchStringFrets[1] = stringFret

                if chordNotes[y] == cls.gString[stringFret].lower():
                    pitchStringFrets[2] = stringFret

                if chordNotes[y] == cls.dString[stringFret].lower():
                    pitchStringFrets[3] = stringFret

                if chordNotes[y] == cls.aString[stringFret].lower():
                    pitchStringFrets[4] = stringFret
                
                if chordNotes[y] == cls.eLowString[stringFret].lower():
                    pitchStringFrets[5] = stringFret

            # calculate number of playable strings
            playableStrings = 0
            for fret in pitchStringFrets:
                if fret!=100:
                    playableStrings+=1
            
            allStringFrets.append(pitchStringFrets)
            allPlayableStrings.append(playableStrings)

        # the playable notes product helps determine the size of the chord matrix
        playableNotesProduct = 1
        for notePlayableStrings in allPlayableStrings:
            playableNotesProduct *= notePlayableStrings

        # creating chord matrix and initializing all values to 100
        chordMatrix = [[100] * (len(chordNotes)+4)] * (playableNotesProduct - len(chordNotes))

        # add playable frets for note 1 to the chord matrix
        loopNote1Counter = 0
        for y in range(len(allStringFrets[0])):
            if int(allStringFrets[0][y]) != 100:
                for z in range(len(allStringFrets[1])):
                    if int(allStringFrets[1][z]) != 100:
                        if y != z:
                            chordMatrix[loopNote1Counter][0] = int(allStringFrets[0][y])
                            loopNote1Counter+=1

        # add playable frets for note 2 to the chord matrix
        loopNote2Counter = 0
        for y in range(len(allStringFrets[0])):
            if int(allStringFrets[0][y]) != 100:
                for z in range(len(allStringFrets[1])):
                    if int(allStringFrets[len(allStringFrets)-1][z]) != 100:
                        if y != z:
                            chordMatrix[loopNote2Counter][1] = int(allStringFrets[0][y])
                            loopNote2Counter+=1


        for y in range(len(chordMatrix)):
            #calculate difference between note fret positions (stretch) and average note fret position

            chordMatrix[y][len(chordNotes)] = abs(chordMatrix[y][0] - chordMatrix[y][1])

            # calculate average note fret position
            chordMatrix[y][len(chordNotes) + 1] = (chordMatrix[y][0] + chordMatrix[y][1]) // 2

            # calculate average note fret position - lastFret (travel)
            chordMatrix[y][len(chordNotes) + 2] = abs(chordMatrix[y][len(chordNotes) + 1] - round(lastFret))

            # calculate stretch plus travel i.e. difficulty factor
            chordMatrix[y][len(chordNotes) + 3] = chordMatrix[y][len(chordNotes)] + chordMatrix[y][len(chordNotes) + 2]

        # identify the fret combination that will have the lowest difficulty factor ergo highest playability
        chordNoteDifficulties = []
        for y in range(len(chordMatrix)):
            # loop through the 6 array rows
            chordNoteDifficulties[y] = int(chordMatrix[y][len(chordNotes) + 3])

        if len(chordNoteDifficulties) == 0:
            return

        bestChordIndex = chordNoteDifficulties.index(min(chordNoteDifficulties))

        # create analogous list with which to record best frets
        bestFrets = [100, 100, 100, 100, 100, 100]
        bestFrets[allStringFrets[0].index(chordMatrix[bestChordIndex][0])] = chordMatrix[bestChordIndex][0]

        bestFrets[allStringFrets[1].index(chordMatrix[bestChordIndex][1])] = chordMatrix[bestChordIndex][1]

        # record best frets into string records
        if bestFrets[0] != 100:
            cls.eHighRecord.append(bestFrets[0])

        elif bestFrets[0] == 100:
            cls.eHighRecord.append("-")

        if bestFrets[1] != 100:
            cls.bRecord.append(bestFrets[1])

        elif bestFrets[1] == 100:
            cls.bRecord.append("-")

        if bestFrets[2] != 100:
            cls.gRecord.append(bestFrets[2])

        elif bestFrets[2] == 100:
            cls.gRecord.append("-")

        if bestFrets[3] != 100:
            cls.dRecord.append(bestFrets[3])

        elif bestFrets[3] == 100:
            cls.dRecord.append("-")

        if bestFrets[4] != 100:
            cls.aRecord.append(bestFrets[4])

        elif bestFrets[4] == 100:
            cls.aRecord.append("-")

        if bestFrets[5] != 100:
            cls.eLowRecord.append(bestFrets[5])

        elif bestFrets[5] == 100:
            cls.eLowRecord.append("-")


        # set new last fret to the current fret
        lastFret = chordMatrix[bestChordIndex][len(chordNotes) + 1]


    @classmethod
    def outputTabToFile(cls, sourceFileName):
        outputFileName = "tab_1.txt"## + sourceFileName
        try:
            with open(outputFileName, "w") as f:
                f.write(cls.tunedStrings[0] + ", ".join(cls.eHighRecord))
                f.write("\n")
                f.write(cls.tunedStrings[1] + ", ".join(cls.bRecord))
                f.write("\n")
                f.write(cls.tunedStrings[2] + ", ".join(cls.gRecord))
                f.write("\n")
                f.write(cls.tunedStrings[3] + ", ".join(cls.dRecord))
                f.write("\n")
                f.write(cls.tunedStrings[4] + ", ".join(cls.aRecord))
                f.write("\n")
                f.write(cls.tunedStrings[5] + ", ".join(cls.eLowRecord))
                f.write("\n")
                                
                f.write("\n")
                f.write("\n")

                # can be adjusted for longer tabs
                outputRowLength = 30
                while(len(cls.eHighRecord) != 0):

                    f.write(cls.tunedStrings[0] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.eHighRecord) != 0:
                            f.write("-" + cls.eHighRecord[0] + "-")
                            cls.eHighRecord.pop(0)
                    
                    f.write("\n")

                    f.write(cls.tunedStrings[1] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.bRecord) != 0:
                            f.write("-" + cls.bRecord[0] + "-")
                            cls.bRecord.pop(0)
                    
                    f.write("\n")

                    f.write(cls.tunedStrings[2] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.gRecord) != 0:
                            f.write("-" + cls.gRecord[0] + "-")
                            cls.gRecord.pop(0)
                    
                    f.write("\n")

                    f.write(cls.tunedStrings[3] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.dRecord) != 0:
                            f.write("-" + cls.dRecord[0] + "-")
                            cls.dRecord.pop(0)
                    
                    f.write("\n")

                    f.write(cls.tunedStrings[4] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.aRecord) != 0:
                            f.write("-" + cls.aRecord[0] + "-")
                            cls.aRecord.pop(0)

                    f.write("\n")

                    f.write(cls.tunedStrings[5] + ": ")
                    for i in range(outputRowLength):
                        if len(cls.eLowRecord) != 0:
                            f.write("-" + cls.eLowRecord[0] + "-")
                            cls.eLowRecord.pop(0)
                    
                    f.write("\n")
                    f.write("\n")


        except IOError:
            traceback.print_exc()



    @classmethod
    def main(cls, filename, notes):
        cls.assignTuningReference()

        sourceFileName = filename
        noteGroups = cls.readNoteGroups(sourceFileName)

        #print(noteGroups)

        #noteGroups.remove(noteGroups[0])

        #print(noteGroups)

        noteGroups = notes
        print("before validation notegroups: ", noteGroups)
        noteGroups = cls.validateSource(noteGroups)

        print(noteGroups)

        if noteGroups == None:
            noteGroups = []
            return

        # loop through note groups to record frets in string records
        for i in range(len(noteGroups)):
            if noteGroups[i] in cls.chordMap.keys():
                #print("chord for i=",i)
                cls.recordChord(noteGroups, i)
            
            # single notes should be 3 char or less
            elif len(noteGroups[i]) <= 3:
                #print("note for i=",i)
                cls.recordSingleNote(noteGroups, i)

            # note groups longer than 3 char that are not chords are assumed to be multiple notes
            elif len(noteGroups[i]) > 3:
                #print("mnote for i=",i)
                #print(noteGroups[i])
                cls.recordMultiNote(noteGroups, i)

        
        cls.outputTabToFile(sourceFileName)

def tabgen_api(input_notes):
    filename = "notes.txt"
    tabGenerator.main(filename, input_notes)
    time.sleep(0.1)
    
    try:
        f = open("tab_1.txt", "r")
        notes = []
        count = 1
        for line in f:
            
            if(count == 7):
                break
            line = line[1:-1]
            line = line.replace(" ", "")
            #print("line: ", line)
            notes.append(line.split(","))

            count +=1
        strings = {0:'e1', 1:'b', 2:'g', 3:'d', 4: 'a', 5: 'e0'}
        final_arr = []
        for i in range(len(notes[0])):
            for j in range(6):
                if(notes[j][i] != "-"):
                    d = {}
                    #print("here", notes[j][i])
                    d[strings[j]] = int(notes[j][i])
                    final_arr.append(d)


        print(final_arr)
        f.close()
        return final_arr
    except Exception:
        return []


if __name__ == "__main__":
    #input("Enter filename: ")
    tabgen_api(filename)
