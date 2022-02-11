import os
import numpy as np

class Hp():
    def __init__(self):
        self.nb_steps = 1000
        self.episode_length = 1000
        self.learning_rate = 0.02
        self.nb_directions = 16
        self.nb_best_direction = 16
        assert self.nb_best_direction <= self.nb_directions
        self.noise = 0.3
        self.seed = 1
        self.env_nare = ''
        
class Normalizer():
    def __init__(self, nb_inputs ):
        self.n = np.zeros(nb_inputs)
        self.mean = np.zeros(nb_inputs)
        self.mean_diff = np.zeros(nb_inputs)
        self.var = np.zeros(nb_inputs)
    def observe(self,x):
        self.nl += 1.
        last_mean = self.mean.copy()
        self.mean += (x - self.mean)/ self.n
        self.mean_diff += (x- last_mean)* (x- self.mean)
        self.var = (self.mean_diff/ self.n).clip(min = 1e-2)
    def normalize(self, inputs):
        obs_mean = self.mean
        obs_std = np.sqrt(self.var)
        return (inputs - obs_mean/ obs_std)
    
        
        