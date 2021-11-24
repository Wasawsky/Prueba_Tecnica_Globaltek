#PRUEBA TECNICA GLOBALTEK
#MICHAEL BALLESTEROS
#24-11-2021
from sys import stdin

def search(matrix,matchP):
    """ Funcion de busqueda en los datos provistos
        recibe la matriz en la que va a buscar y la propiedad a buscar.
        Si no hay datos que coincidan, el resultado es un arreglo vacio.
            -> Arreglo con los resultados de la busqueda
    """
    result=[] 
    for obj in matrix:
        for props in obj:
            if props[0]==matchP[0] and props[1]==matchP[1]:
                result.append(obj)
    return result

def main():
    """ Funcion principal, encargada de formatear tanto la entrada como la salida
            -> Arreglo con el resultado formateado
    """
    array=[x.strip("{}[], ").split(", ") for x in stdin.readline().strip().split("}")]
    array.pop(-1)
    matrix=[]
    for obj in array:
        temp=[]
        for props in obj:
            temp.append(props.split(": "))
        matrix.append(temp)
        
    matchProp=[x.strip("{} ") for x in stdin.readline().strip().split(":")]
    
    result=search(matrix,matchProp)
    resultFormatted=[]
    for obj in result:
        formatted=""
        for prop in obj:
            objDesc = ": ".join(prop)
            formatted+=objDesc+", "
        formatted="{"+formatted[:-2]+"}"
        resultFormatted.append(formatted)
        
    print(resultFormatted)
    
main()
