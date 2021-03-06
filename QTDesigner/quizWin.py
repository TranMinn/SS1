# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuizWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.i = 0
        self.questionList = []
        self.answerList = []
        self.length = len(self.questionList)
        self.selectedAns = list(range(5))
        self.wrong = 0
        self.correct = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(80, 70, 631, 41))
        self.question.setObjectName("question")
        self.answers = QtWidgets.QLabel(self.centralwidget)
        self.answers.setGeometry(QtCore.QRect(80, 70, 631, 131))
        self.answers.setObjectName("answers")
        self.optionA = QtWidgets.QRadioButton(self.centralwidget)
        self.optionA.setGeometry(QtCore.QRect(60, 190, 95, 20))
        self.optionA.setObjectName("optionA")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.optionA)
        self.optionB = QtWidgets.QRadioButton(self.centralwidget)
        self.optionB.setGeometry(QtCore.QRect(210, 190, 95, 20))
        self.optionB.setObjectName("optionB")
        self.buttonGroup.addButton(self.optionB)
        self.optionC = QtWidgets.QRadioButton(self.centralwidget)
        self.optionC.setGeometry(QtCore.QRect(380, 190, 95, 20))
        self.optionC.setObjectName("optionC")
        self.buttonGroup.addButton(self.optionC)
        self.optionD = QtWidgets.QRadioButton(self.centralwidget)
        self.optionD.setGeometry(QtCore.QRect(540, 190, 95, 20))
        self.optionD.setObjectName("optionD")
        self.buttonGroup.addButton(self.optionD)
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(360, 240, 93, 28))
        self.nextButton.setObjectName("nextButton")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(250, 290, 93, 28))
        self.submitButton.setObjectName("submitButton")
        self.retryButton = QtWidgets.QPushButton(self.centralwidget)
        self.retryButton.setGeometry(QtCore.QRect(250, 340, 93, 28))
        self.retryButton.setObjectName("retryButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.question.setText("1. Which is the most prioritized vehicle?")
        # self.answers.setText("A: ambulance B: bicycle C:motocycle D: police car")

        self.startButton.clicked.connect(self.generateQues)
        self.nextButton.clicked.connect(self.nextQues)
        self.prevButton.clicked.connect(self.prevQues)

        self.optionA.clicked.connect(self.selectA)
        self.optionB.clicked.connect(self.selectB)
        self.optionC.clicked.connect(self.selectC)
        self.optionD.clicked.connect(self.selectD)

        self.submitButton.clicked.connect(self.submitQuiz)

    # Start quiz
    def generateQues(self):
        # open files
        file_ques = open("questions.txt")
        file_ans = open("answers.txt")

        # read each line of files, form lists
        ques_lst = file_ques.readlines()
        ans_lst = file_ans.readlines()

        for i in range(len(ans_lst)):
            self.questionList.append(ques_lst[i])
            self.answerList.append(ans_lst[i])

        self.length = len(ans_lst)

        self.i = 0
        self.reset()
        self.question.setText(self.questionList[self.i])
        self.answers.setText(self.answerList[self.i])

    # Get selected answers
    def selectA(self):
        print(self.selectedAns)
        self.selectedAns[self.i] = 'A'

    def selectB(self):
        print(self.selectedAns)
        self.selectedAns[self.i] = 'B'

    def selectC(self):
        print(self.selectedAns)
        self.selectedAns[self.i] = 'C'

    def selectD(self):
        print(self.selectedAns)
        self.selectedAns[self.i] = 'D'

    # Get next question
    def nextQues(self):
        self.reset()
        if self.i == (self.length - 1):
            self.i = (self.length - 1)
        else:
            self.i += 1
            self.question.setText(self.questionList[self.i])
            self.answers.setText(self.answerList[self.i])

    # Go back to previous question
    def prevQues(self):
        self.reset()
        if self.i == 0:
            self.i = 0
        else:
            self.i -= 1
            self.question.setText(self.questionList[self.i])
            self.answers.setText(self.answerList[self.i])

    def submitQuiz(self):
        file_key = open("key.txt")
        key_lst = file_key.readlines()

        # Create a list of keys (extract /n)
        ans = []
        for i in key_lst:
            i = i[:-1]
            ans.append(i)

        for i in range(self.length):
            # Compare selected ans with true keys
            if ans[i] == self.selectedAns[i]:
                self.wrong += 1
            else:
                self.correct += 1

        # Message Box
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("You {} {}!".format("have" if self.correct >= 2 else "NOT", "pass the quiz!"))
        msg.setInformativeText("Correct answers: {} \n"
                               "Wrong answers: {}".format(self.correct, self.wrong))

        msg.setWindowTitle("Result")
        msg.exec_()

    # Reset radio buttons
    def reset(self):
        self.buttonGroup.setExclusive(False)
        self.optionA.setChecked(False)
        self.optionB.setChecked(False)
        self.optionC.setChecked(False)
        self.optionD.setChecked(False)
        self.buttonGroup.setExclusive(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question.setText(_translate("MainWindow", "Question"))
        self.answers.setText(_translate("MainWindow", "Answers"))
        self.optionA.setText(_translate("MainWindow", "A"))
        self.optionB.setText(_translate("MainWindow", "B"))
        self.optionC.setText(_translate("MainWindow", "C"))
        self.optionD.setText(_translate("MainWindow", "D"))
        self.prevButton.setText(_translate("MainWindow", "Prev"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.retryButton.setText(_translate("MainWindow", "Retry"))
        self.startButton.setText(_translate("MainWindow", "Start Quiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
