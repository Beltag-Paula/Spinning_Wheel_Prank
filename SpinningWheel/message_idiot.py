import webbrowser
import tkinter as tk
from tkinter import messagebox


class MessageIdiot:
    def __init__(self):
        # Initialize Tkinter
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window as it's not used

        # Variable to track if a popup is currently open
        self.popup_open = False

    def show_popup(self):
        if not self.popup_open:
            self.popup_open = True

            # Function to handle button clicks
            def on_button_click(answer):
                self.popup_open = False
                if answer == 'yes':
                    # Open the URL in the browser
                    webbrowser.open(
                        "https://d7hftxdivxxvm.cloudfront.net/?height=658&quality=85&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FxE_Mc-tnI7w4av0DnX5UxA%2Fmain.jpg&width=800")
                    # Close the Tkinter app and terminate the script
                    self.root.quit()  # Stop the Tkinter main loop
                    # sys.exit()  # Terminate the Python script, use it only if you are using the class itself without the spinning wheel
                else:
                    # Schedule the next popup immediately if 'No' is clicked
                    self.root.after(10, self.show_popup)

            # Show the message box and handle the user's response
            answer = messagebox.askquestion("Question", "Are you an idiot?")
            on_button_click(answer)

    def run(self):
        # Show the initial popup
        self.show_popup()
        # Start the Tkinter main loop (necessary to keep the UI running)
        self.root.mainloop()

# if __name__ == "__main__":
#    message_idiot = MessageIdiot()
#    message_idiot.run()
