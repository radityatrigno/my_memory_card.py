# Memory card game with PyQt5
from PyQt5.QtCore import Qt
# importing necessary modules from PyQt5
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
# importing necessary modules from Python standard library
from random import randint, shuffle 

# defining the Question class
# this class will contain a question, a correct answer and three incorrect ones
class Question():
    # constructor of the Question class
    # it takes a question, a correct answer and three incorrect answers as parameters
    # and initializes the corresponding attributes
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# creating a list of questions
questions_list = [] 

# adding questions to the list
questions_list.append(
        Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(
        Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(
        Question('Yakut national house', 'Urasa', 'Yurta', 'Igloo', 'Khata'))

# creating the main application object 
app = QApplication([])

# creating the main widgets and layouts
btn_OK = QPushButton('Reply') # the reply button
lb_Question = QLabel('The most difficult question in the world!') # question text

# creating a group box for the answer options
RadioGroupBox = QGroupBox("Answer options")  # on-screen group of radio buttons

# creating radio buttons for the answer options
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

# grouping the radio buttons to control their behavior
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# creating a layout for the answer options
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # vertical guides inside the horizontal one
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)  # two answer options in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answer options in the second column
layout_ans3.addWidget(rbtn_4)

# adding the radio buttons to the layout
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  # columns placed in one line

# setting the alignment of the answer options
RadioGroupBox.setLayout(layout_ans1) # the "panel" with answer options is ready 

# creating a group box for the test results
AnsGroupBox = QGroupBox("Test results")
lb_Result = QLabel('are you right or not?') # here it will be written if you are "right" or "wrong"
lb_Correct = QLabel('answer will be here!') # here will be the text of the correct answer

# creating a layout for the test results
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result 
layout_line3 = QHBoxLayout() # "Answer" button

# adding widgets to the layouts
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # hide the answer panel, the question panel should be visible first 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large

# adding stretchable space to the left and right of the button  
layout_line3.addStretch(1)
# setting the alignment of the layouts
layout_card = QVBoxLayout()

# adding the layouts to the main layout
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content elements

# setting the alignment of the main layout
def show_result():
    # show result panel
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next')

# this function hides the question panel and shows the answer panel
def show_question():
    # show question panel
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Reply')
    RadioGroup.setExclusive(False) # removed the restrictions so as to reset the radio button choice
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # returned the restrictions, now only one radio button can be selected

# creating a list of radio buttons for the answers
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# defining the function to ask a question
def ask(q: Question):
    # this function takes a Question object as a parameter
    shuffle(answers) # shuffled the list of buttons, now some random button is first in the list
    answers[0].setText(q.right_answer) # fill the first element of the list with the right answer, the rest with wrong ones
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # question
    lb_Correct.setText(q.right_answer) # reply
    show_question() # show question panel 

# defining the function to show the correct answer
def show_correct(res):
    ''' this function shows the correct answer '''
    lb_Result.setText(res)
    show_result()

# defining the function to check the answer
def check_answer():
    ''' if any answer option is chosen, we need to check and show the answer panel'''
    if answers[0].isChecked():
        # right answer!
        show_correct('Right!')
        window.score += 1
        print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
        print('Rating: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # wrong answer!
            show_correct('Wrong answer!')
            print('Rating: ', (window.score/window.total*100), '%')
    

# defining the function to show the next question
def next_question():
    ''' asks a random question from the list '''
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # we don't need the old value,
                                                        # this means that you can use a local variable!  
            # randomly picked a question within the list
            # if you enter about a hundred words, they will rarely be repeated
    q = questions_list[cur_question] # picked a question
    ask(q) # asks

# defining the function to handle the button click   
def click_OK():
    ''' determines whether to show another question or check the answer to this one '''
    if btn_OK.text() == 'Answer':
        check_answer() # answer check
    else:
        next_question() # next question

# creating the main window and setting its layout   
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

# connecting the button click event to the function   
btn_OK.clicked.connect(click_OK) # by clicking on the button, we choose what exactly happens

# initializing the score and total variables
window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
