import re


def validate_url(url):
    if not url.startswith("https://www.youtube.com/"):
        raise ValueError("Invalid YouTube URL")


def validate_time_format(start_time_str, end_time_str):
    time_format = re.compile(r'^\d{1,2}:\d{2}$')

    if not time_format.match(start_time_str) or not time_format.match(end_time_str):
        raise ValueError(
            "Invalid time format. Please use the format 'HH:MM' (e.g., 23:00).")

    start_time_parts = start_time_str.split(':')
    end_time_parts = end_time_str.split(':')

    start_time = int(start_time_parts[0]) * 60 + int(start_time_parts[1])
    end_time = int(end_time_parts[0]) * 60 + int(end_time_parts[1])

    if start_time >= end_time:
        raise ValueError("End time must be greater than start time.")

    return start_time, end_time
