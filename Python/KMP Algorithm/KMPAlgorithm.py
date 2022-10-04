# KMP i.e Knuth Morris Pratt is a pattern searching algorithm.
def getKMP(pat, txt):
	len_pat = len(pat)
	len_txt = len(txt)
	lps = [0]*len_pat
	j = 0
	getLPSArray(pat, len_pat, lps)
	i = 0 
	while (len_txt - i) >= (len_pat - j):
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == len_pat:
			print ("Pattern found at index " + str(i-j))
			j = lps[j-1]

		elif i < len_txt and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
#lps indicates longest proper prefix which is also suffix
def getLPSArray(pat, len_pat, lps):
	len = 0
	lps[0]
	i = 1
	while i < len_pat:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

txt = "wwowowddwowowowowo"
pat = "wowdd"
getKMP(pat, txt)
