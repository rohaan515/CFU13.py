import simplegui

def draw_handler(canvas):
    #create the drawing
    #canvas.draw_point([x,y],"color")
    canvas.draw_point([50,50],"black")
    canvas.draw_point([100,50],"black")
    canvas.draw_point([40,55],"black")
    canvas.draw_point([45,60],"black")
    canvas.draw_point([55,65],"black")
    canvas.draw_point([60,70],"black")
    canvas.draw_point([70,75],"black")
    canvas.draw_point([80,75],"black")
    canvas.draw_point([85,75],"black")
    canvas.draw_point([95,70],"black")
    canvas.draw_point([100,65],"black")
    canvas.draw_point([110,55],"black")
    
    
    
    
frame = simplegui.create_frame("happy dots", 200,200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
