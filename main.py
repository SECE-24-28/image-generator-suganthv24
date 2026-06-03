from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True
)

pipe.enable_attention_slicing()
pipe.enable_vae_slicing()

pipe = pipe.to("cuda")

prompt = input("Enter your prompt: ")

image = pipe(
    prompt,
    num_inference_steps=20,
    height=512,
    width=512
).images[0]

plt.imshow(image)
plt.axis("off")
plt.show()

image.save("result/generated_image.png")