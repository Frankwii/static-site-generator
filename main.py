from src.markdown_parser import markdown_to_html
import os
import logging
from copystatic import copystatic

logging.basicConfig(filename="LOG-main", level=logging.INFO)
logger=logging.getLogger(__name__)

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise ValueError("No title for the markdown file")

    firstline=markdown.splitlines()[0]

    return firstline.split("# ",1)[1].strip(" \t\n")

def generate_page(from_path,template_path,dest_path):
    logger.info(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as markdown_file:
        markdown=markdown_file.read()

    with open(template_path, 'r') as template_file:
        template=template_file.read()

    html_content=markdown_to_html(markdown)
    title=extract_title(markdown)

    html=template.replace("{{ Title }}",title).replace("{{ Content }}",html_content)

    dest_dir=os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as html_file:
        html_file.write(html)

if __name__=="__main__":
    copystatic()
    generate_page(from_path="content/index.md",dest_path="public/index.html",template_path="template.html")
