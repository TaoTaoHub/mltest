from snownlp import SnowNLP
from aipNlp import aipNlp

def getMax(list):
    temp = list[0]
    for arr in list:
        if arr['texts']['text_2'] in arr['texts']['text_1']:
            arr['score'] = 1
            temp = arr
            break
        if temp['score'] < arr['score']:
            temp = arr
    return temp

def getEvaluate(result):
    if result['score'] > 0.77:
        result['evaluate'] = '得1.0分，本题要点：【' + result['texts']['text_2'] + '】，考生答案：'+result['texts']['text_1']
    elif(result['score'] >= 0.66 and result['score'] <= 0.78):
        result['evaluate'] = '得0.5分，本题要点：【' + result['texts']['text_2'] + '】，考生答案：' + result['texts']['text_1']
    else:
        result['evaluate'] = '得0.0分，本题要点：【' + result['texts']['text_2'] + '】，考生答案：考生漏答该要点'
    return result


def analize(text, targets):
    s = SnowNLP(text)
    resultList = []
    for target in targets:
        tempList = []
        for sentence in s.sentences:
            tempList.append(aipNlp.simnet(sentence, target))
        result = getMax(tempList)
        result = getEvaluate(result)
        resultList.append(result['evaluate'])
    return resultList

text1 = '问题：' \
       '1、图书馆数量不足,人们想读书也没地方读。' \
       '2、低头族盛行，真正读书的人太少。' \
       '3、国外同胞文明缺失现象突出。' \
       '4、社上出现违反传统礼仪规范现象，一些优良的传统道德和礼仪在现代化过程中流失。' \
       '5、大学生社会责任感缺失，对家庭缺乏情感关怀等现象突出，' \
       '建议：' \
       '1、制定图书馆法，多建图书馆，共享大学图书馆。' \
       '2、加强社公文明素养教育，提升国民文明修养。领导干部、公众人物发挥表率示范作用,' \
       '3、擦亮国人“礼仪名片”，落小落细落实核心价值观。' \
       '4、归纳整理行业和地域礼俗，并编制礼仪教材。' \
       '5、高效开设孝道教育的国学课程，大力开展以“孝爱”为主题的教育活动。'

text2 ='主要关注国民素质的相关问题：' \
       '1、各个地方供阅读场所不足,国民缺乏阅读；' \
       '2、不文明现象频发,国民素质低；' \
       '3、优良传统道德文化流失,出现违反传统礼仪规范现象；' \
       '4、大学生缺乏社会责任感,缺乏对家庭的情感关怀。' \
       '建议有:' \
       '1.多建、开放图书馆,倡导全民阅读,建设书香社会；' \
       '2.加强自身文明修养，领导干部、公众人物起示范作闵；' \
       '3.挖掘文明精华，编制礼仪教材，让全社会共同遵循文明礼仪；' \
       '4.开设国学课程，增强孝道意识，开展教育活动，推行素质教育。'

text3 = '问题：社会公德、职业道德、家庭美德、个人品德存在缺失。1、国人文明素质低屡被曝光；2、违反传统礼仪规范；3、大学生社会责任感缺失；4、低头族普遍缺乏真正的阅读。建议：1、增设阅读场所，创造条件倡导全民阅读，资源共享，实现书香社会；2、发挥榜样模范作用，领导干部，公众人物要做好表率；3、提倡文明礼仪，古今结合，归纳行业和地域礼俗并编制礼仪教材；4、弘扬孝爱美德，加强素质教育，引导学生从我做起，从小做起，开设孝道教育课程，开展孝爱主题活动，学习音乐和美术知识，鼓励创新。'

text4 = '1、道德教育口号化，大众缺乏深度阅读。建议：增加阅读场所，引导全民阅读。2、国民素质降低，海外形象被破坏。建议：做好榜样示范工作，加强自身文明修养。3、漠视传统礼仪规范。建议：编制礼仪教材，普及文明礼仪。4、大学生缺乏社会责任感及家庭情感关怀。建议：开设孝道教育课程，开展相关主题教育活动。5、缺乏文化素养。建议：加强中小学生素质教育'

text5 = '问题：1.国民缺少阅读场所；2.文明缺失；3,优良传统道德文化流失。具体建议：1.建设图书馆，共享大学图书馆；2.加强社会文明素养教育，传承发扬优秀传统文化，领导干部、公众人物应做好表率；3.挖掘古代文明礼仪精华，整理行业和地域礼俗，编制礼仪教材，供国民学习；4.高效开设国学课程，大力开展传统文化主题活动，从中学开始，进行艺术类教育学习。'



problems = ['阅读场所不足', '低头族多，读书人少', '文明缺失', '道德礼俗缺失', '社会责任感缺失']
advices = ['倡导全民阅读，广建阅读场所', '加强法律保障，营造氛围，大学图书馆与公众共享', '加强素质教育，发挥榜样典型作用', '重新建构社会礼俗与价值体系，并与日常生活结合起来', '开设素质教育，开设专门的教育课程、活动']

print('########答案1#######')
resultList = analize(text1, problems)
for x in resultList:
    print(x)


print('########答案2#######')
resultList = analize(text2, problems)
for x in resultList:
    print(x)

print('########答案3#######')
resultList = analize(text3, problems)
for x in resultList:
    print(x)

print('########答案4#######')
resultList = analize(text4, problems)
for x in resultList:
    print(x)

print('########答案5#######')
resultList = analize(text5, problems)
for x in resultList:
    print(x)