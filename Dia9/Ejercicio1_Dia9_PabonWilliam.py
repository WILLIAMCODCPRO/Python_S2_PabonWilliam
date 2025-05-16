# #####################
# # #### Dia 9 ########
# #####################

from funciones import*

def registrarArtista():
    artista = {}

    artista["nombreArtista"] = input("Nombre del artista: ")
    artista["paisOrigenNombre"] = input("País de origen (nombre): ")
    artista["paisOrigenIso3"] = input("Código ISO3: ")
    artista["anosActividad"] = int(input("Años de actividad: "))
    artista["anoPrimerDiscoListas"] = int(input("Año del primer disco en listas: "))
    artista["generoMusical"] = input("Género musical: ")
    artista["unidadesCertificadasTotales"] = int(input("Unidades certificadas totales: "))
    artista["ventasReclamadas"] = int(input("Ventas reclamadas: "))
    estado = input("¿Está activo? (s/n): ").lower()
    artista["estaActivo"] = True if estado == 's' else False

    return artista


listaArtistas = []


nuevoArtista = registrarArtista()
listaArtistas.append(nuevoArtista)













# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412