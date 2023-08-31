"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import logging
import yaml

from expecter import expect
from yaml.loader import SafeLoader

from jsonmask_ng import parsing


def test_multiple_builds():
    tests = [
        {
            'fields': None,
            'mask': {},
        },
        {
            'fields': '',
            'mask': {},
        },
        {
            'fields': '()',
            'mask': {},
        },
        {
            'fields': 'a,b',
            'mask': {'a': {}, 'b': {}},
        },
        {
            'fields': ' a,b',
            'mask': {'a': {}, 'b': {}},
        },
        {
            'fields': 'a ,b',
            'mask': {'a': {}, 'b': {}},
        },
        {
            'fields': ' a , b ',
            'mask': {'a': {}, 'b': {}},
        },
        {
            'fields': 'a/b',
            'mask': {'a': {'b': {}}},
        },
        {
            'fields': 'a/b,c',
            'mask': {'a': {'b': {}}, 'c': {}},
        },
        {
            'fields': 'a/b,a/c',
            'mask': {'a': {'b': {}, 'c': {}}},
        },
        {
            'fields': 'a/b,a/c,c',
            'mask': {'a': {'b': {}, 'c': {}}, 'c': {}},
        },
        {
            'fields': 'a/b/z,a/c,c',
            'mask': {'a': {'b': {'z': {}}, 'c': {}}, 'c': {}},
        },
        {
            'fields': 'a(b)',
            'mask': {'a': {'b': {}}},
        },
        {
            'fields': 'a(b,c)',
            'mask': {'a': {'b': {}, 'c': {}}},
        },
        {
            'fields': ' a ( b , c )',
            'mask': {'a': {'b': {}, 'c': {}}},
        },
        {
            'fields': 'a(b,c/d)',
            'mask': {'a': {'b': {}, 'c': {'d': {}}}},
        },
        {
            'fields': 'z,a(b,c/d)',
            'mask': {'a': {'b': {}, 'c': {'d': {}}}, 'z': {}},
        },
        {
            'fields': 'a(b,c/d),z',
            'mask': {'a': {'b': {}, 'c': {'d': {}}}, 'z': {}},
        },
        {
            'fields': 'a(b,c/d(x,y,z))',
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}}}},
        },
        {
            'fields': 'a(b,c/d(x,y,z),abc(xyz/z(a)))',
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}, 'abc': {'xyz': {'z': {'a': {}}}}}}},
        },
        {
            'fields': yaml.load(yaml_input_1(), Loader=SafeLoader)['fields'],
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}, 'abc': {'xyz': {'z': {'a': {}}}}}}},
        },
        {
            'fields': 'a(b,c/d(x,y,z)),abc(xyz/z(a))',
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}}}, 'abc': {'xyz': {'z': {'a': {}}}}},
        },
        {
            'fields': '''
              a(
                b,
                c/
                  d(
                    x,
                    y,
                    z
                  )
              ),
              abc(
                xyz/
                  z(
                    a
                  )
              )
            ''',
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}}}, 'abc': {'xyz': {'z': {'a': {}}}}},
        },
        {
            'fields': yaml.load(yaml_input_2(), Loader=SafeLoader)['fields'],
            'mask': {'a': {'b': {}, 'c': {'d': {'x': {}, 'y': {}, 'z': {}}}}, 'abc': {'xyz': {'z': {'a': {}}}}},
        },
        {
            'fields': coplex_list(),
            'mask': {'a': {}, 'attrs': {'a': {}, 't': {}, 't': {}, 'r': {}, 's': {}}, 'z': {}},
        },
    ]

    for test in tests:
        error_msg = 'Failed to compile fields {}'.format(test['fields'])
        try:
            expect(parsing.parse_fields(test['fields'])) == test['mask']
        except Exception as e:
            logging.exception(e)
            raise e


def yaml_input_1():
    return '''
fields:
  - a:
    - b
    - c:
      - d:
        - x
        - y
        - z
      - abc:
        - xyz:
          - z:
            - a
'''


def yaml_input_2():
    return '''
fields:
  - a:
    - b
    - c:
      - d:
        - x
        - y
        - z
  - abc:
    - xyz:
      - z:
        - a
'''


def coplex_list():
    class Object(object):
        pass

    obj = Object()
    obj.attrs = ['a', 't', 't', 'r', 's']

    return ['a', obj, 'z']
