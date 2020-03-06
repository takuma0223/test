n,m=input(),1
for i in range(2,int(n)):
	m*=(int(n)%i)
print("not prime") if m==0 else print("prime")