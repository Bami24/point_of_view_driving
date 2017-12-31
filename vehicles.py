class Vehicle():
    def __init__(self, make, model, image, dvideo):
        """This is a class to create an instance of a vehicle"""
        print("A Vehicle instance has been created")
        self.make = make
        self.model = model
        self.image = image
        self.dvideo = dvideo

    def print_details(self):
        #prints the make and model of the vehicle
              print("The make of this vehicle is :" + self.make)
              print("The model of this vehicle is :" + self.model) 
