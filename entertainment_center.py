#coding=utf-8
import media
import fresh_tomatoes

#模拟真实的数据流格式，一般为list，这里代用list
"""
模拟真实的数据流格式，一般为json，这里暂用list
数据来源：豆瓣电影：https://movie.douban.com/
获取方式：阅读网页源码获取http链接
"""
movie_list = [["我不是药神",
                "本片改编自慢粒白血病患者陆勇代购抗癌药的真实事迹。",
                "https://img3.doubanio.com/view/photo/l/public/p2525712050.webp",
                "http://vt1.doubanio.com/201807181531/73583c5fe0fddba9a69f8779efb14fba/view/movie/M/402330315.mp4"],
                ["邪不压正",
                "本片根据张北海的小说《侠隐》改编。",
                "https://img3.doubanio.com/view/photo/l/public/p2524634631.webp",
                "http://vt1.doubanio.com/201807181104/05773e67056b9c4f8e2e07babbbb21cd/view/movie/M/402330091.mp4"],
                ["后来的我们",
                "两个北漂青年的奋斗生活。",
                "https://img1.doubanio.com/view/photo/l/public/p2519994468.webp",
                "http://vt1.doubanio.com/201807181540/b4e82b899bc73ea034b2cf06cf9d2559/view/movie/M/402300311.mp4"],
                ["三块广告牌",
                "被绝望和痛苦缠绕的米尔德雷德租下了高速公路边上的三块巨型广告牌，在上面控诉警方办案无能。",
                "https://img1.doubanio.com/view/photo/l/public/p2510081688.webp",
                "http://vt1.doubanio.com/201807181541/e1f0abc18f6f3692e6098d4a6a272896/view/movie/M/302250906.mp4"],
                ["爱你，西蒙",
                "每个人都值得拥有一个伟大的爱情故事。",
                "https://img1.doubanio.com/view/photo/l/public/p2516430118.webp",
                "http://vt1.doubanio.com/201807181543/9bb69ce99831f693f5c11432119c5ffc/view/movie/M/302260847.mp4"],
                ["头号玩家",
                "五人踏上了寻找彩蛋的征程。",
                "https://img1.doubanio.com/view/photo/l/public/p2516578307.webp",
                "http://vt1.doubanio.com/201807181544/c3179965097a79400cd2822f11dcaf52/view/movie/M/402290187.mp4"]]

"""
make_movies方法是由输入的数据流，转换成可供生成页面的对象流的函数
data-list   ：   真实的数据流
return      :    以自定义对象Movie为泛型的list列表
"""

def make_movies(data_list):
    movies = []
    for data in data_list:
        new_movie = media.Movie(data[0],data[1],data[2],data[3])
        movies.append(new_movie)
    return movies

movies = make_movies(movie_list)

"""
2018-07-18：
原始的open_movies_page方法并不能实现打开豆瓣预告片的链接
所以对fresh_tomatoes.py文件进行了小幅度的修改，以便支持豆瓣电影的超链接
修改记录详见fresh_tomatoes.py
by shenzuoxin
"""
fresh_tomatoes.open_movies_page(movies)
