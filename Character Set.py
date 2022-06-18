#MenuTitle: Character Set
# -*- coding: utf-8 -*-
__doc__="""
Print all alphabetical characters in the font.
"""

result = ""
excluded_categories = ["Mark", "Separator"]

for myGlyph in Glyphs.font.glyphs:
	if myGlyph.export == True and myGlyph.category not in excluded_categories:
		result += myGlyph.string

print(result)