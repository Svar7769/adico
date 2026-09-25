# ADiCo research webpaper

A lightweight, three-page research website built with HTML and CSS. The main page has seven question-based sections, with populated DiCo and ESC method pages.

## Preview locally

Extract the download and open `index.html` in your browser. No server or package installation is required.

## Publish on GitHub Pages

1. Create a GitHub repository, for example `adico-webpaper`, with a `main` branch. A public repository works with GitHub Free.
2. Put the **contents** of this folder at the repository root, so `index.html`, `build.py`, and `.github/` are at the top level. Commit all files, including the workflow folder. GitHub Desktop or Git can preserve the entire folder structure.
3. Open repository **Settings → Pages → Build and deployment**. Set **Source** to **GitHub Actions**.
4. Open **Actions → Publish webpaper → Run workflow**, choosing `main`. Every subsequent push to `main` also rebuilds and publishes automatically.
5. After the workflow succeeds, find the website URL in Settings → Pages or the deployment result. A typical project URL is `https://USERNAME.github.io/adico-webpaper/`.

If your default branch has another name, update the branch in `.github/workflows/pages.yml`. This workflow publishes the website files, styles, and assets only; it does not publish the section sources or build script as part of the website.

Reference: [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## What to edit

| File or folder | Purpose |
| --- | --- |
| `templates/index.html` | Main-page header, navigation, sidebar, and section insertion point |
| `sections/adico/*.html` | Individual main-page sections, ordered by numeric filename |
| `dico.html` | DiCo method page |
| `esc.html` | ESC method page |
| `styles/theme.css` | Shared colors and typography |
| `styles/layout.css` | Page widths, spacing, and responsive layout |
| `styles/components.css` | Navigation, figure placeholders, and reusable blocks |
| `assets/figures/` | Plots and diagrams |
| `assets/videos/` | Demonstration clips |
| `assets/documents/` | Paper and presentation |
| `build.py` | Assembles the main page and exports static files |
| `.github/workflows/pages.yml` | Builds and publishes on GitHub Pages |

Edit the source sections or template, then push your changes. GitHub automatically assembles the published main page. For a local preview after editing, run `python3 build.py` (Windows: `python build.py`) and refresh the browser. The checked-in `index.html` is a generated local preview; avoid editing it directly because rebuilding replaces it.

CSS changes need only a browser refresh locally. Update the sidebar in `templates/index.html` when adding, removing, or renaming sections.

## Add content later

Replace a figure-placeholder block with an image and meaningful alt text. Use relative paths such as `assets/figures/overview.png`, without a leading slash, so links work under a GitHub project URL. Replace resource labels with links once their destinations exist. Keep media files reasonably sized; use externally hosted video embeds for large clips.

## Export manually

Run `python3 build.py --output _site` to produce a deployment folder. The output directory must be new or empty. It is excluded from Git because the workflow regenerates it.
