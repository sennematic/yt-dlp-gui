# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowpDkNAO.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.requiredFieldsBox = QGroupBox(self.centralwidget)
        self.requiredFieldsBox.setObjectName(u"requiredFieldsBox")
        self.requiredFieldsBox.setGeometry(QRect(0, 0, 791, 352))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requiredFieldsBox.sizePolicy().hasHeightForWidth())
        self.requiredFieldsBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.requiredFieldsBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveFileOptionsContainer = QGroupBox(self.requiredFieldsBox)
        self.saveFileOptionsContainer.setObjectName(u"saveFileOptionsContainer")
        self.gridLayout_2 = QGridLayout(self.saveFileOptionsContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.saveFileNameLabel = QLabel(self.saveFileOptionsContainer)
        self.saveFileNameLabel.setObjectName(u"saveFileNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveFileNameLabel.sizePolicy().hasHeightForWidth())
        self.saveFileNameLabel.setSizePolicy(sizePolicy1)
        self.saveFileNameLabel.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.saveFileNameLabel, 0, 0, 1, 1)

        self.saveFileLocationLabel = QLabel(self.saveFileOptionsContainer)
        self.saveFileLocationLabel.setObjectName(u"saveFileLocationLabel")

        self.gridLayout_2.addWidget(self.saveFileLocationLabel, 1, 0, 1, 1)

        self.saveFileLocationBox = QLineEdit(self.saveFileOptionsContainer)
        self.saveFileLocationBox.setObjectName(u"saveFileLocationBox")

        self.gridLayout_2.addWidget(self.saveFileLocationBox, 1, 1, 1, 1)

        self.SaveFileLocationSearchButton = QPushButton(self.saveFileOptionsContainer)
        self.SaveFileLocationSearchButton.setObjectName(u"SaveFileLocationSearchButton")

        self.gridLayout_2.addWidget(self.SaveFileLocationSearchButton, 1, 2, 1, 1)

        self.saveFileNameInput = QPlainTextEdit(self.saveFileOptionsContainer)
        self.saveFileNameInput.setObjectName(u"saveFileNameInput")
        sizePolicy.setHeightForWidth(self.saveFileNameInput.sizePolicy().hasHeightForWidth())
        self.saveFileNameInput.setSizePolicy(sizePolicy)
        self.saveFileNameInput.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.saveFileNameInput, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.saveFileOptionsContainer, 1, 0, 1, 1)

        self.VideoSourceBox = QGroupBox(self.requiredFieldsBox)
        self.VideoSourceBox.setObjectName(u"VideoSourceBox")
        self.VideoSourceBox.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout = QHBoxLayout(self.VideoSourceBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pasteURLLabel = QLabel(self.VideoSourceBox)
        self.pasteURLLabel.setObjectName(u"pasteURLLabel")
        sizePolicy1.setHeightForWidth(self.pasteURLLabel.sizePolicy().hasHeightForWidth())
        self.pasteURLLabel.setSizePolicy(sizePolicy1)
        self.pasteURLLabel.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.pasteURLLabel)

        self.pasteURLInput = QPlainTextEdit(self.VideoSourceBox)
        self.pasteURLInput.setObjectName(u"pasteURLInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pasteURLInput.sizePolicy().hasHeightForWidth())
        self.pasteURLInput.setSizePolicy(sizePolicy2)
        self.pasteURLInput.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.pasteURLInput)


        self.gridLayout.addWidget(self.VideoSourceBox, 0, 0, 1, 1)

        self.optionalFieldsContainer = QGroupBox(self.centralwidget)
        self.optionalFieldsContainer.setObjectName(u"optionalFieldsContainer")
        self.optionalFieldsContainer.setGeometry(QRect(0, 360, 791, 201))
        self.gridLayout_3 = QGridLayout(self.optionalFieldsContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.selectFileTypeLabel = QLabel(self.optionalFieldsContainer)
        self.selectFileTypeLabel.setObjectName(u"selectFileTypeLabel")
        sizePolicy1.setHeightForWidth(self.selectFileTypeLabel.sizePolicy().hasHeightForWidth())
        self.selectFileTypeLabel.setSizePolicy(sizePolicy1)
        self.selectFileTypeLabel.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.selectFileTypeLabel, 0, 0, 1, 1)

        self.selectFileFormatComboBox = QComboBox(self.optionalFieldsContainer)
        self.selectFileFormatComboBox.setObjectName(u"selectFileFormatComboBox")
        sizePolicy.setHeightForWidth(self.selectFileFormatComboBox.sizePolicy().hasHeightForWidth())
        self.selectFileFormatComboBox.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.selectFileFormatComboBox, 0, 4, 1, 1)

        self.selectFileFormatLabel = QLabel(self.optionalFieldsContainer)
        self.selectFileFormatLabel.setObjectName(u"selectFileFormatLabel")

        self.gridLayout_3.addWidget(self.selectFileFormatLabel, 0, 3, 1, 1)

        self.selectFileTypeComboBox = QComboBox(self.optionalFieldsContainer)
        self.selectFileTypeComboBox.addItem("")
        self.selectFileTypeComboBox.addItem("")
        self.selectFileTypeComboBox.setObjectName(u"selectFileTypeComboBox")
        sizePolicy2.setHeightForWidth(self.selectFileTypeComboBox.sizePolicy().hasHeightForWidth())
        self.selectFileTypeComboBox.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.selectFileTypeComboBox, 0, 2, 1, 1)

        self.fileEncodingTypeLabel = QLabel(self.optionalFieldsContainer)
        self.fileEncodingTypeLabel.setObjectName(u"fileEncodingTypeLabel")
        sizePolicy1.setHeightForWidth(self.fileEncodingTypeLabel.sizePolicy().hasHeightForWidth())
        self.fileEncodingTypeLabel.setSizePolicy(sizePolicy1)
        self.fileEncodingTypeLabel.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.fileEncodingTypeLabel, 1, 0, 1, 1)

        self.fileEncodingTypeComboBox = QComboBox(self.optionalFieldsContainer)
        self.fileEncodingTypeComboBox.setObjectName(u"fileEncodingTypeComboBox")
        sizePolicy.setHeightForWidth(self.fileEncodingTypeComboBox.sizePolicy().hasHeightForWidth())
        self.fileEncodingTypeComboBox.setSizePolicy(sizePolicy)
        self.fileEncodingTypeComboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.fileEncodingTypeComboBox, 1, 2, 1, 1)

        self.getVideoButton = QPushButton(self.centralwidget)
        self.getVideoButton.setObjectName(u"getVideoButton")
        self.getVideoButton.setGeometry(QRect(657, 570, 131, 34))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.getVideoButton.sizePolicy().hasHeightForWidth())
        self.getVideoButton.setSizePolicy(sizePolicy3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 30))
        self.menubar.setDefaultUp(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.selectFileTypeComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.requiredFieldsBox.setTitle(QCoreApplication.translate("MainWindow", u"Required Fields", None))
        self.saveFileOptionsContainer.setTitle(QCoreApplication.translate("MainWindow", u"Save File Options", None))
        self.saveFileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Save File Name", None))
        self.saveFileLocationLabel.setText(QCoreApplication.translate("MainWindow", u"Save File Location", None))
        self.saveFileLocationBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type or select file location", None))
        self.SaveFileLocationSearchButton.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.saveFileNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Do not include extension", None))
        self.VideoSourceBox.setTitle(QCoreApplication.translate("MainWindow", u"Video Source", None))
        self.pasteURLLabel.setText(QCoreApplication.translate("MainWindow", u"Paste URL Here", None))
        self.pasteURLInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste url here (ie: https://youtu.be/dQw4w9WgXcQ)", None))
        self.optionalFieldsContainer.setTitle(QCoreApplication.translate("MainWindow", u"Optional Fields", None))
        self.selectFileTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Select File Type", None))
        self.selectFileFormatComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the file format/extension", None))
        self.selectFileFormatLabel.setText(QCoreApplication.translate("MainWindow", u"Select File Format", None))
        self.selectFileTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Video", None))
        self.selectFileTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))

        self.selectFileTypeComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select whether to create a video or audio output", None))
        self.fileEncodingTypeLabel.setText(QCoreApplication.translate("MainWindow", u"File Encoding", None))
        self.fileEncodingTypeComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Encoding", None))
        self.getVideoButton.setText(QCoreApplication.translate("MainWindow", u"Start Download", None))
    # retranslateUi

