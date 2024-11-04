import pytest

# Import the student's validate function
from student_code import validate

# The template dictionary
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

def test_valid_data():
    john = {
        'user_id': 100,
        'name': {
            'first': 'John',
            'last': 'Cleese'
        },
        'bio': {
            'dob': {
                'year': 1939,
                'month': 11,
                'day': 27
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Weston-super-Mare'
            }
        }
    }
    state, error = validate(john, template)
    assert state == True
    assert error == ''

def test_missing_key():
    eric = {
        'user_id': 101,
        'name': {
            'first': 'Eric',
            'last': 'Idle'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 3,
                'day': 29
            },
            'birthplace': {
                'country': 'United Kingdom'
            }
        }
    }
    state, error = validate(eric, template)
    assert state == False
    assert error == 'mismatched keys: bio.birthplace.city'

def test_bad_type():
    michael = {
        'user_id': 102,
        'name': {
            'first': 'Michael',
            'last': 'Palin'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 'May',  # Should be int
                'day': 5
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Sheffield'
            }
        }
    }
    state, error = validate(michael, template)
    assert state == False
    assert error == 'bad type: bio.dob.month'

def test_extra_key():
    # Data with an extra key
    graham = {
        'user_id': 103,
        'name': {
            'first': 'Graham',
            'last': 'Chapman',
            'middle': 'Arthur'  # Extra key not in template
        },
        'bio': {
            'dob': {
                'year': 1941,
                'month': 1,
                'day': 8
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Leicester'
            }
        }
    }
    state, error = validate(graham, template)
    assert state == False
    assert error == 'mismatched keys: name.middle'

def test_wrong_type_at_top_level():
    # Data where a top-level key has wrong type
    terry_j = {
        'user_id': '104',  # Should be int
        'name': {
            'first': 'Terry',
            'last': 'Jones'
        },
        'bio': {
            'dob': {
                'year': 1942,
                'month': 2,
                'day': 1
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Colwyn Bay'
            }
        }
    }
    state, error = validate(terry_j, template)
    assert state == False
    assert error == 'bad type: user_id'

def test_missing_top_level_key():
    # Data missing a top-level key
    terry_g = {
        # 'user_id' is missing
        'name': {
            'first': 'Terry',
            'last': 'Gilliam'
        },
        'bio': {
            'dob': {
                'year': 1940,
                'month': 11,
                'day': 22
            },
            'birthplace': {
                'country': 'United States',
                'city': 'Minneapolis'
            }
        }
    }
    state, error = validate(terry_g, template)
    assert state == False
    assert error == 'mismatched keys: user_id'

def test_additional_nested_key():
    # Data with an additional nested key
    neil = {
        'user_id': 105,
        'name': {
            'first': 'Neil',
            'last': 'Innes'
        },
        'bio': {
            'dob': {
                'year': 1944,
                'month': 12,
                'day': 9
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Danbury',
                'postcode': 'CM3'  # Extra key
            }
        }
    }
    state, error = validate(neil, template)
    assert state == False
    assert error == 'mismatched keys: bio.birthplace.postcode'

def test_empty_dictionary():
    # Empty data
    empty_data = {}
    state, error = validate(empty_data, template)
    assert state == False
    assert error == 'mismatched keys: user_id'

def test_none_value():
    # Data with None as value
    carol = {
        'user_id': 106,
        'name': {
            'first': 'Carol',
            'last': None  # Should be str
        },
        'bio': {
            'dob': {
                'year': 1942,
                'month': 8,
                'day': 24
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Bedford'
            }
        }
    }
    state, error = validate(carol, template)
    assert state == False
    assert error == 'bad type: name.last'

def test_correct_types_but_extra_keys():
    # Correct types but extra keys
    connie = {
        'user_id': 107,
        'name': {
            'first': 'Connie',
            'last': 'Booth'
        },
        'bio': {
            'dob': {
                'year': 1940,
                'month': 1,
                'day': 31
            },
            'birthplace': {
                'country': 'United States',
                'city': 'Indianapolis'
            },
            'spouse': 'John Cleese'  # Extra key
        }
    }
    state, error = validate(connie, template)
    assert state == False
    assert error == 'mismatched keys: bio.spouse'

def test_wrong_type_in_nested_dict():
    # Wrong type in nested dictionary
    chapman = {
        'user_id': 108,
        'name': {
            'first': 'Chapman',
            'last': 'Brothers'
        },
        'bio': {
            'dob': {
                'year': 1962,
                'month': 9,
                'day': 14
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': ['Cheltenham']  # Should be str, not list
            }
        }
    }
    state, error = validate(chapman, template)
    assert state == False
    assert error == 'bad type: bio.birthplace.city' 