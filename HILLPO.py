from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
import numpy as np
import webbrowser as wb



class Application():
    def __init__(self):
        app = QApplication(sys.argv)
        win =QWidget()
        
        menu = "menu.png"
        note = "not.png"
        code = "code.png"
        about ="about.png"
        cross = "cross.png"
        min = "min.png"
        back = "back1.png"
        github ="github.png"
        insta="instag.png"
        wolf = "wolf2.gif"
        icon = "darkwo.ico"
        
        txt = "Hill cipher is a polygraphic substitution cipher based on linear algebra.Each letter is represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used, but this is not an essential feature of the cipher. To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption.The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26)."
        
        def min_desk():
            win.showMinimized()
        
        def call():
            win.close()
            
            
           
            
            
        def pro_gr():
            
            def back1():
                frame.deleteLater()
                b2.deleteLater()
                pu1.deleteLater()  
                l13.deleteLater()
                pu.deleteLater()
                li2.deleteLater()
                l3.deleteLater() 
                li1.deleteLater()
                l2.deleteLater()
                l1.deleteLater()
                
            def remove():
                l13.clear()
                    
                
            
            def run():


                def encrypt(msg):
                    msg = msg.replace(" ", "")
                    C = make_key()
                    len_check = len(msg) % 2 == 0
                    if not len_check:
                        msg += "0"
                    P = create_matrix_of_integers_from_string(msg)
                    msg_len = int(len(msg) / 2)
                    encrypted_msg = ""
                    
                        
                    for i in range(msg_len):
                        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
                        integer = int(row_0 % 26 + 65)
                        encrypted_msg += chr(integer)
                        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
                        integer = int(row_1 % 26 + 65)
                        encrypted_msg += chr(integer)
                    print(str(encrypted_msg))
                    l13.appendPlainText("Your Encrypted String: \n")
                    l13.setStyleSheet("color:white;background-color:#303633;border-radius:0px") 
                    l13.appendPlainText(str(encrypted_msg)+"\n")    
                    return encrypted_msg
                    

                def decrypt(encrypted_msg):
                    C = make_key()
                    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
                    determinant = determinant % 26
                    multiplicative_inverse = find_multiplicative_inverse(determinant)
                    C_inverse = C
                    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
                    C[0][1] *= -1
                    C[1][0] *= -1
                    for row in range(2):
                        for column in range(2):
                            C_inverse[row][column] *= multiplicative_inverse
                            C_inverse[row][column] = C_inverse[row][column] % 26

                    P = create_matrix_of_integers_from_string(encrypted_msg)
                    msg_len = int(len(encrypted_msg) / 2)
                    decrypted_msg = ""
                    for i in range(msg_len):
                        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
                        integer = int(column_0 % 26 + 65)
                        decrypted_msg += chr(integer)
                        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
                        integer = int(column_1 % 26 + 65)
                        decrypted_msg += chr(integer)
                    if decrypted_msg[-1] == "0":
                        decrypted_msg = decrypted_msg[:-1]
                    
                        
                    l13.appendPlainText("Your Decrypted String: \n") 
                    l13.setStyleSheet("color:white;background-color:#303633;border-radius:0px")   
                    l13.appendPlainText(str(decrypted_msg)+"\n")
                    return decrypted_msg

                def find_multiplicative_inverse(determinant):
                    multiplicative_inverse = -1
                    for i in range(26):
                        inverse = determinant * i
                        if inverse % 26 == 1:
                            multiplicative_inverse = i
                            break
                    return multiplicative_inverse


                def make_key():
                    determinant = 0
                    C = None
                    while True:
                        #cipher = input("Input 4 letter cipher: ")
                        cipher = str(li1.text())
                        
                        C = create_matrix_of_integers_from_string(cipher)
                        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
                        determinant = determinant % 26
                        inverse_element = find_multiplicative_inverse(determinant)
                        if inverse_element == -1:
                            l13.setStyleSheet("color:red;background-color:#303633;border-radius:0px")
                            li2.clear()
                            li1.clear()
                            l13.clear()

                            l13.appendPlainText("not relatively prime to 26, cant invert this key \n")
                            print("not relatively prime to 26, cant invert this key ")
                        elif np.amax(C) > 26 and np.amin(C) < 0:
                            l13.setStyleSheet("color:red;background-color:#303633")
                            li2.clear()
                            li1.clear()
                            l13.clear()

                            l13.appendPlainText("Only a-z characters are accepted \n")
                            print("Only a-z characters are accepted")
                            print(np.amax(C), np.amin(C))
                        else:
                            break
                    return C

                def create_matrix_of_integers_from_string(string):
                    integers = [chr_to_int(c) for c in string]
                    length = len(integers)
                    M = np.zeros((2, int(length / 2)), dtype=np.int32)
                    iterator = 0
                    for column in range(int(length / 2)):
                        for row in range(2):
                            M[row][column] = integers[iterator]
                            iterator += 1
                    return M

                def chr_to_int(char):
                    char = char.upper()
                    integer = ord(char) - 65
                    return integer

                if __name__ == "__main__":
                    #msg = input("Message: ")
                    msg = str(li2.text())
                    encrypted_msg = encrypt(msg)
                    print(encrypted_msg)
                    decrypted_msg = decrypt(encrypted_msg)
                    print(decrypted_msg)
            
                

            frame = QFrame(win)
            frame.setFixedHeight(430)
            frame.setFixedWidth(790)
            frame.setStyleSheet("background-color:#222624")
            frame.move(180,50)
            frame.show()
            
            l1= QLabel(win)
            l1.setText("HillPO")
            l1.setFont(QFont("arial",40))
            l1.setStyleSheet("color:white;font-weight:bold;")
            l1.move(510,80)
            l1.show()

            l2 = QLabel(win)
            l2.setText("Text")
            l2.setFont(QFont("century gothic",20))
            l2.move(200,160)
            l2.setStyleSheet("color:white;")
            l2.show()
            
            li1 = QLineEdit(win)
            li1.setFont(QFont("arial",20))
            li1.setFixedHeight(50)
            li1.setStyleSheet("""QLineEdit{
                background-color:#303633;
                color:white;
                border-radius:0px;
                }
                
                
                
                }""")
            li1.setFixedWidth(250)
            li1.move(280,150)
            li1.show()
            
            l3 = QLabel(win)
            l3.setText("Key")
            l3.setFont(QFont("century gothic",20))
            l3.move(200,240)
            l3.setStyleSheet("color:white;")
            l3.show()
            
            
            li2 = QLineEdit(win)
            li2.setFont(QFont("arial",20))
            li2.setFixedHeight(50)
            li2.setStyleSheet("""QLineEdit{
                background-color:#303633;
                color:white;
                border-radius:0px;
                }
                
                
                
                }""")
            li2.setFixedWidth(250)
            li2.move(280,230)
            li2.show()
            
            pu = QPushButton(win)
            pu.setFixedHeight(50)
            pu.setFixedWidth(200)
            pu.setText("DO IT")
            pu.setStyleSheet("""QPushButton{
                background-color:#303633;
                color:white;
                border-radius:0px;
                }
                QPushButton::hover{
                    background-color:#222624;
                    
                }
                
                }""")
            pu.setFont(QFont("arial",20))
            pu.move(200,420)
            pu.show()
            pu.clicked.connect(run)
            
            l13 = QPlainTextEdit(win)
            l13.setFont(QFont("arial",20))
            l13.setStyleSheet("background-color:#303633;border-radius:0px;color:white")
            l13.setFixedHeight(300)
            l13.setFixedWidth(350)
            l13.setReadOnly(True)
            l13.move(580,150)
            l13.show()
            
            pu1= QPushButton(win)
            pu1.setToolTip("Screen Clear")
            pu1.setFixedHeight(50)
            pu1.setFixedWidth(150)
            pu1.setText("Remove")
            pu1.setStyleSheet("""QPushButton{
                background-color:#303633;
                color:white;
                border-radius:0px;
                }
                QPushButton::hover{
                    background-color:#222624;
                    
                }
                
                }""")
            pu1.setFont(QFont("arial",20))
            pu1.move(410,420)
            pu1.show()
            pu1.clicked.connect(remove)
            
            b2 = QPushButton(win)
            b2.setIcon(QIcon(back))
            b2.setToolTip("Back")
            b2.setStyleSheet("""QPushButton{

                    background-color:#222624;
                    border-radius:0px;
                    }
                    QPushButton::hover{
                        background-color:#303633;
                    }
                    
                }""")
            b2.setIconSize(QSize(30,50))
            b2.setFixedHeight(50)
            b2.setFixedWidth(80)
            b2.move(220,80)
            b2.show()
            b2.clicked.connect(back1)
            
            
        def about_e():
            
            def back1():
                frame.deleteLater()
                l1.deleteLater()
                l2.deleteLater()
                l3.deleteLater()
                bu.deleteLater()
                bu1.deleteLater()
                b2.deleteLater()
                
            
            def git():
                
                wb.open("https://github.com/frozbite079")
                
            def ins():
                wb.open("https://www.instagram.com/frozbite079/")    
                
            frame = QFrame(win)
            frame.setFixedHeight(430)
            frame.setFixedWidth(790)
            frame.setStyleSheet("background-color:#222624")
            frame.move(180,50)
            frame.show()
            
            
            l1= QLabel(win)
            l1.setText("ABOUT")
            l1.setFont(QFont("century gothic",40))
            l1.setStyleSheet("color:white;font-weight:bold;")
            l1.move(490,80)  
            l1.show()  
            
            l2 = QLabel(win)
            l2.setText("$ This Project is made by 6ITC class students see we are logically smart.")
            l2.setFont(QFont("century gothic",15))
            l2.setStyleSheet("color:white;")
            l2.move(220,250)
            l2.show()
            
            l3 = QLabel(win)
            l3.setText("$ Social media  Below:")
            l3.setFont(QFont("century gothic",15))
            l3.setStyleSheet("color:white;")
            l3.move(220,320)
            l3.show()
            
            
            bu1 =QPushButton(win)
            bu1.setToolTip("Github")
            bu1.setIcon(QIcon(github))
            bu1.setIconSize(QSize(30,50))
            bu1.setStyleSheet("background-color:#222624;border-radius:0px;")
            bu1.setFixedHeight(50)
            bu1.setFixedWidth(50)
            bu1.move(220,370)
            bu1.show()
            bu1.clicked.connect(git)
            
            bu =QPushButton(win)
            bu.setToolTip("Instagram")
            bu.setIcon(QIcon(insta))
            bu.setIconSize(QSize(30,50))
            bu.setStyleSheet("background-color:#222624;border-radius:0px;")
            bu.setFixedHeight(50)
            bu.setFixedWidth(50)
            bu.move(270,370)
            bu.show()
            bu.clicked.connect(ins)
            
            
            b2 = QPushButton(win)
            b2.setIcon(QIcon(back))
            b2.setToolTip("Back")
            b2.setStyleSheet("""QPushButton{

                    background-color:#222624;
                    border-radius:0px;
                    }
                    QPushButton::hover{
                        background-color:#303633;
                    }
                    
                }""")
            b2.setIconSize(QSize(30,50))
            b2.setFixedHeight(50)
            b2.setFixedWidth(80)
            b2.move(220,80)
            b2.show()
            b2.clicked.connect(back1)
            
            
            
        
            
             
              
        
        def hillpy():
            
            def back1():
                frame.deleteLater()
                l1.deleteLater()
                b2.deleteLater()
                l12.deleteLater()
            
            frame = QFrame(win)
            frame.setFixedHeight(430)
            frame.setFixedWidth(790)
            frame.setStyleSheet("background-color:#222624")
            frame.move(180,50)
            frame.show()
            
            l1 = QPlainTextEdit(win)
            l1.setFont(QFont("arial",20))
            l1.appendPlainText(str(txt))
            l1.setStyleSheet("background-color:#303633;border-radius:0px;color:white")
            l1.setFixedHeight(250)
            l1.setFixedWidth(720)
            l1.setReadOnly(True)
            l1.move(220,180)
            l1.show()
            
            b2 = QPushButton(win)
            b2.setToolTip("Generate Cipher")
            b2.setIcon(QIcon(back))
            b2.setToolTip("Back")
            b2.setStyleSheet("""QPushButton{

                    background-color:#222624;
                    border-radius:0px;
                    }
                    QPushButton::hover{
                        background-color:#303633;
                    }
                    
                }""")
            b2.setIconSize(QSize(30,50))
            b2.setFixedHeight(50)
            b2.setFixedWidth(80)
            b2.move(220,100)
            b2.show()
            b2.clicked.connect(back1)
            
            
            l12 = QLabel(win)
            l12.setText("INFORMATION")
            l12.setFont(QFont("Century Gothic",50))
            l12.setStyleSheet("color:white;font-weight:bold")
            l12.move(360,80)
            l12.show()
            
           
            
        
            
        
        def animate1():
            
            f1.setFixedWidth(80)
            
            hi1.setFixedWidth(80)
            hi1.setText("")
            
            hi2.setFixedWidth(80)
            hi2.setText("")
            hi3.setFixedWidth(80)
            hi3.setText("")


            
            
            bu.setFixedWidth(80)
            
            
            
            bu.clicked.connect(animate)
        
        
        def animate():
            f1.setFixedWidth(140)
            
            hi1.setFixedWidth(140)
            hi1.setText(" Info")
            hi2.setFixedWidth(140)
            hi2.setText(" Code")
            hi3.setFixedWidth(140)
            hi3.setText(" About")
            
            
            
            
            
            bu.setFixedWidth(140)
            
            
            
            
            
        
             
            bu.clicked.connect(animate1)
        
        
        
        
        f = QFrame(win)
        f.setFixedHeight(500)
        f.setFixedWidth(1000)
        f.setStyleSheet("background-color:#303633")
        
        f.show()
        
        
        
        f2 = QFrame(win)
        f2.setFixedHeight(40)
        f2.setFixedWidth(1000)
        f2.setStyleSheet("background-color:#222624")
        
        f2.show()
        
        
        
        img = QLabel(win)
        mov = QMovie(wolf)
        img.setMovie(mov)
        img.setFixedHeight(460)
        mov.setScaledSize(QSize(1000,460))
        img.setFixedWidth(1000)
        img.move(0,40)
        mov.start()
        img.show()
        
        
        
        
        
        
        f1 = QFrame(win)
        f1.setFixedHeight(500)
        f1.setFixedWidth(80)
        f1.setStyleSheet("background-color:#222624")
        
        f1.show()
        
        
        
        
        
        
        
        
        
        
        
        hi1 = QPushButton(win)
        hi1.setFixedHeight(80)
        hi1.setIcon(QIcon(note))
        hi1.setToolTip("Information")
        hi1.setText("")
        hi1.setFont(QFont("century gothic",15))
        hi1.setIconSize(QSize(30,50))
        hi1.setFixedWidth(80)
        hi1.setStyleSheet("""QPushButton{
                background-color:#222624;
                border-radius:0px;
                color:white;
                }
                QPushButton::hover{
                    background-color:#303633
                }
            }""")
        hi1.show()
        hi1.move(0,80)
        hi1.clicked.connect(hillpy)
        
        hi2 = QPushButton(win)
        hi2.setToolTip("Code")
        hi2.setFixedHeight(80)
        hi2.setFont(QFont("century gothic",15))
        hi2.setIcon(QIcon(code))
        hi2.setIconSize(QSize(30,50))
        hi2.setFixedWidth(80)
        hi2.setStyleSheet("""QPushButton{
                background-color:#222624;
                border-radius:0px;
                color:white;
                }
                QPushButton::hover{
                    background-color:#303633;
                }
            }""")
        hi2.show()
        hi2.move(0,160)
        hi2.clicked.connect(pro_gr)
        
        hi3 = QPushButton(win)
        hi3.setToolTip("About")
        hi3.setFont(QFont("century gothic",15))
        hi3.setFixedHeight(80)
        hi3.setIcon(QIcon(about))
        hi3.setIconSize(QSize(30,50))
        hi3.setFixedWidth(80)
        hi3.setStyleSheet("""QPushButton{
                background-color:#222624;
                border-radius:0px;
                color:white;
                }
                QPushButton::hover{
                    background-color:#303633;
                }
            }""")
        hi3.show()
        hi3.move(0,240)
        hi3.clicked.connect(about_e)
        
        
        
        bu = QPushButton(win)
        bu.setIcon(QIcon(menu))
        bu.setIconSize(QSize(30,50))
        bu.setStyleSheet("""QPushButton{
                background-color:#222624;
                border-radius:0px;
                }
                QPushButton::hover{
                    background-color:#303633;
                }
            }""")
        bu.setFixedHeight(80)
        bu.setFixedWidth(80)
        bu.move(0,420)
        bu.show()
        bu.clicked.connect(animate)
        
        cl = QPushButton(win)
        cl.setFixedHeight(40)
        cl.setFixedWidth(50)
        cl.setIcon(QIcon(cross))
        cl.setStyleSheet("""QPushButton{
            background-color:#222624;
            }
            QPushButton::hover{
                background-color:red;
            }
            
            }""")
        cl.setIconSize(QSize(30,90))
        cl.move(950,0)

        cl.show()
        cl.clicked.connect(call)
        
        mi = QPushButton(win)
        mi.setFixedHeight(40)
        mi.setFixedWidth(50)
        mi.setIcon(QIcon(min))
        mi.setStyleSheet("""QPushButton{
            background-color:#222624;
            border-radius:0px;
            }
            QPushButton::hover{
                background-color:#303633;
            }
            
            }""")
        mi.setIconSize(QSize(30,90))
        mi.move(890,0)

        mi.show()
        mi.clicked.connect(min_desk)
        
        
        
        
        
        
        win.setFixedHeight(500)
        win.setWindowFlags(Qt.FramelessWindowHint)
        win.setFixedWidth(1000)
        win.setWindowIcon(QIcon(icon))
        win.setWindowTitle("HillPO")
        win.setAttribute(Qt.WA_TranslucentBackground)
        win.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    Application()       
        
        
        