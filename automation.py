import os
import re

# Path to the directory containing your images
image_dir = "pcb_images"

# Function to update the README.md with new images
def update_readme_with_images():
    # Get a list of image files in the directory
    images = sorted([f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])

    # Generate the Markdown table for the images
    markdown_images = "\n".join([f"| <img src='{image_dir}/{image}' width='300' />" for image in images])

    # Read the existing README.md
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Find the start and end markers for the pictures section
    start_marker = "## Pictures"
    end_marker = "|  |  |  |  |"

    # Replace the existing pictures section with the updated one
    new_readme_content = re.sub(
        f"{start_marker}.*?{end_marker}",
        f"{start_marker}\n\n{markdown_images}\n\n{end_marker}",
        readme_content,
        flags=re.DOTALL,
    )

    # Update the README.md file
    with open("README.md", "w") as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    update_readme_with_images()
