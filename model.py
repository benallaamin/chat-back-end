import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        #ReLU activation 
        """ Une fonction d’activation est une fonction mathématique utilisé sur un signal.
            Elle va reproduire le potentiel d’activation que l’on retrouve dans
            le domaine de la biologie du cerveau humain.Elle va permettre le passage
            d’information ou non de l’information si le seuil de stimulation est atteint. 
            Concrètement, elle va avoir pour rôle de décider si on active ou non une réponse du neurone. 
            Un neurone ne va faire qu’appliquer la fonction suivante :

               X  = ∑ ( entrée * poids ) + biais """
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
       
        return out
