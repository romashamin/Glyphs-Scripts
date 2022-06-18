#MenuTitle: Select All Anchors
# -*- coding: utf-8 -*-
__doc__="""
Just selects all anchors on the current layer.
"""

selectedLayers = Glyphs.font.selectedLayers

def selectAllAnchors(layer):
	anchors = layer.anchors
	if anchors is not None and len(anchors) > 0:
		for anchor in anchors:
			anchor.selected = True

if selectedLayers is not None and len(selectedLayers) > 0:
	currentLayer = selectedLayers[0]
	selectAllAnchors(currentLayer)