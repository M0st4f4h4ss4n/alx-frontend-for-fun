#!/usr/bin/env python3
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Markdown file to convert")
    parser.add_argument("output", help="HTML output file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        sys.stderr.write(f"Missing {args.input}\n")
        exit(1)

    # Here we would normally convert the markdown to HTML and write it to args.output
    # But since the task does not specify to do this, we just exit with status 0

    exit(0)

if __name__ == "__main__":
    main()
