class trie_node:
    node_cnt = 0
    def __init__(self, data):
        trie_node.node_cnt += 1
        self.data = data
        self.link = {}



class trie_tree:
    def __init__(self):
        self.data = ""     #just a patch to keep it consist with other nodes of the  tree
        self.link = {}

    def update(self, w):
        trav = self.link
        for i in range(len(w)):
            if w[i] not in trav.keys():
                trav[w[i]] = trie_node(w[i])
            trav = trav[w[i]].link

# @vs(ignore_args = ["v_list","w"], node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
# def add(u, v_list, w):
#     # print(u, v_list)
#     for v,lis in v_list:
#         # print(lis)
#         add(v, v_list = lis.link.items(), w=w+v)
#     return w



# if __name__ == "__main__":
#     my_trie = trie_tree()

#     my_trie.update("apple")
#     my_trie.update("hello")
#     my_trie.update("helmet")
#     my_trie.update("hamlet")
#     my_trie.update("appy")

#     # print(my_trie.link)
#     # print(list(map(tuple,my_trie.link.items())))
#     add("", v_list = my_trie.link.items(), w="")
#     vs.write_image("test.png")
