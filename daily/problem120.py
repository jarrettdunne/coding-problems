# This problem was asked by Microsoft.

# Implement the singleton pattern with a twist. 
# First, instead of storing one instance, store two instances. 
# And in every even call of getInstance(), return the first 
#   instance and in every odd call of getInstance(), return the second instance.

class Singleton:
    __instance = None

    def __new__(cls, *args):
        if  cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

class DoubleSingleton:
    __instance_1 = None
    __instance_2 = None

    def __new__(cls, *args):
        ''''''
        # need to rememebr call state
        