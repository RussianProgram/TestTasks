import hashlib
from websocket import create_connection
import hmac

def hmac_encode(msg):
    key = 'n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx'
    byte_key = bytes(key, 'UTF-8')
    message = msg.encode()
    h = hmac.new(byte_key, message, hashlib.sha256)
    return h.digest()


if __name__=='__main__':
    ip = "ws://46.229.214.188/"
    ws = create_connection(ip)
    ws.recv() # b'Key: n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx'
    ws.recv() # b'Sign your email with HMAC256 and send it back'
    ws.recv() # b'<email>:<hmac(email)>'
    ws.recv() # b'Example:'
    ws.recv() # b'user@example.com:{i\x89E\n\x82\xb2L\r\x92\xb8\x92\xc0\xac-eoT\xabIOwz\t\xf9U\x17Ea{\xf7F'

    email = 'k....n.k.......v@mail.ru:'
    email_hmac = hmac_encode(email[:-1])

    result_send = bytes(email.encode()) + email_hmac

    ws.send(result_send)

    print('sended')
    print(ws.recv())

    ws.close()


