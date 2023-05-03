import sys
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore

class LaptopPricePredictor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create GUI widgets
        self.company_label = QtWidgets.QLabel('Company:')
        self.company_combo = QtWidgets.QComboBox()
        self.company_combo.addItems(['Dell', 'HP', 'Lenovo', 'Apple', 'Asus', 'Acer'])
        self.type_label = QtWidgets.QLabel('Type:')
        self.type_combo = QtWidgets.QComboBox()
        self.type_combo.addItems(['Ultrabook', 'Notebook', 'Gaming', '2 in 1', 'Netbook'])
        self.inches_label = QtWidgets.QLabel('Screen size (inches):')
        self.inches_input = QtWidgets.QLineEdit()
        self.resolution_label = QtWidgets.QLabel('Screen resolution:')
        self.resolution_combo = QtWidgets.QComboBox()
        self.resolution_combo.addItems(['1366x768', '1920x1080', '1600x900', '3840x2160', '3200x1800'])
        self.cpu_label = QtWidgets.QLabel('CPU:')
        self.cpu_input = QtWidgets.QLineEdit()
        self.ram_label = QtWidgets.QLabel('RAM (GB):')
        self.ram_input = QtWidgets.QLineEdit()
        self.memory_label = QtWidgets.QLabel('Memory (GB):')
        self.memory_input = QtWidgets.QLineEdit()
        self.gpu_label = QtWidgets.QLabel('GPU:')
        self.gpu_input = QtWidgets.QLineEdit()
        self.opsys_label = QtWidgets.QLabel('Operating System:')
        self.opsys_combo = QtWidgets.QComboBox()
        self.opsys_combo.addItems(['Windows', 'macOS', 'Linux'])
        self.weight_label = QtWidgets.QLabel('Weight (kg):')
        self.weight_input = QtWidgets.QLineEdit()
        self.predict_button = QtWidgets.QPushButton('Predict')
        self.predict_label = QtWidgets.QLabel()

        # Create the layout
        grid_layout = QtWidgets.QGridLayout()
       
        grid_layout.addWidget(self.company_label, 0, 0)
        grid_layout.addWidget(self.company_combo, 0, 1)
        grid_layout.addWidget(self.type_label, 1, 0)
        grid_layout.addWidget(self.type_combo, 1, 1)
        grid_layout.addWidget(self.inches_label, 2, 0)
        grid_layout.addWidget(self.inches_input, 2, 1)
        grid_layout.addWidget(self.resolution_label, 3, 0)
        grid_layout.addWidget(self.resolution_combo, 3, 1)
        grid_layout.addWidget(self.cpu_label, 4, 0)
        grid_layout.addWidget(self.cpu_input, 4, 1)
        grid_layout.addWidget(self.ram_label, 5, 0)
        grid_layout.addWidget(self.ram_input, 5, 1)
        grid_layout.addWidget(self.memory_label, 6, 0)
        grid_layout.addWidget(self.memory_input, 6, 1)
        grid_layout.addWidget(self.gpu_label, 7, 0)
        grid_layout.addWidget(self.gpu_input, 7, 1)
        grid_layout.addWidget(self.opsys_label, 8, 0)
        grid_layout.addWidget(self.opsys_combo, 8, 1)
        grid_layout.addWidget(self.weight_label, 9, 0)
        grid_layout.addWidget(self.weight_input, 9, 1)
        grid_layout.addWidget(self.predict_button, 10, 0)
        grid_layout.addWidget(self.predict_label, 10, 1)

        # Set the layout
        self.setLayout(grid_layout)

        # Connect signals and slots
        self.predict_button.clicked.connect(self.predict_price)

        # Load the data
        self.laptops = pd.read_csv('laptop_data.csv')

        # Train the model
        self.model = self.train_model()

    def train_model(self):
        # TODO: Train the model using the data in self.laptops
        # Use a suitable algorithm, such as Linear Regression, Random Forest, or Gradient Boosting.
        # Return the trained model.
        pass

    def predict_price(self):
        # Retrieve the input values from the GUI widgets
        company = self.company_combo.currentText()
        type_ = self.type_combo.currentText()
        inches =self.inches_input.text()
        resolution = self.resolution_combo.currentText()
        cpu = self.cpu_input.text()
        ram = int(self.ram_input.text())
        memory = self.memory_input.text()
        gpu = self.gpu_input.text()
        opsys = self.opsys_combo.currentText()
        weight = self.weight_input.text()

        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame({
            'Company': [company],
            'TypeName': [type_],
            'Inches': [inches],
            'ScreenResolution': [resolution],
            'Cpu': [cpu],
            'Ram': [ram],
            'Memory': [memory],
            'Gpu': [gpu],
            'OpSys': [opsys],
            'Weight': [weight]
        })

        # Predict the price using the trained model
        predicted_price = self.model.predict(input_data)[0]

        # Display the predicted price in the GUI
        self.predict_label.setText(f'${predicted_price:.2f}')

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     predictor = LaptopPricePredictor()
#     predictor.show()
#     sys.exit(app.exec_())

