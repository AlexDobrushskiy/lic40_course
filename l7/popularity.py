def popularity(p):
	score = 0
	for f in friends(p):
		score += popularity(f)
	return score


