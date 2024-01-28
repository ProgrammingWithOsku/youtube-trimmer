# YouTube Video Downloader and Trimmer by Osku

This project, developed by Osku, comprises a Python script for downloading and trimming specific portions of YouTube videos. It's organized into modular components for ease of use and maintenance.

## Getting Started

### Prerequisites

- Python 3
- pip
- pipenv

### Installation

1. **Install Pipenv**:
   ```bash
   pip install pipenv
   ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/ProgrammingWithOsku/youtube-trimmer.git
   cd youtube-trimmer
   ```

3. **Set Up Environment and Dependencies**:
   ```bash
   pipenv install pytube moviepy
   ```

### Usage

1. **Activate the Environment**:
   ```bash
   pipenv shell
   ```

2. **Run the Main Script**:
   ```bash
   python main.py
   ```

3. **Follow the Prompts**:

   - Enter the YouTube video URL.
   - Enter the start time in "HH:MM" format (e.g., 23:00).
   - Enter the end time in "HH:MM" format (e.g., 24:00).
   - Enter the output filename (e.g., "output.mp4").

4. **Exit the Environment**:
   ```bash
   exit
   ```

### Example:

Suppose you want to download a portion of the video at the URL "https://www.youtube.com/watch?v=27CGOLqp-to" from 23:00 to 24:00. Here's how to do it:

1. Run the script and follow the prompts:
   - Enter YouTube video URL: https://www.youtube.com/watch?v=27CGOLqp-to
   - Enter start time (e.g., 23:00): 23:00
   - Enter end time (e.g., 24:00): 24:00
   - Enter output filename: output.mp4

2. The script will download the specified portion of the video and save it as "output.mp4" in the same directory.

## Modules

- **youtube_downloader.py**: Contains the `YouTubeVideoDownloader` class for downloading and trimming videos.
- **validation.py**: Houses the validation functions for URL and time inputs.
- **main.py**: The entry point of the script.

## Validation

### YouTube URL Validation

The provided YouTube URL must start with "https://www.youtube.com/". If the URL is invalid, an error will be displayed.

### Start and End Time Validation

The start and end times must be in "HH:MM" format and satisfy the format validation. The end time must also be greater than the start time. If any of these conditions are not met, an error will be displayed.

## Note

- Ensure compliance with YouTube's terms of service.
- Intended for educational purposes.

## Creator

- Osku(Eng: Osamah Amer)

---