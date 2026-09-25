# ADiCo: Adaptive Diversity Control

Project page for **Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning**, IEEE Conference on Decision and Control (CDC) 2026.

Svar Rajankumar Patel · Kshitij Jerath
EXA Lab, University of Massachusetts Lowell

**Website:** [https://Svar7749.github.io/adico/](https://Svar7749.github.io/REPO-NAME/)

ADiCo automatically selects how much behavioral diversity a cooperative multi-agent team needs. It combines Diversity Control (DiCo), which regulates diversity toward a target, with Extremum Seeking Control (ESC), which adjusts that target using team-performance feedback during training.

## About this site

A lightweight, three-page research website built with plain HTML and CSS, with no framework or package installation.

| Page | Content |
| --- | --- |
| `index.html` | Main page: motivation, method, experimental setup, results, and future directions |
| `dico.html` | Method page: measuring and controlling behavioral diversity |
| `esc.html` | Method page: Extremum Seeking Control and how it updates the diversity target |

Each page has a side navigation that stays fixed on desktop and collapses into a menu on mobile.

## Preview locally

Open `index.html` in your browser. After editing a main-page section or the template, run `python3 build.py` (Windows: `python build.py`) and refresh.

## Publish on GitHub Pages

1. Create a public GitHub repository with a `main` branch.
2. Put the **contents** of this folder at the repository root, so `index.html`, `build.py`, and `.github/` are at the top level. Commit all files, including the workflow folder.
3. Open repository **Settings → Pages → Build and deployment**, and set **Source** to **GitHub Actions**.
4. Open **Actions → Publish webpaper → Run workflow**, choosing `main`. Every later push to `main` rebuilds and publishes automatically.
5. After the workflow succeeds, the URL appears in **Settings → Pages**. A project repository publishes at `https://USERNAME.github.io/REPO-NAME/`; a repository named `NAME.github.io` in an organization named `NAME` publishes at `https://NAME.github.io/`.

If your default branch has another name, update it in `.github/workflows/pages.yml`. The workflow publishes the pages, styles, and assets only, not the section sources or build script.

Reference: [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Project structure

| File or folder | Purpose |
| --- | --- |
| `templates/index.html` | Main-page header, side navigation, resource links, and section insertion point |
| `sections/adico/*.html` | Main-page sections, assembled in numeric filename order |
| `index.html` | Generated main page; do not edit directly |
| `dico.html` | DiCo method page, edited directly |
| `esc.html` | ESC method page, edited directly |
| `styles/theme.css` | Colors and typography |
| `styles/layout.css` | Page widths, spacing, and responsive layout |
| `styles/components.css` | Navigation, figures, videos, and reusable blocks |
| `assets/figures/` | Plots and diagrams |
| `assets/videos/` | Demonstration clips |
| `assets/documents/` | Paper and presentation |
| `build.py` | Assembles the main page and exports static files |
| `.github/workflows/pages.yml` | Builds and publishes on GitHub Pages |

## Editing

**Main page.** Edit files in `sections/adico/` or `templates/index.html`, then rebuild. `index.html` is regenerated on every build, so direct edits to it are overwritten. When adding, removing, or renaming a section, update the side navigation in `templates/index.html` to match.

**Method pages.** `dico.html` and `esc.html` are standalone and are not generated. Edit them directly, including their side navigation.

**Styles.** CSS changes need only a browser refresh. If a change does not appear, hard refresh with Ctrl + F5.

**Media.**
- Use relative paths without a leading slash, such as `assets/figures/Plot-1.svg`, so links work under a project URL.
- Paths are case-sensitive on GitHub Pages: `Plot-1.svg` and `plot-1.svg` are different files.
- Avoid spaces in filenames.
- Prefer SVG for plots and diagrams, and MP4 over GIF for clips, which is much smaller.
- Keep media files reasonably sized.

## Export manually

Run `python3 build.py --output _site` to produce a deployment folder. The output directory must be new or empty. It is excluded from Git because the workflow regenerates it.

## Citation

```bibtex
@inproceedings{patel2026adico,
  title     = {Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning},
  author    = {Patel, Svar Rajankumar and Jerath, Kshitij},
  booktitle = {Proceedings of the IEEE Conference on Decision and Control (CDC)},
  year      = {2026}
}
```
