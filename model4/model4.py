import matlab.engine

'''
you need to install matlab above version of r2017a
to ensure the program won't have any error out of control...
'''

class npk2plant:
    def __init__(self,n,p,k):
        self.n = float(n)
        self.p = float(p)
        self.k = float(k)
    def predict(self):
        columnarray = [[self.n],[self.p],[self.k]]
        eng = matlab.engine.start_matlab()
        eng.cd(r'model4', nargout=0)
        num = matlab.double(columnarray)
        ans = eng.NPK2(num)
        return ans

