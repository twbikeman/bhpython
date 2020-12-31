import sys

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0



def usage():

    print("BHP NET TOOL")
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    


    try:
        opts, args = getopt.getop(sys.argv[:1])
    except getopt.GetoptError as err:
        print(str(err))
        usage()


if __name__ == '__main__':
    main()
