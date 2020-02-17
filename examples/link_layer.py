from photoshop import Application
from photoshop import DocumentFill
from photoshop import NewDocumentMode
from photoshop import Units

app = Application()

start_ruler_units = app.preferences.rulerUnits

if len(app.documents) < 1:
    if start_ruler_units is not Units.PIXELS:
        app.preferences.rulerUnits = Units.PIXELS
    docRef = app.documents.add(
        320, 240, 72, None, NewDocumentMode.RGB,
        DocumentFill.BACKGROUNDCOLOR,
    )
else:
    docRef = app.activeDocument

layerRef = docRef.artLayers.add()
layerRef2 = docRef.artLayers.add()
layerRef.link(layerRef2)

# Set the ruler back to where it was
app.preferences.rulerUnits = start_ruler_units