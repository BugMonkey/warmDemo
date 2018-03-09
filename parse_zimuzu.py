import requests
from requests.exceptions import MissingSchema, ReadTimeout

from RankingListBean import RankingListBean
from bs4 import BeautifulSoup


class parse(object):
    def __init__(self, url):
        self.url = url
        pass

    def start_parse(self):
        # 整个网页
        soup = self.get_soup(self.url)

        # 标题栏
        title = soup.title.text
        print('标题 ：%s' % title)
        print('------------------------------------------------------\n')

        #  相关链接
        links = soup('div', class_='xy-tags')[0]('a')
        print('链接\n')
        for link in links:
            print(' http://www.zimuzu.tv%s  :  %s' % (link.get('href'), link.text))
        print('---------------------------------------------\n')

        # 排行
        ranks = soup('div', class_='box xy-list')
        # 返回数据list
        result_list = []
        for rank in ranks:
            #  如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
            # 如果tag包含了多个子节点, tag就无法确定.string方法应该调用哪个子节点的内容,.string的输出结果是None:
            #  二级标题 ：
            sec_title = rank(class_='title clearfix')[0](class_='a0')[0]
            print('%s  : \n' % sec_title.string)
            all_link_url = rank(class_='btn-top50')[0]
            if all_link_url:
                print(' http://www.zimuzu.tv%s' % (all_link_url.a['href']))
                # self.get_sub_item(' http://www.zimuzu.tv%s' % (all_link_url.a.get('href')))
                result_list.append(self.get_sub_item(' http://www.zimuzu.tv%s' % (all_link_url.a.get('href'))))

                # self.get_sub_item('http://www.zimuzu.tv/html/top/month_fav_list.html')
            print('\n-------------------------------------------------')
            result_list.append('\n-----------------------------------------------------------------------------------')
        return result_list

    # 获取列表项详细信息返回实体bean
    def get_sub_item(self, url):
        all_soup = self.get_soup(url)

        if all_soup:
            rank_item = all_soup('div', class_='box xy-list xy-list-grid')[0].ul('li')
            count = 0
            str_result = []

            for li in rank_item:
                count = count + 1
                a0 = li('div', class_='a0')
                # tag的属性操作方法与字典一样  a['']
                img = a0[0]('img')[0]['rel']

                link_url = a0[0]('div', class_='fl info')[0].a['href']
                sub_item_name = a0[0]('div', class_='fl info')[0].a.strong.string
                sub_item_ename = a0[0]('div', class_='fl info')[0].a.text
                # p 节点直接gettext
                print(a0[0]('div', class_='fl info')[0].p.split('</br>', '\n'))
                sub_item_type = a0[0]('div', class_='fl info')[0].p.get_text() + '    ' + \
                                a0[0]('div', class_='fl info')[0].p.span.string
                # print(sub_item_type)
                '''print("%s  : %s - %s  http://www.zimuzu.tv%s   描述 ：%s" % (
                    count, sub_item_name, sub_item_ename, link_url, sub_item_type))
                    '''
                str_result.append("%s  : %s - %s  http://www.zimuzu.tv%s   描述 ：%s" % (
                    count, sub_item_name, sub_item_ename, link_url, sub_item_type) + '\n')
            return str_result

    # 获取指定网页
    def get_soup(self, url):

        session = requests.Session()
        session.trust_env = False

        try:

            response = session.get(url)
            response.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

            return BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

        except MissingSchema:
            print
            'invalid url %s' % (url)
        except Exception as e:
            print(e)
