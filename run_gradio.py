import gradio as gr
from PIL import Image
from typing import Literal

from run import generate_scene

MAX_RESOLUTION_GRADIO = 1000

def generate_scene_gradio_id(
    image: Image.Image, prompt: str
):
    from hashlib import sha1
    from datetime import datetime

    run_id = sha1(datetime.now().isoformat().encode()).hexdigest()[:6]
    run_name = f"outputs/gradio_{run_id}.ply"

    return generate_scene(image, prompt, run_name, mode="stage", seed=0, max_resolution=MAX_RESOLUTION_GRADIO)

if __name__ == "__main__":
    demo = gr.Interface(
        fn=generate_scene_gradio_id,
        inputs=[
            gr.Image(label="Input Image", sources=["upload", "clipboard"], type="pil"),
            gr.Textbox(label="Scene Hallucination Prompt")
        ],
        outputs=gr.Model3D(label="Generated Scene"),
        allow_flagging="never",
        title="Invisible Stitch: Generating Smooth 3D Scenes with Depth Inpainting",
        description="Hallucinate geometrically coherent 3D scenes from a single input image in less than 30 seconds.<br /> [Project Page](https://research.paulengstler.com/invisible-stitch) | [GitHub](https://github.com/paulengstler/invisible-stitch) | [Paper](#) <br /><br />To keep this demo snappy, we have limited its functionality. Scenes are generated at a low resolution without densification, supporting views are not inpainted, and we do not optimize the resulting point cloud. Imperfections are to be expected, in particular around object borders. Please allow a couple of seconds for the generated scene to be downloaded (about 40 megabytes).",
        article="Please consider running this demo locally to obtain high-quality results (see the GitHub repository).<br /><br />Here are some observations we made that might help you to get better results:<ul><li>Use generic prompts that match the surroundings of your input image.</li><li>Ensure that the borders of your input image are free from partially visible objects.</li><li>Keep your prompts simple and avoid adding specific details.</li></ul>",
        examples=[
            ["examples/photo-1667788000333-4e36f948de9a.jpeg", "a street with traditional buildings in Kyoto, Japan"],
            ["examples/photo-1628624747186-a941c476b7ef.jpeg", "a suburban street in North Carolina on a bright, sunny day"],
            ["examples/photo-1469559845082-95b66baaf023.jpeg", "a view of Zion National Park"],
            ["examples/photo-1514984879728-be0aff75a6e8.jpeg", "a close-up view of a muddy path in a forest"],
            ["examples/photo-1618197345638-d2df92b39fe1.jpeg", "a close-up view of a white linen bed in a minimalistic room"],
            ["examples/photo-1546975490-e8b92a360b24.jpeg", "a warm living room with plants"],
            ["examples/photo-1499916078039-922301b0eb9b.jpeg", "a cozy bedroom on a bright day"],
            ["examples/20240811_093727.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075732.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075804.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075832.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075900.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075918.jpg", "a street with a tree and an eletric pole"],
            ["examples/20240818_075933.jpg", "a street with a tree and an eletric pole"],
        ])
    demo.queue().launch(share=True)
