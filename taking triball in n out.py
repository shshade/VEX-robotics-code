def autonomous():
    drivetrain.drive_for(FORWARD, 900, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    # make sure to change the 90 degrees bc it's probably not gonna be precise like the medbot lab (pain)
    
    armMotor.spin_to_position(1200, DEGREES)
    # line 8 moves the arm so that it can reach the ball
    
    intakeMotor.spin(FORWARD)
    # line 9 takes the ball
    
    intakeMotor.stop()
    wait(2, SECONDS)
    
    intakeMotor.spin(REVERSE)
    # line 14 throws it out :D
    
    wait(2, SECONDS)
    intakeMotor.stop()
    break
