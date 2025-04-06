🖼️ Image to Sketch Web App 🎨
Convert any photo into a high-quality pencil sketch using OpenCV and Flask.
Upload an image, hit "Convert & Download", and instantly get a 1080p sketch-style image!

✨ Features
🔄 Instant Conversion of images to pencil sketches

📸 Supports all image types (JPG, PNG, etc.)

⚡ Outputs sharp, high-resolution 1080p sketches

💡 Simple, minimal, and responsive UI

🧠 Uses OpenCV for image processing

🔥 Built with Python + Flask




📁 Project Structure
bash
Copy
Edit
image-to-sketch/
├── app.py
├── uploads/         # Stores uploaded images
├── sketches/        # Stores sketch output
└── templates/
    └── index.html   # Frontend upload form




    
🛠 Tech Stack
Python

Flask

OpenCV

HTML/CSS (Minimal styling)

🧠 How It Works
Image is uploaded by the user

OpenCV converts it to grayscale

Applies inversion, blur, and dodge blend technique

Optionally sharpens the sketch for better edges

Resizes the result to 1080p resolution

Sends the sketch back for instant download

📦 To-Do / Improvements
 Live image preview before download

 Drag & Drop UI

 Convert multiple images at once

 Online deployment (Render, Vercel, etc.)

 Optional sketch filters (soft, pencil, charcoal)



