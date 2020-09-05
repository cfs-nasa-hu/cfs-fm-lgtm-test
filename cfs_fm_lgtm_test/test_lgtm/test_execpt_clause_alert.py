import json


def test_except_clause_alert_lgtm():
  response = ''
  try:
    data = {'project': 'cfs-fm-lgtm-test'}
    response = json.dumps(data, indent=4)
  except ValueError:
    pass
  return response
    
