class Mama:
    def face(self):
        print('好看的容颜')
    def chu_yi(self):
         print('好吃的饭菜')
    def shen_gao(self):
         print('身高160CM')

class Baba:
     def car(self):
         print('会开车')
     def banzhuan(self):
         print('会搬砖')
     def shen_gao(self):
         print('身高175CM')


nvhai = Mama()
print(nvhai)
print(nvhai.face())


class Haizi(Baba,Mama):
    def play(self):
        print('一大堆玩具')

boy = Haizi()
print(boy.play())
print(boy.face())
print(boy.chu_yi())
print(boy.car())
print(boy.shen_gao())
