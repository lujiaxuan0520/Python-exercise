#!/usr/bin/python
#coding=utf-8
import numpy as np
def sortLabel():
    MTLLabel=np.loadtxt("MTL_Male.dat")
    CMTLLabel=np.loadtxt("CMTL_Male.dat")
    CEMTLLabel=np.loadtxt("CEMTL_Male.dat")
    MTLLabel=np.abs(MTLLabel)
    CMTLLabel=np.abs(CMTLLabel)
    CEMTLLabel=np.abs(CEMTLLabel)
    MTLIndex = np.argsort(-MTLLabel)
    MTLLabel=sorted(MTLLabel,reverse=True)
    CMTLIndex=np.argsort(-CMTLLabel)
    CMTLLabel=sorted(CMTLLabel,reverse=True)
    CEMTLIndex=np.argsort(-CEMTLLabel)
    CEMTLLabel=sorted(CEMTLLabel,reverse=True)
    #调用降维函数
    reduceDimension(CEMTLIndex, 3304)#选择文件和k


def reduceDimension(Index,k):
    #对训练集进行降维
    TrainSample =np.loadtxt("MTL_Male_train.dat",delimiter=',')
    print(TrainSample.shape)
    index=Index[0]
    TrainSub=np.array([TrainSample[:,index]])
    TrainSub.resize(1000,1)
    for i in range(1,k):
        index=Index[i]
        col=TrainSample[:,index]
        TrainSub=np.column_stack((TrainSub,col))
    np.savetxt("TrainSub.txt",TrainSub)

    #对测试集进行降维
    TestSample = np.loadtxt("MTL_Male_test.dat", delimiter=',')
    print(TestSample.shape)
    index = Index[0]
    TestSub = np.array([TestSample[:, index]])
    TestSub.resize(800, 1)
    for i in range(1, k):
        index = Index[i]
        col = TestSample[:, index]
        TestSub = np.column_stack((TestSub, col))
    np.savetxt("TestSub.txt", TestSub)


if __name__=='__main__':
    sortLabel()
