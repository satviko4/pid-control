import gym
import ballbeam_gym
from matplotlib import pyplot as plt
env = gym.make('VisualBallBeamSetpoint-v0')
observation = env.reset()


for _ in range(500):
  env.render()  
