**广东省自学考试管理系统自动登录脚本**

这个 Python 脚本使用 Selenium 和 ddddocr 库自动登录广东省自学考试管理系统。它会打开 Chrome 浏览器并输入指定的考生号和密码，然后自动识别验证码并尝试登录。如果登录失败，则会重新加载页面并重试。



**环境要求**

•  Python 3

•  Chrome 浏览器



**安装依赖**

使用以下命令安装脚本所需的 Python 库：

`pip install selenium webdriver-manager ddddocr`



**使用方法**

1. 下载脚本并解压到任意目录。

2. 在命令行中进入脚本目录。

3. 运行脚本：

   `python login.py`

  脚本会提示您输入考生号和密码。输入后按回车键继续。

  注意：脚本只会尝试登录一次，如果登录失败则会退出。如果您需要多次登录，请手动运行脚本多次。

4. 如果登录成功，脚本会打印提示信息并退出。

**常见问题**



**如何指定 Chrome 浏览器的路径？**

脚本使用 webdriver_manager 库来自动下载和管理 Chrome 驱动程序。如果您的 Chrome 浏览器安装在非标准路径下，可以使用以下方式指定 Chrome 可执行文件的路径：

```python
from selenium.webdriver.chrome.service import Service

from selenium import webdriver

service = Service('/path/to/chromedriver')

driver = webdriver.Chrome(service=service)
```

将 `/path/to/chromedriver` 替换为实际的 Chrome 可执行文件路径即可。



**如何修改验证码识别模型**

脚本使用 ddddocr 库来识别验证码。如果您发现识别率不高，可以尝试使用其他识别模型。请参考 ddddocr 文档中的说明：https://github.com/ouyanghuiyu/ddddocr#%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F



**如何修改验证码图片保存路径？**

脚本默认将验证码图片保存为 code.png 文件。如果您需要修改保存路径，请修改以下代码：

`code_img.screenshot('code.png')`

将 `'code.png'` 替换为其他文件路径即可。注意，路径必须是相对于脚本当前目录的相对路径，否则可能无法正常保存文件。



**版权和许可**

代码采用 MIT 许可证发布，详情请参见 LICENSE 文件。