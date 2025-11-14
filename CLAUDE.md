# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based academic website using the Academic Pages template, designed for showcasing research publications, projects, and academic CV. The site is hosted on GitHub Pages.

## Build & Development Commands

### Local Development
```bash
# Install Ruby dependencies (first time setup)
bundle install

# Serve locally with live reload
jekyll serve -l -H localhost
# Or alternatively:
bundle exec jekyll serve --host 0.0.0.0 --watch

# Access at: http://localhost:4000
```

Note: Configuration changes in [_config.yml](_config.yml) require server restart.

### Docker Development
```bash
# Build container
docker build -t jekyll-site .

# Run container
docker run -p 4000:4000 --rm -v $(pwd):/usr/src/app jekyll-site
```

### JavaScript/Assets
```bash
# Install Node dependencies (first time)
npm install

# Uglify and minify JavaScript assets
npm run build:js

# Watch for changes and rebuild automatically
npm run watch:js
```

## Site Architecture

### Jekyll Configuration
- **Main config**: [_config.yml](_config.yml) - Controls site-wide settings, collections, author profile, and publication categories
- **Navigation**: [_data/navigation.yml](_data/navigation.yml) - Header menu configuration
- **Base URL**: `https://joonkyung-kim.github.io`
- **Markdown processor**: kramdown (GitHub Pages compatible)

### Content Collections
The site uses Jekyll collections with specific frontmatter structures:

#### Publications (`_publications/`)
- **Required fields**:
  - `title` - Publication title
  - `collection: publications`
  - `category` - One of: `manuscripts`, `conferences`, `journals`
  - `date` - Publication date (YYYY-MM-DD format)
  - `permalink` - URL path (e.g., `/publication/paper-slug`)
- **Optional fields**:
  - `header.teaser` - Thumbnail image path (defaults to `/images/default-thumbnail.png`)
  - `authors` - Author list
  - `venue` - Conference/journal name
  - `buttons` - Array of action buttons with `type` (paper/video/code) and `url`

#### Projects (`_projects/`)
- **Required fields**: `title`, `collection: projects`, `date`, `permalink`
- **Optional fields**: `excerpt`, `image.feature`, `links`

#### Pages (`_pages/`)
- Static pages: [about.md](_pages/about.md), [cv.md](_pages/cv.md), etc.
- Use `permalink` for custom URLs
- Control visibility via frontmatter

### Custom Components
- **Publication cards**: [_includes/custom-publication.html](_includes/custom-publication.html) - Custom layout for publication listings with thumbnails and action buttons
- **Author profile**: Configured in [_config.yml](_config.yml) under `author:` section
- **Publication categories**: Defined in [_config.yml](_config.yml) under `publication_category:` section

## Python Utility Scripts

### BibTeX to Markdown Converter
Convert BibTeX entries to Jekyll markdown files for publications:

```bash
cd markdown_generator
python3 simple_bibtex_converter.py path/to/your_publications.bib
```

**Features**:
- No external dependencies (uses only Python standard library)
- Automatic categorization (conferences, journals, manuscripts)
- Extracts paper/video/code URLs from BibTeX fields
- Creates properly formatted markdown files in `_publications/`

**Supported BibTeX fields**: `title`, `author`, `year`, `month`, `day`, `booktitle`, `journal`, `url`, `doi`, `video`, `code`, `github`, `abstract`, `note`

See [README_BIBTEX.md](README_BIBTEX.md) for detailed BibTeX conversion documentation.

### Publication Frontmatter Management
Two utility scripts for bulk-updating publication frontmatter:

```bash
# Add default category field to all publications missing it
python3 add_category.py

# Add default teaser image to all publications missing it
python3 add_teaser.py
```

Both scripts use the `python-frontmatter` library and modify files in `_publications/` directory.

### TSV-based Generators
Alternative method using TSV files (located in `markdown_generator/`):

```bash
# Generate publications from TSV
python3 markdown_generator/publications.py

# Generate talks from TSV
python3 markdown_generator/talks.py
```

These scripts require properly formatted TSV files with columns like `pub_date`, `title`, `venue`, `excerpt`, `citation`, `site_url`, `paper_url`.

## File Organization

### Assets
- **Images**: [/images/](/images/) - Profile photos, publication figures, project thumbnails
- **Files**: [/files/](/files/) - PDFs (CV, papers) accessible at `/files/filename.pdf`
- **Styles**: [_sass/](_sass/) - SCSS files for styling
- **JavaScript**: [assets/js/](assets/js/) - Site functionality (minified to `main.min.js`)

### Key Directories
```
_includes/          # Reusable template components
_layouts/           # Page layout templates
_sass/              # Styling (SCSS)
_site/              # Generated site (auto-generated, do not edit manually)
_data/              # Site data (navigation, UI text)
markdown_generator/ # Python scripts for content generation
vendor/             # Ruby gems (bundler install location)
```

## Development Workflow

1. **Add Publications**:
   - **Option A** (Recommended): Create `.bib` file and run `simple_bibtex_converter.py`
   - **Option B**: Manually create markdown files in `_publications/` with required frontmatter
   - Run `add_category.py` and `add_teaser.py` to ensure consistent frontmatter

2. **Update Content**: Edit markdown files in `_publications/`, `_projects/`, `_pages/`

3. **Change Site Settings**: Modify [_config.yml](_config.yml) and restart Jekyll server

4. **Update Navigation**: Edit [_data/navigation.yml](_data/navigation.yml)

5. **Style Changes**: Edit SCSS files in [_sass/](_sass/) directory

6. **JavaScript Changes**:
   - Edit source files in [assets/js/](assets/js/)
   - Run `npm run build:js` to regenerate minified bundle
   - Use `npm run watch:js` during development

7. **Test Locally**: Use `jekyll serve -l -H localhost` before deploying

8. **Deploy**: Push to GitHub - site auto-builds via GitHub Pages

## Important Notes

- The `_site/` directory is auto-generated by Jekyll - never edit files there directly
- Configuration changes in [_config.yml](_config.yml) require server restart
- Images should be optimized before adding to `/images/`
- PDF files go in `/files/` directory
- The site must maintain GitHub Pages compatibility (uses `github-pages` gem)
- Publication categories are configured globally in [_config.yml](_config.yml) under `publication_category:`
