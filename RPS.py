# use regret matching to compute a best-response strategy to an opponent's RPS strategy

def RPS_response(opp, sims=10000):
    """Compute best response strategy to a given RPS strategy."""
    
    games_played = 1
    cumulative_regrets = [0, 0, 0]
    
    my_payoffs = np.array([
        [0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]])
    
    
