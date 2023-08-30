import os

def generate_image_markdown(num_cols, image_dir):
    # Initialize the markdown string with table header
    markdown = f"|{' |'.join([''] * num_cols)} |\n"
    markdown += f"|{' |'.join(['-------'] * num_cols)} |\n"

    # Get a sorted list of image files in the directory
    images = sorted(os.listdir(image_dir))
    num_images = len(images)

    # Calculate the number of rows needed for the table
    num_rows = (num_images + num_cols - 1) // num_cols

    # Populate the table with image links using a ternary operator
    markdown += "".join(
        f"| ![Image]({image_dir}/{images[i * num_cols + j]}) |" if i * num_cols + j < num_images
        else " |"
        for i in range(num_rows)
        for j in range(num_cols)
    ) + "\n"

    return markdown

if __name__ == "__main__":
    num_cols = 4
    image_dir = "pcb_images"
    markdown = generate_image_markdown(num_cols, image_dir)

    # Read the existing README.md
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Find the start and end markers for the pictures section
    start_marker = "## Pictures"
    end_marker = "|  |  |  |  |"

    # Replace the existing pictures section with the updated one
    new_readme_content = re.sub(
        f"{start_marker}.*?{end_marker}",
        f"{start_marker}\n\n{markdown}\n\n{end_marker}",
        readme_content,
        flags=re.DOTALL,
    )

    # Update the README.md file
    with open("README.md", "w") as f:
        f.write(new_readme_content)
