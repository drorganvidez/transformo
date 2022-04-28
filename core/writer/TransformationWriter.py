from core.stm.AvailableAction import AvailableAction
import jinja2


class TransformationWriter:

    def __init__(self, available_action: AvailableAction = None, first_write: bool = None, close : bool = False) -> None:
        
        self._available_action = available_action

        templateLoader = jinja2.FileSystemLoader(searchpath = "./core/writer/transformation_templates")
        self.__template_env = jinja2.Environment(loader = templateLoader)

        self.__filename = "stm/ministm.xml"
        self.__filename_all_transformation = "stm/all.xml"

        self.__first_write = first_write

    def filename(self):
        return self.__filename

    def clear(self, filename):
        open(filename, 'w').close()

    def write_empty_line(self, filename):
        with open(filename, "a") as f:
            f.write("\n")

    def write(self):

        # clear file
        self.clear(self.__filename)

        if(self.__first_write):
            self.clear(self.__filename_all_transformation)

        # write transformation of type ENTITY
        if self._available_action.action().transformation_type() == "entity":

            if self._available_action.action().action_type() == "create":

                self._write_in_template("create_entity_action.stub")

            if self._available_action.action().action_type() == "rename":

                self._write_in_template("rename_entity_action.stub")

            if self._available_action.action().action_type() == "delete":

                self._write_in_template("delete_entity_action.stub")

        # write transformation of type ATTRIBUTE
        if self._available_action.action().transformation_type() == "attribute":

            if self._available_action.action().action_type() == "create":

                self._write_in_template("create_attribute_action.stub")

            if self._available_action.action().action_type() == "rename":

                self._write_in_template("rename_attribute_action.stub")

            if self._available_action.action().action_type() == "retype":

                self._write_in_template("retype_attribute_action.stub")

            if self._available_action.action().action_type() == "move":

                self._write_in_template("move_attribute_action.stub")


    def close(self):
        template = self.__template_env.get_template("g_end.stub")
        render = template.render()

        with open(self.__filename_all_transformation, "a") as f:
            f.write(render)

        self.write_empty_line(self.__filename_all_transformation)


    def _write_in_template(self, template_file):
        
        # write unique transformation in file
        template = self.__template_env.get_template(template_file)
        render = template.render(action = self._available_action.action())

        with open(self.__filename, "a") as f:
            f.write(render)

        self.write_empty_line(self.__filename)

        # write with the rest of transformation

        # write the start
        if self.__first_write:
            template = self.__template_env.get_template("g_start.stub")
            render = template.render(action = self._available_action.action())

            with open(self.__filename_all_transformation, "a") as f:
                f.write(render)

        # write the transformation in the rest of all transformations
        template = self.__template_env.get_template("g_" + template_file)
        render = template.render(action = self._available_action.action())

        with open(self.__filename_all_transformation, "a") as f:
            f.write(render)

        self.write_empty_line(self.__filename_all_transformation)

