import web
from web import form
import RPi.GPIO as GPIO

#dont bug me with warnings
GPIO.setwarnings(False)

# to use Raspberry Pi bcm numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channels
GPIO.setup(28, GPIO.OUT)  # Green
GPIO.setup(29, GPIO.OUT)  # Red
GPIO.setup(30, GPIO.OUT)  # Blue

# Green LED at pin 28, 500 Hz
G = GPIO.PWM(28, 500)
# Start off
G.start(100)
R = GPIO.PWM(29, 500)
R.start(100)
B = GPIO.PWM(30, 500)
B.start(100)

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("Red",
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 0', lambda x: int(x) >= 0),
        form.Validator('Must be less than 100', lambda x: int(x) <= 100)),
    form.Textbox("Green",
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 0', lambda x: int(x) >= 0),
        form.Validator('Must be less than 100', lambda x: int(x) <= 100)),
    form.Textbox("Blue",
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 0', lambda x: int(x) >= 0),
        form.Validator('Must be less than 100', lambda x: int(x) <= 100)),
    #form.Textarea('moe'),
    #form.Checkbox('curly'),
    #form.Dropdown('french', ['mustard', 'fries', 'wine']))
    )


class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            G.ChangeDutyCycle(int(form.d.Green))
            R.ChangeDutyCycle(int(form.d.Red))
            B.ChangeDutyCycle(int(form.d.Blue))
            #return "Grrreat success! boe: %s, bax: %s" %
            #(form.d.boe, form['bax'].value)
            return render.formtest(form)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
