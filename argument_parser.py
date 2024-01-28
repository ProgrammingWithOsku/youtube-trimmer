import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download and trim YouTube videos.')
    parser.add_argument('url', type=str, help='YouTube video URL')
    parser.add_argument('start_time', type=int, help='Start time in seconds')
    parser.add_argument('end_time', type=int, help='End time in seconds')
    parser.add_argument('output_filename', type=str,
                        help='Output filename for the trimmed video')
    return parser.parse_args()
