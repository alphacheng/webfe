import numpy as np

def search_average(data,datanum,doorvalue,mode='LargerThan'):
    ''' search the one dimension data when there are datanum of continuous data larger than doorvalue'''
    
    for i in range(0,data.shape[0]):
        
        if np.average(data[i:i+datanum]) > doorvalue and mode =='LargerThan':
        
            return i
    
    
def search_continue(data,datanum,doorvalue,mode='LargerThan'):
    ''' search the one dimension data when there are datanum of continuous data larger than doorvalue'''
    count = 0
    for i in range(0,data.shape[0]):
        
        if mode == 'LargerThan':
            if data[i] > doorvalue: 
                count += 1
                if count >= datanum:
                    return i-datanum
            else:
                count = 0

def search_drop(data,dropamount):
    for i in range(data.shape[0]-1,1,-1):
        drop = float(data[i] - data[i-1])
        #print drop,data[i],data[i-1]
        if  abs(drop) >  dropamount: 
                return i-1

class dmask():
    def __init__(self,name,paralib):
        self.name = name
        self.paralib = paralib
    
    
    # single column operation
    def operlist(self,coldata,operlist):
        for oper in operlist:
            coldata = self.oper(coldata,oper)
            #print coldata
        return coldata
    
    def oper(self,coldata):
        oper = self.paralib
        if oper['oper'] == 'Shift':
            newcoldata = coldata + oper['scalar']
            
        elif oper['oper'] == 'FlipSign':
            newcoldata =  - coldata
        
        elif oper['oper'] == 'CutStart':
            newcoldata =  coldata[oper['scalar']:]
            
        elif oper['oper'] == 'CutEnd':
            newcoldata =  coldata[0:-oper['scalar']]

        elif oper['oper'] == 'Scale':
            newcoldata =  oper['scalar'] * coldata
            
        elif oper['oper'] == 'StartUntilLargerThan':  # do not start until reach some value
            if nodenum not in oper.keys():
                oper['nodenum'] = 5  # 5 node continuous
                
            newcoldata =  oper['scalar'] * coldata
            
        else:
            raise KeyError,('Operation',oper['oper'], ' do not defined\n')
            
        return newcoldata
        
    
    # double column operation
    def coop(self,coldatax,coldatay):
        oper = self.paralib
        if oper['oper'] in  ['Shift','FlipSign','CutStart','CutEnd','Scale']:
            newcoldatax = self.oper(coldatax)
            newcoldatay = self.oper(coldatay)
            
        elif oper['oper'] == 'CutNegative':
            ''' cut the initial negative portion and until n continuous point reach certain value'''
            # which column to detect
            if 'mode' not in oper.keys():
                oper['mode'] = 'x'
            
            if 'nodenum' not in oper.keys():
                oper['nodenum'] = 10
            
            # operation
            if oper['mode'] == 'x':
                id = search_continue(coldatax,oper['nodenum'],0,mode='LargerThan')
                newcoldatax = coldatax[id:]
                newcoldatay = coldatay[id:]
                
        elif oper['oper'] == 'CutDrop':
            if 'mode' not in oper.keys():
                oper['mode'] = 'y'
            
            if oper['mode'] == 'y':  
                id = search_drop(coldatay,oper['scalar'])
                newcoldatax = coldatax[:id]
                newcoldatay = coldatay[:id]               
                    

            
        else:
            raise KeyError,('Operation',oper['oper'], ' do not defined\n')
            
        return newcoldatax,newcoldatay
        
        


if __name__ == '__main__':
    import numpy as np
    

    
    a1 = np.array([1,2,3,4,5,6,8,9,0,1,2,3,4,5,6])
    a2 = np.array([1,2,3,4,5,6,8,9,0,1,2,3,4,5,6])
    a3 = np.array([1,2,3,4,5,6,8,9,0,1,2,3,4,5,6])
    print search_continue(a1,3,5,mode='LargerThan')
    print search_drop(a3,1)
    '''
    m1 = dmask('d1',{'oper':'Shift','scalar':2})
    operlist = [
        {'oper':'shift','scalar':2},
        {'oper':'flipsign'},
        {'oper':'cutstart','scalar':2},
        {'oper':'cutend','scalar':2}
        
        
    ]
    
    a1 = m1.operlist(a1,operlist)
    print a1
    print 1
    '''
    
    
        
        
        
        