class Styles:
    def __init__(self, root):
        self.root = root

    def apply(self, root, task_listbox, task_entry, add_button, update_button, delete_button):
        # Set the background color of the root window
        root.configure(bg="#f0f0f0")
        
        # Style for Listbox
        task_listbox.configure(
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 12),
            borderwidth=2,
            relief="sunken"
        )

        # Style for Entry widget
        task_entry.configure(
            font=("Arial", 12),
            bd=2,
            relief="sunken"
        )

        # Style for Buttons
        button_style = {
            "bg": "#007bff",
            "fg": "#ffffff",
            "font": ("Arial", 12),
            "bd": 2,
            "relief": "raised",
            "padx": 10,
            "pady": 5
        }

        add_button.configure(**button_style, text="Add Task")
        update_button.configure(**button_style, text="Update Task")
        delete_button.configure(**button_style, text="Delete Task")
