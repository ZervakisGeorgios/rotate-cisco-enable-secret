import paramikoModule
import threading
import time
import utils


def rotate_pass(router, secret):
    client = paramikoModule.connect(**router)
    shell = paramikoModule.get_shell(client)

    paramikoModule.send_command(shell, 'conf t')
    paramikoModule.send_command(shell, f'enable secret {secret}')
    paramikoModule.send_command(shell, 'wr')

    # afto to output ine me mia grammi keno anamesa stis grammes kai afto thelume na min to exume
    output = paramikoModule.show(shell)
    # print(output)
    # edo pera spame to output se list apo strings oste na xefortothume to keno "\n"
    output_list = output.splitlines()
    # print(output_list)
    # edo we use the string function join() gia na enosume ta list items sto keno "\n"
    output = '\n'.join(output_list)
    # print(output)
    # save changes in individual txt files
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    # if needed, more options can be used
    # hour = now.hour
    # minute = now.minute
    # seconds = now.second

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
    with open(file_name, 'w') as f:
        f.write(output)

    paramikoModule.close(client)
    time.sleep(5)


while True:
    # Calls Georgios's banner
    utils.banner()
    # Provides the menu options to the user
    answer = utils.menu()

    if answer == '1':

        # Rather than storing creds in the code. Call the get_creds method to get them
        # it will return a dictionary consisting of the username & password variables
        credentials = utils.get_creds()
        # gets the new secret
        secret = utils.get_secret()

        # creating a dictionary for each device to connect to. It could read from a file the IPs...
        # add more routers as needed
        router1 = {
            'server_ip': '10.x.x.x', 'server_port': '22', 'user': credentials["username"], 'passwd': credentials["password"]}
        # in case we need to stores the credentials locally on the code
        # router1 = {'server_ip': '10.x.x.x', 'server_port': '22', 'user': '', 'passwd': ''}

        # creating a list of dictionaries (of devices)
        routers = [router1]

        # creating an empty list (it will store the threads)
        threads = list()
        for router in routers:
            # creating a thread for each router that executes the backup function
            th = threading.Thread(target=rotate_pass, args=(router, secret,))
            threads.append(th)  # appending the thread to the list

        # starting the threads
        for th in threads:
            th.start()

        # waiting for the threads to finish
        for th in threads:
            th.join()
    else:
        print("\n*** Not supported button. Please, try again ***\n")
        time.sleep(2)
