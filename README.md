# fofa-gui
利用pyqt5实现的简易版fofa采集gui程序并简单美化

## Notice
1 .使用了QCandyUi美化，当然你可以使用QtAwesome
``` bash
pip3 install QCandyUi -i http://pypi.douban.com/simple
```
2 .如果使用QCandyUi美化，记得修改\Lib\site-packages\QCandyUi\CandyWindow.py中的信息，否则你设置的title和ico可能会不生效
``` python
def createWindow(mainWidget, theme=None, title='FOFA工程狮', ico_path='favicon.ico'):
    """
    快速创建彩色窗 (带TitleBar)
    :param mainWidget:
    :param theme:
    :param title:
    :param ico_path:
    :return:
    """
    coolWindow = WindowWithTitleBar.WindowWithTitleBar(mainWidget)
    coolWindow.setWindowTitle(title)
    coolWindow.setWindowIcon(QIcon(ico_path))
    setTheme(theme)
    return coolWindow
```
3 .textBowser根据场景应使用append()而不是setText()，否则只会显示最后一条数据，且应设置自动换行，否则不会显示更多的结果
``` python
ui.textBrowser.append(lis)
ui.textBrowser.lineWrapMode()#设置自动换行
```
4 .pyinstaller报UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 22: invalid start byte，可尝试在pyinstaller下的compat.py中做如下修改（共两处）
``` python
#out = out.decode(encoding)
out = out.decode(encoding, errors='ignore')
```
## screenshot
![img](https://blog-1259438478.cos.ap-nanjing.myqcloud.com/post-picture1/fofa-gui.png)
