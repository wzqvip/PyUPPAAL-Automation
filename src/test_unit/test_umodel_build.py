"""尝试构建与解析constructed_model, test_umodel_build.xml

Returns:
    None
"""
import os
import pyuppaal

from pyuppaal.nta import Template, Location, Edge

pyuppaal.DeveloperTools.set_verifyta_path_dev()


def bring_to_root(file_name: str):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ROOT_DIR, file_name)


def test_load_model():
    model_path = bring_to_root('test_umodel_build.xml')
    umodel = pyuppaal.UModel(model_path)

    assert "sender = Sender(a, b);" in umodel.system
    assert "int count = 0;" in umodel.declaration
    # 判断queries是否正确
    assert "E<> sender_count == 10" == umodel.queries[0]
    assert "A[] not deadlock" == umodel.queries[-1]

    # 判断template是否正确
    assert len(umodel.templates) == 2

    # 通过测试能否验证某个语句来判断构建的模型的语法正确性。
    assert "Verifying formula" in umodel.verify()
    # print(umodel.verify())
    # Options for the verification:
    # Generating no trace
    # Search order is breadth first
    # Using conservative space optimisation
    # Seed is 1688188053
    # State space representation uses minimal constraint systems

    # Verifying formula 1 at /nta/queries/query[1]/formula
    # -- Formula is NOT satisfied.

    # Verifying formula 2 at /nta/queries/query[2]/formula
    # -- Formula is satisfied.

    # Verifying formula 3 at /nta/queries/query[3]/formula
    # -- Formula is satisfied.

    # Verifying formula 4 at /nta/queries/query[4]/formula
    # -- Formula is satisfied.

    # Verifying formula 5 at /nta/queries/query[5]/formula
    # -- Formula is NOT satisfied.


def test_construct_model():
    model_path = bring_to_root('constructed_model.xml')
    os.remove(model_path)
    umodel = pyuppaal.UModel.new(model_path)

    umodel.declaration = """// Place global declarations here.
broadcast chan a, b, c;
int count = 0;
int sender_count = 0;
const int rec_end = 10;\n"""

