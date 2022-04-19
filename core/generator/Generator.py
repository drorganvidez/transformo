import jinja2
from datetime import datetime

class Generator:

    def __init__(self, stm) -> None:
        
        self.__stm = stm
        self.__sdm = self.__stm.sdm()
        self.__filename = "scripts/example.sql"
        self.__database_name = "example"
        templateLoader = jinja2.FileSystemLoader(searchpath = "./core/generator")
        self.__template_env = jinja2.Environment(loader = templateLoader)

    def generate(self):

        # clear file
        self.clear()

        # generate base sql
        self.generate_base()
        
        # generate tables
        for e in self.__sdm.entities():
            self.generate_entity(e)

        # generate transformations
        for t in self.__stm.transformations():
            self.generate_transformation(t)


    def clear(self):
        open(self.__filename, 'w').close()

    def write_empty_line(self):
        with open(self.__filename, "a") as f:
            f.write("\n")

    def write(self, template):
        with open(self.__filename, "a") as f:
            f.write(template)
        self.write_empty_line()

    def generate_base(self):

        template = self.__template_env.get_template("base_sql_script.stub")

        today = datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')

        output_from_parsed_template = template.render(
            database_name = self.__database_name, 
            today = today)

        self.write(output_from_parsed_template)
        self.write_empty_line()

    def generate_entity(self, entity):

        template = self.__template_env.get_template("entity.stub")

        output_from_parsed_template = template.render(
            database_name = self.__database_name, 
            entity = entity)

        self.write(output_from_parsed_template)
        self.write_empty_line()

    def generate_transformation(self, transformation):

        if transformation.type() == "attribute":

            for a in transformation.actions():

                if a.type() == "retype":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file="retype_attribute_action.stub")

    def write_transformation(self, transformation, action, template_file):
        template = self.__template_env.get_template(template_file)
        render = template.render(
            transformation_name = transformation.id(), 
            database_name = self.__database_name, 
            action = action.apply())
        self.write(render)

