import os

def generate_image_markdown(num_cols, dir):
    markdown = "|"
    for i in range(num_cols):
        markdown += f"  |"
    markdown += "\n"
    markdown += "|"
    for i in range(num_cols):
        markdown += " ------- |"
    markdown += "\n"
    images = sorted(os.listdir(dir))
    num_images = len(images)
    num_rows = num_images // num_cols
    if num_images % num_cols != 0:
        num_rows += 1
    for i in range(num_rows):
        markdown += "|"
        for j in range(num_cols):
            index = i * num_cols + j
            if index < num_images:
                image = images[index]
                markdown += f" <img src='{dir}/{image}' width='300' /> |"
            else:
                markdown += " |"
        markdown += "\n"
    return markdown

if __name__ == "__main__":
    num_cols = 4
    dir = "pcb_images"
    markdown = generate_image_markdown(num_cols, dir)
    with open("test.md", "w") as f:
        f.write(f"# My Project\n\n{markdown}")
