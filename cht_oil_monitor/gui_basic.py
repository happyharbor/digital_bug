from guizero import App, Drawing

a = App(title="Digital Bug", height=500, width=500)

# create drawing object
d = Drawing(a, width=500, height=500)
d.rectangle(50, 50, 300, 300, color="light blue")
d.rectangle(20, 30, 120, 120, color="grey")
d.line(50, 180, 50, 160, color="red", width=5)


a.display()