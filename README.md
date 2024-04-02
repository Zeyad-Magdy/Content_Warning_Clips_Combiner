# Content Warning Clips Concatenator

This script is designed to concatenate separate video clips recorded during gameplay for Content Warning game by Landfall. The clips are temporarily saved in your PC's default temp folder under a `rec` folder, with each round of recording saved in a separate folder. Each time you press the record button, a new folder is created within the round's folder.

## Requirements

- **Python**: Version 3.8 or higher is required.

## Installation

1. Install the `moviepy` library, which is used for video editing tasks.
    ```
    pip install moviepy
    ```
## Usage

1. Save this script in the same directory where you want to save the clips.
2. Run the script using Python.
    ```
    python main.py
    ```
This will concatenate all the clips found in the `rec` folder and its subfolders using moviepy, and save the concatenated video in the directory you choose.