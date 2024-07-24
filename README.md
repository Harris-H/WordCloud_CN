# WordCloud_CN



`WordCloud_CN` 是一个用于生成中文词云的 Python 脚本。它使用了 `jieba` 分词库和 `wordcloud` 库，可以生成高质量的中文词云图像。

<img src="https://pic.imgdb.cn/item/669fad04d9c307b7e91872b3.jpg#pic_center" />



<img src="https://pic.imgdb.cn/item/669fad04d9c307b7e9187312.jpg#pic_center" />

## 特点😎

- **中文分词**：使用 `jieba` 分词库进行中文分词，支持用户自定义词典，可以更准确地进行中文分词。

- **灵活的词云生成**：使用 `wordcloud` 库生成词云，可以自定义词云的形状、颜色、字体、大小等。

- **图片保存**：支持将生成的词云保存为图片，支持多种格式，包括 jpg 和 svg 等。

- **命令行参数**：支持通过命令行参数来指定输入文本、停用词、遮罩图像、字体文件、图片保存路径、用户自定义词典和图片格式等。

## 优势😺

- **易用性**：只需要简单的命令行参数就可以生成词云，无需复杂的配置。

- **灵活性**：支持多种自定义选项，可以生成各种样式的词云。

- **高效性**：使用了 `jieba` 分词库和 `wordcloud` 库，可以快速生成词云。

- **兼容性**：支持多种图片格式(jpg，svg等)，可以在多种环境下使用。



## 1 环境准备🗃️

在运行 `WordCloud_CN` 脚本之前，请确保您的环境中已经安装了所需的 Python 依赖项。您可以使用以下步骤来准备环境：

1. **克隆仓库**：
    ```sh
    git clone https://github.com/Harris-H/WordCloud_CN
    cd WordCloud_CN
    ```

2. **本地环境或创建虚拟环境**（可选，但推荐）：
    
    ```sh
    conda create -n myenv python=3.11.5
    conda activate myenv
    ```
    
3. **安装依赖项**：
    
    ```sh
    pip install -r requirements.txt
    ```

`requirements.txt` 文件内容如下：
```plaintext
argparse
jieba
imageio
matplotlib
wordcloud
```

## 2 使用方法🚩

### 默认参数

如果你想使用默认的参数来生成词云，你可以直接运行 `wordcloud_cn.py` 脚本：

```sh
python wordcloud_cn.py
```

这将使用脚本中预设的默认参数来生成词云。

### 自定义参数

如果你想自定义参数来生成词云，你可以在运行 `wordcloud_cn.py` 脚本时添加命令行参数：

```sh
python wordcloud_cn.py --text_path your_text.txt --stopwords_path your_stopwords.txt --mask_path your_mask.jpg --font_path your_font.otf --img_path your_directory/ --userDict_list your_words --img_format jpg
```

