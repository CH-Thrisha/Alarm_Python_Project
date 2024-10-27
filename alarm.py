# Import Required Libraries
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x250")

# Variable to control the alarm
alarm_running = False

# Use Threading
def start_alarm():
    global alarm_running
    alarm_running = True  # Start the alarm
    t1 = Thread(target=alarm)
    t1.start()pyp

def stop_alarm():
    global alarm_running
    alarm_running = False  # Stop the alarm
    winsound.PlaySound(None, winsound.SND_ASYNC)  # Stop any ongoing sound

def alarm():
    # Infinite Loop
    while alarm_running:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check if the set alarm time matches the current time
        if current_time == set_alarm_time:
            print("Time to Wake up")
            winsound.Beep(1000, 1000)
            break

# Add Labels, Frame, Buttons, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

# Hour Dropdown Menu
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Minute Dropdown Menu
minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(60))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Second Dropdown Menu
second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(60))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Set Alarm and Stop Alarm Buttons
Button(root, text="Set Alarm", font=("Helvetica 15"), command=start_alarm).pack(pady=10)
Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm).pack(pady=10)

# Execute Tkinter
root.mainloop()
