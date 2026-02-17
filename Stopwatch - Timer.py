import simplegui

# ── globals
elapsed   = 0        # tenths of a second
running   = False
attempts  = 0
precise   = 0        # stopped exactly on a whole second

# ── format helper 
def format(t):
    d   =  t % 10
    s   = (t // 10) % 60
    m   =  t // 600
    return str(m) + ":" + str(s // 10) + str(s % 10) + "." + str(d)

# ── button handlers 
def btn_start():
    global running
    running = True
    clock.start()

def btn_stop():
    global running, attempts, precise
    if not running:
        return
    running = False
    clock.stop()
    attempts += 1
    if elapsed % 10 == 0:
        precise += 1

def btn_reset():
    global elapsed, running, attempts, precise
    clock.stop()
    running  = False
    elapsed  = 0
    attempts = 0
    precise  = 0

# ── timer 
def update():
    global elapsed
    elapsed += 1

# ── draw 
def draw(canvas):
    # background grid lines for style
    for y in range(0, 250, 50):
        canvas.draw_line((0, y), (300, y), 1, "#1a3a1a")

    # status indicator
    status_color = "lime" if running else "red"
    status_label = "● RUN" if running else "■ STP"
    canvas.draw_text(status_label, (10, 22), 16, status_color, "monospace")

    # score — top right
    score_color = "yellow" if precise > 0 else "white"
    canvas.draw_text(str(precise) + "/" + str(attempts), (200, 22), 20, score_color, "monospace")

    # main time — centred
    canvas.draw_text(format(elapsed), (38, 140), 52, "white", "monospace")

    # thin divider line
    canvas.draw_line((20, 155), (280, 155), 1, "#336633")

    # best-of note
    canvas.draw_text("hit a whole second!", (60, 185), 14, "#669966", "monospace")

# ── frame setup 
frame = simplegui.create_frame("Stopwatch: The Game", 300, 250)
frame.set_canvas_background("#0d1f0d")
frame.add_button("Start", btn_start, 100)
frame.add_button("Stop",  btn_stop,  100)
frame.add_button("Reset", btn_reset, 100)
frame.set_draw_handler(draw)

clock = simplegui.create_timer(100, update)

frame.start()
btn_reset()