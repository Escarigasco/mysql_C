#include <stdio.h>
#include <stdlib.h>
#include <my_global.h>
#include <mysql.h>

void finish_with_error(MYSQL *con)
{
	fprintf(stderr, "%s\n", mysql_error(con));
	mysql_close(con);
	exit(1);
}

int main(void)
{
    int date = 5;
	MYSQL *con = mysql_init(NULL);

	if (con == NULL) {
		fprintf(stderr, "%s\n", mysql_error(con));
		exit(1);
	}

	if (mysql_real_connect(con, "localhost", "escarigasco", "bandabassotti", "testdb", 0, NULL,0) == NULL) {
		finish_with_error(con);
	}


	if (mysql_query(con, "DROP TABLE IF EXISTS Climate_Data")) {
		finish_with_error(con);
	}

	if (mysql_query(con, "CREATE TABLE Climate_Data(Date INT, Parameter TEXT, Value INT)")) {
		finish_with_error(con);
	}

	if (mysql_query(con, "INSERT INTO Climate_Data VALUES(1, 'temp bathroom', 35)")) {
		finish_with_error(con);
	}

	if (mysql_query(con, "INSERT INTO Climate_Data VALUES(2, 'temp bathroom', 33)")) {
		finish_with_error(con);
	}

	if (mysql_query(con, "SELECT * FROM Climate_Data")) {
		finish_with_error(con);
	}

	MYSQL_RES *result = mysql_store_result(con);

	if (result == NULL) {
		finish_with_error(con);
	}

	int num_fields = mysql_num_fields(result);

	MYSQL_ROW row;

	while ((row = mysql_fetch_row(result))) {
		for(int i = 0; i < num_fields; i++) {
			printf("%s ", row[i] ? row[i] : "NULL");
		}
		printf("\n");
	}

	mysql_free_result(result);

	printf("MySQL client version: %s\n", mysql_get_client_info());
	mysql_close(con);
	return 0;

}
