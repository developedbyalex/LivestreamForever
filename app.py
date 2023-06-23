import os
import random
import subprocess
import threading

# Replace with the path to your audio folder and background image
audio_folder = r'C:\Users\Rooft\Desktop\Python projects\24-7 Livestream\audio'
background_image = r'C:\Users\Rooft\Desktop\Python projects\24-7 Livestream\background\bg.jpg'

# Replace with your own YouTube Live stream URL and stream key
stream_url = 'rtmp://a.rtmp.youtube.com/live2'
stream_key = '32h3-w2j9-et97-8r9p-8v77'

# Get a random audio file from the folder
def get_random_audio_file():
    audio_files = os.listdir(audio_folder)
    return os.path.join(audio_folder, random.choice(audio_files))

# Start the streaming process
def start_streaming(audio_file):
    # Run FFmpeg subprocess to handle the video streaming with the provided audio file
    subprocess.call([
        'ffmpeg',
        '-re',
        '-loop', '1',
        '-i', background_image,
        '-i', audio_file,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-c:a', 'aac',
        '-pix_fmt', 'yuv420p',
        '-f', 'flv',
        stream_url + '/' + stream_key
    ])

# Select audio files and start streaming
def audio_track_selection():
    while True:
        current_audio_file = get_random_audio_file()

        # Start the streaming process in a separate thread
        streaming_thread = threading.Thread(target=start_streaming, args=(current_audio_file,))
        streaming_thread.start()

        # Wait for the streaming thread to finish
        streaming_thread.join()

# Main program loop
def main():
    # Start audio track selection in a separate thread
    audio_track_thread = threading.Thread(target=audio_track_selection)
    audio_track_thread.start()

    # Keep the program running until interrupted
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    # Stop the audio track selection thread
    audio_track_thread.join()

# Run the main program
if __name__ == '__main__':
    main()
