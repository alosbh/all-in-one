class theme_controller():
    def set_blue(self):
        try:
            self.sidebar.setStyleSheet("background-color:rgb(67,67,67)")
            self.logo_container.setStyleSheet("background-color:#5152f3")
            self.sidebar_apps.setStyleSheet("QPushButton {border:none;color:white;text-align:left;padding-left:20px;border:none;}QPushButton:hover {color:white;text-align:left;padding-left:20px;border:none;background-color:#5253ee}")
            self.header.setStyleSheet("background-color: white;border:none;")
            self.footer.setStyleSheet("background-color:white;border:none;")
            self.bar_total.setStyleSheet("background-color:#5253ee;border-radius:5px;")
            self.btn_reset.setStyleSheet("QPushButton{image:url(:/Img/desligar2.png)}QPushButton:hover {image:url(:/Img/desligar (1).png)}")
            self.lbl_value_name.setStyleSheet("background-color:rgb(67,67,67);color: white;")
        except:
            pass

    def set_red(self):
        try:
            self.sidebar.setStyleSheet("background-color:#FD2F2F")
            self.logo_container.setStyleSheet("background-color:#aa0002")
            self.sidebar_apps.setStyleSheet("QPushButton {border:none;color:white;text-align:left;padding-left:20px;border:none;}QPushButton:hover {color:white;text-align:left;padding-left:20px;border:none;background-color:#aa0002}")
            self.header.setStyleSheet("background-color: #FFD0D0;border:none;")
            self.footer.setStyleSheet("background-color:#FFD0D0;border:none;")
            self.bar_total.setStyleSheet("background-color:#aa0002;border-radius:5px;")
            self.btn_reset.setStyleSheet("QPushButton{image:url(:/Img/desligar2VVV.png)}QPushButton:hover {image:url(:/Img/desligar VVVV(1).png)}")
            self.lbl_value_name.setStyleSheet("background-color:#FD2F2F;color: white;")
        except:
            pass