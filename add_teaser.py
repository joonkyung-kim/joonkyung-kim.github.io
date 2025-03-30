import os
import frontmatter

PUBLICATION_DIR = "_publications"
DEFAULT_TEASER_PATH = "/images/default-thumbnail.png"


def add_teaser_to_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)

    header = post.get("header", {})
    teaser_exists = isinstance(header, dict) and "teaser" in header

    if not teaser_exists:
        post.metadata["header"] = {"teaser": DEFAULT_TEASER_PATH}
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))
        print(f"✅ teaser 추가됨: {os.path.basename(filepath)}")
    else:
        print(f"➖ 이미 있음: {os.path.basename(filepath)}")


for filename in os.listdir(PUBLICATION_DIR):
    if filename.endswith(".md"):
        add_teaser_to_file(os.path.join(PUBLICATION_DIR, filename))
