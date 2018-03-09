# 排行榜类
class RankingListBean(object):
    name = 'RankingListBean'



    @property
    def aname(self):
        return self._aname

    @aname.setter
    def aname(self, value):
        if not isinstance(value, str):
            raise ValueError('score must be an str!')
        self._aname = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def print(self):
        log = 'RankListBean : \n  aname = %s \n image =%s' % (self.aname, self.image)
        return log
