# YouTube Video Downloader

A simple and efficient Python script to download YouTube videos using the yt-dlp library.

## Features

- Download YouTube videos in the best available quality
- Simple command-line interface
- Automatic creation of download directory
- Error handling for failed downloads
- Support for single video downloads

## Prerequisites

Before running this script, make sure you have:

1. Python 3.6 or higher installed
2. pip (Python package manager)

## Installation

1. Clone this repository or download the source code.

2. Install the required dependencies:
```bash
pip install yt-dlp
```

## Usage

1. Run the script:
```bash
python main.py
```

2. When prompted, enter the YouTube video URL you want to download.

3. The video will be downloaded to the `downloads` folder in the project directory.

## Project Structure

```
├── main.py           # Main script file
├── downloads/        # Directory where downloaded videos are saved
└── README.md        # Project documentation
```

## How It Works

The script uses the `yt-dlp` library (a fork of youtube-dl) to:
1. Accept a YouTube URL as input
2. Create a downloads directory if it doesn't exist
3. Download the video in the best available quality
4. Save the video with its original title as the filename

## Error Handling

The script includes basic error handling to:
- Catch and display download errors
- Handle invalid URLs
- Manage file system errors

## Limitations

- Currently only supports single video downloads (no playlist support)
- Downloads videos in the best available quality (no quality selection option)

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for personal use only. Please respect YouTube's terms of service and content creators' rights when downloading videos.