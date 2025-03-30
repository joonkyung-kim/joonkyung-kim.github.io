import pandas as pd
import os
import frontmatter

# 경로 설정
TSV_FILE = "publications.tsv"
OUTPUT_DIR = "../_publications"
DEFAULT_THUMBNAIL = "/images/default-thumbnail.png"

# 필요한 열: pub_date, title, authors, venue, url_slug, paper_url, video_url, code_url, image_path, category
df = pd.read_csv(TSV_FILE, sep="\t")


def to_button_list(row):
    buttons = []
    if pd.notna(row.get("paper_url")):
        buttons.append({"type": "paper", "url": row["paper_url"]})
    if pd.notna(row.get("video_url")):
        buttons.append({"type": "video", "url": row["video_url"]})
    if pd.notna(row.get("code_url")):
        buttons.append({"type": "code", "url": row["code_url"]})
    return buttons


for idx, row in df.iterrows():
    md = frontmatter.Post("")
    slug = row["url_slug"]
    date = row["pub_date"]
    filename = f"{date}-{slug}.md"

    md["title"] = row["title"]
    md["collection"] = "publications"
    md["category"] = row.get("category", "conferences")
    md["date"] = date
    md["permalink"] = f"/publication/{slug}"
    md["authors"] = row["authors"]
    md["venue"] = row["venue"]

    md["header"] = {"teaser": row.get("image_path", DEFAULT_THUMBNAIL)}

    buttons = to_button_list(row)
    if buttons:
        md["buttons"] = buttons

    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(md))
        print(f"✅ 생성됨: {filename}")
