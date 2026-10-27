import requests as rq
import re

# === Scratch to Turbowarp, Return Link ===
def scratch_to_turbo(user:str) -> dict[str, str] | str:
    try:
        # 1.Get user page from input :
        us_site : str = rq.get(f'https://scratch.mit.edu/users/{user}/projects/').text
    except:
        # FAILSAFE :
        return "User doesn't exists!\nTry another..."
    else:
        # 2.Identify info :
        finder : re.Pattern[str] = re.compile(r'<a href="/projects/([0-9]+)/">(.+)</a>')
        found : list[tuple[str, str]] = finder.findall(us_site)
        # 3.Create dict with name as key, link as value :
        converted : dict[str,str] = {game[1]:f'https://turbowarp.org/{game[0]}/embed' for game in found}
        # 4.Return dict of links :
        return converted

if __name__ == '__main__':
    print(scratch_to_turbo('griffpatch'))