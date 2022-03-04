'''
입력값 옮길 더명, 본 폴더
본 폴더의 하위 폴더들어가 조건에 맞는 파일들 탐색
딕셔너리값
{알, 애벌레, 번데기, 성충, 감염곤충}
{누에, 흰꽃, 갈색거저리, 동애등에}

1_원천데이터
    상위 폴더에 두가지 만족시 폴더 생성
    실화상
    고화질-> 고화질
    저화질->2번 카메라(2,3,4 저화질 카메라 수에 따라 폴더 생성)

    열화상-> 저화질 안에 열화상 파일들 저장

2_라벨링데이터

'''

generation=['알', '애벌레', '번데기', '성충', '감염곤충']

species = ['누에', '흰점박이꽃무지','갈색거저리','동애등에']

# C:\Users\awa\Desktop\Otest\1.이미지 데이터\3.청주 왕굼벵이농장

# C:\Users\awa\Desktop\Otest\1.이미지 데이터\3.청주 왕굼벵이농장\1.흰점박이꽃무지\4.성충\2.저해상도\4번상자cam_121.188.35.158\열화상

import os

os.walk("C:/Users/awa/Desktop/test_data").__next__()
class Cpf:
    def __init__(self,xpath, opath):
        xpath = self.trim_path(xpath)
        opath = self.trim_path(opath)
        self.find_file(opath)
        try:
            if not os.path.exists(xpath+'원천데이터/'):
                os.makedirs(xpath+'원천데이터/')

            if not os.path.exists(xpath+'원천데이터/'+'실화상/'):
                os.makedirs(xpath + '원천데이터/'+'실화상/')

            for i, j in enumerate(species):
                path=xpath+'원천데이터/'+'실화상/'+i+'.'+j+'/'
                if not os.path.exists(path):
                    os.makedirs(path)

            for k,l in enumerate(generation):
                path = path+k+'.'+l+'/'
                if not os.path.exists(path):
                    os.makedirs(path)


            if not os.path.exists(xpath+'1_원천데이터/'+'열화상/'):
                os.makedirs(xpath + '1_원천데이터/'+'열화상/')


            if not os.path.exists(xpath+'2_라벨링데이터/'):
                os.makedirs(xpath+'2_라벨링데이터/')
            else:
                pass
        except:
            pass

    def find_file(self,path):

        path_info = os.walk(path).__next__()
        print(path_info)
        if len(path_info[1]) > 0:
            for path in path_info[1]:
                path_=  path_info[0]+path
                self.find_file(path_)
        else:
            if path_info[2]:
                files = [path+i for i in path_info[2]]
                for file in files:

                    if '열화상' in file:


    def mk_dir(self, file_path):
        if '열화상' in file_path:
            pass

    def trim_path(self, path):
        path = path.replace('\\', '/')
        if path[-1] != "/":
            path += "/"
        return path

if __name__=="__main__":
    xpath,opath = input().split() #빈폴더, 파일이 있는 폴더
    window = Cpf(xpath, opath)
