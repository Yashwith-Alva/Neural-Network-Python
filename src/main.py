import basics
import num_math

def initialize():
    pass

def main():
    print("**************BASIC**********************")
    basics.singleNeuron()
    basics.layeredNeuron()
    
    print()
    print("**************NUMPY*****************")
    num_math.layeredNeuron()
    

if __name__ == '__main__':
    initialize()
    main()