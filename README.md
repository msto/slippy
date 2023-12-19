# README

`slippy` is a simple [Snakemake](https://snakemake.readthedocs.io/en/stable/)
linter that checks Snakefiles adhere to Fulcrum Genomics guidelines.

## Installation

```sh
git clone https://github.com/msto/slippy.git
pip install -e slippy
```

## Usage

```sh
$ slippy -h
usage: slippy [-h] -s SNAKEFILE [-i | --include-all | --no-include-all]

Slippy is a simple snakemake linter.

options:
  -h, --help            show this help message and exit
  -s SNAKEFILE, --snakefile SNAKEFILE
                        Snakefile to lint.
  -i, --include-all, --no-include-all
                        Lint the all rule.
                        (default: False)
```

## Checks
TODO enumerate the lint checks `slippy` enforces

## Why "slippy"?

`slippy` first came to mind as the "Simple Snakemake Linter". "SSL" is already taken, but `ssl.py` could sound like "slippy". 

And `slippy` is helpful, like everybody's favorite digital assistant who also rhymes with "lippy".

And [Rust did it first](https://doc.rust-lang.org/stable/clippy/usage.html).
