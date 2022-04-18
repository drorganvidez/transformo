import jinja2

class Generator:

    def __init__(self, sdm_base) -> None:
        self.__sdm_base = sdm_base
        pass

    def generate(self):

        print("##### GENERATE #####")
        templateLoader = jinja2.FileSystemLoader(searchpath = "./core/generator")
        templateEnv = jinja2.Environment(loader = templateLoader)

        # generate base sql
        TEMPLATE_FILE = "base_sql_script.stub"
        template = templateEnv.get_template(TEMPLATE_FILE)
        output_from_parsed_template = template.render(database_name = "base_sql")

        with open("script/example.sql", "w") as f:
            f.write(output_from_parsed_template)

        # generate tables
        for e in self.__sdm_base.entities():
            print(e)

        print(output_from_parsed_template)