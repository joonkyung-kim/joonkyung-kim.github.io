import os
import frontmatter

PUBLICATION_DIR = "_publications"
DEFAULT_CATEGORY = "manuscripts"


def add_category_to_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)

    if "category" not in post.metadata:
        post.metadata["category"] = DEFAULT_CATEGORY
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))
        print(f"✅ category 추가됨: {os.path.basename(filepath)}")
    else:
        print(f"➖ 이미 있음: {os.path.basename(filepath)}")


def main():
    for filename in os.listdir(PUBLICATION_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(PUBLICATION_DIR, filename)
            add_category_to_file(filepath)


if __name__ == "__main__":
    main()
