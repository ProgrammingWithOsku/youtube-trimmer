# YouTube Video Downloader and Trimmer by Osku

Effortlessly download and trim specific parts of YouTube videos with this Python script developed by Osku. Designed for simplicity and modularity, it's ideal for educational purposes.

## Getting Started

### Prerequisites

- Python 3.6 or higher
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
   pipenv install
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

   - Input the YouTube URL.
   - Input start and end times in "HH:MM" format.
   - Input the output filename.

4. **Exit the Environment**:
   ```bash
   exit
   ```

### Example:

Download a video segment from "https://www.youtube.com/watch?v=27CGOLqp-to" between 23:00-24:00, saving it as "output.mp4".

## Modules

- **youtube_downloader.py**: Downloads and trims videos.
- **validation.py**: Validates URLs and time inputs.
- **main.py**: Script entry point.

## Validation

YouTube URLs must start with "https://www.youtube.com/". Start and end times should be in "HH:MM" format, with the end time later than the start.

## Note

Comply with YouTube's terms of service. For educational use.

## Creator

Osku (Eng: Osamah Amer)