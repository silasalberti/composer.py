import random
from itertools import combinations
import time

random.seed(time.time())

rhythms = [(4,), (2, 2), (2, 1, 1), (1, 1, 2), (1, 1, 1, 1), (1, 2, 1)]

class Recipe:
    def __init__(self, rhythms):
        self.rhythms = rhythms

standard_recipe = Recipe(random.choice(tuple(combinations(rhythms,3))))

# Takes (0, 4, 7)
# Returns [(2, {0}), (1, {4, 7}, (1, {-8, 7, 12})]
def make_measure(harmony):
    rhythm = random.choice(standard_recipe.rhythms)

    measure = []

    # Solange probieren bis Kriterien erfüllt sind
    legit = False
    while not legit: 
        # Annahme, dass legit ist
        legit = True

        notes = set()
        # Grundton hinzufügen
        notes.add(harmony[0])

        # Zählzeiten durchlaufen
        for length in rhythm:
            # Zwischen 1 und 4 Tönen gleichzeitig
            num_tones = random.choice([1]*4 + [2]*4 + [3]*1 + [4]*1)

            for i in range(num_tones):
                octave = random.choice([-2] + [-1]*6 + [0])
                notes.add(random.choice(harmony) + octave*12)

            # Kriterium Nr. 1
            # Maximal eine Oktave Abstand pro Zählzeit
            if max(notes) - min(notes) > 12:
                legit = False

            beat = (length, notes)
            measure.append(beat)

            notes = set()
        
        # Kriterien
        if not legit:
            pass
        # Kriterium Nr. 2
        # Maximal eine Duodezime pro Takt
        elif max(max(beat[1]) for beat in measure) - min(min(beat[1]) for beat in measure) > 19:
            legit = False
        # Kriterium Nr. 3
        # Alle Töne der Harmonie
        elif len(set(note % 12 for note in beat[1] for beat in measure)) != len(harmony):
            legit = False
        
        if not legit:
            measure = []
        
    return measure

def final_measure(harmony):
    notes = set()
    notes.add(harmony[0]-24)
    notes.add(harmony[0]-12)
    notes.add(harmony[1]-12)
    notes.add(harmony[2]-12)
    measure = [(4, notes)]

    return measure

# Takes [(0, 4, 7),  ...,  (7, 11, 14)]
# Returns [
#    [(2, {0}), (1, {4, 7}, (1, {-8, 7, 12})],
#    [(2, {0}), (1, {4, 7}, (1, {-8, 7, 12})],
#    ...
# ]
def make_accompaniment(harmonies):
    accompaniment = []

    for harmony in harmonies:
        measure = make_measure(harmony)
        accompaniment.append(measure)

    accompaniment.append(final_measure(harmonies[0]))

    return accompaniment
