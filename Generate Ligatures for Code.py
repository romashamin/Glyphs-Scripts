#MenuTitle: Generate Ligatures for Code Features
# -*- coding: utf-8 -*-
__doc__="""
Generates features code for ligatures for code, like these:
  sub hyphen greater by hyphen_greater.liga;
  pos hyphen_greater.liga <750 0 750 0 (wdth:3) 600 0 600 0>;
"""

marker_ligature = ".liga"
marker_part = "_part."
parts_separator = "_"

max_width = 750
min_width = 600

def is_ligature(name):
	if marker_ligature in name and marker_part not in name:
		return True
	return False

def get_rid_of_extention(name):
	return name.split(marker_ligature)[0]

def ligature_parts_number(name):
	return len(name.split(parts_separator))

def code_line(name):
	glyphs_sequence = get_rid_of_extention(name).replace("_", " ")
	spaces_number = ligature_parts_number(name) - 1
	spaces_max_width = max_width * spaces_number
	spaces_min_width = min_width * spaces_number
	rule_sub = f"sub {glyphs_sequence} by {name};"
	rule_pos = f"pos {name} <{spaces_max_width} 0 {spaces_max_width} 0 (wdth:3) {spaces_min_width} 0 {spaces_min_width} 0>;"
	return f"{rule_sub}\n{rule_pos}"

glyphs_names = map(lambda glyph : glyph.name, Glyphs.font.glyphs)
ligatures_full_names = filter(is_ligature, glyphs_names)
ligatures_clean_names = map(get_rid_of_extention, ligatures_full_names)
sorted_names = sorted(ligatures_full_names, key=ligature_parts_number, reverse=True)
code_lines = map(code_line, sorted_names)

print("\n".join(list(code_lines)))