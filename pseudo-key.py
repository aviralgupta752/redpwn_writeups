from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

ct= "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
pk= "iigesssaemk"

def decrypt(ctxt, key):
	for i in range(len(ct)):
	    key = ''.join(key[i % len(key)] for i in range(len(ctxt)))
	    ptxt = ''
	    for i in range(len(ctxt)):
	        if ctxt[i] == '_':
	            ptxt += '_'
	            continue
	        x = chr_to_num[ctxt[i]]
	        y = chr_to_num[key[i]]
	        ptxt += num_to_chr[(x - y +26) % 26]
	    return ptxt

key="redpwwwactf"
print(decrypt(ct, key))
'''
for a in ['e', 'r']:
	for b in ['e', 'r']:
		for c in ['d', 'q']:
			for d in ['c', 'p']:
				for e in ['j', 'w']:
					for f in ['j', 'w']:
						for g in ['j', 'w']:
							for h in ['a']:
								for i in ['c', 'p']:
									for j in ['g', 't']:
										for k in ['f', 's']:

'''
