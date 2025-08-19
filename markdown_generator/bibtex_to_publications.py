#!/usr/bin/env python3
"""
BibTeX to Publications Converter for Academic Pages

This script converts BibTeX entries to Jekyll markdown files for academic websites.
It creates publication entries that match your existing format and supports chronological ordering.

Usage:
    python bibtex_to_publications.py your_publications.bib
"""

import argparse
import os
import re
import sys
from pathlib import Path
from datetime import datetime

try:
    from pybtex.database.input import bibtex
    from pybtex.database import BibliographyData
except ImportError:
    print("Error: pybtex library not found. Install with: pip install pybtex")
    sys.exit(1)


def clean_string(text):
    """Clean BibTeX strings by removing braces and escaping quotes"""
    if not text:
        return ""
    # Remove braces and clean up formatting
    cleaned = text.replace("{", "").replace("}", "").replace("\\", "")
    # Escape quotes for YAML
    cleaned = cleaned.replace('"', '\\"')
    return cleaned.strip()


def create_url_slug(title):
    """Create URL-friendly slug from title"""
    # Remove special characters and convert to lowercase
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    # Replace spaces and multiple dashes with single dash
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def determine_category(entry_type, venue):
    """Determine publication category based on entry type and venue"""
    entry_type = entry_type.lower()
    venue_lower = venue.lower() if venue else ""

    # Check for preprint indicators
    preprint_indicators = ["arxiv", "preprint", "submitted", "under review"]
    if any(indicator in venue_lower for indicator in preprint_indicators):
        return "manuscripts"

    # Check entry type
    if entry_type in ["inproceedings", "conference"]:
        return "conferences"
    elif entry_type in ["article", "journal"]:
        return "journals"
    else:
        # Default based on venue keywords
        conference_keywords = ["conference", "proceedings", "workshop", "symposium"]
        journal_keywords = ["journal", "transactions", "letters"]

        if any(keyword in venue_lower for keyword in conference_keywords):
            return "conferences"
        elif any(keyword in venue_lower for keyword in journal_keywords):
            return "journals"
        else:
            return "manuscripts"  # Default to manuscripts


def extract_date_info(entry):
    """Extract date information from BibTeX entry"""
    fields = entry.fields

    # Get year
    year = fields.get("year", "2024")

    # Get month (convert month names to numbers)
    month = fields.get("month", "01")
    if month and len(month) > 2:
        month_map = {
            "jan": "01",
            "feb": "02",
            "mar": "03",
            "apr": "04",
            "may": "05",
            "jun": "06",
            "jul": "07",
            "aug": "08",
            "sep": "09",
            "oct": "10",
            "nov": "11",
            "dec": "12",
        }
        month = month_map.get(month.lower()[:3], "01")
    elif month and len(month) == 1:
        month = f"0{month}"

    # Get day
    day = fields.get("day", "01")
    if day and len(day) == 1:
        day = f"0{day}"

    return f"{year}-{month}-{day}"


def extract_authors(entry):
    """Extract author names from BibTeX entry"""
    if "author" not in entry.persons:
        return ""

    authors = []
    for person in entry.persons["author"]:
        # Get first names (including middle initials)
        first_names = " ".join(person.first_names)
        # Get last names
        last_names = " ".join(person.last_names)
        authors.append(f"{first_names} {last_names}".strip())

    return ", ".join(authors)


def extract_venue(entry):
    """Extract venue information from BibTeX entry"""
    fields = entry.fields
    entry_type = entry.original_type

    # Try different venue fields based on entry type
    if entry_type.lower() in ["inproceedings", "conference"]:
        venue = fields.get("booktitle", "")
    elif entry_type.lower() in ["article", "journal"]:
        venue = fields.get("journal", "")
    else:
        # Try multiple fields
        venue = (
            fields.get("booktitle", "")
            or fields.get("journal", "")
            or fields.get("venue", "")
            or fields.get("publisher", "")
        )

    return clean_string(venue)


def extract_urls(entry):
    """Extract URL information from BibTeX entry"""
    fields = entry.fields
    buttons = []

    # Paper URL
    paper_url = fields.get("url", "") or fields.get("doi", "")
    if paper_url:
        if paper_url.startswith("10."):  # DOI
            paper_url = f"https://doi.org/{paper_url}"
        buttons.append({"type": "paper", "url": paper_url})

    # Video URL
    video_url = fields.get("video", "")
    if video_url:
        buttons.append({"type": "video", "url": video_url})

    # Code URL
    code_url = fields.get("code", "") or fields.get("github", "")
    if code_url:
        buttons.append({"type": "code", "url": code_url})

    return buttons


def convert_bibtex_to_markdown(bib_file_path, output_dir):
    """Convert BibTeX file to Jekyll markdown files"""

    # Parse BibTeX file
    parser = bibtex.Parser()
    try:
        bib_data = parser.parse_file(bib_file_path)
    except Exception as e:
        print(f"Error parsing BibTeX file: {e}")
        return

    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    successful_conversions = 0

    # Process each entry
    for bib_id, entry in bib_data.entries.items():
        try:
            fields = entry.fields

            # Extract basic information
            title = clean_string(fields.get("title", ""))
            if not title:
                print(f"Warning: No title found for entry {bib_id}, skipping...")
                continue

            authors = extract_authors(entry)
            venue = extract_venue(entry)
            date = extract_date_info(entry)
            category = determine_category(entry.original_type, venue)

            # Create URL slug and filename
            url_slug = create_url_slug(title)
            filename = f"{date}-{url_slug}.md"

            # Extract URLs
            buttons = extract_urls(entry)

            # Build markdown content
            md_content = []
            md_content.append("---")
            md_content.append(f'title: "{title}"')
            md_content.append("collection: publications")
            md_content.append(f"category: {category}")
            md_content.append(f"date: {date}")
            md_content.append(f"permalink: /publication/{url_slug}")

            # Add authors if available
            if authors:
                md_content.append(f"authors: {authors}")

            # Add venue if available
            if venue:
                md_content.append(f"venue: {venue}")

            # Add buttons if available
            if buttons:
                md_content.append("buttons:")
                for button in buttons:
                    md_content.append(f"  - type: {button['type']}")
                    md_content.append(f"    url: {button['url']}")

            md_content.append("---")
            md_content.append("")

            # Add abstract or note if available
            abstract = clean_string(fields.get("abstract", ""))
            note = clean_string(fields.get("note", ""))

            if abstract:
                md_content.append(abstract)
            elif note:
                md_content.append(note)

            # Write to file
            output_file = output_path / filename
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(md_content))

            print(f"✓ Created: {filename} ({category})")
            successful_conversions += 1

        except Exception as e:
            print(f"Error processing entry {bib_id}: {e}")
            continue

    print(f"\nSuccessfully converted {successful_conversions} publications!")
    print(f"Files saved to: {output_path}")


def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(
        description="Convert BibTeX entries to Jekyll markdown files for Academic Pages"
    )
    parser.add_argument("bibtex_file", help="Path to BibTeX file")
    parser.add_argument(
        "--output",
        "-o",
        default="../_publications/",
        help="Output directory for markdown files (default: ../_publications/)",
    )

    args = parser.parse_args()

    # Check if BibTeX file exists
    if not os.path.exists(args.bibtex_file):
        print(f"Error: BibTeX file '{args.bibtex_file}' not found")
        sys.exit(1)

    print(f"Converting {args.bibtex_file} to Jekyll markdown files...")
    convert_bibtex_to_markdown(args.bibtex_file, args.output)


if __name__ == "__main__":
    main()
