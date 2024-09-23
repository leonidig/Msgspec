import msgspec


json_encode = msgspec.json.encode({"hello": "world"})
msgspec_encode = msgspec.msgpack.encode({"hello": "world"})
print(f'JSON -> {json_encode}\nmsgspec -> {msgspec_encode}\n')


json_decode = msgspec.json.decode(b'{"hello":"world"}')
msgspec_decode = msgspec.msgpack.decode(b'\x81\xa5hello\xa5world')
print(f"JSON decode -> {json_decode}\nMsgspec decode -> {msgspec_decode}")