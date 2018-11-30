MAJOR = 1
MINOR = 0
DIMINISHED = 2
DOMINANT_7TH = 3

chord_progressions = [(MAJOR, ("I", "IV", "V", "I")), 
                      (MAJOR, ("I","vi","IV","V")), 
                      (MAJOR, ("I","V","vi","IV")),
                      (MINOR, ("i", "VI", "iv", "V")),
                      (MINOR, ("i", "iv", "VII", "III", "VI", "iv", "V7", "V7"))]

intervals = {
    "P1" : 0,
    "m2" : 1,
    "M2" : 2,
    "m3" : 3,
    "M3" : 4,
    "P4" : 5,
    "A4" : 6,
    "P5" : 7,
    "m6" : 8,
    "M6": 9,
    "m7" : 10,
    "M7" : 11,
    "P8" : 12
}

chords_major = {
    "I" : ("P1", MAJOR),
    "ii" : ("M2", MINOR),
    "iii" : ("M3", MINOR),
    "IV" : ("P4", MAJOR),
    "V" : ("P5", MAJOR),
    "vi" : ("M6", MINOR),
    "V7" : ("P5", DOMINANT_7TH)
}

chords_minor = {
    "i" : ("P1", MINOR),
    "III" : ("m3", MAJOR),
    "iv" : ("P4", MINOR),
    "V" : ("P5", MAJOR),
    "VI" : ("m6", MAJOR),
    "VII" : ("m7", MAJOR),
    "V7" : ("P5", DOMINANT_7TH)
}

# Takes ("M6", MINOR) or ("P5", MAJOR)
# Retunrs (9, 0, 4) or (5, 9, 0)
def make_chord(chord):
    if chord[1] is MAJOR:
        return sorted((intervals[chord[0]], 
                (intervals[chord[0]] + intervals["M3"]) % 12,
                (intervals[chord[0]] + intervals["P5"]) % 12))
    elif chord[1] is MINOR:
        return sorted((intervals[chord[0]], 
                (intervals[chord[0]] + intervals["m3"]) % 12,
                (intervals[chord[0]] + intervals["P5"]) % 12))
    elif chord[1] is DOMINANT_7TH:
        return sorted((intervals[chord[0]], 
                (intervals[chord[0]] + intervals["M3"]) % 12,
                (intervals[chord[0]] + intervals["P5"]) % 12,
                (intervals[chord[0]] + intervals["m7"]) % 12))

# Takes (MINOR, ("I","vi","IV","V"))
# Returns [(0, 4, 7), (9, 12, 16), (5, 9, 12), (7, 11, 14), ..., (0, 4, 7), (9, 12, 16), (5, 9, 12), (7, 11, 14)]
def make_harmonies(chord_progression):
    harmonies = []

    if chord_progression[0] is MINOR:
        chords = chords_minor
    elif chord_progression[0] is MAJOR:
        chords = chords_major

    for chord in chord_progression[1]:
        harmonies.append(make_chord(chords[chord]))

    harmonies *= 12

    return harmonies





    