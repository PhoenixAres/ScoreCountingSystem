from student import *
import matplotlib.pyplot as plt
import xlwt

def generate(n):
    id = set()
    ls = []
    for i in range(n):
        stu = STU()
        stu.generate()
        while stu.GetID() in id:
            stu.generate()
        id.add(stu.GetID())
        stu.cal()
        ls.append(stu)
    return ls

def draw(ls, fname):
    data = []
    group = [0, 60, 70, 80, 90, 100]
    for i in ls:
        data.append(i.GetFinalGrade())
    plt.hist(data, group, rwidth=0.8)
    plt.savefig(fname + '.jpg')  # 图片的存储
    plt.close()

def show(ls, fname = '测试样例'):
    ls.sort()
    cnt = [0, 0, -1, 101, 0]
    m1 = -1
    m2 = 101
    sum = 0
    txt = ''
    for i in ls:
        txt += i.GetStr()
        temp = i.GetFinalGrade()
        if temp != -1:
            cnt[2] = max(cnt[2], temp)
            cnt[3] = min(cnt[3], temp)
            cnt[4] += temp
            if temp >= 60:
                cnt[1] += 1
        else:
            cnt[0] += 1
    data = ['总人数:' + str(len(ls)) + '\n']
    data.append('旷考数:' + str(cnt[0]) + '\n')
    data.append('最高分:' + str(cnt[2]) + '\n')
    data.append('最低分:' + str(cnt[3]) + '\n')
    data.append('平均分:' + '{:.2f}'.format(cnt[4]/(len(ls)-cnt[0])) + '\n')
    data.append('及格率:' + '{:.2%}'.format(cnt[1]/(len(ls)-cnt[0])) + '\n')
    for i in data:
        txt += i
    draw(ls, fname)
    txt += '\n生成了 ' + fname + '.jpg' + ' 文件\n'
    record(ls, data, fname)
    txt += '生成了 ' + fname + '.xls' + ' 文件\n'
    return txt

def record(ls, data, fname):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('学生成绩统计')
    temp = ['学号', '姓名', '班级', '平时成绩', '期中成绩', '期末成绩', '总评成绩']
    for i in range(0, len(temp)):
        sheet.write(0, i, temp[i])
    for i in range(0, len(ls)):
        s = ls[i].GetStr().split()
        for j in range(0, len(s)):
            sheet.write(i+1, j, s[j])  # row, column, value
    temp = []
    for i in range(0, len(data)):
        temp.append(data[i].split(':'))
    for i in range(0, 2):
        for j in range(0, len(temp)):
            sheet.write(len(ls)+2+i, j, temp[j][i])
    workbook.save(fname + '.xls')