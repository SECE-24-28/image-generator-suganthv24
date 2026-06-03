from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt
from datetime import datetime
import os

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True
)

pipe.enable_attention_slicing()
pipe.enable_vae_slicing()

pipe = pipe.to("cuda")

os.makedirs("result", exist_ok=True)

while True:
    prompt = input("\nEnter prompt (or type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("Exiting...")
        break

    print("Generating image...")

    image = pipe(
        prompt,
        num_inference_steps=20,
        height=512,
        width=512
    ).images[0]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result/generated_{timestamp}.png"

    image.save(filename)

    plt.imshow(image)
    plt.axis("off")
    plt.show()

    print(f"Image saved as: {filename}")