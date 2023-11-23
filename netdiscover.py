import requests
import threading

def ip_scanner(ip):

    try:
        ip = f"http://192.168.1.{ip}"
        ip2 = f"http://10.0.2.{ip}"
        sonuç = requests.get(ip,timeout=3).status_code
        if sonuç == 200:
            print(ip)
        else:
            sonuç = requests.get(ip2,timeout=3).status_code
            if sonuç == 200:
                print(ip2)
    except:
        pass

def rastgele():
    for ip in range(256):
        başla = threading.Thread(target=ip_scanner,args=(ip,))
        başla.start()

if __name__ == "__main__":
    rastgele()
