from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image, ImageDraw, ImageGrab, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Painter')
root.geometry("1366x768")

brush_color = "black"

def paint(e):
    # Brush parameters
    brush_width = int(my_slider.get())
    #brush_color = 'cyan'
    # brush type : BUTT, ROUND, PROJECTING
    brush_type2 = brush_type.get()

    # starting point
    x1, y1 = e.x - 1, e.y - 1
    # ending point
    x2, y2 = e.x + 1, e.y + 1
    # draw on the canvas
    my_canvas.create_line(x1, y1, x2, y2, fill = brush_color,width = brush_width, capstyle = brush_type2,  smooth = True)

def change_brush_size(thing):
    #change the size of brush
    slider_label.config(text = int(my_slider.get()))

def change_brush_color():
    #change the brush color
    global brush_color
    brush_color = colorchooser.askcolor(color = brush_color)[1]

def change_canvas_color():
    global bg_color
    bg_color = colorchooser.askcolor(color = brush_color)[1]
    my_canvas.config(bg = bg_color)

def clear_screen():
    # Clear the canvas area
    my_canvas.delete(ALL)
    my_canvas.config(bg = 'white')

def save_as_png():
    # Save the image as PNG
    result = filedialog.asksaveasfilename(initialdir = 'C:/Users/Public/Pictures', filetypes = (("png files", "*.png"), ("all files", "*.*")))

    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'

    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)

        #pop up success message
        messagebox.showinfo("Image Saved", "Your image has been saved :)")



#create canvas
w = 600
h = 400
my_canvas = Canvas(root, width = w, height = h, bg = "white" )
my_canvas.pack(pady=20)


my_canvas.bind('<B1-Motion>', paint)

# create a brush options frame
brush_options = Frame(root)
brush_options.pack(pady=20)

# brush size
brush_size_frame = LabelFrame(brush_options, text = "Brush Size")
brush_size_frame.grid(row = 0, column = 0, padx = 50)
# brush slider
my_slider = ttk.Scale(brush_size_frame, from_ = 1, to = 100, command = change_brush_size, orient = VERTICAL, value = 10)
my_slider.pack(pady = 10, padx = 10)
#brush slider laber
slider_label = Label(brush_size_frame, text = my_slider.get())
slider_label.pack(pady = 5)

# brush type
brush_type_frame = LabelFrame(brush_options, text = "Brush Type", height = 400)
brush_type_frame.grid(row = 0, column = 1, padx = 50)

brush_type = StringVar()
brush_type.set("round")

# create radio buttons for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text = "Round", variable = brush_type, value= "round")
brush_type_radio2 = Radiobutton(brush_type_frame, text = "Slash", variable = brush_type, value= "butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text = "Diamond", variable = brush_type, value= "projecting")

brush_type_radio1.pack(anchor = W)
brush_type_radio2.pack(anchor = W)
brush_type_radio3.pack(anchor = W)

# change colors
change_colors_frame = LabelFrame(brush_options, text = "Change Color")
change_colors_frame.grid(row = 0, column = 2)

# change brush color button
brush_color_button = Button(change_colors_frame, text = "Brush Color", command=change_brush_color)
brush_color_button.pack(pady = 10, padx = 10)

# Change canvas color
canvas_color_button = Button(change_colors_frame, text = "Canvas Color", command=change_canvas_color)
canvas_color_button.pack(pady = 10, padx = 10)

# program options frame
options_frame = LabelFrame(brush_options, text = "Program Options")
options_frame.grid(row = 0, column = 3)

# clear screen button
clear_button = Button(options_frame, text = "Clear Screen", command = clear_screen)
clear_button.pack(padx = 10, pady = 10)

# save image
save_image_button = Button(options_frame, text = "Save to PNG", command = save_as_png)
save_image_button.pack(pady = 10, padx = 10)

root.mainloop()