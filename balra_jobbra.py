def on_button_pressed_a():
    basic.clear_screen()
    images.create_image("""
                . . . . .
                . # . . .
                # # # # .
                . # . . .
                . . . . .
    """).scroll_image(1, 500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    images.create_big_image("""
                . # . # . . # . # .
                # . # . # # # # # #
                # . . . # # # # # #
                . # . # . . # # # .
                . . # . . . . # . .
    """).scroll_image(1, 200)
input.on_button_pressed(Button.B, on_button_pressed_b)
