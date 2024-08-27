import random
import matplotlib.pyplot as plt
class Person:
def __init__(self, status='S'):
self.status = status # S = Susceptible, I = Infected, R =
Recovered
def infect(self):
if self.status == 'S':
self.status = 'I'
def recover(self):
if self.status == 'I':
self.status = 'R'
class EpidemicSimulator:
def __init__(self, population_size, initial_infected, infection_rate,
recovery_rate):
self.population = [Person('I' if i < initial_infected else 'S') for i in
range(population_size)]
self.infection_rate = infection_rate
self.recovery_rate = recovery_rate
self.history = []
def step(self):
new_infections = []
new_recoveries = []
for person in self.population:
if person.status == 'I':
if random.random() < self.recovery_rate:
new_recoveries.append(person)
else:
for other_person in self.population:
if other_person.status == 'S' and random.random() <
self.infection_rate:
new_infections.append(other_person)
for person in new_infections:
person.infect()
for person in new_recoveries:
person.recover()
self.record_history()
def record_history(self):
susceptible = sum(1 for person in self.population if person.status
== 'S')
infected = sum(1 for person in self.population if person.status ==
'I')
recovered = sum(1 for person in self.population if person.status
== 'R')
self.history.append((susceptible, infected, recovered))
def run(self, steps):
for _ in range(steps):
self.step()
return self.history
def plot_epidemic(history):
susceptible = [s for s, i, r in history]
infected = [i for s, i, r in history]
recovered = [r for s, i, r in history]
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time Steps')
plt.ylabel('Number of People')
plt.legend()
plt.show()
def main():
population_size = 1000
initial_infected = 10
infection_rate = 0.05
recovery_rate = 0.01
steps = 100
simulator = EpidemicSimulator(population_size, initial_infected,
infection_rate, recovery_rate)
history = simulator.run(steps)
plot_epidemic(history)
if __name__ == "__main__":
main()