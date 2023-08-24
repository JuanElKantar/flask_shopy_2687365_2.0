from app import app

if __name__ =="__main__":
    app.run() 


    #la clase debe ir con mayuscula

    #EN CASO DE TENER ERROR BORRAR EL ARCHIVO CON ESE POCO DE NUMEROS DE "versions" o si no borrar y crear la bd
    #model en mvc-> es una clase en la que se puede instanciar objetos, viene con atributos/metodos especificos para la CRUD
    #ORM OBJECT RELATIONAL MAPPER (especie de traductor) permite construir objetos para los registros

    #entrar a la consola python en vs:

    #python
    #from app(en este caso nombre del archivo) import "nombre" <- para acceder a un elemento, clase.
    #exit()  <-para salir
    # >>> c = Cliente(username = 'Juan A', email = 'jj@misena.edu.co', password = "123") EJEMPLO DE CREAR OBJETOS E INGRESAR ATRIBUTOS
    #db.session.add(c) para selecionar lo que esta en el objeto 
    #db.session.commit()   para actualizra en la base de datos 

    #clientes = Cliente.query.all() para hacer una consulta de los datos que estan en la tabla 
    #> xd = Cliente.query.get(3) para llamar uno especifio
    #para saber un campo de objeto xd.nombre_campo
    #db.session.delete(xd)  para eliminar objeto de la db 






