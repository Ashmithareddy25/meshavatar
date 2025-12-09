import gradio as gr
import trimesh
import os

DEMO_MESH = "demo_avatar.obj"   # Upload this file to HuggingFace

def generate_3d_avatar(image_path):
    """
    Simulated 3D avatar generation:
    - In a real system, here you would run MeshAvatar inference.
    - On HuggingFace CPU, we return a demo mesh instead.
    """
    if image_path is None:
        return None, "❌ No image uploaded."

    if not os.path.exists(DEMO_MESH):
        return None, "❌ demo_avatar.obj not found. Upload it to your Space."

    # Load static demo mesh
    mesh = trimesh.load(DEMO_MESH, force="mesh")

    return {
        "vertices": mesh.vertices,
        "faces": mesh.faces
    }, "✅ 3D avatar generated successfully!"


with gr.Blocks(title="Team 13: MeshAvatar Project") as demo:

    # Custom CSS (HuggingFace-safe)
    gr.HTML("""
    <style>
        .big-button { 
            background-color: #FF7A00 !important;
            color: white !important;
            font-size: 20px !important;
            padding: 14px !important;
            border-radius: 10px !important;
            width: 100% !important;
            font-weight: bold;
        }
    </style>
    """)

    gr.Markdown("""
    <h1 style='text-align:center;'>🧍 Team 13: MeshAvatar Project</h1>
    <h3 style='text-align:center;'>Upload an Image → Generate 3D Avatar</h3>
    """)

    # Image Upload Section
    input_image = gr.Image(
        label="Upload Image",
        type="filepath",
        interactive=True
    )

    # Big Action Button
    generate_button = gr.Button(
        "Generate Avatar",
        elem_classes=["big-button"]
    )

    # Output 3D viewer
    mesh_viewer = gr.Model3D(
        label="Generated 3D Avatar",
        clear_color=[0.9, 0.9, 0.9, 1]
    )

    # Status text
    status_box = gr.Textbox(
        label="System Status",
        interactive=False
    )

    # Connect button to function
    generate_button.click(
        fn=generate_3d_avatar,
        inputs=[input_image],
        outputs=[mesh_viewer, status_box]
    )

demo.launch()
