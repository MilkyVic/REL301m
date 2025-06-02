


state_map = {i + 1: i for i in range(14)}
state_map[15] = 14
inv_state_map = {i: i + 1 for i in range(14)}
inv_state_map[14] = 15

num_states = 15

terminal_states_idx = [state_map[1], state_map[14]] # Index 0 and 13

actions = ['up', 'down', 'left', 'right']
num_actions = len(actions)

reward = -1

gamma = 1.0

policy = {a: 1.0 / num_actions for a in actions}

def get_next_state_case1(state_idx, action):
    if state_idx in terminal_states_idx:
        return state_idx

    grid_positions = {
        state_map[1]: (0, 0), state_map[2]: (0, 1), state_map[3]: (0, 2), state_map[4]: (0, 3),
        state_map[5]: (1, 0), state_map[6]: (1, 1), state_map[7]: (1, 2), state_map[8]: (1, 3),
        state_map[9]: (2, 0), state_map[10]: (2, 1), state_map[11]: (2, 2), state_map[12]: (2, 3),
        state_map[13]: (3, 0), state_map[14]: (3, 1) 
    }

    pos_to_state_idx = {v: k for k, v in grid_positions.items()}

    if state_idx == state_map[15]:
        if action == 'left': return state_map[12] 
        elif action == 'up': return state_map[13]   
        elif action == 'right': return state_map[14] 
        elif action == 'down': return state_map[15] 
        return state_idx # 

    if state_idx in grid_positions:
        row, col = grid_positions[state_idx]
        next_row, next_col = row, col

        if action == 'up': next_row -= 1
        elif action == 'down': next_row += 1
        elif action == 'left': next_col -= 1
        elif action == 'right': next_col += 1

        if (next_row, next_col) in pos_to_state_idx:
             return pos_to_state_idx[(next_row, next_col)]
        else:
             return state_idx 

    return state_idx

def get_next_state_case2(state_idx, action):
    if state_idx == state_map[13] and action == 'down':
        return state_map[15]
    return get_next_state_case1(state_idx, action) 

def iterative_policy_evaluation(transitions_func, theta=1e-6):
    V = {i: 0.0 for i in range(num_states)}

    while True:
        delta = 0
        V_new = V.copy()
        for s_idx in range(num_states):
            if s_idx not in terminal_states_idx:
                v_s = V[s_idx]
                # Bellman equation
                q_s = 0
                for action in actions:
                    next_s_idx = transitions_func(s_idx, action)
                    q_s += policy[action] * (reward + gamma * V[next_s_idx])
                V_new[s_idx] = q_s
                delta = max(delta, abs(V_new[s_idx] - v_s))

        V = V_new
        if delta < theta:
            break
    return V

V_case1 = iterative_policy_evaluation(get_next_state_case1)
print(f"Giá trị hội tụ v_pi(15) cho Trường hợp 1: {V_case1[state_map[15]]}")

V_case2 = iterative_policy_evaluation(get_next_state_case2)
print(f"Giá trị hội tụ v_pi(15) cho Trường hợp 2: {V_case2[state_map[15]]}")
