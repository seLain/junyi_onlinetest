
def reverse_string_by_order(s):
	return ' '.join([''.join(reversed(w)) for w in s.split()])