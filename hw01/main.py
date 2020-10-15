from Crypto.Cipher import AES

SEED = '5003485003485003'
KEY = '3005843005843005'

key_arr = bytearray(KEY, encoding='utf-8')
seed_arr = bytearray(SEED, encoding='utf-8')
dt_vector = bytearray(16)

aes_ctx = AES.new(key_arr, AES.MODE_CBC, seed_arr)

i = aes_ctx.encrypt(dt_vector)
r = aes_ctx.encrypt(i ^ seed_arr)