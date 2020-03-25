from Models.Connection import Connection
from Extra.ActivationFunctions import sigmoid


# Default activation functions is sigmoid - maybe change later

class Neuron:

    def __init__(self, serialNo, bias=0, inputs=[], outputConnectins=[]):
        self.id = serialNo
        self.bias = bias
        self.output = 0
        self.outputConn = outputConnectins
        self.inputs = inputs
    
    def activate(self):

        if not self.inputs:
            for curr_input in self.inputs:
                self.output += curr_input

        self.output = sigmoid(self.output)
        self.output -= self.bias

        if not self.outputConn:
            for curr_conn in self.outputConn:
                curr_conn.send(self.output)
            

