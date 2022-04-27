from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableAction import AvailableAction
from core.stm.AvailableActionsExtractor import AvailableActionsExtractor
from core.stm.SimpleTransformationModel import SimpleTransformationModel
from core.writer.TransformationWriter import TransformationWriter


class Migration:

    def __init__(self, sdm_source : SimpleDatabaseModel, sdm_target: SimpleDatabaseModel) -> None:

        self._A = sdm_source
        self._B = sdm_target

        self._extractor = AvailableActionsExtractor(sdm_source = self._A, sdm_target = self._B)

        self._selected_actions : list[AvailableAction] = list()

    def migrate(self):

        self._extractor.print()

        print("")

        inputed = str(input("Select an available action ('q' for quit): "))

        if inputed == "q":
            return self.finish()

        option = int(inputed)

        # selection of action from available actions in current SDM
        selected_action = self._extractor.available_actions()[option]
        self._selected_actions.append(selected_action)
        print("Selected action: ")
        print()
        print(selected_action)

        # write transformation in file of type STM
        stm_file = self.write_transformation(selected_action)
        stm = SimpleTransformationModel(sdm = self._A, file = stm_file)
        new_sdm = stm.sdm()
        self.extractor = AvailableActionsExtractor(sdm_source = new_sdm, sdm_target = self._B)
        #stm.sdm().print()
        self.extractor.B().print()

        return self.migrate()

        '''
        try:
            

        except:
            return self.migrate()
        '''

    def finish(self):
        print("finished")

    def write_transformation(self, action):
        transformation_writer = TransformationWriter(action)
        transformation_writer.write()
        return transformation_writer.filename()