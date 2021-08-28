
class modelo_negocio:
    def __init__(self,nom,ced,ape,dir,sal):
        self.nombre=nom
        self.cedula=ced
        self.apellido=ape
        self.direccion=dir
        self.salario=sal
    def empresa(self):
        print("empresa:¨{}ruc:{}".format(self.nombre,self.direccion))

    def empleador(self):
        print(self.nombre,self.cedula,self.direccion)

class empleadoEmpresa(modelo_negocio):
    def __init__(self,contrato,nom,ced):
        super().__init__(self,nom,dir,ced,contrato)
        self.__contrato=contrato

    @property
    def contrato(self):
        return self.__contrato
    @contrato.setter
    def contrato(self,value):
        if value:
            self.__contrato = value
        else:
            self.__contrato= 'sin contrato'
        self.__contrato=value
    
    def mostarmodelo_negocio(self):
        print(self.nombre)


#empleadoEmpresa=empleadoEmpresa("comisariato",1102125624,"9 de octubre")
#empleadoEmpresa.mostra()

class nomina:

    def __init__(self,codigo,hrDiurnas,hrNocturnas):
        self.codigo=codigo
        self.hrDiurnas=hrDiurnas
        self.hrNocturnas=hrNocturnas

    def getcodigo(self):
        return self.codigo
    def getHrDiurnas(self):
        return self.hrDiurnas
    def getHrNocturnas(self):
        return self.hrNocturnas
    

    def getTOTAL(self):
        total= self.getHrDiurnas()*500 + self.getHrNocturnas()* 500 *0.90
        total= total-(total* 00.7)
        return total

    def mostarNomina(self):
        print("codigo de empleado:"+self.getcodigo()+"salario mensual: "+str(self.getTOTAL()))
        

    codigo= input("ingrese codigo de empleado:")
    hrDiurnas=input("ingrese cantidad de horas diurnas:")
    hrNocturnas=input("ingrese cantidad la hora nocturna:")

    #e=nomina(codigo,hrDiurnas,hrNocturnas)
    #e.mostraNomina
