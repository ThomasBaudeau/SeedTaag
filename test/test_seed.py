
import SeedTaag.topology_results as topology
import SeedTaag.data_storage as storage
import SeedTaag.Taagseed as Seed

EXPECTED_RESULT_SEED={}
EXPECTED_RESULT_SEED[1]={'seed':['A'],'proba':'1/1'}
EXPECTED_RESULT_SEED[2] = {'seed': ['F','H','G'], 'proba': '1/3'}
EXPECTED_SEED1 = sorted(EXPECTED_RESULT_SEED[1]['seed'])
EXPECTED_SEED2 = sorted(EXPECTED_RESULT_SEED[2]['seed'])


def test_seed():
    S, R = storage.init_data('toy_metabolic.sbml.xml')
    G = storage.init_graph(S, R)
    DAG=Seed.dag_init(R, G)
    specie = Seed.scc_species(G)
    result = Seed.find_seed(DAG, specie)
    assert result[2]['proba'] == EXPECTED_RESULT_SEED[2]['proba']
    assert result[1]['proba'] == EXPECTED_RESULT_SEED[1]['proba']
    assert sorted(result[1]['seed']) == EXPECTED_SEED1
    assert sorted(result[2]['seed']) == EXPECTED_SEED2


if __name__=="__main__":
    test_seed()
