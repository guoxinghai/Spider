import DBUtil
import requests
import json


class Spider(object):
    def __init__(self):
        self.url = "https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.37997175&x-zp-page-request-id=99cb08a8ab3446338433325c01713a96-1558357664883-153990"
        self.header = {
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        self.db = DBUtil.MysqlUtil()

    # 获取主页信息xhr
    def getxhr(self, url):
        resp = requests.get(url, headers=self.header)
        data = resp.text
        self.parsexhr(data)

    # 解析xhr信息
    def parsexhr(self, data):
        js = json.loads(data)
        res = js['data']['results']
        for item in res:
            self.save(item)

    # 解析dict并写入数据库
    def save(self, data):
        res = []
        res.append(data['salary'])
        res.append(data['jobName'])
        res.append(data['city']['display'])
        res.append(data['eduLevel']['name'])
        res.append(','.join(data['extractSkillTag']))
        res.append(data['workingExp']['name'])
        self.db.insert(res)

    # 循环爬取
    def start(self, item):
        for i in range(0, item):
            url = self.url % (i*90)
            self.getxhr(url)
            print("爬取了第%s页" % (i+1))
        # 将事务提交
        self.db.commit()


# 开始爬取
Spider().start(12)
