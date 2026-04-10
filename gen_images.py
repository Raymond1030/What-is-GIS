from google import genai
from google.genai import types
import os, time

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
base = "/Users/raymond/Documents/What is GIS/images"

images_to_generate = [
    ("hero_earth_gis.png", "A stunning wide-angle view of Earth from space at night, showing city lights and network connections between cities glowing in teal and cyan colors, with subtle grid overlay representing GIS coordinate systems. Dark space background with stars. Photorealistic, cinematic, high detail."),
    ("gis_layers_concept.png", "An educational diagram showing the GIS data layers concept: multiple transparent map layers stacked vertically in 3D perspective - bottom layer is terrain/topography in greens and browns, then a water/hydrology layer in blue, then a roads/transportation layer with white lines, then a buildings/urban layer, then a boundary/administrative layer. Clean dark background, modern infographic style, labeled layers, glowing edges in teal."),
    ("vector_data.png", "A clean technical illustration showing GIS vector data types: points (as glowing dots representing cities), lines (as colored paths representing roads and rivers), and polygons (as filled shapes representing land parcels and lakes). On a dark navy background with a subtle grid. Modern, minimal, educational diagram style with labels. Teal, blue and gold accent colors."),
    ("raster_data.png", "A technical illustration showing GIS raster data: a landscape image being decomposed into a grid of square pixels/cells, each cell colored to represent different values (elevation, temperature, or land use). Show the transition from smooth landscape on left to pixelated grid on right. Dark background, modern educational style, warm color palette from green to yellow to red representing data values."),
    ("map_projection.png", "An educational illustration showing map projection concepts: a 3D globe on the left being unwrapped or projected onto a flat 2D map on the right, with projection lines visible. Show three small examples: cylindrical Mercator, conical, and azimuthal projections. Clean, modern infographic style on dark background with teal and gold accents."),
    ("spatial_analysis.png", "A professional GIS spatial analysis visualization showing: buffer zones as concentric rings around a point, overlay analysis with two intersecting colored polygons, and a heat map density surface. Modern dark-themed data visualization style, glowing in teal, purple, and gold colors. Clean and technical."),
    ("remote_sensing.png", "An illustration of remote sensing technology: a satellite orbiting Earth, emitting sensor beams down to the surface, capturing multispectral imagery. Show electromagnetic spectrum bands as colored bands. Include a small drone and an aircraft also collecting data. Modern, technical illustration style, dark space background, vibrant colors."),
    ("geoai_concept.png", "A futuristic illustration combining GIS and AI: a detailed city map satellite image being analyzed by neural network nodes and connections overlaid on top, with AI extracting features like buildings roads and vegetation automatically. Glowing nodes and connections in teal and purple. Dark background, cyberpunk meets science aesthetic."),
    ("digital_twin.png", "A split-view illustration of a digital twin city: the left half shows a real photograph style city with buildings roads and parks; the right half shows the same city as a wireframe holographic 3D digital model with data streams, sensors, and IoT connections visible. The two halves merge in the center. Futuristic, blue and teal color scheme, high detail."),
    ("3d_reconstruction.png", "An illustration of 3D city reconstruction from aerial imagery: show a drone capturing photos from multiple angles at top, processing pipeline in the middle with point clouds, and a detailed photorealistic 3D city model at the bottom. Dark background, technical visualization style, teal and gold accents."),
    ("lbs_location.png", "An illustration of Location Based Services LBS: a smartphone in the center showing a map with navigation, surrounded by floating icons representing different LBS applications like ride sharing food delivery social media check-ins augmented reality indoor navigation. Urban cityscape background, modern flat illustration style with depth, vibrant colors on dark background."),
    ("urban_planning.png", "A GIS-powered urban planning visualization: an aerial view of a city with color-coded zoning residential in warm colors commercial in blue industrial in purple green spaces in green, with data overlays showing population density, traffic flow arrows, and proposed development areas highlighted. Modern data visualization style, detailed and professional."),
    ("agriculture_gis.png", "Precision agriculture using GIS and remote sensing: an aerial view of farmland with different crop fields shown in various colors based on NDVI vegetation health index red for stressed yellow for moderate green for healthy. Include a small drone flying over, tractor with GPS guidance, and data dashboard overlay. Professional, educational style."),
    ("emergency_gis.png", "GIS in emergency management: a map showing natural disaster response with flood inundation zones in blue gradient, evacuation routes as highlighted roads, emergency shelter locations as red markers, rescue team positions as moving dots. Real-time dashboard overlay with statistics. Dark theme, urgent color scheme with red, orange, and blue."),
    ("webgis_dev.png", "WebGIS development concept: a large monitor displaying an interactive web map application with layers panel, drawing tools, and data visualization. Code snippets floating around in JavaScript and Python. Modern developer workspace aesthetic, dark theme with code syntax highlighting colors."),
    ("gis_career.png", "An illustration representing GIS careers and job market: diverse professionals working with maps data drones satellites and computers in a modern office lab setting. Include elements of different industries environment urban planning tech. Professional, warm lighting, inclusive representation, modern illustration style."),
]

for filename, prompt in images_to_generate:
    filepath = os.path.join(base, filename)
    if os.path.exists(filepath):
        print(f"SKIP (exists): {filename}")
        continue
    print(f"Generating: {filename}...", flush=True)
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(filepath)
                print(f"  OK: {filepath}", flush=True)
                break
        else:
            print(f"  WARN: No image returned for {filename}", flush=True)
    except Exception as e:
        print(f"  ERROR: {filename}: {e}", flush=True)
    time.sleep(3)

print("\nDone generating images!")
