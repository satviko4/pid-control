import gym
from matplotlib import pyplot as plt
env = gym.make("CartPole-v1")
observation = env.reset()


Kp = 135
Ki = 90
Kd = 40

force = 0
integral = 0
for _ in range(500):
  env.render()  
  
  observation, reward, done, info = env.step(force) 

  position = observation[0]
  angular_velocity = observation[3]
  angle = observation[2]

  integral = integral + angle


  F = Kp*(angle) + Kd*(angular_velocity) + Ki*(integral)

  force = 1 if F > 0 else 0
  if done:
    observation = env.reset()
    integral = 0
  
env.close()

  