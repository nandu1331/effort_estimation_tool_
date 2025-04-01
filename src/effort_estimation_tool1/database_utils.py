# database.py
import psycopg2
from psycopg2 import sql

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect("postgresql://neondb_owner:npg_9k8hYdwKFNTW@ep-proud-cell-a5waynh9-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

# Close database connection
def close_db_connection(conn):
    if conn:
        conn.close()

# Store project data in the database
def store_project_data(conn, project_data):
    try:
        with conn.cursor() as cur:
            # Insert into projects table
            cur.execute(
                sql.SQL("INSERT INTO projects (client_id, project_name, sow_doc, aggregated_estimations) VALUES (%s, %s, %s, %s) RETURNING project_id"),
                (project_data["client_id"], project_data["project_name"], project_data["sow"], project_data["aggregated_estimations"])
            )
            project_id = cur.fetchone()[0]

            # Insert personas
            for persona in project_data["personas"]:
                cur.execute(
                    sql.SQL("INSERT INTO personas (project_id, persona_name, description, aggregated_estimations) VALUES (%s, %s, %s, %s) RETURNING persona_id"),
                    (project_id, persona["name"], persona["description"], persona["aggregated_estimations"])
                )
                persona_id = cur.fetchone()[0]

                # Insert modules
                for module in persona["modules"]:
                    cur.execute(
                        sql.SQL("INSERT INTO modules (persona_id, module_name, module_desc, aggregated_estimations) VALUES (%s, %s, %s, %s) RETURNING module_id"),
                        (persona_id, module["name"], module["description"], module["aggregated_estimations"])
                    )
                    module_id = cur.fetchone()[0]

                    # Insert features
                    for feature in module["features"]:
                        cur.execute(
                            sql.SQL("INSERT INTO features (module_id, feature_name, feature_desc, aggregated_estimations) VALUES (%s, %s, %s, %s) RETURNING feature_id"),
                            (module_id, feature["name"], feature["description"], feature["aggregated_estimations"])
                        )
                        feature_id = cur.fetchone()[0]

                        # Insert sub-features
                        for sub_feature in feature["sub_features"]:
                            cur.execute(
                                sql.SQL("""
                                    INSERT INTO sub_features (
                                        feature_id, subfeature_name, description, ui_ux_effort, mobile_effort, mobile_buffer,
                                        mobile_testing, backend_effort, backend_buffer, backend_testing, buffer, management_effort,
                                        risk_factor, historical_deviation, confidence_level, aggregated_effort
                                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """),
                                (
                                    feature_id, sub_feature["name"], sub_feature["description"],
                                    sub_feature.get("ui_ux_effort", 0.0), sub_feature.get("mobile_effort", 0.0),
                                    sub_feature.get("mobile_buffer", 0.0), sub_feature.get("mobile_testing", 0.0),
                                    sub_feature.get("backend_effort", 0.0), sub_feature.get("backend_buffer", 0.0),
                                    sub_feature.get("backend_testing", 0.0), sub_feature.get("buffer", 0.0),
                                    sub_feature.get("management_effort", 0.0), sub_feature.get("risk_factor", 0.0),
                                    sub_feature.get("historical_deviation", 0.0), sub_feature.get("confidence_level", 1.0),
                                    sub_feature["aggregated_effort"]
                                )
                            )
            conn.commit()
            print(f"Stored project data for project_id: {project_id}")
    except Exception as e:
        conn.rollback()
        print(f"Error storing project data: {e}")
        raise

# Fetch historical data for model training or estimation adjustments
def fetch_historical_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT ui_ux_effort, mobile_effort, mobile_buffer, mobile_testing, backend_effort,
                       backend_buffer, backend_testing, buffer, management_effort
                FROM sub_features
                WHERE aggregated_effort IS NOT NULL
            """)
            return cur.fetchall()
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        raise