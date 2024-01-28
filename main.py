from src.youtube_downloader import YouTubeVideoDownloader
from src.validation import validate_url, validate_time_format


def get_input(prompt):
    return input(prompt)


if __name__ == "__main__":
    url = get_input("Enter YouTube video URL: ")
    start_time_str = get_input("Enter start time (e.g., 23:00): ")
    end_time_str = get_input("Enter end time (e.g., 24:00): ")
    output_filename = "trimmed.mp4"  # Default output filename

    try:
        validate_url(url)
        start_time, end_time = validate_time_format(
            start_time_str, end_time_str)
        downloader = YouTubeVideoDownloader(
            url, start_time, end_time, output_filename)
        downloader.download_and_trim_video()
    except ValueError as e:
        print(f"Error: {e}")
