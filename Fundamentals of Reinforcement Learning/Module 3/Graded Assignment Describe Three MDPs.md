# Assignment: Describe Three Different MDPs

## Question 1: What is the structure of a Roomba Cleaning Robot MDP?

The Roomba cleaning robot MDP represents a complex decision-making process where the robot must efficiently clean a room while managing its resources. The state space includes the robot's position (x, y coordinates), the cleanliness status of different areas, battery level, and current movement direction. The available actions are moving in four directions, vacuuming, charging, and turning. The reward structure is designed to encourage efficient cleaning: +10 for cleaning a dirty area, +5 for moving to an uncleaned area, -1 for each movement step (energy consumption), -20 for running out of battery, and +15 for completing the entire room. This MDP is particularly interesting because it combines continuous state space (position) with discrete states (clean/dirty areas) and requires the agent to balance immediate cleaning actions with long-term energy management.

## Question 2: How does a Traffic Control System MDP work?

The Traffic Control System MDP is designed to optimize traffic flow through an intersection or network of roads. Its state space includes traffic density at intersections, vehicle wait times, traffic light states, time of day, and weather conditions. The system can take actions such as adjusting green/red light durations, modifying light cycles, prioritizing lanes, and activating priority signals. The reward structure focuses on traffic optimization: +5 for reducing average wait time, +10 for reducing congestion, -3 for increasing wait time, -5 for creating new congestion, and +15 for optimizing overall traffic flow. This MDP is unique because it deals with multiple interacting variables and requires the system to make decisions that affect the entire traffic network, balancing immediate traffic flow with long-term system efficiency.

## Question 3: What makes a Chess AI MDP different from other MDPs?

The Chess AI MDP is distinct from other MDPs due to its discrete but extremely large state space and strategic nature. The state space includes piece positions, piece status (movable/blocked), move history, remaining time, and current score. Available actions are moving pieces, capturing opponent pieces, castling, and en passant captures. The reward structure is heavily weighted toward strategic outcomes: +10 for capturing a piece, +50 for checkmate, -5 for losing a piece, +20 for check, and +30 for winning the game. This MDP is particularly challenging because it requires the agent to learn complex strategic patterns, plan multiple moves ahead, and adapt to opponent strategies, all while operating in a state space that is both discrete and enormous.

## Comparison of the Three MDPs

While all three MDPs share common characteristics such as complex state spaces, long-term consequence consideration, multiple possible actions, and goal-oriented reward structures, they differ significantly in their focus and complexity. The Roomba MDP emphasizes efficiency and resource management, the Traffic Control MDP deals with multiple interacting variables, and the Chess AI MDP operates in a discrete but vast state space. Each MDP presents unique challenges and requires different approaches to solve effectively.

-------------------------------------------------------------------------------------------------------
##### 5-17-2025 at 8PM.
##### Course: Fundamentals of Reinforcement Learning/Module 3.
##### Reading Material: Graded Assignment Describe Three MDPs
##### Learning Content from: MDP Examples
