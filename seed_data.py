from AppAscenzi.models import Mayorista, Minorista, Pedido

Mayorista(nombre = "WorldTech",
          cuil = "5468352445",
          telefono = "03416253251",
          email = "info@worldtech.com",
          direccion = "Lavalle 925",
          codigo_postal = "2000",
        ).save()

Minorista(nombre = "WorldTech",
          apellido = "Palmero",
          dni = "37561345",
          telefono = "03416253251",
          email = "info@worldtech.com",
          direccion = "Lavalle 925",
          codigo_postal = "2000",
        ).save()

Pedido(precio = "5468352445",
          marca = "Matias",
          medio_de_pago = "Efvo",
          nombre_comprador = "Luis Miguel",
          cantidad = "37",
          quien_retira = "Marcos Alonso",
        ).save()