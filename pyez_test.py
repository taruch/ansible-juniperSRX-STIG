from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from getpass import getpass

def main():
    hostname = input("Device hostname: ")
    username = input("Username: ")
    password = getpass("Password: ")

    try:
        with Device(host=hostname, user=username, password=password) as dev:
            print("Connected to device:", dev.facts["hostname"])

            # Execute some commands
            print("Retrieving software version...")
            version = dev.rpc.get_software_information()
            print(version)

    except ConnectError as err:
        print("Could not connect to device:", err)

if __name__ == "__main__":
    main()