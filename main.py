import yt_dlp
import os

def download_youtube_video(url, output_path="downloads"):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # Set options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"Download completed successfully!")
            return filename
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Get YouTube video URL from user
    video_url = input("Please enter the YouTube video URL: ")
    downloaded_file = download_youtube_video(video_url)
    if downloaded_file:
        print(f"Video saved to: {downloaded_file}")
