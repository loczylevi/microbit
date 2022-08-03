def on_button_pressed_a():
    for index in range(4):
        basic.show_leds("""
                        # . # . .
                        . # # # .
                        . . # . #
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
                        . # # . .
                        . # # # .
                        . . # . #
                        . # . # .
                        . # . # .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

# balra dőlés______________________________________________---

def on_gesture_tilt_left():
    for index3 in range(4):
        basic.show_leds("""
                        # . # . .
                        . # # # .
                        . . # . #
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
                        . # # . .
                        . # # # .
                        . . # . #
                        . # . # .
                        . # . # .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    for index4 in range(4):
        basic.show_leds("""
                        # . # . #
                        . # # # .
                        . . # . .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
                        . # # # .
                        . # # # .
                        . . # . .
                        . # . # .
                        . # . # .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index5 in range(4):
        basic.show_leds("""
                        . . # . #
                        . # # # .
                        # . # . .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
                        . . # # .
                        . # # # .
                        # . # . .
                        . # . # .
                        . # . # .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

# jobbra dőlés______________________________________________---

def on_gesture_tilt_right():
    for index6 in range(4):
        basic.show_leds("""
                        . . # . #
                        . # # # .
                        # . # . .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
                        . . # # .
                        . # # # .
                        # . # . .
                        . # . # .
                        . # . # .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

# lefelé dőlés______________________________________________---

def on_gesture_logo_down():
    for index7 in range(4):
        basic.show_leds("""
                        # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
        basic.show_leds("""
                        # . # . #
                        . # . # .
                        # . # . #
                        . # . # .
                        # . # . #
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

# felfelé dőlés______________________________________________---

def on_gesture_logo_up():
    for index2 in range(4):
        basic.show_leds("""
                        . . . . .
                        . . # . .
                        . # # # .
                        . . # . .
                        . . . . .
        """)
        basic.show_leds("""
                        . . # . .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . # . .
        """)
    basic.show_leds("""
                . . # . .
                . # # # .
                # . # . #
                . # . # .
                . # . # .
    """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        . # . # .
        . # . # .
""")
