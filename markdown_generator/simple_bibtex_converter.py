#!/usr/bin/env python3
"""
Simple BibTeX to Publications Converter (No External Dependencies)

This script converts BibTeX entries to Jekyll markdown files without requiring pybtex.
It uses basic string parsing to extract publication information.

Usage:
    python3 simple_bibtex_converter.py your_publications.bib
"""

import argparse
import os
import re
import sys
from pathlib import Path

def parse_bibtex_entry(entry_text):
    """Parse a single BibTeX entry using basic string operations"""
    entry = {}
    
    # Extract entry type and key
    type_match = re.match(r'@(\w+)\{([^,]+),', entry_text)
    if type_match:
        entry['type'] = type_match.group(1).lower()
        entry['key'] = type_match.group(2).strip()
    
    # Extract fields - improved regex to handle nested braces better
    field_pattern = r'(\w+)\s*=\s*[{"]([^{}]*(?:\{[^{}]*\}[^{}]*)*)[}"]'
    
    for match in re.finditer(field_pattern, entry_text, re.DOTALL):
        field_name = match.group(1).lower()
        field_value = match.group(2).strip()
        # Clean up the field value
        field_value = re.sub(r'\s+', ' ', field_value)  # Normalize whitespace
        entry[field_name] = field_value
    
    return entry

def parse_bibtex_file(file_path):
    """Parse BibTeX file and return list of entries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into individual entries
    entries = []
    entry_pattern = r'@\w+\{[^@]*(?=@|\Z)'
    
    for match in re.finditer(entry_pattern, content, re.DOTALL):
        entry_text = match.group(0)
        entry = parse_bibtex_entry(entry_text)
        if entry:
            entries.append(entry)
    
    return entries

def clean_string(text):
    """Clean text for YAML output"""
    if not text:
        return ""
    # Remove extra braces and clean up formatting
    cleaned = text.replace('{}', '').replace('\\', '')
    # Escape quotes for YAML
    cleaned = cleaned.replace('"', '\\"')
    return cleaned.strip()

def create_url_slug(title):
    """Create URL-friendly slug from title"""
    # Remove special characters and convert to lowercase
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces and multiple dashes with single dash
    slug = re.sub(r'[-\s]+', '-', slug)
    # Limit length to avoid filesystem issues
    slug = slug[:50]  # Keep it reasonable length
    return slug.strip('-')

def determine_category(entry_type, venue):
    """Determine publication category"""
    entry_type = entry_type.lower()
    venue_lower = venue.lower() if venue else ""
    
    # Check for preprint indicators
    preprint_indicators = ['arxiv', 'preprint', 'submitted', 'under review']
    if any(indicator in venue_lower for indicator in preprint_indicators):
        return 'manuscripts'
    
    # Check entry type
    if entry_type in ['inproceedings', 'conference']:
        return 'conferences'
    elif entry_type in ['article', 'journal']:
        return 'journals'
    else:
        # Default based on venue keywords
        conference_keywords = ['conference', 'proceedings', 'workshop', 'symposium']
        journal_keywords = ['journal', 'transactions', 'letters']
        
        if any(keyword in venue_lower for keyword in conference_keywords):
            return 'conferences'
        elif any(keyword in venue_lower for keyword in journal_keywords):
            return 'journals'
        else:
            return 'manuscripts'

def extract_date_info(entry):
    """Extract date from entry"""
    year = entry.get('year', '2024')
    month = entry.get('month', '01')
    
    # Convert month names to numbers
    if month and len(month) > 2:
        month_map = {
            'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04',
            'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
            'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12',
            'january': '01', 'february': '02', 'march': '03', 'april': '04',
            'june': '06', 'july': '07', 'august': '08', 'september': '09',
            'october': '10', 'november': '11', 'december': '12'
        }
        month = month_map.get(month.lower(), '01')
    elif month and len(month) == 1:
        month = f"0{month}"
    
    day = entry.get('day', '01')
    if day and len(day) == 1:
        day = f"0{day}"
    
    return f"{year}-{month}-{day}"

def extract_venue(entry):
    """Extract venue from entry"""
    entry_type = entry.get('type', '')
    
    if entry_type in ['inproceedings', 'conference']:
        venue = entry.get('booktitle', '')
    elif entry_type in ['article', 'journal']:
        venue = entry.get('journal', '')
    else:
        venue = (entry.get('booktitle', '') or 
                entry.get('journal', '') or 
                entry.get('venue', '') or 
                entry.get('publisher', ''))
    
    return clean_string(venue)

def extract_urls(entry):
    """Extract URL information from entry"""
    buttons = []
    
    # Paper URL
    paper_url = entry.get('url', '') or entry.get('doi', '')
    if paper_url:
        if paper_url.startswith('10.'):  # DOI
            paper_url = f"https://doi.org/{paper_url}"
        buttons.append({
            'type': 'paper',
            'url': paper_url
        })
    
    # Video URL
    video_url = entry.get('video', '')
    if video_url:
        buttons.append({
            'type': 'video',
            'url': video_url
        })
    
    # Code URL
    code_url = entry.get('code', '') or entry.get('github', '')
    if code_url:
        buttons.append({
            'type': 'code',
            'url': code_url
        })
    
    return buttons

def convert_bibtex_to_markdown(bib_file_path, output_dir):
    """Convert BibTeX file to Jekyll markdown files"""
    
    # Parse BibTeX file
    try:
        entries = parse_bibtex_file(bib_file_path)
    except Exception as e:
        print(f"Error parsing BibTeX file: {e}")
        return
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    successful_conversions = 0
    
    # Process each entry
    for entry in entries:
        try:
            # Extract basic information
            title = clean_string(entry.get('title', ''))
            if not title:
                print(f"Warning: No title found for entry {entry.get('key', 'unknown')}, skipping...")
                continue
            
            author = clean_string(entry.get('author', ''))
            venue = extract_venue(entry)
            date = extract_date_info(entry)
            category = determine_category(entry.get('type', ''), venue)
            
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
            if author:
                md_content.append(f"authors: {author}")
            
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
            abstract = clean_string(entry.get('abstract', ''))
            note = clean_string(entry.get('note', ''))
            
            if abstract:
                md_content.append(abstract)
            elif note:
                md_content.append(note)
            
            # Write to file
            output_file = output_path / filename
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(md_content))
            
            print(f"✓ Created: {filename} ({category})")
            successful_conversions += 1
            
        except Exception as e:
            print(f"Error processing entry {entry.get('key', 'unknown')}: {e}")
            continue
    
    print(f"\nSuccessfully converted {successful_conversions} publications!")
    print(f"Files saved to: {output_path}")

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert BibTeX entries to Jekyll markdown files for Academic Pages'
    )
    parser.add_argument('bibtex_file', help='Path to BibTeX file')
    parser.add_argument(
        '--output', '-o', 
        default='../_publications/',
        help='Output directory for markdown files (default: ../_publications/)'
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