import socket
import time
import threading


def defense_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    
 
    ip_attempts = {}

    while True:
        try:
            client_sock, addr = server.accept()
            ip = addr[0]
            current_time = time.time()

            if ip not in ip_attempts:
                ip_attempts[ip] = []

          
            ip_attempts[ip].append(current_time)

            
            ip_attempts[ip] = [t for t in ip_attempts[ip] if current_time - t < 3]

        
            if len(ip_attempts[ip]) > 4:
                print(f"Alet ! a port scanning attempt was detected , the suspect ip : {ip}")
            else:
                print(f"nothing wrong from the ip : {ip}")

            client_sock.close()
        except Exception as e:
            break


def attack_scanner(target='127.0.0.1', target_port=9999):
    print(f"Sending packet attempt to {target_port}...")
    

    for i in range(6):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target, target_port))
            s.close()
        except:
            pass
        time.sleep(0.2) 


if __name__ == "__main__":

    server_thread = threading.Thread(target=defense_server, daemon=True)
    server_thread.start()

 
    time.sleep(1)

    attack_scanner()

  
    time.sleep(2)