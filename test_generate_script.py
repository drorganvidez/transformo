from jinja2 import Template

def test_generate():

    temp1 = "Hola {{nombre}}"
    print(Template(temp1).render(nombre="Pepe"))

test_generate()