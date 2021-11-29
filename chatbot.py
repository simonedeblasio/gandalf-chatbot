#Check that aiml for python is installed through pip
try:
    import aiml
except ModuleNotFoundError:
    print("ERROR: AIML interpreter not installed")
    print("Install by typing:") 
    print('\tpython3 -m pip install python-aiml')
    exit(1)

#Import sys so that we can read filename from the commandline
import sys

if __name__ == '__main__':
    #Check that a filename is specified
    if len(sys.argv) < 2:
        print('ERROR: No file specified')
        print(f'Usage: python3 {sys.argv[0]} [name of aiml file]')
        exit(1)
    #Extract file name from command line argument
    filename = sys.argv[1]

    #The aiml library has bad error checking so lets check that 
    #the file actually exists
    try:
        open(filename, 'r')
    except FileNotFoundError:
        print(f"ERROR: No file found with name {filename}")
        exit(1)
        
    #Create instance of aiml kernel
    k = aiml.Kernel()
    #Have kernel read from file
    k.learn(filename)
    
    #Run the actuall chatbot
    done = False
    print("Lets make a pizza!")
    print("What part do you want to start with?")
    print("Dough or sauce?")


    print("To quit enter 'q'")
    while not done:
        #Store pattern
        pattern = input("> ")
        #Check if user wants to quit
        if pattern.lower() in ['q', 'quit']:
            done = True
            continue
        response = k.respond(pattern)
        print(response)
    exit(0)