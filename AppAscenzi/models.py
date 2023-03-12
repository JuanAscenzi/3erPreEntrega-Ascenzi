from django.db import models

class Mayorista(models.Model):
    nombre = models.CharField(max_length=30)
    cuil= models.CharField(max_length=10)
    telefono= models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    codigo_postal=models.CharField(max_length=4)

    def str(self):
        return f"""Datos del cliente mayorista: 
    Nombre del comprador: {self.nombre}
    CUIL: {self.cuil}                           
    Numero de telefono: {self.telefono}
    Correo electronico: {self.email}
    Direccion domicilio: {self.direccion}
    Codigo postal: {self.codigo_postal}
    """

class Minorista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    telefono= models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    codigo_postal=models.CharField(max_length=4)

    def str(self):
        return f"""Datos del cliente minorista: 
    Nombre del comprador: {self.nombre}
    Apellido del comprador: {self.apellido} 
    DNI: {self.dni}
    Numero de telefono: {self.telefono}
    Correo electronico: {self.email}
    Direccion domicilio: {self.direccion}
    Codigo postal: {self.codigo_postal}
    """

class Pedido(models.Model):
    precio= models.CharField(max_length=6) #digitos
    marca= models.CharField(max_length=20) #hasbro/mattel/fisherprice
    medio_de_pago=models.CharField(max_length=35) #efvo/tarjeta
    nombre_comprador=models.CharField(max_length=50) #si es una empresa o un minorista
    cantidad=models.CharField(max_length=5) #digitos
    quien_retira=models.CharField(max_length=50)

    def str(self):
        return f"""Datos del pedido: 
    Precio del producto: {self.precio} 
    Marca del producto{self.marca}
    Medio de pago: {self.medio_de_pago}
    Nombre del comprador/empresa responsable: {self.nombre_comprador}
    Cantidad: {self.cantidad}
    Nombre de quien retira: {self.quien_retira}
    """

#class Busqueda(models.Model):
#    nombre = models.CharField(max_length=30)
#    apellido = models.CharField(max_length=30)
#    dni = models.CharField(max_length=10)
#    telefono= models.CharField(max_length=15)
#    email = models.CharField(max_length=30)
#    direccion= models.CharField(max_length=50)


#    def str(self):
#       return f"""Datos de la busqueda: 
#    {self.nombre}
#    {self.apellido} 
#    {self.dni}
#    {self.telefono}
#    {self.email}
#    {self.direccion}
#    """
    