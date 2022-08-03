while True:
    led.toggle(randint(0, 4), randint(0, 4))
    led.unplot(randint(0, 4), randint(0, 4))
    basic.pause(100)
