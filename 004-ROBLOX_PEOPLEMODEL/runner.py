import requests as rq
from time import sleep

# === Extract User and Friends Profile Photo ===
headers = {
  "Content-Type": "application/json",
  # Cookie of placeholder account :
  "Cookie": ".ROBLOSECURITY=" + '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEQAhoGCAIQBBgBIhwKBGR1aWQSFDExODk0MTQxODI1Nzc4NTc4MDQ1IhwKBXVuYW1lEhNqdXN0Zm9ydGVzdGluZ2hleXlhIhIKA3VpZBILMTE4OTEyOTM3NjgoAw.vWN3WxVtcYlYdZRCYGC38xYijyIIZMRiRa0W8LcxGfud_QBRmRTl-fvSzSq-8McJIc858OoG77Ouasl5cmT-zvSbeaW7OhOO16Q4SKkbukGGHbD8byl-ROwJhoM6fLVR0ZtJE8OxeErV4GcaHjembRe5VcNkYWakIxu2zMkPgI8Pr7bDBlMVPUBm_v_bU0LZLmnDebCXzBmKJyc1wq72zxTpgRxrsQSArZpZJDJZQHCbRU3kv8SDfoyhO24wxNt7zcK-g_ICsUuu4HgEJCydPIDmNsKknCvByDnsm9bjiyy9QyFKGgFTrvLxrjPSm7jyvGE5090E2BTCnbPprk5A4_B2FxHwHc8e4cPQvr65G-vTLSERCJ4S-zjFEW4n1oLsq6wEgc1Ex_T4XRYTF46TnBifXHr4-pMlyyBI3h6pcSQM76HZbz3Ehs-hnVjyPPejLw9ZK_VvBmeYZ66zdm15MSqx7BiywSUC1cJRo3e-z2Y1eaa1V5ViYme9--nPS1Bv74QhCQIrI7HThvuK3GdYb7pGsJ0Eb7K1EUpUA6nSDyWlt3jwOuXKWtvuChZGeFqqOBtK0e8y3-Mmrp32qYex9xjHt79-o-Z_VgGlVjLVBQZq4HA26jWgPyBDGTBtqCw6j5uWW6ofBEmVnb7HWw19I7FdbowqrPSbKsU5d18xPGMrt_PC8oLO2hi7YqBE_YQCaMimpGQ3fPL0Qp-wd8F4rmshSZBt8U9MJTPzqidgzWQMdNEFNCWq_VWEBj_4Swqk31WTvn8pj8WtE0HNj3LgJWGk0V8sNkIZPaUxLMvfT6ACJPl003mp6TY5Y4QlgUSbiD_Z3IY1izl919wvcy80_uQQJYd37SlMYX0n-vtn1Kxa6w_hQjAhsQKRL-xkLdJD.XZVJB87zVwFB-j2GY8at9J0IHlM'
}

def get_user_model(id:int, repeat:bool=False) -> None :
    try:
        us_id : int = int(id)
    except:
        raise ValueError('NOT VALID ID')
    else:
        user : rq.Response = rq.get(f'https://thumbnails.roblox.com/v1/users/avatar-3d?userId={us_id}', headers=headers)
        model : rq.Response = rq.get(user.json()['imageUrl'], headers=headers).json()['obj']
        for i in range(8):
            sleep(10)
            print('dont', 'ry', i)
            extracted : rq.Response = rq.get(f'https://t{i}.rbxcdn.com/' + model, headers=headers)
            if 'g Handle1' in extracted.text:
                print('Found')
                extracted : bytes = extracted.content
                break

        with open(__file__.rpartition('\\')[0] + '\\' + str(us_id) + '.obj', 'wb') as file :
            file.write(extracted)

        if not repeat :
            friends : rq.Response = rq.get(f'https://friends.roblox.com/v1/users/{us_id}/friends').json()
            friends : list[int] = [friend['id'] for friend in friends['data']]
            for friend in friends:
                sleep(10)
                print('go')
                get_user_model(friend, True)

if __name__ == '__main__':
    get_user_model(1894484118)