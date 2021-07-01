from PyQt5 import QtCore, QtGui, QtWidgets

class widget_achiev():
    def construction_achiev(self):
        self.container_achiev = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.icon_frame = QtWidgets.QWidget(self.container_achiev)
        self.icon_image = QtWidgets.QLabel(self.icon_frame)
        self.lbl_achiev_desc = QtWidgets.QLabel(self.container_achiev)
        self.bar_achievatual = QtWidgets.QWidget(self.container_achiev)
        self.bar_achievtotal = QtWidgets.QWidget(self.container_achiev)
        self.lbl_achiev_points = QtWidgets.QLabel(self.container_achiev)
    
        self.bar_achievatual.raise_()
        self.icon_frame.raise_()
        self.lbl_achiev_desc.raise_()
        self.bar_achievtotal.raise_()
        self.lbl_achiev_points.raise_()

        self.font_config()
        self.layout_pos()
        self.size_policy()

    def layout_pos(self):

        self.container_achiev.setMinimumSize(QtCore.QSize(222, 51))
        self.container_achiev.setMaximumSize(QtCore.QSize(222, 51))
        self.icon_frame.setGeometry(QtCore.QRect(6, 6, 41, 41))
        self.icon_image.setGeometry(QtCore.QRect(3, 3, 35, 35))
        self.lbl_achiev_desc.setGeometry(QtCore.QRect(54, 6, 121, 31))
        self.bar_achievatual.setGeometry(QtCore.QRect(54, 38, 80, 10))
        self.lbl_achiev_points.setGeometry(QtCore.QRect(170, 0, 51, 31))
        self.bar_achievtotal.setGeometry(QtCore.QRect(54, 38, 160, 10))

    def size_policy(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.container_achiev.sizePolicy().hasHeightForWidth())
        self.container_achiev.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(self.lbl_achiev_desc.sizePolicy().hasHeightForWidth())
        self.lbl_achiev_desc.setSizePolicy(sizePolicy)
    
    def font_config(self):
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        self.lbl_achiev_desc.setFont(font)
        self.lbl_achiev_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_achiev_desc.setWordWrap(True)
        self.lbl_achiev_desc.setIndent(-1)
        font.setWeight(50)
        self.lbl_achiev_points.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_achiev_points.setWordWrap(True)
        self.lbl_achiev_points.setIndent(-1)

                
class build_achievments_widgets(widget_achiev):
    def set_atributes(self, x, y, description,  points, is_completed, is_true):
        if is_completed == True:
            self.lbl_achiev_points.setText(str(points) + 'xp')
            self.bar_achievatual.setVisible(False)
            self.bar_achievtotal.setVisible(True)
            self.bar_achievtotal.setStyleSheet("background-color:#5695f6;border-radius:5px;")
            self.lbl_achiev_desc.setStyleSheet("color:rgb(0,0,170);border:none;background:transparent;")
            self.lbl_achiev_points.setStyleSheet("color:rgb(0,0,170);border:none;background:transparent;")
            self.icon_image.setStyleSheet("border-image:url(:/Img/ideia.png);border:1px solid rgb(78, 109, 153);background:#7f82db;")
            self.icon_frame.setStyleSheet("background-color:rgb(157, 185, 224);")
            
        else:
            self.lbl_achiev_points.setText('0xp')
            self.bar_achievatual.setVisible(False)
            self.bar_achievtotal.setVisible(True)
            self.bar_achievatual.setStyleSheet("background-color:#5695f6;border-radius:5px;")
            self.lbl_achiev_desc.setStyleSheet("color:rgb(170,170,170);border:none;background:transparent;")
            self.bar_achievtotal.setStyleSheet("background-color:rgba(220,220,220,0.8);border-radius:5px;")
            self.lbl_achiev_points.setStyleSheet("color:rgb(170,170,170);border:none;background:transparent;")
            self.icon_image.setStyleSheet("border-image:url(:/Img/ideia.png);border:1px solid rgb(0,123,255);background:transparent")
            self.icon_frame.setStyleSheet("background-color:rgb(200,200,200);")
            self.lbl_achiev_points.setStyleSheet("color:rgb(170,170,170);border:none;background:transparent;")

            if is_true < 4:
                self.scrollArea.setGeometry(QtCore.QRect(-8, 30, 491, 251))
            else:
                self.scrollArea.setGeometry(QtCore.QRect(0, 30, 491, 251))
        
        self.container_achiev.setStyleSheet("background-color:rgb(240,240,240);border-radius:8px;border:1px solid rgb(0,123,255);")
        self.lbl_achiev_desc.setText(description)
        self.gridLayout_achiev.addWidget(self.container_achiev, x, y, 1, 1)
        
        
    def set_level_xp(self, level, points_level, next_level):
        self.lbl_value_level.setText(str(level))
        self.lbl_value_xp_atual.setText(str(points_level))
        perc = (points_level/next_level) * 100
        bar_atual = (perc * 202)/100 
        perc = round(perc, 2)
        self.bar_total.setGeometry(QtCore.QRect(16, 210, bar_atual, 10)) # 3 index = actual bar
        self.lbl_value_percnextlvl.setText((str(perc) + "%"))



    def get_atributes(self):
        atributes = {"level":3,"stage":"Silver","points": 1150 ,"nextlevel":2200 , "achievments":[
        {"description":"Yiel semanal acima de 90%","points": 250,"completed":True},
        {"description":"Produtividade semanal igual a 90%","points": 650,"completed":False},
        {"description":"Scrap Mensal igual a zero","points": 200,"completed":False},
        {"description":"Complete 40 horas logged in All in One","points": 700,"completed":False},
        {"description":"Checar o Posto ideal por 6 dias consecutivos","points": 400,"completed":True}]}


        total_achiev = atributes['achievments']
        number_achiev = len(total_achiev)
        achiev = [''] * number_achiev
        posX_true = 0
        posX_false = 0
        is_true = 0

        for n in range(0,number_achiev):
            desc = atributes["achievments"][n]["description"]
            points = atributes["achievments"][n]["points"]
            completed = atributes["achievments"][n]["completed"]

            achiev[n] = self.construction_achiev()
            
            if completed == True:
                posY = 0
                posX_true = posX_true + 1
                posX = posX_true
                is_true = is_true + 1
            else:
                posY = 1
                posX_false = posX_false + 1
                posX = posX_false

            self.set_atributes(posX, posY, desc, points, completed, is_true)

        level = atributes["level"]
        points_level = atributes["points"]
        next_level = atributes["nextlevel"]

        self.set_level_xp(level, points_level, next_level)


    def build_achiev(self):
        self.get_atributes()
        