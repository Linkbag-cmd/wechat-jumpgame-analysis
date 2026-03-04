import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
 
# sessionid
session_id = "your sessionid"
 
# 整个明文 JSON（直接复制粘贴）
outer_json = {'score': 198, 'times': 9, 'game_data': '。。。。。。'}
 
# 生成 actionData
def encrypt_action_data(session_id: str, data_dict: dict) -> str:
    key = session_id[:16].encode('utf-8')   # Key 和 IV 完全一样
    iv = key
    
    # 注意：必须用 separators=(',', ':') 去掉空格，否则服务器可能校验失败
    plaintext = json.dumps(data_dict, separators=(',', ':')).encode('utf-8')
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded)
    
    return base64.b64encode(ciphertext).decode('utf-8')
 
action_data = encrypt_action_data(session_id, outer_json)
print("生成的 actionData：")
print(action_data)
