---
permalink: /
title: "Hello, I'm Joonkyung Kim!"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<!-- This is the front page of a website that is powered by the [Academic Pages template](https://github.com/academicpages/academicpages.github.io) and hosted on GitHub pages. [GitHub pages](https://pages.github.com) is a free service in which websites are built and hosted from code and data stored in a GitHub repository, automatically updating when a new commit is made to the respository. This template was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) created by Michael Rose, and then extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this repository](https://github.com/academicpages/academicpages.github.io) right now, modify the configuration and markdown files, add your own PDFs and other content, and have your own site for free, with no ads! An older version of this template powers my own personal website at [stuartgeiger.com](http://stuartgeiger.com), which uses [this Github repository](https://github.com/staeiou/staeiou.github.io). -->

<div style="margin: 2rem 0;">
  <div style="font-size: 0.95em;">
    <p style="margin-top: 0;">I am a Ph.D. student in Computer Science and Engineering at Texas A&M University, advised by Prof. <a href="https://yiweilyu-tamu.github.io/homepage/" style="color: #324aa8; text-decoration: underline; text-decoration-style: dotted; text-decoration-thickness: 1px; text-underline-offset: 3px;">Yiwei Lyu</a>. I received my B.S. and M.S. degrees in Electronic Engineering from Sogang University, where I worked at the <a href="https://airobotics.sogang.ac.kr/" style="color: #324aa8; text-decoration: underline; text-decoration-style: dotted; text-decoration-thickness: 1px; text-underline-offset: 3px;">AI Robotics Lab</a> under Prof. <a href="https://sites.google.com/site/changjoonam/" style="color: #324aa8; text-decoration: underline; text-decoration-style: dotted; text-decoration-thickness: 1px; text-underline-offset: 3px;">Changjoo Nam</a>. From Aug. 2024 to Feb. 2025, I was a Visiting Scholar at Carnegie Mellon University.</p>

    <p>I work on <strong>safety in multi-agent robotic systems</strong> — developing control-theoretic methods that enable heterogeneous robots and humans to safely interact and cooperate in shared environments. More broadly, I study expanded notions of robotics safety beyond physical constraints, including semantic, decision-level, and human-centered safety for AI-enabled robotic systems.</p>

    <!-- Research Interests -->
    <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 1rem 0;">
      {% assign interests = "Multi-Robot Systems|Safety Control|Safe AI for Robotics|Human-Robot Interaction" | split: "|" %}
      {% for interest in interests %}
        <span style="background-color: #eef2f7; color: #2c3e50; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.8em; font-weight: 500; border: 1px solid #d8dee6;">{{ interest }}</span>
      {% endfor %}
    </div>

    <!-- Contact row -->
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; font-size: 0.95em;">
      <a href="mailto:joonkyung@tamu.edu" style="text-decoration: none; color: #444;" title="Email"><i class="fas fa-envelope"></i> Email</a>
      <a href="https://scholar.google.com/citations?user=_Bamlg4AAAAJ&hl=en" target="_blank" style="text-decoration: none; color: #444;" title="Google Scholar"><i class="ai ai-google-scholar"></i> Scholar</a>
      <a href="https://github.com/joonkyung-kim" target="_blank" style="text-decoration: none; color: #444;" title="GitHub"><i class="fab fa-github"></i> GitHub</a>
      <a href="https://www.linkedin.com/in/joonkyung-kim" target="_blank" style="text-decoration: none; color: #444;" title="LinkedIn"><i class="fab fa-linkedin"></i> LinkedIn</a>
      <a href="/files/Joonkyung_Kim_CV_recent.pdf" target="_blank" style="text-decoration: none; color: #444;" title="CV"><i class="fas fa-file-pdf"></i> CV</a>
    </div>
  </div>
</div>

<div style="margin: 2rem 0;">
  <div style="padding-bottom: 0.2rem; margin-bottom: 1rem; border-bottom: 2px solid #ddd;">
    <h2 style="margin: 0; color: #000000;">News</h2>
  </div>
  <div style="font-size: 0.95em; max-height: 360px; overflow-y: auto; padding-right: 0.5rem;">
    {% assign news = site.data.news | sort: 'date' | reverse %}
    {% for item in news %}
      {% case item.tag %}
        {% when 'paper' %}{% assign tag_bg = '#1f6feb' %}{% assign tag_label = 'PAPER' %}
        {% when 'workshop' %}{% assign tag_bg = '#8957e5' %}{% assign tag_label = 'WORKSHOP' %}
        {% when 'talk' %}{% assign tag_bg = '#2da44e' %}{% assign tag_label = 'TALK' %}
        {% when 'award' %}{% assign tag_bg = '#d29922' %}{% assign tag_label = 'AWARD' %}
        {% when 'milestone' %}{% assign tag_bg = '#6e7681' %}{% assign tag_label = 'MILESTONE' %}
        {% else %}{% assign tag_bg = '#6e7681' %}{% assign tag_label = item.tag | upcase %}
      {% endcase %}
      <div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.6rem; margin-bottom: 0.4rem;">
        <span style="color: #555; min-width: 75px;">{{ item.date | date: "%b %Y" }}</span>
        <span style="background-color: {{ tag_bg }}; color: #fff; padding: 0.1rem 0.45rem; border-radius: 3px; font-size: 0.7em; font-weight: 700; letter-spacing: 0.03em;">{{ tag_label }}</span>
        <span style="flex: 1; min-width: 200px;">{{ item.text }}</span>
      </div>
    {% endfor %}
  </div>
</div>

<!-- A data-driven personal website
======
Like many other Jekyll-based GitHub Pages templates, Academic Pages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
