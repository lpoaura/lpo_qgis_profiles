from qgis.core import QgsFeatureRequest, QgsProject
from qgis.PyQt.QtWidgets import QComboBox, QPushButton
from qgis.utils import iface


def openProject():
    iface.showAttributeTable((QgsProject.instance().mapLayersByName("Communes"))[0])
    toolBar = iface.mainWindow().addToolBar("My Toolbar")
    toolBar.setObjectName("My Toolbar")

    countryCombo = QComboBox(toolBar)
    toolBar.addWidget(countryCombo)
    countryCombo.setToolTip("Select a country")

    filterButton = QPushButton("Filtrer")
    filterButton.setToolTip("Filtrer")
    toolBar.addWidget(filterButton)

    resetButton = QPushButton("Sans Filtre")
    resetButton.setToolTip("Sans Filtre")
    toolBar.addWidget(resetButton)

    # We want to sort the layer by country names
    # configure QgsFeatureRequest and use it with getFeatures()
    request = QgsFeatureRequest()
    clause = QgsFeatureRequest.OrderByClause("Nom")
    orderby = QgsFeatureRequest.OrderBy([clause])
    request.setOrderBy(orderby)
    layer = (QgsProject.instance().mapLayersByName("intervenant"))[0]

    # Read the country names and save in a list
    list_prenom = []
    for f in layer.getFeatures(request):
        name = f["tab_theme"]
        if name:
            for n in name:
                if n not in list_prenom:
                    list_prenom.append(n)

    # Add items to the combobox
    for country in list(set(list_prenom)):  ##list(set()) supprime les doublons
        countryCombo.addItem(country)

    # Define functions to apply and reset filters
    def filter_layer():
        # layer = iface.activeLayer()
        country = countryCombo.currentText()
        expression = "('{}' = ANY(\"tab_theme\"))".format(country)
        layer.setSubsetString(expression)

    def reset_layer():
        # layer = iface.activeLayer()
        layer.setSubsetString("")
        countryCombo.clear()
        for country in list(set(list_prenom)):  ##list(set()) supprime les doublons
            countryCombo.addItem(country)

    filterButton.clicked.connect(filter_layer)
    resetButton.clicked.connect(reset_layer)


def saveProject():
    pass


def closeProject():
    pass
