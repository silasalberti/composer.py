file_header = '''<?xml version="1.0" encoding="UTF-8"?>
<museScore version="2.06">
  <programVersion>2.3.2</programVersion>
  <programRevision>4592407</programRevision>
  <Score>
    <LayerTag id="0" tag="default"></LayerTag>
    <currentLayer>0</currentLayer>
    <Synthesizer>
      </Synthesizer>
    <Division>480</Division>
    <Style>
      <lastSystemFillLimit>0</lastSystemFillLimit>
      <page-layout>
        <page-height>1683.36</page-height>
        <page-width>1190.88</page-width>
        <page-margins type="even">
          <left-margin>56.6929</left-margin>
          <right-margin>56.6929</right-margin>
          <top-margin>56.6929</top-margin>
          <bottom-margin>113.386</bottom-margin>
          </page-margins>
        <page-margins type="odd">
          <left-margin>56.6929</left-margin>
          <right-margin>56.6929</right-margin>
          <top-margin>56.6929</top-margin>
          <bottom-margin>113.386</bottom-margin>
          </page-margins>
        </page-layout>
      <Spatium>1.76389</Spatium>
      </Style>
    <showInvisible>1</showInvisible>
    <showUnprintable>1</showUnprintable>
    <showFrames>1</showFrames>
    <showMargins>0</showMargins>
    <metaTag name="arranger"></metaTag>
    <metaTag name="composer"></metaTag>
    <metaTag name="copyright"></metaTag>
    <metaTag name="creationDate">2018-11-23</metaTag>
    <metaTag name="lyricist"></metaTag>
    <metaTag name="movementNumber"></metaTag>
    <metaTag name="movementTitle"></metaTag>
    <metaTag name="platform">Microsoft Windows</metaTag>
    <metaTag name="poet"></metaTag>
    <metaTag name="source"></metaTag>
    <metaTag name="translator"></metaTag>
    <metaTag name="workNumber"></metaTag>
    <metaTag name="workTitle"></metaTag>
    <PageList>
      <Page>
        <System>
          </System>
        <System>
          </System>
        </Page>
      </PageList>
    <Part>
      <Staff id="1">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
        <Staff id="2">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Piano</trackName>
      <Instrument>
        <longName>Piano</longName>
        <shortName>Pno.</shortName>
        <trackName>Piano</trackName>
        <minPitchP>21</minPitchP>
        <maxPitchP>108</maxPitchP>
        <minPitchA>21</minPitchA>
        <maxPitchA>108</maxPitchA>
        <instrumentId>keyboard.piano</instrumentId>
        <clef staff="2">F</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>95</gateTime>
          </Articulation>
        <Channel>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>'''

file_bottom = '''
</Score>
</museScore>'''

import random

def make_beat(length, chord):
    notes = ""
    for tone in chord:
        notes += f'''
        <Note>
            <pitch>{tone + BASE_NOTE}</pitch>
        </Note>
        '''

    lengths = {
        "0.25" : "16th",
        "0.5" : "eighth",
        "1" : "quarter",
        "2" : "half",
        "4" : "whole"
    }

    beat = f'''
    <Chord>
        <durationType>{lengths[str(length)]}</durationType>
        {notes}
    </Chord>
    '''

    return beat

def make_measure(measure, number):
    beats = ""

    for beat in measure:
        beats += make_beat(*beat)
        
    return f'''
    <Measure number="{number}">
        {beats}
    </Measure>'''

def make_staff(voice, id):
    text = f'<Staff id="{id}">'
    for number, chord in enumerate(voice):
        measure = make_measure(chord, number+1)
        text += measure
    text += f'</Staff>'

    return text


def make_piece(righthand, lefthand, key=60, name="piece"):
    global BASE_NOTE
    BASE_NOTE = key

    text = file_header
    text += make_staff(righthand, 1)
    text += make_staff(lefthand, 2)
    text += file_bottom

    with open(f"{name}.mscx", "w") as f:
        f.write(text)