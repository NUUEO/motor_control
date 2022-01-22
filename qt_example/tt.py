from PySide2.QtGui import Qt
from PySide2.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QMessageBox,
                               QSpinBox, QVBoxLayout)


class spinBoxInputDialog(QDialog):
  def __init__(self, parent=None, title='', label='', reg=''):
    super(spinBoxInputDialog, self).__init__(parent)
    # setup UI
    self.setWindowTitle(title)
    
    self.verticalLayout = QVBoxLayout()
    self.label = QLabel(label)
    
    # 設定限制
    self.SpinBox = QSpinBox()
    self.SpinBox.setMaximum(999)
    self.SpinBox.setMinimum(1)
    
    self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
    self.buttonBox.setOrientation(Qt.Horizontal)
    
    self.verticalLayout.addWidget(self.label)
    self.verticalLayout.addWidget(self.SpinBox)
    self.verticalLayout.addWidget(self.buttonBox)
    self.setLayout(self.verticalLayout)

    # setting
    self.value = None
    self.status = None
    self.buttonBox.rejected.connect(self.reject)
    self.buttonBox.accepted.connect(self.accept)   

  def reject(self) -> None:
    self.value = self.SpinBox.value()
    self.status = False
    super().reject()

  def accept(self) -> None:
    self.value = self.SpinBox.value()
    if self.value:
      self.status = True
      super().accept()
    else:
      QMessageBox.warning(self,
              "警告",
              "不能空白!",
              QMessageBox.Yes)

  @classmethod
  def getValue(cls, parent, title='', label='', reg='[0-9]+$'):
    dialog = cls(parent, title, label, reg)
    dialog.exec_()
    return dialog.status, dialog.value