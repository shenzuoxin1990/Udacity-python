#coding=utf-8
import webbrowser


class Movie():
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                poster_image, trailer_youtube):
        """
        初始化Movie对象的构造方法
        movie_title：电影名称，赋值到Movie对象的title变量
        movie_storyline：电影简介，赋值到Movie对象的storyline变量
        poster_image：电影海报，赋值到Movie对象的poster_image_url变量
        trailer_youtube：电影预告片，赋值到Movie对象的trailer_youtube_url变量
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ 输入Movie对象，以Movie的trailer_youtube_url变量为url打开浏览器"""
        webbrowser.open(self.trailer_youtube_url)
