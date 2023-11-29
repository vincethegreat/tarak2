# from flask import Flask, render_template, request
# import RPi.GPIO as GPIO
# import time

# app = Flask(__name__)

# # GPIO setup
# GPIO.setmode(GPIO.BOARD)
# # Define GPIO pins for motor control
# # Adjust these pins based on your hardware setup
# motor1_pwm = 12
# motor1_dir1 = 16
# motor1_dir2 = 18

# motor2_pwm = 22
# motor2_dir1 = 24
# motor2_dir2 = 26

# GPIO.setup(motor1_pwm, GPIO.OUT)
# GPIO.setup(motor1_dir1, GPIO.OUT)
# GPIO.setup(motor1_dir2, GPIO.OUT)

# GPIO.setup(motor2_pwm, GPIO.OUT)
# GPIO.setup(motor2_dir1, GPIO.OUT)
# GPIO.setup(motor2_dir2, GPIO.OUT)

# # PWM setup
# pwm1 = GPIO.PWM(motor1_pwm, 100)
# pwm2 = GPIO.PWM(motor2_pwm, 100)

# # Initial state
# pwm1.start(0)
# pwm2.start(0)

# # Define routes
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/forward")
# def forward():
#     set_motor_direction(1, 1)
#     return "Moving forward"

# @app.route("/backward")
# def backward():
#     set_motor_direction(0, 1)
#     return "Moving backward"

# @app.route("/left")
# def left():
#     set_motor_direction(1, 0)
#     return "Turning left"

# @app.route("/right")
# def right():
#     set_motor_direction(0, 0)
#     return "Turning right"

# @app.route("/stop")
# def stop():
#     pwm1.ChangeDutyCycle(0)
#     pwm2.ChangeDutyCycle(0)
#     return "Stopping"

# def set_motor_direction(left_motor, right_motor):
#     GPIO.output(motor1_dir1, left_motor)
#     GPIO.output(motor1_dir2, not left_motor)
#     GPIO.output(motor2_dir1, right_motor)
#     GPIO.output(motor2_dir2, not right_motor)
#     pwm1.ChangeDutyCycle(50)
#     pwm2.ChangeDutyCycle(50)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')



from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forward")
def forward():
    print("Car going forward")
    return "Moving forward"

@app.route("/backward")
def backward():
    print("Car going backward")
    return "Moving backward"

@app.route("/left")
def left():
    print("Turning left")
    return "Turning left"

@app.route("/right")
def right():
    print("Turning right")
    return "Turning right"

@app.route("/stop")
def stop():
    print("Stopping")
    return "Stopping"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
