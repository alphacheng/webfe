#!/usr/bin/env python
""" This is the module define the units and their operations """
import unittest
import pickle
from units import *


class unitsystem():
    """ define unit systems with basic unit specified
    """
    def __init__(self,system='SI'):
        self.unitlib = {}
        self.system = 'SI'
    
    def add(self,unitinst):
        ''' add derived units '''
        if isinstance(unitinst,unit):
            if unitinst.name not in self.unitlib.keys():
                self.unitlib[unitinst.name] = unitinst
            else:
                raise KeyError,('unit already exist',unitinst.name)
        else:
            raise TypeError,'input is not a unit instance'
        
    def get(self,key):
        try:
            return self.unitlib[key]
        except TypeError:
            raise TypeError, str(key) + 'do not exist'
                            
        
    def derive(self,name,coeff,dimstr,latex=None,const=0):

        # create derived units
        pa={}
        coef = float(coeff)
        
        for para in dimstr.split(','):
            [units,power] = para.split(':')
            
            # check if the used derived unit exist in system
            if units in self.unitlib.keys():
                od = self.unitlib[units]
                basis = set(pa.keys()) | set(od.dimensions.keys())
                for d in basis:
                    pa[d] = pa.get(d,0) + (
                            od.dimensions.get(d,0) * float(power))
                            
                coef = coef * (od.coef ** float(power))
            else:
                print "unit'" + units + "'do not exist, create it first"
                raise KeyError        
        
        sd = unit(coef, pa,name=name,latex=latex,const=const)
        self.add(sd)
            
    def convert(self,key1,key2):
        ''' Get conversion factor coeff that key1 * coeff = key2
        fshould be two units with same dimensions
        '''
        if isinstance(key1,unit) and isinstance(key2,unit):  # unit input
            uleft = key1
            uright = key2
        elif isinstance(key1,type('')) and isinstance(key2,type('')): # key input
            uleft = self.get(key1)
            uright = self.get(key2)            
        else:    
            raise TypeError,('Unit conversion need unit or unitlib keys')
            
        return uleft.conversion(uright)

    def multiply(self,key1,key2):
        ''' Get conversion factor coeff that key1 * coeff = key2
        fshould be two units with same dimensions
        '''
        if isinstance(key1,unit) and isinstance(key2,unit):  # unit input
            uleft = key1
            uright = key2
        elif isinstance(key1,type('')) and isinstance(key2,type('')): # key input
            uleft = self.get(key1)
            uright = self.get(key2)            
        else:    
            raise TypeError,('Unit conversion need unit or unitlib keys')
            
        return uleft * uright
       
    def search(self,other):
        ''' search unit with same dimdict'''
        potential = []
        for key in self.unitlib.keys():
            if self.unitlib[key].isequivalent(other):
                potential.append(key)
        return potential
            
            
def create_units():
    '''create SI unit system
    '''
    units = unitsystem()
    units.add(unit(1,{'L':1},name='m'))
    units.add(unit(1,{'T':1},name='s'))
    units.add(unit(1,{'M':1},name='kg'))
    units.derive('cm',0.01,'m:1')
    units.derive('mm',0.001,'m:1')
    units.derive('in.',25.4,'mm:1')
    units.derive('ft',12,'in.:1')
    units.derive('G',9.8,'m:1,s:-2')
    units.derive('N',1.0,'kg:1,G:1')
    units.derive('kN',1000.0,'N:1')
    units.derive('kip',4.448,'kN:1')
    units.derive('lbf',0.001,'kip:1')
    units.derive('Pa',1,'N:1,m:-2')
    units.derive('MPa',1e6,'Pa:1')
    units.derive('in^2',1,'in.:2')
    units.derive('m^2',1,'m:2')
    units.derive('N*mm',1,'N:1,mm:1',latex=r'${\rm{N}} \cdot {\rm{mm}}$')
    units.derive('kN*m',1,'kN:1,m:1',latex=r'${\rm{kN}} \cdot {\rm{m}}$')
    units.derive('kip*in',1,'kip:1,in.:1',latex=r'${\rm{kip}} \cdot {\rm{in}}$')
    units.derive('kN/m',1,'kN:1,m:-1')
    units.derive('in^(-1)',1,'in.:-1')
    units.derive('in^(-2)',1,'in.:-2')
    units.derive('m^(-1)',1,'m:-1')
    units.derive('mm^(-1)',1,'mm:-1')
    units.derive('kN/mm',1,'kN:1,mm:-1')
    units.derive('ksi',1,'kip:1,in.:-2')
    units.derive('ksi^0.5',1,'ksi:0.5',latex=r'$\sqrt{\rm{ksi}}$')
    units.derive('MPa^0.5',1,'MPa:0.5',latex=r'$\sqrt{{\rm{MPa}}}$')
    units.derive('in./in.',1,'m:0,s:0')
    units.derive('1/in.',1,'in.:-1')
    units.derive('1/m',1,'m:-1')
    units.derive('strain',1,'m:0')
    units.derive('ms',1e-6,'strain:0')
    units.derive('microstrain',1e-6,'strain:0')
    #f = open('unit.pydat','w')
    #pickle.dump(units,f)
    return units
    
# start unit test
class MyTest(unittest.TestCase):

    def setUp(self):
        ''' Create units used in the test
        '''
        self.units = unitsystem()
        self.units.add(unit(1,{'L':1},name='m'))
        self.units.derive('cm',0.01,'m:1')
        self.units.derive('mm',0.001,'m:1')
        
    def test_add_derive(self):
        pass

    
    def test_convert(self):
        self.assertEqual(self.units.convert('cm','m'),[0.01,0])
if __name__ == '__main__':
    create_units()
    unittest.main()
    
    