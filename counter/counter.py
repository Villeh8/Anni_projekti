import time
import os

SAVE_FILE = "time_elapsed.txt"

def load_elapsed_time():
    """Load the previously saved elapsed time and the last stop time from the file."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()
            try:
                elapsed_time = float(lines[0].strip())
                last_stop_time = float(lines[1].strip())
            except (ValueError, IndexError):
                elapsed_time = 0
                last_stop_time = 0
    else:
        elapsed_time = 0
        last_stop_time = 0
    return elapsed_time, last_stop_time

def save_elapsed_time(elapsed_time, last_stop_time):
    """Save the total elapsed time and the current stop time to a file."""
    with open(SAVE_FILE, "w") as f:
        f.write(f"{elapsed_time}\n")
        f.write(f"{last_stop_time}\n")

class TimeCounter:
    def __init__(self):
        # Load the saved elapsed time and last stop time
        self.saved_elapsed_time, self.last_stop_time = load_elapsed_time()

        # Calculate time since the last stop
        if self.last_stop_time != 0:
            time_since_last_stop = time.time() - self.last_stop_time
            self.saved_elapsed_time += time_since_last_stop

        # Set the start time for the current session
        self.start_time = time.time()

    def get_elapsed_time(self):
        """Calculate and return the total elapsed time in seconds."""
        current_elapsed_time = time.time() - self.start_time
        total_elapsed_time = self.saved_elapsed_time + current_elapsed_time
        return total_elapsed_time

    def reset_timer(self):
        """Reset the saved elapsed time and start a new session."""
        self.saved_elapsed_time = 0
        self.start_time = time.time()
        save_elapsed_time(0, time.time())  # Save the reset state

    def save_progress(self):
        """Save the current progress (elapsed time) when exiting the app."""
        final_elapsed_time = self.saved_elapsed_time + (time.time() - self.start_time)
        current_time = time.time()
        save_elapsed_time(final_elapsed_time, current_time)
