BOTTLE TARANG – HINDUSTANI CLASSICAL MUSIC PLAYER

This project was done by Abhijeet Shetty and Akhila Joshi. 

Hindustani classical music is the classical music of the Northern regions of the Indian subcontinent. It is based on the Raga system, which are melodic scales consisting of combinations of different notes.The forms of Hindustani classical music were designed primarily for vocal performances but have found adaptations in other instruments over the years. 

This project delves into the realm of Indian classical music, particularly the Bhoopali Raag, and translates its essence into the digital realm. We have taken a mesmerizing Bandish (a musical composition) and voiced it through a unique instrument made by us - the Bottle Tarang.

Bottle Tarang: Crafting Unique Sounds

The Bottle-tarang is inspired by an ancient Indian instrument called the Jal-tarang which was invented in the 17th century. The word Jal-tarang literally translates to ‘waves in water’. The instrument consists of several water filled bowls of either porcelain, copper or other metal alloys. When these bowls or containers are struck with a stick, they produce melodious sounds of varying notes. A variety of notes is obtained by varying the sizes of the bowls and levels of water. 

The instrument works on the principle that the motion of sound is created or modified by changing the amount of water levels. When the edge of the bowl filled with water is stuck with the wooden sticks, it produces vibrations that travel through this water and are transferred to the surrounding air to produce sweet melodic sounds. Tuning them to the right frequencies is challenging. The material of the bowls used also determines the quality of the sound. 

Inspired by the Jal-tarang, we designed our own instrument with different empty alcohol bottles filled with water, and spoons to strike them. Each bottle was filled with varying levels of water and when struck, produced distinct and harmonious sounds reminiscent of the Jal-tarang. 
Since different bottles were used, the timbre for each note is different.

For recording, we used a dynamic microphone, ‘Sennheiser E945’, for each of the bottles. The mic was placed towards the lower end of each bottle’s body and they were struck below their respective water levels. 

Bhoopali Raag: A Musical Heritage

Bhoopali Raag, also known as Bhop, is a serene and soulful Raag in Hindustani classical music. Its ascending and descending scale, coupled with a pentatonic structure, evokes a tranquil and contemplative mood. The choice of this Raag marries well with the sweet sound of the Bottle-tarang.

Project Details:

At the core of this project is a Python program that generates a MIDI file representing a Bandish in the Bhoopali Raag. 
The program uses Python libraries to convert the predefined note progression of the Bandish into MIDI notes.
We then use a MIDI channel on ‘Logic Pro’ loaded with an empty electronic drum kit and import the generated MIDI file onto the channel
The recorded sounds of the Bottle Tarang are used as samples which are loaded onto the empty drum kit by mapping the notes of our instrument to the corresponding notes on the kit.
In this way, we prepare the MIDI channel with the sounds of the Bottle Tarang to be able to play any MIDI file that we generate using our code.


Libraries Used:

Midiutil library:
The `midiutil` library is utilized for creating MIDI files. It simplifies the process of MIDI file generation by providing a straightforward interface to add notes, tempo, and other musical elements to the file. The MIDIFile class is employed to initiate and manage the MIDI file structure.

Mingus Library:
The `mingus` library is used for note manipulation. It facilitates the handling and manipulation of musical notes, including converting between different note representations and managing note properties. In this project we use the notes module from mingus.core for converting and managing note representations, and the swap_accidentals function handles note names with accidentals, ensuring accurate conversion to MIDI representation.

Summarizing The Process Steps:

Note Progression Definition:
The note progression for the Bhoopali Raag Bandish is predefined in the program.

Conversion to MIDI:
The program iterates through the note progression, converts each note to its MIDI representation, and adds it to the MIDI file.

OCTAVE Handling:
The program dynamically adjusts the octave for certain notes, enhancing the musical richness.

Duration Variation:
Different note durations are applied to create rhythmic variations within the composition.

Sampling: 
The sounds of the Bottle-tarang are recorded and sampled onto an empty kit with the correct mappings

Future Scope for the project:
This project showcases the fusion of programming and music theory, offering both practical utility and educational value in the realm of Indian classical music. We could build up by incorporating the features of Google Magenta to create Raga melodies. Google Magenta is centered around NoteSequences, which are abstract representations of a series of notes with customizable pitches, instruments and strike velocities. This enables us to feed the notes of any Raga into it. 

Moreover, Google Magenta has also come up with a Melodic Recurrent Neural Network Model (an LSTM based model) that continues to create random notes in continuation with the NoteSequence you feed into it. This could be used to make our own compositions in any Raga as opposed to only playing the existing ones.

Additionally, implementing a user interface could enhance accessibility, allowing users to customize the note progression and other parameters.
