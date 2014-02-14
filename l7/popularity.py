def popularity(p):
	score = 0
	for f in friends(p):
		score += popularity(f)
	return score


def popularity(t, p):
	if t==0:
		return 1

	for f in friends(p):
		score += popularity(t, f)
	return score

