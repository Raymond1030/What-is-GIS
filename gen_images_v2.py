from google import genai
from google.genai import types
import os, time

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
base = "/Users/raymond/Documents/What is GIS/images"

images = [
    ("app_logistics.png", "Modern logistics and delivery route optimization visualization: a city map with multiple colored delivery routes radiating from warehouses to destinations, drones and vehicles moving along paths, package icons, optimization algorithm visualization. Dark background, teal and gold accents, professional data visualization style."),
    ("app_retail_site.png", "Retail site selection analysis visualization: an aerial view of urban area with color-coded heatmap showing customer density, competitor locations marked, candidate store locations highlighted with circles of different sizes representing market potential. Modern data visualization, dark theme."),
    ("app_new_energy.png", "Renewable energy site planning using GIS: a landscape view showing solar panel farms and wind turbines placed on terrain based on GIS analysis - solar radiation heatmap, wind speed overlays, terrain slope colors, transmission line networks. Blue and gold color scheme, sunset lighting."),
    ("app_archaeology.png", "Archaeological site mapping with LiDAR: a dense jungle landscape with hidden ancient pyramid structures revealed through LiDAR scanning, showing the transition from overgrown forest on one side to exposed Mayan ruins on the other. Dramatic lighting, discovery aesthetic."),
    ("app_crime.png", "Crime analysis heatmap visualization: a city street grid map overlaid with red-orange hotspot clusters showing crime density, police patrol routes, and analysis charts. Professional police analytics style, dark theme with red accents."),
    ("app_healthcare.png", "Public health GIS mapping: a city map showing disease spread patterns with concentric circles, hospital locations, medical resource allocation zones, and epidemiological data visualization. COVID-era dashboard aesthetic, modern healthcare analytics."),
    ("concept_gis_what.png", "Vibrant concept illustration showing GIS connecting everything: a central globe with data layers flowing out - roads, buildings, rivers, people, weather, satellites all connected by glowing lines. Infographic style, bright colors on dark background, educational and inviting."),
    ("learning_path.png", "A visual learning roadmap for GIS: mountain path illustration with checkpoints labeled Basic GIS → QGIS → Python → Remote Sensing → Deep Learning → GeoAI Research, with flags and milestones. Motivational, journey metaphor, dark blue background with bright path."),
    ("research_papers.png", "Academic research concept: floating research papers, arXiv logo elements, neural network diagrams, satellite imagery, mathematical formulas, all interconnected by glowing lines. Futuristic academic aesthetic, cyan and purple glow, dark background."),
    ("coord_earth.png", "Educational illustration of Earth's geometric models: three transparent layers showing the physical Earth surface, geoid (bumpy equipotential surface), and reference ellipsoid (smooth mathematical model), with labels and measurement lines. Technical diagram style, clean background."),
]

for filename, prompt in images:
    filepath = os.path.join(base, filename)
    if os.path.exists(filepath):
        print(f"SKIP: {filename}")
        continue
    print(f"Generating: {filename}", flush=True)
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(filepath)
                print(f"  OK", flush=True)
                break
    except Exception as e:
        print(f"  ERROR: {e}", flush=True)
    time.sleep(2)

print("Done!")
