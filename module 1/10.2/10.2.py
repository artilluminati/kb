import turtle
tr = turtle.Turtle()
wn = turtle.Screen()

password = "nosokBobra228"

for i in range(100):
    if input('пароль: ') == password:
        wn.addshape('img.jpg')
        tr.shape('img.jpg')
        break
    else:
        print('попробуйте снова')


wn.mainloop()