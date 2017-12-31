from vehicles import Vehicle


class MotorBike(Vehicle):
    """This is a class to create an instance of a motorbike"""
    print("A Motorbike instance has been created")

# This is a MotorBike class which inherits from class Vehicle
# at the moment it does not have any additional variables

    def __init__(self, make, model, image, dvideo):
        Vehicle.__init__(self, make, model, image, dvideo)
# seperate class created to make scaling the project easier
