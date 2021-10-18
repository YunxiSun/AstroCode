import cv2 as cv
from  matplotlib import pyplot as plt
import numpy as np
from astropy.io import fits

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#同态滤波函数
def TongTai(img,d0=10,rL=0.5,rH=2,c=4,h=2.0,l=0.5):
    row,col=img.shape
    imgftt=np.fft.fft2(img)
    imgfttshift=np.fft.fftshift(imgftt)
    M,N=np.meshgrid(np.arange(-col//2,col//2),np.arange(-row//2,row//2))
    D=np.sqrt(M**2+N**2)
    Z=(rH-rL)*(1-np.exp(-c*(D**2/d0**2)))+rL
    dstfftshift=Z*imgfttshift
    dstfftshift=(h-l)*dstfftshift+l
    dstfftshift=np.fft.fftshift(dstfftshift)
    dstfft=np.fft.ifft2(dstfftshift)
    dst=np.real(dstfft)
    return dst



ImagePath='1.fits'

hdu=fits.open(ImagePath)
image=hdu[0].data
image_new=TongTai(image)

plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title('原图')
plt.subplot(1,2,2)
plt.imshow(image_new,cmap='gray')
plt.title('同态滤波后的图')
plt.show()