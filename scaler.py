"""
Author: devall6@yahoo.com
Version: 1.0

Description:
This standalone Python3 program allows you to calculate scaling options for images used in AI art creation. 
It supports both downscaling and upscaling while preserving the original aspect ratio. The primary use case 
is for optimizing image dimensions to avoid VRAM overflow or to upscale smaller inputs within acceptable limits 
of Stable Diffusion models such as SDXL.

Algorithm:
1. Accept input image dimensions and mode (downscale/upscale).
2. Calculate the aspect ratio.
3. Based on the mode:
   - Downscale: compute scale factors to reduce size within max bounds.
   - Upscale: compute scale factors to enlarge image without exceeding bounds.
4. Output a list of valid width, height, and scale factor combinations.

How to Use:
1. Save the script as `image_scaling_tool.py`.
2. Open a terminal or command prompt.
3. Run the script using Python with the required arguments:

   Example (Downscale):
   python image_scaling_tool.py 2048 1152 --max 1024 --mode downscale

   Example (Upscale):
   python image_scaling_tool.py 512 288 --max 2048 --mode upscale

4. The output will display a list of scaled width x height pairs and their corresponding scale factors.
"""

def calculate_scaling_options(original_width: int, original_height: int, max_size: int = 1024, mode: str = "downscale"):
    """
    Calculates a list of scaling options for a given image size that maintain
    the aspect ratio and either upscale or downscale to fit within the max_size.

    Args:
        original_width (int): Original width of the image.
        original_height (int): Original height of the image.
        max_size (int): The maximum size for width or height.
        mode (str): 'downscale' to reduce size, 'upscale' to increase size.

    Returns:
        aspect_ratio (float): The width/height ratio.
        options (list): List of tuples with (width, height, scale_factor)
    """
    aspect_ratio = original_width / original_height

    if mode == "downscale":
        width_scale = max_size / original_width
        height_scale = max_size / original_height
        max_scale = min(width_scale, height_scale)
        scales = [round(s, 3) for s in list(np.arange(0.1, max_scale + 0.05, 0.05)) if s <= max_scale]
    elif mode == "upscale":
        width_scale = max_size / original_width
        height_scale = max_size / original_height
        min_scale = max(width_scale, height_scale)
        scales = [round(s, 3) for s in list(np.arange(min_scale, min_scale + 2.0, 0.1))]
    else:
        raise ValueError("Mode must be 'downscale' or 'upscale'")

    # Calculate new dimensions for each scale
    scaled_sizes = [
        (int(original_width * s), int(original_height * s), s) for s in scales
    ]

    return aspect_ratio, scaled_sizes


if __name__ == "__main__":
    import argparse
    import numpy as np

    parser = argparse.ArgumentParser(description="Scale image dimensions to fit within max resolution.")
    parser.add_argument("width", type=int, help="Original image width")
    parser.add_argument("height", type=int, help="Original image height")
    parser.add_argument("--max", type=int, default=1024, help="Maximum size for width or height (default: 1024)")
    parser.add_argument("--mode", choices=["downscale", "upscale"], default="downscale", help="Choose to downscale or upscale the image")

    args = parser.parse_args()

    aspect_ratio, options = calculate_scaling_options(args.width, args.height, args.max, args.mode)

    print(f"Original Aspect Ratio: {aspect_ratio:.3f} (Width:Height)")
    print(f"\nScaling options ({args.mode}) that fit within {args.max}x{args.max}:")
    print("Width x Height | Scale Factor")
    print("-----------------------------")
    for w, h, s in options:
        print(f"{w} x {h}      | {s:.3f}")

