

def prepare_translations(file_eng, file_trans, file_to_evaluate):
    eng_file = open(file_eng, 'r')
    trans_file = open(file_trans, 'r')
    evaluating_file = open(file_to_evaluate, 'w+')
    while True:
        line1 = eng_file.readline()
        line2 = trans_file.readline()
        line1=line1.replace('\n','')
        line2=line2.replace(' .','.')
        line2=line2.replace(' , ', ', ')

        line_to_write= line1+" ||| "+line2
        evaluating_file.write(line_to_write)

        if not line1 and not line2:
            break

def original_sent(file_eng, eng_to_append):
    eng_file = open(file_eng, 'r')

    evaluating_file = open(eng_to_append, 'w+')
    while True:
        line1 = eng_file.readline()
        fields = line1.split("\t")
        if len(fields)>1:
            print(fields[2])

            line_to_write = fields[2]+'\n'
            evaluating_file.write(line_to_write)

        if not line1:
            break

if __name__ == "__main__":
    #original_sent('data/aggregates/en.txt', 'data/aggregates/en_sen_only.txt')
    #original_sent('data/aggregates/en_pro.txt', 'data/aggregates/en_pro_sen_only.txt')
    #original_sent('data/aggregates/en_anti.txt', 'data/aggregates/en_anti_sen_only.txt')

    #prepare_translations('data/aggregates/en_sen_only.txt','translations/winomtspeech/st_winomtspeech_ende.hyp', 'translations/winomtspeech/en-de.txt')
    #prepare_translations('data/aggregates/en_sen_only.txt', 'translations/winomtspeech/st_winomtspeech_enes.hyp','translations/winomtspeech/en-es.txt')
    #prepare_translations('data/aggregates/en_sen_only.txt', 'translations/winomtspeech/st_winomtspeech_enfr.hyp','translations/winomtspeech/en-fr.txt')
    #prepare_translations('data/aggregates/en_sen_only.txt', 'translations/winomtspeech/st_winomtspeech_enit.hyp','translations/winomtspeech/en-it.txt')

    prepare_translations('data/iwslt-es/train.en-es.en', 'data/iwslt-es/train.en-es.es',
                         'data/iwslt-es/for_align_trans.en')



