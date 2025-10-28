jupyter nbconvert --to slides --no-input docs/source/0*.ipynb --output-dir=docs/slides/
@REM jupyter nbconvert --to slides --no-input docs/source/1*.ipynb --output-dir=docs/slides/
git config --global user.name "ScottChiuNYC"
git config --global user.email "scott.chiu@rutgers.edu"
git add *
git commit -m "auto save"
git push