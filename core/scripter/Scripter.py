from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
import jinja2
from datetime import datetime
from copy import copy

class Scripter:

    def __init__(self, stm, output_database = None) -> None:
        
        self.__today = datetime.today()

        self.__stm = stm
        self.__sdm = stm.sdm()
        
        self.__database_name_from = "base1"
        templateLoader = jinja2.FileSystemLoader(searchpath = "./core/scripter")
        self.__template_env = jinja2.Environment(loader = templateLoader)

        #output database
        if output_database is not None:
            self.__filename = "scripts/" + output_database + ".sql"
            self.__database_name_to = output_database
        else :
            name = self.__database_name_from + "_transformed_" +self.__today.strftime('%Y_%m_%d_%Y_%H_%M_%S')
            self.__filename = "scripts/" + name + ".sql"
            self.__database_name_to = name

    def sdm(self):
        return self.__stm.sdm()


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

        today = self.__today.strftime('%A, %B %d, %Y %H:%M:%S')

        output_from_parsed_template = template.render(
            database_name_to = self.__database_name_to, 
            today = today)

        self.write(output_from_parsed_template)
        self.write_empty_line()

    def generate_entity(self, entity):

        template = self.__template_env.get_template("entity.stub")

        output_from_parsed_template = template.render(
            database_name_to = self.__database_name_to, 
            database_name_from = self.__database_name_from, 
            entity = entity)

        self.write(output_from_parsed_template)
        self.write_empty_line()

    def generate_transformation(self, transformation):

        if transformation.type() == "entity":

            for a in transformation.actions():

                if a.type() == "create":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "create_entity_action.stub")

                if a.type() == "rename":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "rename_entity_action.stub")

                if a.type() == "delete":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "delete_entity_action.stub")

        if transformation.type() == "attribute":

            for a in transformation.actions():

                if a.type() == "create":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "create_attribute_action.stub")

                if a.type() == "retype":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "retype_attribute_action.stub")

                if a.type() == "move":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "move_attribute_action.stub")

                if a.type() == "rename":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "rename_attribute_action.stub")

                if a.type() == "delete":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "delete_attribute_action.stub")

        if transformation.type() == "relation":

            for a in transformation.actions():

                if a.type() == "create":

                    self.write_transformation(
                        transformation = transformation,
                        action = a,
                        template_file = "create_relation_action.stub")
                        

    def write_transformation(self, transformation, action, template_file):
        template = self.__template_env.get_template(template_file)
        render = template.render(
            transformation_name = transformation.id(), 
            database_name_from = self.__database_name_from,
            database_name_to = self.__database_name_to,
            action = action.apply())
        self.write(render)
        self.write_empty_line()

