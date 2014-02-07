# {url:[url....], ...}
def revers_graph (graph):
	reversed = {}
	for page in graph:
		inlinks  = []
		for j in graph:
			for url in graph[j]:
				if url == page:
					inlinks.append (j)
		reversed [page] = inlinks

def compute_ranks(graph):
	reversed = revers_graph (graph)
	d = 0.8
	numloops = 10
	ranks = {}
	npanges = len(graph)
	for page in graph:
		ranks[page] = 1.0/npanges

	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = (1-d) / npanges
			# ...
			summ = 0
			for i in reversed:
				summ += ranks [i]/len (graph [i])
				newrank += d*summ 

			newranks [page] = newrank
		ranks  = newranks
	return ranks

