# Website Project

## Overview

- Personal academic/research website for Pablo Capilla-Lasheras, deployed through GitHub Pages at `pablocl.com`.
- Built with Jekyll and the Minimal Mistakes theme.
- The site has undergone a major redesign. The current direction is a restrained, editorial, photography-led research portfolio rather than a conventional theme-driven academic website.
- Pablo is now presented as a Ramón y Cajal Fellow at the Biology Department and Global Change Research Institute at Rey Juan Carlos University (IICG-URJC, Madrid, Spain)
- Ruby dependencies and Jekyll plugins are defined in `Gemfile`.
- Site-wide settings, author links, and theme configuration are in `_config.yml`.

## Redesign Status

- A first complete redesign pass was implemented in September 2026 and is currently being reviewed page by page by the user.
- The welcome page is intentionally minimal: one full-screen scops owl field image, a short research statement, current appointment, and one link into the research section.
- The three navigation blocks that initially appeared below the landing image were removed after review. Do not reintroduce them unless requested.
- The visual language uses warm ivory, charcoal, muted moss and ochre, with serif display typography and sans-serif supporting text.
- The main responsive design system is consolidated in `assets/css/main.scss`.
- Search and the home-page news feed have been removed to reduce visual and maintenance overhead.
- The footer carries the name of current appointment and links to Google Scholar, Bluesky, GitHub, email and the MIGRALIGHT Instagram account.
- Continue making small, reviewable refinements. Do not replace the design wholesale without discussing a new direction with the user.

## Current Navigation And Routes

- `BeEcoEvo in an Anthropogenic World` -> `/research/`
- `The Scops Owl Project` -> `/scops_owl_project/`
- `Team` -> `/team/`
- `Publications` -> `/publications/`
- `Diversity and Inclusion Manifesto` -> `/manifesto/`
- Navigation labels are intentionally project-specific and were chosen by the user. Do not revert them to generic Research/Projects/People labels.

## Content Structure

- `_pages/`: primary website pages. Add or update page front matter, prose, and page-specific HTML here.
- `_pages/home.md`: minimal landing-page content rendered by `_layouts/landing.html`.
- `_pages/research.md`: BeEcoEvo research overview.
- `_pages/MIGRALIGHT.md`: Scops Owl Project/MIGRALIGHT page despite the legacy filename.
- `_pages/team.md`: people page rendered from `_data/team.yml`.
- `_pages/bio.md`: About page and career timeline.
- `_data/publications.yml`: canonical structured publication list, including papers, preprints and other research outputs.
- `_data/team.yml`: canonical current members, past members and collaborator records.
- `_data/navigation.yml`: primary navigation.
- `_data/authors.yml`: author profile data.
- `assets/images/`: site images, organised by page or topic.
- `assets/css/main.scss`: main custom styling layered on Minimal Mistakes.
- `_includes/publications.html`: the single publication-item renderer.
- `_layouts/publications.html`: publication page structure and category grouping.
- `_includes/` and `_layouts/`: Minimal Mistakes overrides. Change these only when page-level content or scoped CSS cannot achieve the required result.

## Publication State

- The publication data currently contains 35 peer-reviewed articles, one preprint and two other research outputs.
- Six recent journal articles from 2025-2026 were added after reconciling the website against Google Scholar and verifying metadata with DOI/Crossref records.
- Existing PDF links were normalised to root-relative paths under `/assets/pub_pdf/`.
- Store DOI fields as bare identifiers, for example `10.1111/ele.70382`, not full DOI URLs.
- New papers should receive a unique numeric `id`; current rendering sorts papers by descending `id` and groups them by year.
- Use `authors` for full author arrays. `authors_text` is supported for exceptionally long author lists.
- Verify Scholar candidates against authoritative DOI or publisher metadata before adding them. Google Scholar alone is not a canonical citation source.
- Do not invent PDF, code or data links. Add them only when known and valid.

## Known Placeholders

- The exact URJC department, research unit, institutional profile URL, appointment start date and institutional email have not yet been provided.
- `_pages/bio.md` visibly marks the institutional unit/profile as details to be added.
- Current team records still need Cristina's full name, Cristina's project details and Alejandro Molinero's project details.
- Affiliations for Blanca Jimeno and Daniel Bustillo de la Rosa remain to be confirmed.
- Most team portraits are unavailable. The people page currently uses typographic initial placeholders where no verified image exists.
- The Scops Owl Project partner network and current project details will need further factual review.
- Existing images are being used as working imagery. The user may replace them after reviewing the layouts.

## Development

- Install dependencies: `bundle install`
- Run locally: `bundle exec jekyll serve`
- Build for verification: `bundle exec jekyll build`
- Restart the local server after changing `_config.yml`.
- Do not edit generated output in `_site/`.
- The build currently succeeds with only the expected unauthenticated GitHub Metadata warning.

## Content Conventions

- Use UK English unless reproducing a publication title, journal name or quoted source.
- Preserve the current research-focused, clear, professional visual style.
- Write meaningful image `alt` text; do not use placeholders in published content.
- Prefer Markdown for prose. Use HTML only where required for layout or custom components.
- Use root-relative internal URLs, such as `/BeEcoEvo/`, to work on the production domain.
- Keep publication entries consistent with the existing fields and order; retain DOI, PDF, code, data, and Altmetric fields when available.
- Keep publication years and career dates accurate. Remove temporary copy, "under construction" text, and test values before publishing.

## Styling And Responsive Design

- Prefer small, scoped CSS changes in `assets/css/main.scss`; it is now the single project-owned stylesheet entry point.
- Test changes at mobile and desktop widths.
- Avoid inline styles unless a genuinely page-specific exception is required.
- Reuse the established editorial page, publication, people and project patterns before adding new components.
- Preserve one logical `<h1>` and one `#main` landmark on every principal page.
- Use responsive image dimensions and `loading="lazy"` below the fold.
- The optimised landing and project hero derivatives are `assets/images/home/landing-hero.jpg` and `assets/images/research/scops-owl-project-hero.jpg`.

## Removed Legacy Content

- Default Jekyll sample posts, post archives, the `/welcome/` draft and the `/ethics/` test page were removed during the redesign.
- Separate `publications.css`, `MIGRALIGHT_css.css` and empty custom CSS files were removed after their rules were consolidated into `main.scss`.
- Do not restore obsolete Glasgow-current-affiliation copy. Glasgow references may remain where they describe career history or active collaborators.

## Safety

- Never commit `_site/`, dependency caches, or macOS `.DS_Store` files.
- Do not expose or add API keys, tokens, or credentials to tracked files.
- Treat existing uncommitted changes as user work: do not revert or overwrite them unless explicitly asked.
