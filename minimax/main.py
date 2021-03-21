'''
    TIC TAC TOE AI.

    MINMAX is applied on the graph that represent all possible games.

    +1: 'X' wins
    -1: 'O' wins
     0:  Draw 

'''
import pickle
from trie import trie_node, trie_tree
from vis import Visualiser as vs
from game_list import did_some1_win, gen_grid
from collections import defaultdict

mapped_val = {"O": -1, "X": 1, "Draw":0 }
inv_map = {-1:"O", 1:"X", 0:"Draw"}
statemapping = None


graph = {}
@vs(ignore_args=["root", "action_list", "maximizingPlayer"], node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def minimax(pos, root, action_list , maximizingPlayer = True):
    '''
        Return the path taken by the player.
    '''
    if(root.data != ""):
        graph.setdefault(uni_id(action_list), set()).add(action_list+root.data)

    #if at the end of the game
    if len(root.link) == 0:
        # print(action_list+root.data)
        if did_some1_win(gen_grid(map(int,action_list+root.data))):
            if maximizingPlayer:
                return "O"
            else:
                return "X"

        return "Draw"

    if maximizingPlayer:
        maxEval = -1

        for child_data, child_link in root.link.items():
            pos = (int(child_data)//3, int(child_data)%3)
            winner = minimax(pos, root=child_link, action_list=action_list+root.data, maximizingPlayer=False)
            v = mapped_val[winner]
            maxEval = max(maxEval, v)
        return inv_map[maxEval]

    else:
        minEval = +1

        for child_data, child_link in root.link.items():
            pos = (int(child_data)//3, int(child_data)%3)
            winner = minimax(pos, root=child_link, action_list=action_list+root.data, maximizingPlayer=True)
            v = mapped_val[winner]
            minEval = min(minEval, v)
        return inv_map[minEval]

    raise Exception #should not reach this point program should enter the else and return

def uni_id(w):
    ow = "".join(sorted([w[i] for i in range(0,len(w),2)]))
    ew = "".join(sorted([w[i] for i in range(1,len(w),2)]))
    return ow,ew

def get_allgames(filename):
    with open(filename) as InputFile:
        ways = InputFile.read().split('\n')

    return ways
    
if __name__ == "__main__":
    allgames = get_allgames('./test_inp.txt')
    tree = trie_tree()

    for each_game in allgames:
        tree.update(each_game)

    with open("./state_mapping.pkl", "rb") as loadFile:
        statemapping = pickle.load(loadFile)


    # id_mapping = {v:k for k,v in enumerate(statemapping.values())}
    # print(set(statemapping.values()))
    minimax((),tree, "", True)

    vs.write_image("minmax.png")

    # for k, v  in graph.items():
    #     print(k,v)
    
    
