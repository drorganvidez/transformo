import jinja2
from datetime import datetime

class Generator:

    def __init__(self, stm) -> None:
        
        self.__stm = stm
        self.__sdm = self.__stm.sdm()
        self.__filename = "scripts/example.sql"
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
            database_name = "example", 
            today = today)

        self.write(output_from_parsed_template)
        self.write_empty_line()

    def generate_entity(self, entity):

        template = self.__template_env.get_template("entity.stub")

        output_from_parsed_template = template.render(
            database_name = "example", 
            entity_id = entity.id(),
            attributes = entity.attributes())

        self.write(output_from_parsed_template)
        self.write_empty_line()