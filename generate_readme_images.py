import os
import re

# === Configurable Parameters ===
image_dir = "pcb_images"
readme_path = "README.md"
start_marker = "<!-- START IMAGES -->"
end_marker = "<!-- END IMAGES -->"
num_cols = 5  # Number of columns per row in the table

# === Helper: Generate Markdown Table ===
def generate_markdown_table(images, num_cols):
    markdown = "| " + " | ".join([""] * num_cols) + " |\n"
    markdown += "| " + " | ".join(["-------"] * num_cols) + " |\n"

    for i in range(0, len(images), num_cols):
        row = images[i:i+num_cols]
        markdown += "| " + " | ".join(
            [f"<img src='{image_dir}/{img}' width='300' />" for img in row]
        ) + " |\n"
    return markdown

# === Main Update Function ===
def update_readme_with_images():
    # Get image files
    images = sorted([
        f for f in os.listdir(image_dir)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ])

    # Generate image Markdown table
    markdown_table = generate_markdown_table(images, num_cols)

    # Load README.md
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the image section using regex
    pattern = f"{start_marker}.*?{end_marker}"
    new_section = f"{start_marker}\n{markdown_table}\n{end_marker}"
    updated_content = re.sub(pattern, new_section, content, flags=re.DOTALL)

    # Write back to README.md
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

# === Run If Executed Directly ===
if __name__ == "__main__":
    update_readme_with_images()
    print("✅ README.md image gallery updated successfully.")
