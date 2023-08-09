import os
import random
import subprocess
import threading
import art

# Display ASCII art title
print(art.text2art("LofiStream"))

# Ask for user input
audio_folder = input("Enter the path to your audio folder: ")
background_image = input("Enter the path to your background image (jpg, png, or gif): ")
stream_url = input("Enter your YouTube Live stream URL: ")
stream_key = input("Enter your stream key: ")

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
        '-ignore_loop', '0',  # This flag is used for looping animated GIFs
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
