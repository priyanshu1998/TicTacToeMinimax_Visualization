import pickle
def get_allgames(filename):
    with open(filename) as InputFile:
        ways = InputFile.read().split('\n')

    return ways

def uni_id(w):
    ow = "".join(sorted([w[i] for i in range(0,len(w),2)]))
    ew = "".join(sorted([w[i] for i in range(1,len(w),2)]))
    return ow,ew

if __name__ == "__main__":
    allconludedgames = get_allgames('./allpossiblegames.txt')
    allgamestates = []
    
    #enlist game from start state to end state and save it in allgamestates
    for eachgame in allconludedgames:
        for i in range(len(eachgame)+1):
            allgamestates.append(eachgame[:i])
    
    state_mapping = {v:uni_id(v) for v in set(allgamestates)}

    for k,v in state_mapping.items():
        print(k,"|", v)
    # with open("state_mapping.pkl", "wb") as storeFile:
    #     pickle.dump(state_mapping, storeFile)