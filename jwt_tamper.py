import base64
import string

mode = 'encode'
#mode = 'decode'

#Results can be verified against jwt tool on official site
#https://jwt.io/

def padding_check(jwt_token):
    #Check token module (base64 needs to be module 4 length)
    padding_needed = len(jwt_token) % 4
    if (padding_needed != 0):
        print("Token section Missing :" + str(padding_needed))
        print("Adding padding due to token corruption")
        jwt_token += ('=' * (4 - padding_needed))
        return jwt_token
    else:
        return jwt_token
if (mode == 'decode'):
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6ImFkYW0xIiwiaWF0IjoiMTQ5MDE2MDI5MyJ9.MjlkYmYyOGU2NmU2ZWRkYTg5NTdjNWRjM2NjYjM3YzUzZDEwODM3YTQwYzkzNzU0YzA0YTdlMDE5Yzk4OTVhZQ"
    jwt_sections = str.split(jwt_token, ".")

    print("[x]Header (Algorithm and Token Type)")
    jwt = padding_check(jwt_sections[0])
    print("Encoded:  ")
    print(jwt)
    print("Decoded:  ")
    print(base64.urlsafe_b64decode(jwt))
    print('\n')
    print("[x]Payload (Data)")
    jwt = padding_check(jwt_sections[1])
    print("Encoded:  ")
    print(jwt)
    print("Decoded:  ")
    print(base64.urlsafe_b64decode(jwt))
    print('\n')
    print("[x]Verification Signature")
    jwt = (jwt_sections[2])
    print("Encoded:  ")

    print(jwt)
    #print(base64.urlsafe_b64decode(jwt_sections[0]))
if (mode == 'encode'):
    jwt_header= b'{"alg": "None","typ": "JWS"}'
    jwt_payload=b'{"login": "admin","iat": "1490155687"}'
    jwt_sig=b''
    print("[x]Header (Algorithm and Token Type)")
    jwt_header_encoded = base64.urlsafe_b64encode(jwt_header)
    print("Decoded:  ")
    print(jwt_header)
    print("Encoded:  ")
    print(jwt_header_encoded)

    print("[x]Payload (Data)")
    jwt_payload_encoded = base64.urlsafe_b64encode(jwt_payload)
    print("Decoded:  ")
    print(jwt_payload)
    print("Encoded:  ")
    print(jwt_payload_encoded)

    print("[x]Verification Signature")

    print("Encoded:  ")
    print(base64.urlsafe_b64encode(jwt_sig))
    print("JWT Token:")
    print(bytes.decode(jwt_header_encoded)+'.'+bytes.decode(jwt_payload_encoded)+'.'+bytes.decode(jwt_sig))
