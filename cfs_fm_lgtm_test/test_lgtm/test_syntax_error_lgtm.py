"""TEST SYNTAX ERROR"""


def test_syntax_error_lgtm():
  while True:
    try:
      print 'Failure'
    except SyntaxError as e:
      print(e)
  
def test_no_syntax_error_lgtm():
  while True:
    print('Success')

