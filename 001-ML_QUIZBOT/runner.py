# Imports :
import requests as rq
import html as ht
import json as js
import random as ra
import numpy as np
import pickle as pk
import datetime as dt

print("Welcome to ML_QUIZBOT, i will answer 50 questions so you'll not have to!")

# Sources :
print("Getting sources...")
source_questions : str = 'https://opentdb.com/api.php?amount=50&type=multiple'
source_parameters : str = __file__.rpartition('\\')[0] + '\\' + 'parameters.json'

# Formatting :
print("Formatting sources...")
questions : dict[str, str] = js.loads(rq.get(source_questions).text.encode('utf-8'))['results']
with open(source_parameters) as f:
    parameters : dict[str, list[dict[str, str|int]]] = js.load(f)

# Extraction and resources :
print("Remembering...")
try:
    with open(__file__.rpartition('\\')[0] + '\\' + 'database.pkl', 'rb') as f:
        database : dict[str, np.ndarray] | list[list[int]] = pk.load(f)

except:
    database : dict[str, np.ndarray] | list[list[int]] = {
    'data' : np.array([
                        [0, 2, 23, 0],
                        [1, 1, 12, 1],
                        [0, 2, 15, 2],
                        [0, 2, 18, 3],
                        [0, 0, 20, 0],
                        [1, 2, 19, 1],
                        [0, 0, 22, 2],
                        [0, 2, 22, 3],
                        [0, 2, 22, 0],
                        [1, 0, 23, 1],
                        [0, 0, 19, 2],
                        [0, 2, 23, 3],
                        [0, 1, 23, 0],
                        [0, 0, 11, 1],
                        [1, 1, 19, 2],
                        [0, 1, 17, 3],
                        [1, 1, 19, 0],
                        [1, 0, 18, 1],
                        [1, 1, 11, 2],
                        [0, 0, 22, 3],
                        [1, 1, 18, 0],
                        [0, 2, 18, 1],
                        [1, 2, 21, 2],
                        [1, 0, 13, 3],
                        [1, 2, 11, 0],
                        [1, 2, 18, 1],
                        [1, 1, 13, 2],
                        [1, 0, 13, 3],
                        [1, 1, 11, 0],
                        [1, 1, 21, 1],
                        [0, 1, 15, 2],
                        [0, 1, 20, 3],
                        [1, 1, 17, 0],
                        [1, 1, 20, 1],
                        [1, 1, 19, 2],
                        [0, 0, 22, 3],
                        [1, 2, 17, 0],
                        [0, 1, 19, 1],
                        [0, 1, 18, 2],
                        [0, 1, 22, 3],
                        [0, 1, 12, 0],
                        [0, 1, 11, 1],
                        [1, 1, 17, 2],
                        [1, 2, 17, 3],
                        [1, 2, 18, 0],
                        [1, 1, 15, 1],
                        [1, 2, 13, 2],
                        [0, 0, 22, 3],
                        [1, 1, 18, 0],
                        [1, 0, 16, 1]]),
    'target' : np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]),
    'target_names' : ['wrong', 'correct'],
}
    
# ML Training :
from sklearn.linear_model import LogisticRegression

x = database['data']
y = database['target']

lg = LogisticRegression()
lg.fit(x, y)

# Game :
def title(repe:int, mess:str) -> None:
    print(f"{'='*(repe + len(mess))}\n{mess:=^{repe + len(mess)}}\n{'='*(repe + len(mess))}")

title(40, 'GAME START')

total_rounds = []
total_states = []
winned, losed = 0, 0
for round in enumerate(questions):
    info = list(round[1].values())
    correct = info[4]

    question, answers = info[3], [info[4], *info[5]]
    ra.shuffle(answers)
    print(f'{question} :\n---{'\n   '.join(['-'.join([str(i) for i in group]) for group in enumerate(answers)])}\n')

    current = []
    [current.append(item['id']) for item in parameters['types'] if item['name'] == info[0]]
    [current.append(item['id']) for item in parameters['difficulties'] if item['name'] == info[1]]
    [current.append(item['id']) for item in parameters['categories'] if item['name'] == ht.unescape(info[2])]

    # Selection :
    print('My answer is...')
    possible = [max(lg.predict_proba([current + [answer]])[0]) for answer in range(len(answers))]
    his_answer = possible.index(max(possible))

    # Round registering :
    current.append(his_answer)
    total_rounds.append(current)

    # Checking :
    print(f'{answers[his_answer]}\n\nIt was...')
    match correct == answers[his_answer]:
        case True:
            winned += 1
            total_states.append(1)
            print('Correct!\n')
        case False:
            losed += 1
            total_states.append(0)
            print('Wrong!\n')

# Database registering :
database['data'] = np.array(database['data'].tolist() + total_rounds)
database['target'] = np.array(database['target'].tolist() + total_states)

# Log registering :
with open(__file__.rpartition('\\')[0] + '\\' + 'history.log', 'a') as f:
    f.write(f'{dt.datetime.now()} : winned {winned}, losed {losed}\n')

# Save train state :
with open(__file__.rpartition('\\')[0] + '\\' + 'database.pkl', 'wb') as f:
    pk.dump(database, f)

title(40, f' Winned {winned}, losed {losed} ')