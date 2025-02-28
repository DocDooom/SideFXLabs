import os
import hou

local_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    try:
        hou.hipFile.load(os.path.join(local_dir, "PDG_UnitTest.hip").replace("\\", "/"))

        _topnode = hou.node("/obj/topnet1/concatenate_text1")

        print ("starting pdg")
        _topnode.dirtyAllTasks(False)
        _topnode.executeGraph(False, True, False, False)
        print("done with pdg")

        if os.path.isfile(os.path.join(local_dir, "REGTEST-LOG.txt").replace("\\", "/")):
            with open(os.path.join(local_dir, "REGTEST-LOG.txt").replace("\\", "/")) as file:
                lines = file.readlines()

                for line in lines:
                    print (line)
        else:
            print ("ERROR, SOMETHING FAILED IN PDG.. NO LOG GENERATED")

    except Exception as e:
        print (str(e))
        pass