import socket,keyboard
serverAddressPort = ("192.168.137.224", 9999)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
thr = 0
kp = 175
ki = 15
kd = 121
data = ""
DATA = ""
prevDATA = DATA
yaw = 50
while True:
        prevdata = data
        roll = 50
        pitch = 50
        key = keyboard.get_hotkey_name()
        if key == "/":
                pitch = 70
        elif key == "1":
                if kp > 0:
                    kp -= 0.001

        elif key == "2":
                if ki > 0:
                    ki -= 0.001

        elif key == "3":
                if kd > 0:
                    kd -= 0.001

        elif key == "4":
                if kp < 600:
                    kp += 0.001
        elif key == "5":
                if ki < 600:
                    ki += 0.001
        elif key == "6":
                if kd < 600:
                    kd += 0.001
        elif key == "7":
                roll = 20
        elif key == "8":
                pitch = 20
        elif key == "9":
                roll = 70
        elif key == "a":
                if thr > 0:
                    thr = thr - 0.001

        elif key == "enter":
                kp = 175
                ki = 15
                kd = 121
        elif key == "q":
                if thr < 100:
                    thr = thr + 0.001
        data = str(roll) + str(pitch) + str(round(thr)) + str(yaw)
        datachar = chr(roll) + chr(pitch) + chr(int(round(thr))) + chr(yaw)
        if data != prevdata:
                UDPClientSocket.sendto(datachar.encode(),serverAddressPort)
                print("trans: ", data)
                print("trans_c: ", datachar)

        recvdata = UDPClientSocket.recv(10)
        # print("recv: ", recvdata)
