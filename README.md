# Cutest Picture — make.fun entry (`cutest-picture-01`)

A fluffy orange kitten with a pink bow, nestled in a basket of soft
pastel blankets, looking straight at the viewer with big round eyes.

## How it works

`main.py` (Python 3 stdlib only) copies the bundled `entry.png` to
`/output/entry.png`, byte-identical. No network, no randomness, no
timestamps — running it twice produces the exact same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the picture (1024×1024 JPEG, 169,783 bytes)
- `LICENSE` — MIT

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
