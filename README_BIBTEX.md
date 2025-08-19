# BibTeX to Publications Converter

This directory contains a tool to automatically convert BibTeX entries to Jekyll markdown files for your academic website.

## Features

- **No external dependencies** - uses only Python standard library
- **Automatic categorization** - detects conferences, journals, and manuscripts
- **URL extraction** - supports paper, video, and code links
- **Chronological ordering** - publications are displayed by date
- **Clean formatting** - matches your existing publication style

## Usage

1. **Create your BibTeX file** with your publications:

```bibtex
@inproceedings{your2024paper,
  title={Your Paper Title},
  author={Your Name and Coauthor Name},
  booktitle={Conference Name},
  year={2024},
  month={June},
  url={https://link-to-paper.com},
  video={https://youtube.com/your-video},
  code={https://github.com/your-repo},
  abstract={Brief description of your work.}
}
```

2. **Run the converter**:

```bash
cd markdown_generator
python3 simple_bibtex_converter.py your_publications.bib
```

This will create markdown files in `_publications/` directory.

## Supported BibTeX Fields

### Required Fields
- `title` - Paper title
- `year` - Publication year
- `author` - Author names

### Optional Fields
- `booktitle` - Conference name (for conferences)
- `journal` - Journal name (for journal articles)
- `month` - Publication month
- `day` - Publication day
- `url` - Link to paper (creates "Paper" button)
- `doi` - DOI (automatically creates paper link)
- `video` - Video link (creates "Video" button)
- `code` - Code repository link (creates "Code" button)
- `github` - GitHub repository (alternative to code)
- `abstract` - Paper abstract
- `note` - Additional notes

## Entry Types

The converter automatically categorizes publications:

- **Conferences**: `@inproceedings`, `@conference`, or venues containing "conference", "proceedings", "workshop", "symposium"
- **Journals**: `@article`, `@journal`, or venues containing "journal", "transactions", "letters"
- **Manuscripts**: `@misc`, entries with "arxiv", "preprint", "submitted", "under review" in venue

## Output Format

Generated files follow this structure:

```yaml
---
title: "Paper Title"
collection: publications
category: conferences
date: 2024-06-01
permalink: /publication/paper-slug
authors: Author Name, Coauthor Name
venue: Conference/Journal Name
buttons:
  - type: paper
    url: https://link-to-paper.com
  - type: video
    url: https://video-link.com
---

Abstract or description text here.
```

## Updated Publications Page

The publications page now displays all papers chronologically without category sections. Papers are sorted by date (newest first) and include all the same styling and buttons as before.

## Tips

- Include abstracts for better paper descriptions
- Use consistent author name formatting
- Add video and code links when available
- The tool handles month names (e.g., "June") and converts them to numbers
- Long titles are automatically truncated for URL slugs