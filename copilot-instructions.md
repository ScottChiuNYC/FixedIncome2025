# Copilot Instructions for FixedIncome2025

This file gives AI assistants (and humans) concise, actionable context for working in this repository. Prefer Windows `cmd.exe` commands and keep changes minimal and focused.

## Project Overview
- Course materials for Analysis of Fixed Income (Fall 2025).
- Source notebooks and Sphinx docs live under `docs/source/` and publish to Read the Docs.
- Static slide decks are in `docs/slides/*.slides.html` (generated outside this repo).

## Tech Stack
- Python: `^3.12`
- Dependency manager: Poetry (`pyproject.toml`). RTD installs via a Poetry export; no hand-maintained `requirements.txt`.
- Docs: Sphinx (`sphinx`, `nbsphinx`, RTD theme). Windows build script: `docs\make.bat`.
- Jupyter: `jupyterlab`, `notebook`, `jupyterlab-rise`.

## Default Environment (Windows / cmd)
Use Poetry and include dev dependencies for docs:

```
py -m pip install --user poetry
poetry --version
poetry install --with dev
```

Activate the Poetry environment when running commands, either via `poetry run <cmd>` or `poetry shell`.

## Common Tasks
- Build docs (HTML):
```
poetry run .\docs\make.bat html
```
Output: `_build\html` under `docs`. Open `_build\html\index.html`.

- Serve JupyterLab for editing notebooks:
```
poetry run jupyter lab
```

- Run a one-off notebook kernel (if needed by nbsphinx):
```
poetry run python -m ipykernel install --user --name=fixedincome2025
```

## Documentation Layout
- Root index: `docs/source/index.rst`
- Notebooks rendered by `nbsphinx`: `docs/source/*.ipynb`
- Data tables used by notebooks: `docs/source/tables/*.csv`
- Sphinx config: `docs/source/conf.py`
- Windows build script: `docs/make.bat`

Scrap notebook:
- `docs/source/scrap.ipynb` is a scratchpad for quick drafts and ideas (often from AI assistants). Keep it lightweight and runnable; if content graduates to the course, move it into a properly named notebook and update the toctree.

Guidance for edits:
- Place new notebooks in `docs/source/` and add to the toctree in `index.rst`.
- Keep notebooks deterministic: avoid network calls and hard-coded local paths.
- Prefer small CSV samples under `docs/source/tables/` for examples.

## Slides
- Static HTML decks live in `docs/slides/*.slides.html`. To change content, edit the corresponding notebook in `docs/source/` and regenerate slides externally (RISE or your chosen pipeline), then replace the HTML file.

## Coding & Repo Conventions
- Keep changes minimal and focused on the requested task.
- Match existing style; do not introduce unrelated refactors.
- Do not add license headers to files.
- Use Windows paths in instructions and commands (`\\` separators) and `cmd.exe` syntax.
- For Python packaging, prefer Poetry commands over raw `pip` unless asked.

## Boundaries for AI Assistants
- Do not introduce external services, secrets, or telemetry.
- Do not modify CI/hosting settings unless explicitly requested (e.g., `.readthedocs.yml`).
- Avoid long-running background servers unless necessary; prefer one-shot commands.
- If a step is ambiguous (e.g., how slides are generated), propose options and ask before committing to a pipeline.

## Quick References
- Build docs: `poetry run .\docs\make.bat html`
- Open docs: `docs\_build\html\index.html`
- Start JupyterLab: `poetry run jupyter lab`
- Python package root: `fixedincome2025/`

## Useful Tips
- When adding notebooks, ensure they render with `nbsphinx` (avoid widgets that require a live kernel).
- If RTD build fails due to missing deps, confirm they’re listed under `[tool.poetry.group.dev.dependencies]`.
- Keep CSVs small to keep repo light.

## About This File
Some AI tools (e.g., GitHub Copilot Agents/Chat) read `copilot-instructions.md` for project-specific guidance. Keep this concise and up to date.

RTD note: Read the Docs installs dependencies exported from Poetry during builds (`poetry export --with dev`). The generated `rtd-requirements.txt` is not committed.
