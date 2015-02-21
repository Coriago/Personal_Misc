import sys
from PySide.QtCore import*
from PySide.QtGui import*

app = QApplication(sys.argv)

label = QLabel("<font color=red size=100>Sample Text</font>")
label2 = QLabel("<font color=blue size=100>Sample Text</font>")
label3 = QLabel("<font color=green size=100>Sample Text</font>")
label.show()
label2.show()
label3.show()
app.exec_()
sys.exit()
