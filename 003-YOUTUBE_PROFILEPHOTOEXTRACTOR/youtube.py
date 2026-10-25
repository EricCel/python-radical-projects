import requests as rq
import re

filer : str = __file__

# == Get user profile photos ==
def get_user_profile(*src:str) -> None:
    for source in src:
        # 1.Process source/sources :
        get : rq.Response = rq.get(source)
        status : int = get.status_code #type:ignore

        # 2.Identify element and user :
        found : str = re.findall(r'\"image\":\"(https://yt3.googleusercontent.com/[-0-9a-zA-Z_=]+)\"', get.text)[0].replace('=s88','=s800')
        print(found)
        user : str = re.findall(r'\"mainEntity\":{\"type\":\"Person\",\"name\":\"([-0-9a-zA-Z_]+)\"', get.text)[0]

        # 3.Extract element :
        extracted : rq.Response = rq.get(found)
        status : int = extracted.status_code #type:ignore

        # 4.Save element :
        processed : bytes = extracted.content
        path : str = filer.rpartition('\\')[0] + '\\' + user + '.png'
        with open(path, 'wb') as file: file.write(processed)

if __name__ == '__main__':
    get_user_profile('https://www.youtube.com/@ericd12345', 'https://www.youtube.com/@Youtube', 'https://www.youtube.com/@bujero54')