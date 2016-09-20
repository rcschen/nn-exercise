import numpy as np


def gen_data(min=50, max=100):
    length=np.random.randint(min, max)
    #print length
    v_seq = np.random.uniform(size=(length,1))
    i_seq = np.zeros((length,1))
    #print v_seq
    #print i_seq
    x_seq = np.concatenate([v_seq, i_seq], axis=1)
    #print x_seq
    x_seq[ np.random.randint(0,length/2),1] =1
    x_seq[ np.random.randint((length/2)+1, length),1] = 1
    #print x_seq
    y_hat = np.sum(x_seq[:,0]*x_seq[:,1])
    #print y_hat
    return x_seq, y_hat
gen_data(5,10)    
