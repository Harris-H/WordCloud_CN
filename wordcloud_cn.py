# - * - coding: utf - 8 -*-
"""
create wordcloud with chinese
=============================

Wordcloud is a very good tool, but if you want to create
Chinese wordcloud only wordcloud is not enough. The file
shows how to use wordcloud with Chinese. First, you need a
Chinese word segmentation library jieba, jieba is now the
most elegant the most popular Chinese word segmentation tool in python.
You can use 'PIP install jieba'. To install it. As you can see,
at the same time using wordcloud with jieba very convenient
"""
import argparse

import jieba
# Setting up parallel processes :4 ,but unable to run on Windows
# jieba.enable_parallel(4)
import imageio.v3 as iio
import matplotlib.pyplot as plt
import os
# jieba.load_userdict("txt\userdict.txt")
# add userdict by load_userdict()
from wordcloud import WordCloud, ImageColorGenerator


class WordCloudGenerator:
    def __init__(self, textPath, stopwordsPath, maskPath, fontPath, imgPath, userDictList, imgFormat):
        self.text_path = textPath
        self.stopwords_path = stopwordsPath
        self.mask_path = maskPath
        self.font_path = fontPath
        self.imgName1 = os.path.join(imgPath, os.path.splitext(os.path.basename(textPath))[0] + '.' + imgFormat)
        self.imgName2 = os.path.join(imgPath, os.path.splitext(os.path.basename(textPath))[0] + '_colored.' + imgFormat)
        self.userDict_list = userDictList
        self.imgFormat = imgFormat

    def read_and_process_text(self):
        with open(self.text_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text

    def read_and_process_stopwords(self):
        with open(self.stopwords_path, 'r', encoding='utf-8') as f:
            stopwords = f.read().splitlines()
        return stopwords

    def read_and_process_mask(self):
        mask = iio.imread(self.mask_path)
        return mask

    def jieba_processing_txt(self, text):
        for word in self.userDict_list:
            jieba.add_word(word)

        mywordlist = []
        seg_list = jieba.cut(text, cut_all=False)
        liststr = "/ ".join(seg_list)

        with open(self.stopwords_path, encoding='utf-8') as f_stop:
            f_stop_text = f_stop.read()
            f_stop_seg_list = f_stop_text.splitlines()

        for myword in liststr.split('/'):
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)
        return ' '.join(mywordlist)

    def generate_wordcloud(self, text):
        wc = WordCloud(font_path=self.font_path, background_color="white", max_words=2000,
                       mask=self.read_and_process_mask(),
                       max_font_size=100, random_state=42, width=1000, height=860, margin=2, )
        wc.generate(self.jieba_processing_txt(text))
        return wc

    def save_wordcloud(self, wc, filename):
        if self.imgFormat == 'svg':
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(wc.to_svg())
        else:
            wc.to_file(filename)

    def display_and_save_wordcloud(self, wc):
        # create coloring from image
        image_colors_default = ImageColorGenerator(self.read_and_process_mask())

        plt.figure()
        # recolor wordcloud and show
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        # save wordcloud
        self.save_wordcloud(wc, self.imgName1)

        # create coloring from image
        image_colors_byImg = ImageColorGenerator(self.read_and_process_mask())

        # show
        # we could also give color_func=image_colors directly in the constructor
        plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
        plt.axis("off")
        plt.figure()
        plt.imshow(self.read_and_process_mask(), interpolation="bilinear")
        plt.axis("off")
        plt.show()

        # save wordcloud
        self.save_wordcloud(wc, self.imgName2)


# The function for processing text with Jieba


if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate a word cloud")

    # Add the arguments
    parser.add_argument('--text_path', default='data/CalltoArms.txt', help='Path to the input text file')
    parser.add_argument('--stopwords_path', default='data/stopwords_cn_en.txt', help='Path to the stopwords file')
    parser.add_argument('--mask_path', default='data/LuXun_color.jpg', help='Path to the mask image file')
    parser.add_argument('--font_path', default='fonts/SourceHanSerif/SourceHanSerifK-Light.otf',
                        help='Path to the font file')
    parser.add_argument('--img_path', default='result/', help='Path to save the word cloud images')
    parser.add_argument('--userDict_list', nargs='+', default=['阿Ｑ', '孔乙己', '单四嫂子'],
                        help='List of user-defined words')
    parser.add_argument('--img_format', default='jpg', help='Format to save the word cloud images(jpg,svg etc.')
    # Parse the arguments
    args = parser.parse_args()

    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(args.img_path):
        os.makedirs(args.img_path)

    # Use the arguments
    wcg = WordCloudGenerator(args.text_path, args.stopwords_path, args.mask_path, args.font_path, args.img_path,
                             args.userDict_list, args.img_format)
    text = wcg.read_and_process_text()
    wc = wcg.generate_wordcloud(text)
    wcg.display_and_save_wordcloud(wc)
