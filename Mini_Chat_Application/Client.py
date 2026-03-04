import socket
import sys

class Client:
    @staticmethod
    def main():
        print("Client of Marvellous Chat messenger is running...")
        sobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sobj.connect(("localhost", 2100))
        print("Client is waiting for server to accept the request...")

        ps = sobj.makefile("w")
        br1 = sobj.makefile("r")
        br2 = sys.stdin

        print("Marvellous Chat Messanger started...")

        while True:
            str1 = br2.readline().strip()
            if str1 == "end":
                break

            ps.write(str1 + "\n")
            ps.flush()

            print("Enter message for server : ")
            str2 = br1.readline().strip()
            print("Server says : " + str2)

        print("Thank you for using Marvellous chat messenger...")
        sobj.close()
        ps.close()
        br1.close()

if __name__ == '__main__':
    Client.main()