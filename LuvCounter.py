
import sys
import time
import math
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer




with open("DATA.txt", "r") as file:
    global D
    D = file.readlines()
    print("Monitoring: " + D[0])
    print("CountNow: " + D[1])  
    global TN
    TN = int(D[1])
    




parameter = "/avatar/parameters/" + D[0]

print("Counting: " + parameter)

duration=0.0

pv = (False,)



def print_handler(address, *args):
    #print(f"{address}: {args}")

    if args == (True,):
        global pv
        if pv == (False,):
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " Counted")
            global time_start
            time_start = time.time()
            with open("DATA.txt", "w") as file:
                global TN
                int(TN)
                TN += 1
                D[1] = str(TN)
                file.writelines(D)
                print("  Count: " + str(TN))
    elif args == (False,):
            
        if pv == (True,):
            global time_end
            time_end = time.time()
            duration = (time_end - time_start)
            print("  Duration: " + str(format(duration, ".2f")) + "s")
                
                
    pv = args


def default_handler(address, *args):
    #print(f"DEFAULT {address}: {args}")
    return
    


dispatcher = Dispatcher()
dispatcher.map(parameter, print_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 9001

print("Initialization complete")

server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever
    


