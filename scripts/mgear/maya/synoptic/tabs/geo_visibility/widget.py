import mgear.maya.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()


class Ui_baker(object):

    def setupUi(self, baker):
        baker.setObjectName("baker")
        baker.resize(325, 840)
        baker.setMinimumSize(QtCore.QSize(325, 790))
        self.gridLayout = QtWidgets.QGridLayout(baker)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = ToggleGeoVisibility(baker)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(baker)
        QtCore.QMetaObject.connectSlotsByName(baker)

    def retranslateUi(self, baker):
        baker.setWindowTitle(gqt.fakeTranslate("baker", "Form", None, -1))
        self.widget.setProperty("geo_root", gqt.fakeTranslate("baker", "geo_root", None, -1))

from mgear.maya.synoptic.toggleGeoVisibilityWidget import ToggleGeoVisibility
