fo = open('foghhgjjo.txt','wb')
print("NAME OF THE FILE NAME",fo.name)
fid= fo.fileno()
print("file descriptor",fid)


fo.close()