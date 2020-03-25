from Models import Neuron

class Connection:

    def __init__(self, innovation_no, weight=1, from_neuron=None, to_neuron=None, is_active=True):
        self.innovation_no = innovation_no
        self.from_neuron = from_neuron
        self.to_neuron = to_neuron
        self.weight = weight
        self.active = is_active
    
    def send(self, input_value):
        connection_val = input_value * self.weight
        self.from_neuron.inputs.apped(connection_val)