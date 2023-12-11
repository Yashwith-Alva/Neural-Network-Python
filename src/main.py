import basics
import num_math
import abstraction

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
    
    print()
    print("**************Abstraction*****************")
    abstraction.someExample()

if __name__ == '__main__':
    initialize()
    main()