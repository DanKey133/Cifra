# TODO решите задачу
import json

def task() -> float:
    s = 0
    with open('input.json') as file:
        score_weights = json.load(file)
    for i in score_weights:
        s  += i['score'] * i['weight']
    return s

print(f'{task():.3f}')
