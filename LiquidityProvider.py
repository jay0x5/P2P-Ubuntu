import socket
import json
import os
import rsa
import time


def verify_client():
    #some way to verify whether its an authenticated client or not, if not then process for exchange will terminate and further actions will be taken :)
    pass


def get_info():

    while 1:
        try:   
            data = conn.recv(1024)
            datastr = data.decode()
            print(datastr)
        except:
            pass
       
    

    

def send_pub_key():
    (pubKey, privKey) = rsa.newkeys(1024)   
    pubkey = pubKey.save_pkcs1('PEM') 

    conn.sendall(str(pubkey).encode())
    conn.close()
    get_info()

   
    

    #writing it to temp json file so i can read it back as dictionary/json format, since direct conversion is not working
    # with open("exchange.json","w") as tempfile:
    #     tempfile.write(datastr)

    # jsonobj = open('exchange.json')
    # dataa = json.load(jsonobj)
    # print(dataa)
        
    # BTC_VAL = dataa["BTCREC"]
    # crypto_to_fiat_C(BTC_VAL)


def crypto_to_fiat_C(crypto_data):
    f = open('LP.json')
    data = json.load(f)
    update_Data = data
    #adding btc and deducting USD
    prev_btc = update_Data["BTC"]
    prev_usd = update_Data["USD"]

    update_Data["BTC"] = int(crypto_data) + int(prev_btc)

    usd_to_be_sent = int(crypto_data) * int(Current_BTC_Rate)


    update_Data["USD"] = int(prev_usd) - int(usd_to_be_sent)
    # print(update_Data)
    with open("LP.json", "w") as outfile:
        json.dump(update_Data, outfile)
    
    data = {"USDREC":int(usd_to_be_sent)}
    send_data = json.dumps(data)
    conn.sendall(send_data.encode())
    print("Transaction done")
    # conn.close()
    

    # if os.path.exists("temp.json"):
    #     os.remove("temp.json")

if __name__ ==  "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('localhost', 50000))

    Current_BTC_Rate = "100" #Hypothetical

    s.listen(1)
    conn, addr = s.accept()
    verify_client()
    send_pub_key()
    
