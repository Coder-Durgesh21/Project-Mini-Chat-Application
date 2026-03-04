import socket
import sys

class Server:
    @staticmethod
    def main():
        print("Server of Marvellous Chat messenger is running...")
        ssobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssobj.bind(("localhost", 2100))
        ssobj.listen(1)
        print("Server is in the listening mode at port no : 2100")
        
        sobj, addr = ssobj.accept()
        print("Client and Server connection is successful...")

        ps = sobj.makefile("w")
        br1 = sobj.makefile("r")
        br2 = sys.stdin

        print("Marvellous chat Messenger started...")

        while True:
            str1 = br1.readline()
            if not str1:
                break

            str1 = str1.strip()
            print("Client says : " + str1)
            print("Enter message for client : ")
            str2 = br2.readline().strip()
            ps.write(str2 + "\n")
            ps.flush()

        print("Thank your for using the chat messenger...")
        ssobj.close()
        sobj.close()
        ps.close()
        br1.close()

if __name__ == '__main__':
    Server.main()