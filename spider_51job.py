# coding:utf-8
# !/usr/bin/python3
import re
import requests

pattern_item = '<div class="el">(.*?)</div>'
pattern_jobName = '<span>.*?>(.*?)</a>.*?</span>'
pattern_companyName = '<span class="t2">.*?>(.*?)</a>.*?</span>'
pattern_location = '<span class="t3">(.*?)</span>'
pattern_salary = '<span class="t4">(.*?)</span>'
pattern_releaseDate = '<span class="t5">(.*?)</span>'

def job(url):
    html = requests.get(url)
    html.encoding = "gbk"
    jobname = []
    companyName = []
    location = []
    salary = []
    releaseDate = []
    itemList = re.findall(pattern_item, html.text, re.S)
    for item in itemList:
        item = item.lstrip().rstrip()
        jobname.append(re.findall(pattern_jobName, item, re.S)[0].strip().lstrip().rstrip())
        companyName.append(re.findall(pattern_companyName, item, re.S)[0])
        location.append(re.findall(pattern_location, item, re.S)[0])
        salary.append(re.findall(pattern_salary, item, re.S)[0])
        releaseDate.append(re.findall(pattern_releaseDate, item, re.S)[0])
    return jobname, companyName, location, salary, releaseDate


def main():
    csv = open('csv.csv', 'a')
    for i in range(1, 51):
        print(i)
        url = "http://search.51job.com/list/080200,000000,0000,00,9,99,python,2," + str(
            i) + ".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        ret = job(url)
        for i in range(ret[0].__len__()):
            for idx, r in enumerate(ret):
                csv.write(r[i])
                if idx!=(ret.__len__()-1):
                    csv.write(',')
                else:
                    csv.write('\n')
    csv.close()


if "__main__" == __name__:
    main()
