'''def printkfreq(a,k):
	words=a.split()
	d={}
	for w in words:
		d[w]=d.get(w,0)+1
	for w in d:
		if d[w]==k:
			print(w)
a=input()
k=int(input())
printkfreq(a,k)

       OR

'''

def printkfreq(a,k):
	d={}
	for w in a:
		d[w]=d.get(w,0)+1
	for w in d:
		if d[w]==k:
			print(w)
a=input().split()
k=int(input())
printkfreq(a,k)

