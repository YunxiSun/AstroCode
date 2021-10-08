import numpy as np
from astropy.io import fits
import struct
import math
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
image_path='small.fits'
out_path='out.txt'

in_file=open(image_path,'rb+')
out_file=open(out_path,'wb+')


header_name=['SIMPLE  =','BITPIX  =','NAXIS   =','NAXIS1  =','NAXIS2  =','END      ']
header_data=['  T ',' -32','  2 ','1340','1300','    ']
for i in range(0,6):
    space=[' 'for j in range(80)]
    space[0:9]=header_name[i]
    space[26:30]=header_data[i]
    str=''.join(space).encode()
    out_file.write(str)

for j in range(30):
    space1=[' 'for i in range(80)]
    str1=''.join(space1).encode()
    out_file.write(str1)

hdu_1=fits.open(image_path)
i_data=hdu_1[0].data[0]
i_data=np.float32(i_data)
o_data=np.transpose(i_data)
col,row=i_data.shape
print(row,col)
for i in range(row):
    for j in range(col):
        out_file.write(struct.pack('!f',o_data[i][j]))

left=2880-((col*row*4+2880)%2880)
for i in range(left):
    spa=' '
    str3=struct.pack('!s',spa.encode())
    out_file.write(str3)
in_file.close()
out_file.close()

hdu_2=fits.open(out_path)
d=hdu_2[0].data

plt.subplot(1,2,1)
plt.imshow(d)
plt.title("生成图")
plt.subplot(1,2,2)
plt.imshow(i_data)
plt.title("原图")
plt.show()