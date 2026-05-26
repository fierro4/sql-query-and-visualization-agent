import sqlite3
import re

DB_FILE = "ecommerce.db"


def sql_tool(sql: str):

    try:

        sql_clean = sql.strip().lower()

        dangerous = [
            "drop",
            "delete",
            "update",
            "insert",
            "alter",
            "create",
            "truncate"
        ]

        if any(
            re.search(rf"\\b{word}\\b", sql_clean)
            for word in dangerous
        ):
            return "ERROR: Dangerous query blocked"

        allowed = (
            sql_clean.startswith("select")
            or sql_clean.startswith("with")
        )

        if not allowed:
            return "ERROR: Only SELECT queries allowed"

        conn = sqlite3.connect(DB_FILE)

        cursor = conn.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = [d[0] for d in cursor.description]

        conn.close()

        return {
            "sql": sql,
            "columns": columns,
            "rows": rows
        }

    except Exception as e:
        return f"SQL ERROR: {str(e)}"