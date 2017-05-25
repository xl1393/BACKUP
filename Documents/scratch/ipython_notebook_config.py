c = get_config()

# 所有matplotlib的图像都通过iline的方式显示
c.IPKernelApp.pylab = 'inline'
# 这一行指向我们刚刚创建的ssl证书
c.NotebookApp.certfile = u'/home/xli/.ipython/profile_nbserver/mycert.pem'
# 给出刚刚创建的密码的哈希值
c.NotebookApp.password = u'sha1:4e45782f0991:e3f59960ee0ec89c7b86d3d850e123408da1e886'
c.NotebookApp.ip = '143.48.140.160'
#  给出运行的端口，ipython默认为8888
c.NotebookApp.port = 8889
#  禁止在运行ipython的同时弹出浏览器
c.NotebookApp.open_browser = False
