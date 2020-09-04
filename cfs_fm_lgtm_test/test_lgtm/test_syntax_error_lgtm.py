"""TEST SYNTAX ERROR"""


def test_syntax_error_lgtm():
  while True:
    print 'Failure'
  
def test_no_syntax_error_lgtm():
  while True:
    print('Success')

