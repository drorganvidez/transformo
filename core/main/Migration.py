import copy
from core.heuristic.Heuristic import Heuristic
from core.scripter.Scripter import Scripter
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableAction import AvailableAction
from core.stm.AvailableActionsExtractor import AvailableActionsExtractor
from core.stm.SimpleTransformationModel import SimpleTransformationModel
from core.writer.TransformationWriter import TransformationWriter


class Migration:

    def __init__(self, sdm_source : SimpleDatabaseModel, sdm_target: SimpleDatabaseModel, output_database_name = "output_database") -> None:

        self._A = sdm_source
        self._B = sdm_target
        self._originalA = SimpleDatabaseModel(sdm_source.file())

        self._extractor = AvailableActionsExtractor(sdm_source = self._A, sdm_target = self._B)

        self._selected_actions : list[AvailableAction] = list()

        self.__first_writing_in_file = True

        self.__output_database = output_database_name

    def migrate(self):

        # show current source SDM
        self._extractor.A().print()

        # show available actions
        self._extractor.print()

        print("")

        inputed = str(input("Select an available action ('q' for quit): "))

        if inputed == "q":

            if self.__first_writing_in_file:
                return self.finish()

            self._close_transformations()
            self._generate_sql_script()
            return self.finish()

        option = int(inputed)

        # selection of action from available actions in current SDM
        selected_action = self._extractor.available_actions()[option]
        self._selected_actions.append(selected_action)
        print("Selected action: ")
        print()
        print(selected_action)

        # write transformation in file of type STM
        print(selected_action.action().transformation_type())
        stm_file = self.write_transformation(selected_action)
        stm = SimpleTransformationModel(sdm = self._A, file = stm_file)

        # new instance of Available Actions Extractor object
        self._extractor = AvailableActionsExtractor(sdm_source = stm.sdm(), sdm_target = self._B)
        

        return self.migrate()

        '''
        try:
            

        except:
            return self.migrate()
        '''

    def heuristic_migrate(self):

        # heuristic dictionary
        d = dict()
    
        heuristic_object = Heuristic(sdm_source = self._A, sdm_target = self._B)
        heuristic_number = heuristic_object.calculate()
        print()
        print("######################")
        print("Current heuristic: " + str(heuristic_number))
        print("######################")
        print()

        if heuristic_number == 0:

            print("Found a solution!")

            self._close_transformations()
            self._generate_sql_script()
            return self.finish()

        for available_action in self._extractor.available_actions():

            stm_file = self.write_single_transformation(available_action)
            stm = SimpleTransformationModel(sdm = copy.deepcopy(self._A), file = stm_file)

            transformed_sdm_A = stm.sdm()
            heuristic_object = Heuristic(sdm_source = transformed_sdm_A, sdm_target = self._B)
            heuristic_number = heuristic_object.calculate()

            d[available_action] = heuristic_number

        for available_action, heuristic in d.items():
            print(available_action)
            print("h = "+ str(heuristic))
            print()

        # get the best available actions
        most_convenient_action = min(d, key = d.get)
        self._selected_actions.append(most_convenient_action)
        print("\t-> Most convenient action: \n")
        print("\t" + str(most_convenient_action))

        # execute the single transformation
        stm_file = self.write_transformation(most_convenient_action)
        stm = SimpleTransformationModel(sdm = self._A, file = stm_file)

        # new instance of Available Actions Extractor object
        self._extractor = AvailableActionsExtractor(sdm_source = stm.sdm(), sdm_target = self._B)

        return self.heuristic_migrate()


    def finish(self):

        print()
        print("SQL script generated successfully!")
        print("You can see the generated script in 'scripts/" + self.__output_database + ".sql'")
        print()
        print("\tThanks for using Transformo Framework")
        print("\tStay tuned for news in https://github.com/drorganvidez/transformo")
        print("\tDavid Romero Organvídez")
        print("\tTechnical Researcher")
        print("\tdrorganvidez@us.es")
        print("\tUniversity of Seville")
        print("\tGNU/GPLv3")
        print()

    def write_single_transformation(self, action):

        transformation_writer = TransformationWriter(available_action = action, single = True)
        transformation_writer.write_single()

        return transformation_writer.filename()

    def write_transformation(self, action):
        transformation_writer = TransformationWriter(available_action = action, first_write = self.__first_writing_in_file)
        transformation_writer.write()

        self.__first_writing_in_file = False

        return transformation_writer.filename()

    def _close_transformations(self):
        transformation_writer = TransformationWriter(close = True)
        transformation_writer.close()


    def _generate_sql_script(self):

        stm = SimpleTransformationModel(sdm = SimpleDatabaseModel(self._A.file()) , file = "stm/all.xml")
        scripter = Scripter(stm = stm, output_database = self.__output_database)
        scripter.generate()