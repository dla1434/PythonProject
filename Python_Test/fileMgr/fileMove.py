import os

def search(dirname):
  fileList = os.listdir(dirname)
  for filename in fileList:
    fullpath = os.path.join(dirname, filename)
    if os.path.isdir(fullpath):
      search(fullpath)
    else:
      print('fullpath : ', fullpath)

      path_split = os.path.split(fullpath)
      print('path_split[0] : ', path_split[0])
      print('path_split[1] : ', path_split[1])

			# 한번 더 split을 하게 되면 해당 폴더의 상위 폴더를 얻을 수 있다.
			# 수행 전) C:\NodeJsProject\book_js_jquery_webdongne
			# 수행 후) C:\NodeJsProject
      parentDir = os.path.split(path_split[0])
      print('parentDir[0] : ', parentDir[0])
      print('parentDir[1] : ', parentDir[1])
			
      # os.rename(fullpath, p[0]+'/'+s[1])

search('C:\\NodeJsProject\\book_js_jquery_webdongne\\01부_자바스크립트코어_문법기초\\01장_변수')