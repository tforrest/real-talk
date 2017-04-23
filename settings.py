import logging
import sys

import boto3

try:
	_client = boto3.resource('dynamodb')
	table = _client.Table('RealTalkSessions')
	# fail app if no table
	table.table_status
except Exception as e:
	logging.critical(e)
	sys.exit(1)
