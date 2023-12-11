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
    num_math.batchedNeurons()
    print("\nMulti-Layer Nuerons")
    num_math.multiLayerNeurons()
    

if __name__ == '__main__':
    initialize()
    main()