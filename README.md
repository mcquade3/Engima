# Engima
A Python version of the famed Enigma machine used in World War II

The program works by reading input from a text file.

The first line of the file lists the settings of the machine.
For example, "B  II,IV,V  EIY".
The settings are separated by TWO SPACES each. The first setting is the reflector used, the second setting is the configuration of rotors, and the last setting is the starting positions of the rotors. The rotors used are separated by commas, while the starting positions of the rotors are not separated.

The second line in the text file is the message, which must be written solely in UPPERCASE, with no numbers, spaces, or other characters.
For example, "ASUMBYPOLELKUPGPDMOIMKOBJXLDKAFLGHZZ" would translate to "WEATHERPATTERNSXHEAVYRAINCHANCEOFFOG". Spaces are represented by 'X' in Enigma messages.
