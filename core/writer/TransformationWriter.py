from core.stm.AvailableAction import AvailableAction
import jinja2


class TransformationWriter:

    def __init__(self, available_action: AvailableAction) -> None:
        
        self._available_action = available_action

        templateLoader = jinja2.FileSystemLoader(searchpath = "./core/writer/transformation_templates")
        self.__template_env = jinja2.Environment(loader = templateLoader)

        self.__filename = "stm/ministm.xml"

    def filename(self):
        return self.__filename

    def clear(self):
        open(self.__filename, 'w').close()

    def write(self):

        # clear file
        self.clear()

        if self._available_action.action().transformation_type() == "entity":

            if self._available_action.action().action_type() == "create":

                self._write_in_template("create_entity_action.stub")

    def _write_in_template(self, template_file):
        
        template = self.__template_env.get_template(template_file)
        render = template.render(action = self._available_action.action())

        with open(self.__filename, "a") as f:
            f.write(render)
