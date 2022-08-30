for i in range(5):
    if i==0:
        print('i=0, então: ', i)
    elif i==1:
        print('i=1, então: continue')
        continue
    elif 1<i<3:
        print('A variável i é: ', i)
    elif i==3:
        print('i=3, então: break')
    break
    else:
       print('i>3, então: ', i)