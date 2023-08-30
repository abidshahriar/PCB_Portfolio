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
        f"| ![Image](/{image_dir}/{images[i * num_cols + j]}) |" if i * num_cols + j < num_images
        else " |"
        for i in range(num_rows)
        for j in range(num_cols)
    ) + "\n"

    return markdown

if __name__ == "__main__":
    num_cols = 4
    image_dir = "pcb_images"
    markdown = generate_image_markdown(num_cols, image_dir)

    # Write the markdown to a file
    with open("test.md", "w") as f:
        f.write(f"# My Project\n\n{markdown}")
