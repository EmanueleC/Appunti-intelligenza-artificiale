# 10 bandit algorithm
from random import random, randint

def bandit(A):
    return randint(0,10)

k = 10
reward = 0

actions = []

for i in range(k):
    actions.append({'action': i, 'reward' : 0, 'step' : 0})

for i in range (100):
    if(random() < 0.5):
        max_reward = 0
        for j in range(10):
            if(max_reward < actions[j]['reward']): max_reward = j
        A = j
    else:
        A = randint(0,k-1)
    R = bandit(A)
    actions[A]['step'] = actions[A]['step'] + 1
    reward = reward + actions[A]['reward']
    actions[A]['reward'] = actions[A]['reward'] + (1/actions[A]['step'])*(R - actions[A]['reward'])
    print(reward, actions[A])
