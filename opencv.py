import os,string

mode='train'
if not os.path.exists('dataset'):
    os.makedirs('dataset')

if not os.path.exists('dataset/train_set'):
    os.makedirs('dataset/train_set')

if not os.path.exists('dataset/test_set'):
    os.makedirs('dataset/test_set')
if mode=='train':
    for alpha in list(string.ascii_uppercase):
        if not os.path.exists('dataset/'+mode+'_set/'+alpha):
            os.makedirs('dataset/'+mode+'_set/'+alpha)
mode='test'
if mode=='test':
    if not os.path.exists('dataset/'+mode+'_set/'+alpha):
        for alpha in list(string.ascii_uppercase):
            os.makedirs('dataset/'+mode+'_set/'+alpha)
