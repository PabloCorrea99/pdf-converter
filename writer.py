#!/usr/bin/env python
# -*- coding: latin-1 -*-
import json

def create_json_file(data, ouput_filename):
    items = []
    for section in data:
        f = open(f'{ouput_filename}/{section["file"]}', 'r', encoding="latin-1")
        lines = f.readlines()
        body = '\t'.join([line.strip() for line in lines])
        # Data to be written
        item = {
            "title": {
            "type": section["type"],
            "value": section["value"]
            },
            "content": {
            "type": "text",
            "value": body
            }
        }
        items.append(item)


    json_object = json.dumps(items, indent=4, ensure_ascii=False)
    
    # Writing to sample.json
    with open(f"{ouput_filename}.json", "w", encoding="latin-1") as outfile:
        outfile.write(json_object)


dataPrivacidad=[
    {"type": "main-title", "value": "AUTORIZACIÓN PARA EL TRATAMIENTO DE DATOS PERSONALES", "file": "AUTORIZACION.txt"},
    {"type": "sub-title", "value": "AVISO DE PRIVACIDAD", "file": "AVISO.txt"},
    {"type": "sub-title", "value": "POLÍTICA DE PRIVACIDAD", "file": "POLITICA.txt"},
    {"type": "sub-title", "value": "1. Objetivo y Alcance", "file": "OBJETIVOYALCANCE.txt"},
    {"type": "sub-title", "value": "2. Aplicabilidad", "file": "APLICABILIDAD.txt"},
    {"type": "sub-title", "value": "3. Principios", "file": "PRINCIPIOS.txt"},
    {"type": "sub-title", "value": "4. Políticas, Procedimientos y Otros Documentos Relacionados.", "file": "PROCEDIMIENTOS.txt"},
    {"type": "sub-title", "value": "5. Definiciones", "file": "DEFINICIONES.txt"},
    {"type": "sub-title", "value": "6. Antecedentes", "file": "ANTECEDENTES.txt"},
    {"type": "sub-title", "value": "7. Responsabilidades", "file": "RESPONSABILIDADES.txt"},
    {"type": "sub-title", "value": "8. Requisitos", "file": "REQUISITOS.txt"},
    {"type": "sub-title", "value": "9. Finalidades del Tratamiento de la Información", "file": "FINALIDADES.txt"},
    {"type": "sub-title", "value": "10. Transferencias Transfronterizas", "file": "TRANSFERENCIA.txt"},
    {"type": "sub-title", "value": "11. Derechos de los Titulares de la Información", "file": "DERECHOS.txt"},
    {"type": "sub-title", "value": "12. Procedimiento para el ejercicio de los derechos", "file": "PROCEDIMIENTOEJERCICIO.txt"},
    {"type": "sub-title", "value": "13. Actualizaciones de esta política de privacidad", "file": "ACTUALIZACION.txt"},
    {"type": "sub-title", "value": "14. Aviso General de Privacidad", "file": "AVISOGENERAL.txt"},
]
#create_json_file(dataPrivacidad, "politica-privacidad")

dataCondiciones=[
    {"type": "main-title", "value": "TÉRMINOS Y CONDICIONES DE USO", "file": "TERMINOS.txt"},
    {"type": "sub-title", "value": "Capacidad para el uso de la plataforma", "file": "CAPACIDAD.txt"},
    {"type": "sub-title", "value": "Proceso de registro y uso de cuenta", "file": "REGISTRO.txt"},
    {"type": "sub-title", "value": "Proceso de compra", "file": "COMPRA.txt"},
    {"type": "sub-title", "value": "Información de pagos", "file": "PAGOS.txt"},
    {"type": "sub-title", "value": "Envío y entrega", "file": "ENVIO.txt"},
    {"type": "sub-title", "value": "Precio", "file": "PRECIO.txt"},
    {"type": "sub-title", "value": "Origen de ingresos", "file": "INGRESOS.txt"},
    {"type": "sub-title", "value": "Protección de Datos Personales", "file": "PROTECCION.txt"},
    {"type": "sub-title", "value": "Propiedad Intelectual", "file": "INTELECTUAL.txt"},
    {"type": "sub-title", "value": "Ley y Jurisdicción aplicable", "file": "LEY.txt"},
    {"type": "sub-title", "value": "Invalidez", "file": "INVALIDEZ.txt"}
]
create_json_file(dataCondiciones, "terminos-condiciones")