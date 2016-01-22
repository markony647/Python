# template for "Stopwatch: The Game"

# define global variables
import simplegui

interval = 0
attempts = 0
guesses = 0
running = False




# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global interval
    interval = t
    A = interval // 600
    B = (interval // 100) % 6
    C = (interval // 10) % 10
    D = interval % 10
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button_handler():
    global running
    timer.start()
    running = True
    

def stop_button_handler():
    global running
    global attempts
    global guesses
    timer.stop()
    if interval % 10 == 0 and running == True:
        guesses += 1
        attempts += 1
    elif running == True:
        attempts += 1
    running = False
      
        
    
    
    
    
def reset_button_handler():
    global interval
    global guesses
    global attempts
    timer.stop()
    interval = 0
    gusses = 0
    attempts = 0
    
   

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global interval
    interval = interval + 1
    return interval
    
    #print interval/100
    

def guess():
    global attempts
    global guesses
    return str(guesses) + '/' + str(attempts)
    

    
    


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(interval), [100,100], 36, 'Red')
    canvas.draw_text(guess(), [240, 50], 20, 'Blue')



    
# created frame
frame = simplegui.create_frame('Stopwatch', 300, 300)

#created timer and started timer
timer = simplegui.create_timer(100, timer_handler)


#added 3 buttons
start = frame.add_button('Start', start_button_handler, 100)
stop = start = frame.add_button('Stop', stop_button_handler, 100)
reset = start = frame.add_button('Reset', reset_button_handler, 100)

#add counters
#attempts_counter = canvas.draw_text(str(attempts), [250, 50], 20, 'Blue')

# register event handlers
frame.set_draw_handler(draw_handler)



# start frame
frame.start()



# Please remember to review the grading rubric
