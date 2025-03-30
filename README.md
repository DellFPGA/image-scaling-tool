# image-scaling-tool
CLI utility to upscale/downscale images while preserving aspect ratio for AI art workflows
# Image Scaling Tool

A standalone Python 3 utility for calculating scaling dimensions of images used in AI art workflows. Perfect for artists working with tools like Stable Diffusion (SDXL/Automatic1111), this script helps you resize images—either up or down—while maintaining their original aspect ratio, ensuring they stay within resolution limits that your GPU can handle.

---

## ✨ Features

- **Preserves aspect ratio**
- **Supports both downscaling and upscaling**
- **CLI-based, lightweight, and fast**
- **Ideal for SDXL and image-to-image workflows**

---

## 🛠 Requirements

- Python 3.6+
- NumPy (`pip install numpy`)

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/image-scaling-tool.git
cd image-scaling-tool
pip install numpy
```

---

## 📌 Usage

```bash
python image_scaling_tool.py WIDTH HEIGHT --max MAX_SIZE --mode [downscale|upscale]
```

### Examples

**Downscale a large image to fit within 1024×1024:**
```bash
python image_scaling_tool.py 2048 1152 --max 1024 --mode downscale
```

**Upscale a small image to fit closer to 2048×2048:**
```bash
python image_scaling_tool.py 512 288 --max 2048 --mode upscale
```

---

## 📎 Output

The tool prints a list of possible width × height pairs and their corresponding scale factors that will preserve the original image's aspect ratio.

---

## 📌 Use Cases

- Scaling reference or generated images in AI art creation
- Avoiding memory crashes in GPU-constrained environments
- Preparing batches of images for consistent resolution output

---

## 📈 Planned Features

- GUI version (Tkinter or PyQt)
- JSON/CSV output
- Integration with image processing (Pillow)
- Web-based drag-and-drop tool

---

## 📃 License

Open source. License to be defined in the repository.

---

## 💌 Contact

**Author:** devall6@yahoo.com

Enjoy creating! 🎨

