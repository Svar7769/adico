"""Assemble the main page; optionally export deployable files. No dependencies."""
import argparse
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', help='Export website into a new or empty directory')
args = parser.parse_args()
sections = sorted((root / 'sections' / 'adico').glob('*.html'))
content = '\n'.join(section.read_text(encoding='utf-8') for section in sections)
template = (root / 'templates' / 'index.html').read_text(encoding='utf-8')
(root / 'index.html').write_text(template.replace('{{SECTIONS}}', content), encoding='utf-8')
print('Built index.html from', len(sections), 'sections.')
if args.output:
    destination = (root / args.output).resolve()
    if destination.exists() and any(destination.iterdir()):
        parser.error('Output directory must be empty; choose a new directory.')
    destination.mkdir(parents=True, exist_ok=True)
    for filename in ('index.html', 'dico.html', 'esc.html'):
        shutil.copy2(root / filename, destination / filename)
    for folder in ('styles', 'assets'):
        if (root / folder).exists():
            shutil.copytree(root / folder, destination / folder)
    (destination / '.nojekyll').touch()
    print('Exported website to', destination)
