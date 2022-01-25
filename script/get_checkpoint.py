"""
Load checkpoint.
"""

import pathlib
import argparse
import subprocess


def get_model(name):
    url = f"https://scifact.s3.us-west-2.amazonaws.com/longchecker/latest/checkpoints/{name}.ckpt"
    cmd = ["wget", "-O", f"checkpoints/{name}.ckpt", url]
    subprocess.run(cmd)


def main():
    choices = ["all", "covidfact", "fever_sci", "fever", "healthver", "scifact"]
    parser = argparse.ArgumentParser(
        description="Download pretrained Longchecker model"
    )
    parser.add_argument("name", type=str, choices=choices, help="Model name")
    args = parser.parse_args()
    name = args.name

    pathlib.Path("checkpoints").mkdir(exist_ok=True)

    # Get all models if requested; else get one of them.
    if name == "all":
        for name_loop in choices[1:]:
            get_model(name_loop)
    else:
        get_model(name)


if __name__ == "__main__":
    main()