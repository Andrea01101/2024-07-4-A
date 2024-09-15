from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    def buildGraph(self, y: int, s):
        nodi = DAO.get_all_nodes(y, s)
        self._graph.add_nodes_from(nodi)

        for n in self._graph.nodes:
            self._idMap[n.id] = n

        archi = DAO.get_all_edges(y, s, self._idMap)
        self._graph.add_edges_from(archi)

    def getConnessa(self):
        listaC = list(nx.weakly_connected_components(self._graph))
        return len(listaC)

    def getConnessaMAX(self):
        listaS = list(nx.weakly_connected_components(self._graph))
        listaS.sort(key=lambda x: len(x), reverse=True)
        return listaS[0]

    def getAllYears(self):
        return DAO.getAllYears()

    def getAllShapes(self, y: int):
        return DAO.getAllShapes(y)

    def getNodes(self):
        return len(self._graph.nodes())

    def getEdges(self):
        return len(self._graph.edges())
