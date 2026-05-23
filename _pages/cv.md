---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
---

<p><em>Last update: May 2026</em></p>

<style>
  .cv-download-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.3rem 0.7rem;
    background-color: #324aa8;
    color: #ffffff !important;
    border-radius: 4px;
    text-decoration: none !important;
    font-weight: 500;
    font-size: 0.9em;
    transition: background-color 0.15s ease;
  }
  .cv-download-btn:hover {
    background-color: #1e2f6e;
    color: #ffffff !important;
  }
  .cv-mobile-notice {
    display: none;
    margin: 1rem 0;
    padding: 0.9rem 1rem;
    background-color: #f5f5f5;
    border-radius: 4px;
    color: #555;
    font-size: 0.92em;
  }
  @media (max-width: 768px) {
    .cv-iframe-wrapper { display: none; }
    .cv-mobile-notice { display: block; }
  }
</style>

<!-- Download button (always visible) -->
<div style="margin: 1rem 0;">
  <a class="cv-download-btn" href="{{ '/files/Joonkyung_Kim_CV_recent.pdf' | relative_url }}" target="_blank">
    <i class="fas fa-file-pdf"></i> Download CV (PDF)
  </a>
</div>

<!-- Mobile-only notice (hidden on desktop) -->
<p class="cv-mobile-notice">
  <i class="fas fa-mobile-alt"></i> Embedded preview is hidden on mobile because PDFs render poorly inside iframes on phones. Tap the button above to view the CV in your device's PDF viewer.
</p>

<!-- Desktop embedded preview (hidden on mobile) -->
<div class="cv-iframe-wrapper">
  <iframe src="{{ '/files/Joonkyung_Kim_CV_recent.pdf' | relative_url }}" width="100%" height="1000px" style="border: none;">
    This browser does not support PDFs. Please download the PDF to view it:
    <a href="{{ '/files/Joonkyung_Kim_CV_recent.pdf' | relative_url }}">Download PDF</a>
  </iframe>
</div>
