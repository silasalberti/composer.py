import random

# Takes (0, 4, 7)
# Returns [(2, {0}), (1, {4}, (1, {-8})]
def make_measure(harmony, last_note):
    measure = []

    remaining_beats = 4

    while remaining_beats > 0:
        length = random.choice([0.25]*0 + [0.5]*4 + [1]*2 + [2])

        if length > remaining_beats:
            continue

        steps_in_harmony = random.choice([-2]*1 + [-1]*4 + [0]*3 + [1]*4 + [2]*1)
        last_octave = (last_note - last_note % 12)/12
        last_tone = last_note % 12
            
        # Find nearest tone
        nearest_tone = harmony[0]
        min_difference = abs(harmony[0] - last_tone)
        for note in harmony[1:]:
            current_difference = abs(note - last_tone)
            if current_difference < min_difference:
                nearest_tone = note
                min_difference = current_difference

        last_index = harmony.index(nearest_tone)
        next_index = last_index + steps_in_harmony
        octave = last_octave

        while next_index < 0:
            octave -= 1
            next_index += len(harmony)
        while next_index >= len(harmony):
            octave += 1
            next_index -= len(harmony)

        if octave > 2:
            continue
        elif octave < 0:
            continue

        note = int(harmony[next_index] + octave*12)
        # Remember note
        last_note = note

        beat = (length, (note,))
        measure.append(beat)

        remaining_beats -= length

    return measure, last_note

def final_measure(harmony):
    notes = set()
    notes.add(harmony[0])
    notes.add(harmony[1])
    notes.add(harmony[2])
    measure = [(4, notes)]

    return measure


# Takes [(0, 4, 7),  ...,  (7, 11, 14)]
# Returns [
#    [(2, {0}), (1, {4, 7}, (1, {-8, 7, 12})],
#    [(2, {0}), (1, {4, 7}, (1, {-8, 7, 12})],
#    ...
# ]
def make_melody(harmonies):
    melody = []

    last_note = harmonies[0][0] + 12

    for harmony in harmonies:
        measure, last_note = make_measure(harmony, last_note)
        melody.append(measure)

    melody.append(final_measure(harmonies[0]))

    return melody