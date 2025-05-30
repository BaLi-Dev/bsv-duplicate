import pytest
from unittest.mock import patch
from src.util.detector import detect_duplicates
from src.util.parser import Article

# develop your test cases here

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
    with patch('src.util.detector.parse') as mock_parse:
        mock_parse.return_value = [Article(key='frattini2023requirements', doi='10.1007/s00766-023-00405-y')]
        with pytest.raises(ValueError):
            duplicates = detect_duplicates(data)

@pytest.mark.unit
def test_detect_duplicates_same_doi_same_key():
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
    with patch('src.util.detector.parse') as mock_parse:
        mock_parse.return_value = [
            Article(key='frattini2023requirements', doi='10.1007/s00766-023-00405-y'), 
            Article(key='frattini2023requirements', doi='10.1007/s00766-023-00405-y')
        ]
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
    with patch('src.util.detector.parse') as mock_parse:
        mock_parse.return_value = [
            Article(key='frattini2023requirements', doi='10.1007/s00766-023-00405-y'), 
            Article(key='testkey', doi='10.1007/s00766-023-00405-y')
        ]
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
    with patch('src.util.detector.parse') as mock_parse:
        mock_parse.return_value = [
            Article(key='frattini2023requirements', doi=None), 
            Article(key='frattini2023requirements', doi='10.1007/s00766-023-00405-y')
        ]
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
    with patch('src.util.detector.parse') as mock_parse:
        mock_parse.return_value = [
            Article(key='frattini2023requirements', doi=None), 
            Article(key='testkey', doi='10.1007/s00766-023-00405-y')
        ]
        duplicates = detect_duplicates(data)
        assert len(duplicates) == 0


# When structuring the test cases, I started with testig the case of a single entry, which should raise a ValueError. Then I tested the cases with two entries, checking for duplicates based on both DOI and key. I also included cases where one entry had missing a DOI to ensure that the function correctly identifies duplicates in those scenarios. Each test case asserts the expected number of duplicates found.
# I ensured test independece by making sure that each test case is self-contained and does not rely on the results of other tests. This way, they can be run in any order without affecting the outcomes.
# There were no challenged faced when implementing these test cases. The first test case fails, as the logit to check for if the list contains more than 1 entry is faulty.