# region: 构建tempaltes，一共两个
    # region: 构建第1个template
    template0 = Template(name="Receiver",
                         locations=[],
                         init_ref=0,
                         edges=[],
                         params="broadcast chan &param1, broadcast chan &param2, int inv_start, int guard_start",
                         declaration="""// Place local declarations here.\nclock t;""")
    # 构造locations
    # l0 是initial location
    l0 = Location(location_id=0, location_pos=(-391, -102),
                  name="Start", name_pos=(-401, -136),
                  invariant="t<=inv_start", invariant_pos=(-401, -85),
                  test_code_on_enter="count ++;", test_code_on_exit="count = 10;",
                  is_initial=True)
    l1 = Location(location_id=1, location_pos=(-170, -102),
                  invariant="t<=200", invariant_pos=(-178, -76),
                  rate_of_exponential=0.8, rate_of_exp_pos=(-179, -93))
    l2 = Location(location_id=2, location_pos=(-42, -93), is_urgent=True)
    l3 = Location(location_id=3, location_pos=(-76, -212), is_committed=True)
    l4 = Location(location_id=4, location_pos=(25, -212),
                  name="End1", name_pos=(15, -246))
    l5 = Location(location_id=5, location_pos=(51, -93),
                  name="End2", name_pos=(41, -127),
                  comments="备注End2", comments_pos=(42, -34))

    # 构造branch points
    bp0 = Location(location_id=6, location_pos=(-119, -144),
                   is_branchpoint=True)

    template0.locations = [l0, l1, l2, l3, l4, l5, bp0]

    # 构造edges
    e0 = Edge(source_location_id=2, source_location_pos=(-42, -93),
              target_location_id=5, target_location_pos=(34, -93),
              sync="param2?", sync_pos=(-24, -110),
              update="t=888", update_pos=(-24, -93))
    e1 = Edge(source_location_id=3, source_location_pos=(-76, -212),
              target_location_id=4, target_location_pos=(25, -212),
              sync="param1?", sync_pos=(-58, -229),
              update="t=999", update_pos=(-51, -212))
    e2 = Edge(source_location_id=6, source_location_pos=(-119, -144),
              target_location_id=3, target_location_pos=(-76, -212),
              probability_weight=0.2, prob_weight_pos=(-93, -178))
    e3 = Edge(source_location_id=6, source_location_pos=(-119, -144),
              target_location_id=2, target_location_pos=(-42, -93),
              probability_weight=0.8, prob_weight_pos=(-93, -119))
    e4 = Edge(source_location_id=1, source_location_pos=(-178, -102),
              target_location_id=6, target_location_pos=(-119, -144))
    e5 = Edge(source_location_id=0, source_location_pos=(-391, -102),
              target_location_id=1, target_location_pos=(-178, -102),
              guard="t>= guard_start", guard_pos=(-331, -102),
              update="count ++", update_pos=(-306, -85),
              test_code="count == -1;")
    template0.edges = [e0, e1, e2, e3, e4, e5]
    # template0.branch_points = [bp0]
    # endregion

    # region: 构建第2个template
    template1 = Template(name="Sender",
                         locations=[],
                         init_ref=7,
                         edges=[],
                         params="broadcast chan &param1, broadcast chan &param2",
                         declaration=None)

    # 构造locations
    l7 = Location(location_id=7, location_pos=(-459, -34),
                  name="Start", name_pos=(-493, -68),
                  test_code_on_enter="sender_count = 10;",
                  test_code_on_exit="sender_count = -1;",
                  comments="""Start:\nTestCode""", comments_pos=(-469, 25),
                  is_initial=True)
    l8 = Location(location_id=8, location_pos=(-187, -102))
    l9 = Location(location_id=9, location_pos=(-178, 17))
    # l10 = Location(location_id=10,location_pos=(-323,-34))

    # 构造branch points
    bp1 = Location(location_id=10, location_pos=(-323, -34),
                   is_branchpoint=True)

    template1.locations = [l7, l8, l9, bp1]

    # 构造edges
    e6 = Edge(source_location_id=10, source_location_pos=(-323, -34),
              target_location_id=9, target_location_pos=(-178, 17),
              sync="param2!", sync_pos=(-305, -34))
    e7 = Edge(source_location_id=10, source_location_pos=(-323, -34),
              target_location_id=8, target_location_pos=(-187, -102),
              sync="param1!", sync_pos=(-305, -80),
              probability_weight=0.8, prob_weight_pos=(-305, -51))
    e8 = Edge(source_location_id=7, source_location_pos=(-459, -34),
              target_location_id=10, target_location_pos=(-323, -34),
              nails=[(-382, -136)])
    template1.edges = [e6, e7, e8]
    # print(template1.edges)

    # template1.branch_points = [bp1]
    # endregion
# endregion 构造templates

    umodel.templates = [template0, template1]
    umodel.system = """// Place template instantiations here.
rec = Receiver(a, b, 10, rec_end);
sender = Sender(a, b);
// List one or more processes to be composed into a system.
system rec, sender;\n"""
    umodel.queries = ["E<> sender_count == 10",
                      "E<> count == 1",
                      "E<> rec.End1",
                      "E<> rec.t >= 10",
                      "A[] not deadlock"]

    assert "E<> sender_count == 10" == umodel.queries[0]

    target_model = pyuppaal.UModel(bring_to_root("test_umodel_build.xml"))
    assert umodel.queries == target_model.queries
    assert umodel.system == target_model.system
    assert umodel.declaration == target_model.declaration
    assert umodel.templates[0].xml == target_model.templates[0].xml
    assert umodel.templates[1].xml == target_model.templates[1].xml
    assert umodel.xml == target_model.xml
    assert "Verifying formula" in umodel.verify()
    # print(umodel.verify())


if __name__ == '__main__':
    test_construct_model()
