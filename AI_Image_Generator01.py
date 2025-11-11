import tkinter
import customtkinter as ctk
import os
import openai
from PIL import Image, ImageTk
import requests, io

window = ctk.CTk()
window.title("AI Image Generator")
window.geometry('600x400')
# === Function to generate and display images ===
def generateImage():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Get user prompt
    UserPrompt = prompt_entry.get()
    UserPrompt += " in style: " + style_selection.get()

    # Call OpenAI API
    Response = openai.Image.create(
        prompt=UserPrompt,
        n=int(no_of_img_Slider.get()),
        size="512x512"
    )

    # Get URLs
    image_urls = [img['url'] for img in Response['data']]

    # Clear previous images
    for widget in images_frame.winfo_children():
        widget.destroy()

    # Store PhotoImage references
    photo_images = []

    # Loop through each image URL
    for idx, url in enumerate(image_urls):
        resp = requests.get(url)
        image = Image.open(io.BytesIO(resp.content))
        photo_image = ImageTk.PhotoImage(image)
        photo_images.append(photo_image)

        # Create label to show image
        img_label = tkinter.Label(images_frame, image=photo_image)
        img_label.image = photo_image  # Keep reference
        img_label.grid(row=idx // 2, column=idx % 2, padx=10, pady=10)

# === Input Frame ===
Input_Frame = ctk.CTkFrame(window)
Input_Frame.pack(side='left', expand=True, padx=20, pady=20)

prompt_label = ctk.CTkLabel(Input_Frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)

prompt_entry = ctk.CTkEntry(Input_Frame, height=12, width=200)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = ctk.CTkLabel(Input_Frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)

style_selection = ctk.CTkComboBox(Input_Frame, values=["Pencil Art", "Realistics", "3D illustration", "Cartoonish"])
style_selection.grid(row=1, column=1, padx=10, pady=10)

No_of_Images_label = ctk.CTkLabel(Input_Frame, text="# Images")
No_of_Images_label.grid(row=2, column=0, padx=10, pady=10)

no_of_img_Slider = ctk.CTkSlider(Input_Frame, from_=1, to=5, number_of_steps=4)
no_of_img_Slider.grid(row=2, column=1, padx=10, pady=10)

generate_button = ctk.CTkButton(Input_Frame, text="Generate", command=generateImage)
generate_button.grid(row=3, column=0, columnspan=2, sticky='news', padx=10, pady=10)

# === Images Display Frame ===
images_frame = tkinter.Frame(window)
images_frame.pack(side='left', padx=20, pady=20)

window.mainloop()
