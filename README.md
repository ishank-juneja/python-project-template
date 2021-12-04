## Legend

1. All `.py` files go into `src` or sub-dir of `src`. All plotting scripts go in `src/plotting`. Avoid any `matplotlib` or related imports in main `src` files
2. All `.pynb` files go into `notebooks`. Using google colab is preffered but files should be downloaded into this folder once done
3. All figures/videos/plots go in the corresponding sub-dir of `results`. Example all `.png` files in `results/figures`
4. All models (bullet/mujoco physcis based, trained, or otherwise) go into `models` or sub-dir of `models`
5. Any documentation that does not belong in the README.md (text files for minor references etc.) and things like referred PDFs go into `notes`
6. All local datasets and problem instance files go into `data` or sub-dir of `data`

## Append project .gitignore with

```
notes/
data/
```

## Command to be able to add an empty directory tree to git
Command used to push this empty template repo to git/guthub was

`find . -type d -empty -not -path "./.git/*" -exec touch {}/.gitkeep \;`
