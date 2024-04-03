import os
from moviepy.editor import concatenate_videoclips, VideoFileClip
from datetime import datetime
import tempfile


def combine_webm_files(output_directory):

    # Get the path to the temporary folder
    temp_folder = tempfile.gettempdir()
    main_directory = os.path.join(temp_folder, 'rec')
    if not os.path.isdir(main_directory):
        print(f"The temp recordings folder was not found, it gets deleted after a while of closing the game or when openning the game again.")
        input('press any key to exit...')
        return
    # Iterate over all folders in the specified directory
    for index,directory in enumerate(os.listdir(main_directory)):
        directory_path = os.path.join(main_directory, directory)
        # print(directory,directory_path)
        if os.path.isdir(directory_path):
            print(f"Processing directory {index + 1}: {directory_path}")
            # Get a list of all directories in the specified directory
            directories = [os.path.join(directory_path, folder) for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
            found_count = 0 # Initialize a counter for found .webm files
            # List to hold all video clips
            clips = []
            # print(directories)
            # Sort directories by last modification time
            directories.sort(key=lambda x: os.path.getmtime(x))
            for folder_path in directories:

                # Check if output.webm exists in the folder
                webm_file = os.path.join(folder_path, 'output.webm')
                if os.path.exists(webm_file):
                    # Increment the found count
                    found_count += 1
                    # Print the updated count on the same line
                    print(f"\rFound {found_count}", end="")
                    # Add the video clip to the list
                    clips.append(VideoFileClip(webm_file))

            if not clips:
                print("\nNo .webm files found in the specified directory.")
                return
            print("\nprocessing...")
            # Concatenate all clips into a single clip
            final_clip = concatenate_videoclips(clips)
            # Write the final clip to a file
            now = datetime.now()
            output_file = "output_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".webm"
            output_file = os.path.join(output_directory, output_file)
            final_clip.write_videofile(output_file, codec='libvpx')
        print("Processing complete for directory:", directory_path)
    input("\nPress any key to exit...")

def main():
    # Ask for the directory containing the folders
    output_directory = input("Please enter the directory where you want to save the output (leave empty for default: current directory) (or 'q' to quit): ")

    if output_directory.lower() == 'q':
        return

    #if empty use current directory
    if not output_directory:
        output_directory = os.getcwd()

    # Check if the directory exists
    if not os.path.exists(output_directory):
        print(f"The directory {output_directory} does not exist.")
        input("\nPress any key to exit...")
        return

    if not os.path.isdir(output_directory):
        print(f"The path {output_directory} is not a directory.")
        #print press any key to exit
        input("\nPress any key to exit...")
        return

    # Process the directory
    combine_webm_files(output_directory)


    

if __name__ == "__main__":
    main()
