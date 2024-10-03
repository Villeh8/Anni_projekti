import time
import os
from datetime import datetime

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

def time_counter():
    saved_elapsed_time, last_stop_time = load_elapsed_time()

    # Calculate the time passed between the last stop and now
    if last_stop_time != 0:
        time_since_last_stop = time.time() - last_stop_time
        saved_elapsed_time += time_since_last_stop

    start_time = time.time()  # Record the starting time for this session

    try:
        while True:
            # Calculate the elapsed time for this session
            current_elapsed_time = time.time() - start_time
            total_elapsed_time = saved_elapsed_time + current_elapsed_time

            # Convert total elapsed time into days, hours, minutes, and seconds
            days = int(total_elapsed_time // 86400)
            hours = int((total_elapsed_time % 86400) // 3600)
            minutes = int((total_elapsed_time % 3600) // 60)
            seconds = int(total_elapsed_time % 60)

            # Display the counter
            print(f"Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}", end="\r")

            # Sleep for 1 second before updating the display
            time.sleep(1)

    except KeyboardInterrupt:
        # Save the total elapsed time and the current stop time when exiting
        final_elapsed_time = saved_elapsed_time + (time.time() - start_time)
        current_time = time.time()
        save_elapsed_time(final_elapsed_time, current_time)
        print("\nProgress saved. Counter stopped.")

if __name__ == "__main__":
    time_counter()
