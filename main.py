from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipe  = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

prompt = input("Enter your prompt: ")

with torch.autocast("cuda"):
  image=pipe(prompt).images[0]

plt.imshow(image)
plt.axis("off")
plt.title("Generate by Stable Diffuser")
plt.show()

image.save("result/generated_image.png")