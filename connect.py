import mysql.connector
cnn = mysql.connector.connect(host ="127.0.0.1",user ="root",password="1234")

if cnn.is_connected():
	db_info = cnn.get_server_info()
	print(db_info)
	cursor=cnn.cursor()
	cursor.execute("Use amazon;")
	query=input("Enter your Queries:")
	cursor.execute(query)
	record=cursor.fetchone()
	for i in record:
		print(record)
	

