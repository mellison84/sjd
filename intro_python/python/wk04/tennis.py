def score(pl_one, pl_two):
    names = ['Player 1', 'Player 2']
    scores = ['love', '15', '30', '40', 'set']
    eq = ['Love all', '15 all', '30 all', 'Deuce']

    # Starting (Zero Zero)
    if (pl_one < 5) and (pl_two < 5):
        if (pl_one == pl_two):
            return [eq[pl_one]], False]
        else:
            return [scores[pl_one]] + ' : ' + [scores[pl_two]]



print(score (0,0)[0]) #'Love all'
print(score (0,0)[1]) # False
print(score (40,40)[0]) # Deuce
