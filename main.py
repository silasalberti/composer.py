import composer
import musescore
import lefthand
import righthand

import random

for i in range(5):
    chord_progression = random.choice(composer.chord_progressions)
    harmonies = composer.make_harmonies(chord_progression)

    accompaniment = lefthand.make_accompaniment(harmonies)
    melody = righthand.make_melody(harmonies)

    key = random.choice(range(60,72))
    musescore.make_piece(melody, accompaniment, name=f"piece{i}", key=key)