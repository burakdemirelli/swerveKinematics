#This example translates the X, Y and Rotation of the entire robot to individual wheels' rot and speed
#Joystick Input: X, Y, Rotation
#Output: individual wheel rotations and speeds
#sources used: https://www.chiefdelphi.com/t/paper-4-wheel-independent-drive-independent-steering-swerve/107383

import math

#rot in radians per second
rot = math.pi/4
#distance between left and right wheels
trackwidth = 12
#distance between front and rear wheels
wheelbase = 12
#the hypotenuse of the robot frame/2
r = math.sqrt(trackwidth**2+wheelbase**2)/2

#wheel class to calculate the induvidual wheel speeds and directions
class wheel:
    def __init__(self, vX, vY):
        self.vX = vector(0, 0, vX, 0)
        self.vY = vector(0, 0, 0, vY)
        self.v = combineVectors(self.vX, self.vY)

    #this returns the angle of the vector
    #!!IMPORTANT!!
    #however, it returns the same thing as getWheelAngle(), but multiplied by -1
    #there is probably something wrong with my math, as both should basically return the same thing?
    def getVectorAngle(self):
        return self.v.getAngle()
    
    #returns the speed of the wheel
    #might need to add a clamp function to scale down the speeds to use in the robot code
    def getWheelMagnitude(self):
        return self.v.getMagnitude()

    #returns the desired wheel angle
    def getWheelAngle(self):
        return math.atan2(self.vX.getMagnitude(), self.vY.getMagnitude())*180/math.pi

#a vector class to make it easier to work with vectors
class vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    #uses the pythagorean theorem to calculate the magnitude
    def getMagnitude(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

    #calculates the slope of the vector
    def getSlope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)
    
    #uses arctangent to calculate the angle of the vector.
    #coincident with x axis = 0 degrees
    #!!RETURNS IN DEGREES, NOT RADIANS!!
    def getAngle(self):
        return math.degrees(math.atan(self.getSlope()))

#combines two vectors and returns a new vector instance
def combineVectors(vector1, vector2):
    return vector(vector1.x1, vector1.y1, vector1.x2 + vector2.x2, vector1.y2 + vector2.y2)

# r_ is used to indicate the vectors of the entire robot
r_velX = vector(0, 0, 40, 0)
r_velY = vector(0, 0, 0, 10)

# a and b are the possible X vectors for wheels
# c and d are the possible Y vectors for wheels
#refer to the sources mentioned on line 4 for further info

a = r_velX.getMagnitude() - rot*wheelbase/2
b = r_velX.getMagnitude() + rot*wheelbase/2
c = r_velX.getMagnitude() - rot*trackwidth/2
d = r_velX.getMagnitude() + rot*trackwidth/2

#creates wheel instances
#the wheel config should be like this:
# wheel 1 = front right
# wheel 2 = front left
# wheel 3 = rear left
# wheel 4 = rear right

wheel1 = wheel(b, c)
wheel2 = wheel(b, d)
wheel3 = wheel(a, d)
wheel4 = wheel(a, c)

print(
    wheel1.getWheelAngle(),
    wheel1.getWheelMagnitude(),
    wheel2.getWheelAngle(),
    wheel2.getWheelMagnitude(),
    wheel3.getWheelAngle(),
    wheel3.getWheelMagnitude(),
    wheel4.getWheelAngle(),
    wheel4.getWheelMagnitude()
)