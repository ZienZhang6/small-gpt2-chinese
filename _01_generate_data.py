with open('/root/learning_deepspeed/_01_小型GPT中文闲聊/data/train.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

train_datas = []
temp_data = ''
for line in lines:

    if line!='\n':
        line = line.strip()
        temp_data+=(line+'\t')
    else:
        train_datas.append(temp_data)
        temp_data=''



with open('/root/learning_deepspeed/_01_小型GPT中文闲聊/data/dataset_train.txt','w',encoding='utf-8') as f:
    for train_data in train_datas:
        f.write(train_data+'\n')

