from datetime import datetime
import socket

def printTime(s= ""):
    print("[" + datetime.now().strftime("%H:%M:%S") + "] ", end= "")
    if (s == ""): return
    print(s)

HOST = "0.0.0.0"
PORT = 9217

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(3)

while True:

    conn, addr = soc.accept()
    printTime("NEW CONNECTION FROM " + str(addr))

    trader_id = conn.recv(1024).decode().strip("\n\r")
    printTime("CLIENT: " + trader_id)

    try:
        html_file = open("html/" + trader_id + ".html", "r")
        html_file_lines = html_file.readlines()
    except:
        printTime("SERVER: ERROR")
        conn.send("ERROR\n".encode())
        conn.close()
        continue

    printTime("SERVER: " + "BEGIN")
    conn.send("BEGIN\n".encode())

    for line in html_file_lines:
        line = line.strip("\n\r")
        printTime("HTML: " + line)
        conn.send((line + "\n").encode())

    printTime("SERVER: END")
    conn.send("END\n".encode())
    conn.close()
