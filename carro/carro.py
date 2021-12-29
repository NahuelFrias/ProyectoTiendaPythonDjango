class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get("carro") # identifica el string con el carro

        if not carro: # si no hay carro, lo creamos
            carro = self.session["carro"]={}
        # si hay
        self.carro = carro

    # agregar productos al carro
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()): # si el producto no esta en el carro
            self.carro[producto.id]={ # lo agregamos con las siguientes caracteristicas
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else: # si ya esta, agregamos mas productos
            for key, value in self.carro.items(): # por cada llave valor en el carro
                if key == str(producto.id): # comparamos las llaves con los id de los productos en el carro
                    value["cantidad"]=value["cantidad"]+1 # sumo un articulo mas
                    value["precio"]=float(value["precio"])+producto.precio # sumo los precios
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro # el carro tiene que ser igual al carro de la session
        self.session.modified=True # se modifica la sesion desp de agregar o restar

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro: # si el producto se encuentra en el carro
            del self.carro[producto.id] # lo elimino
            self.guardar_carro() # y guardo session

    def restar_producto(self,producto):
        for key, value in self.carro.items(): # por cada llave valor en el carro
                if key == str(producto.id): # comparamos las llaves con los id de los productos en el carro
                    value["cantidad"]=value["cantidad"]-1 # resto un articulo
                    value["precio"]=float(value["precio"])-producto.precio # resto precios
                    if value["cantidad"]<1: # si solo queda un producto, llamo a eliminar
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True # como modifico la sesion ratifico que ha sido modificado