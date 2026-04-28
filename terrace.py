import gradio as gr
from google import genai
from google.genai import types
from PIL import Image
import os

# 🔐 API KEY (set this in environment variable)
API_KEY = "AIzaSyDDHx7wSTLPIM2gwbcJzZqNtaMGU1c0Ihk"

if not API_KEY:
    raise ValueError("Please set GOOGLE_API_KEY in your environment variables")

client = genai.Client(api_key=API_KEY)

# 🌿 Plant Database
PLANT_DATABASE = {
    "Hyderabad / South India (Hot & Semi-Arid)": [
        "Bougainvillea", "Ixora", "Areca Palm", "Adenium (Desert Rose)", "Hibiscus", "Curry Leaf", "Jasmine"
    ],
    "Bangalore / Pune (Moderate/Tropical)": [
        "Ferns", "Philodendron", "Crotons", "Petunias", "Snake Plant", "Spider Plant", "Peace Lily"
    ],
    "Delhi / North India (Extreme Temperatures)": [
        "Ficus", "Marigold", "Oleander", "Bamboo Palm", "Money Plant (Epipremnum)", "Aloe Vera"
    ],
    "Coastal (High Humidity)": [
        "Coconut Palm", "Dracaena", "Anthurium", "Orchids", "Bird of Paradise", "Plumeria"
    ]
}

# 🔄 Update plant list
def update_plants(location):
    plants = PLANT_DATABASE.get(location, [])
    return gr.update(choices=plants, value=plants[:3])

# 🌱 Main Function
def generate_three_gardens(input_img, user_prompt, location, selected_plants):
    if input_img is None:
        raise gr.Error("Please upload an image.")

    if not selected_plants:
        raise gr.Error("Please select at least one plant.")

    plant_str = ", ".join(selected_plants)
    enhanced_prompt = f"{user_prompt}. Location: {location}. Include: {plant_str}. Realistic terrace garden."

    try:
        # ✅ Step 1: Check terrace
        check = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=["Is there a terrace or balcony here? Reply Yes or No.", input_img]
        )

        if "no" in check.text.lower():
            raise gr.Error("No terrace detected in the image.")

        # ✅ Step 2: Generate images
        paths = []

        for i in range(1, 4):
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[f"{enhanced_prompt}. Variation {i}", input_img],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"]
                )
            )

            for part in response.candidates[0].content.parts:
                if hasattr(part, "inline_data") or hasattr(part, "image"):
                    img = part.as_image()
                    filename = f"garden_{i}.png"
                    img.save(filename)
                    paths.append(filename)
                    break

        return paths

    except Exception as e:
        raise gr.Error(str(e))

# 🎨 UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌿 AI Terrace Garden Designer")
    gr.Markdown("Design your terrace using plants suitable for your climate.")

    with gr.Row():
        # LEFT
        with gr.Column(scale=1):
            input_view = gr.Image(label="Upload Terrace Image", type="pil")

            location_drop = gr.Dropdown(
                label="Select Location",
                choices=list(PLANT_DATABASE.keys()),
                value=list(PLANT_DATABASE.keys())[0]
            )

            plant_select = gr.CheckboxGroup(
                label="Select Plants",
                choices=PLANT_DATABASE[list(PLANT_DATABASE.keys())[0]],
                value=PLANT_DATABASE[list(PLANT_DATABASE.keys())[0]][:2]
            )

            prompt_input = gr.Textbox(
                label="Design Instructions",
                value="Modern terrace garden with seating"
            )

            generate_btn = gr.Button("Generate Designs", variant="primary")

        # RIGHT
        with gr.Column(scale=2):
            output_gallery = gr.Gallery(label="Generated Designs", columns=3)

            visit_btn = gr.Button("Analyze My Terrace")

    # 🔄 Events
    location_drop.change(update_plants, location_drop, plant_select)

    generate_btn.click(
        generate_three_gardens,
        inputs=[input_view, prompt_input, location_drop, plant_select],
        outputs=output_gallery
    )

    visit_btn.click(None, js="window.open('https://terrace-garden.lovable.app/', '_blank')")

# ▶ Run
if __name__ == "__main__":
    demo.launch()
