import flet as ft
import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        y = self._view.ddyear.value
        s = self._view.ddshape.value
        self._model.buildGraph(y, s)
        self._view.txt_result1.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero vertici: {self._model.getNodes()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero archi: {self._model.getEdges()}"))

        self._view.txt_result1.controls.append(ft.Text(f"Numero componenti connesse: {self._model.getConnessa()}"))
        listaS = self._model.getConnessaMAX()
        for s in listaS:
            self._view.txt_result1.controls.append(ft.Text(s))

        self._view.update_page()



    def handle_path(self, e):
        pass

    def fillDD(self):
        years = self._model.getAllYears()
        for y in years:
            self._view.ddyear.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def handleDDShape(self, e):
        self._view.ddshape.options.clear()
        self._view.ddshape.value = None
        year = self._view.ddyear.value
        shapes = self._model.getAllShapes(year)
        for s in shapes:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()
