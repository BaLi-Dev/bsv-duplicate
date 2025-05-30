import pytest

from src.util.detector import detect_duplicates

# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

@pytest.mark.unit
def test_detect_duplicates_with_1_entry():
    data = '''
    @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
    }
    '''
    with pytest.raises(ValueError):
        duplicates = detect_duplicates(data)

@pytest.mark.unit
def test_detect_duplicates_same_doi_and_key():
    data = '''
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }

    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    '''
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

@pytest.mark.unit
def test_detect_duplicates_same_doi_different_key():
    data = '''
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }

    @article{testkey,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    '''
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 0

@pytest.mark.unit
def test_detect_duplicates_missing_doi_same_key():
    data = '''
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={}
    }

    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    '''
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

@pytest.mark.unit
def test_detect_duplicates_missing_doi_different_key():
    data = '''
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={}
    }

    @article{testkey,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    '''
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 0