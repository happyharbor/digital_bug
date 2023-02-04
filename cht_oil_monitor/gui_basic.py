from guizero import App, Drawing

a = App(title="Digital Bug", width=800, height=480, bg="black",)
a.set_full_screen()
# a.full_screen = True

# create drawing object
d = Drawing(a, width=500, height=500)
d.rectangle(150, 125, 300, 140, color=(100,100,100), outline=3, outline_color=(160, 160, 160))
d.rectangle(150, 150, 300, 400, color=(100,100,100), outline=5, outline_color=(160, 160, 160))
d.rectangle(180, 410, 270, 420, color=(100,100,100), outline=2, outline_color=(160, 160, 160))
d.rectangle(60, 250, 150, 180, color=(100,100,100), outline=5, outline_color=(160, 160, 160))
d.rectangle(60, 350, 150, 280, color=(100,100,100), outline=5, outline_color=(160, 160, 160))
d.rectangle(300, 200, 390, 270, color=(100,100,100), outline=5, outline_color=(160, 160, 160))
d.rectangle(300, 300, 390, 370, color=(100,100,100), outline=5, outline_color=(160, 160, 160))
d.text(305, 220, "165\u2103", color="red", size=24)
d.text(75, 200, "160\u2103", color="red", size=24)
# d.text(190, 245, f"90 {chr(176)} C", color="red", size=24)
d.text(190, 245, "95\u2103", color="red", size=24)

a.display()