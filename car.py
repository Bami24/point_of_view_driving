from vehicles import Vehicle

class Car(Vehicle):
    """This is a class to create an instance of a car"""
    print("A Car instance has been created")
    def __init__(self, make, model, image, dvideo, rdvideo):
        Vehicle.__init__(self, make, model, image, dvideo)
        #Additional variable rdvideo for right hand drive videos
        self.rdvideo = rdvideo

