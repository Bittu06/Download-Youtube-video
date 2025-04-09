# YouTube Video Downloader

A simple Python script to download YouTube videos using yt-dlp.

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

1. Clone this repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```
python main.py
```

Enter the YouTube video URL when prompted. The video will be downloaded to the `downloads` folder.

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