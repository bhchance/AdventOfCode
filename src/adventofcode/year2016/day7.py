

class Node:

    def __init__(self, weight, children):
        self.weight = weight
        self.children = children




def solution(input_string):
    parent_nodes = []
    child_nodes = []
    for line in input_string.split("\n"):
        if "->" in line:
            children = line.split("-> ")[1].split(", ")
            child_nodes.extend(children)

        parent_nodes.append(line.split(" ")[0])

    answer = [pn for pn in parent_nodes if pn not in child_nodes][0]
    return answer


assert solution("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""") == "tknk"