import simplegui

# Global state
time_val  = 0     # tenths of a second (integer)
running   = False
stops     = 0
successes = 0

# --- Helper: format t (tenths) as A:BC.D ---
def format_time(t):
    tenths  = t % 10
    total_s = t // 10
    secs    = total_s % 60
    mins    = total_s // 60
    return str(mins) + ":" + str(secs // 10) + str(secs % 10) + "." + str(tenths)

# --- Timer handler ---
def tick():
    global time_val
    time_val += 1

# --- Button handlers ---
def start():
    global running
    if not running:
        running = True
        timer.start()

def stop():
    global running, stops, successes
    if running:
        timer.stop()
        running = False
        stops += 1
        if time_val % 10 == 0:
            successes += 1

def reset():
    global time_val, running, stops, successes
    timer.stop()
    running   = False
    time_val  = 0
    stops     = 0
    successes = 0

# --- Draw handler ---
def draw(canvas):
    # Main time display - centred
    canvas.draw_text(format_time(time_val), [110, 165], 60, "White", "monospace")
    # Score - upper right
    canvas.draw_text(str(successes) + "/" + str(stops), [310, 40], 28, "Green", "monospace")

# --- Frame setup ---
frame = simplegui.create_frame("Stopwatch: The Game", 400, 300)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw)

frame.add_button("Start", start, 100)
frame.add_button("Stop",  stop,  100)
frame.add_button("Reset", reset, 100)

timer = simplegui.create_timer(100, tick)

frame.start()
