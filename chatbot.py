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
    friend = False
    while not friend:
        print("Oh, it's quite simple. If you are a friend, you speak the password, and the doors will open.")
        pattern = input("> ")
        if pattern.lower() in ['melon', 'mellon']:
            print("Good to see you, 111 years old! Who would believe it? You haven't aged a day.")
            friend = True

    while not done and friend:


        #Store pattern
        pattern = input("> ")

        # disable the alarm after success

        #Check if user wants to quit
        if pattern.lower() in ['q', 'quit']:
            done = True
            continue
        response = k.respond(pattern)
        print(response)
    
    print("My time is over: it is no longer my task to set things to rights, nor to help other folk to do so")
    print("Well, here at last, dear friends, on the shores of the Sea comes the end of our fellowship in Middle-earth. Go in peace!")
    exit(0)