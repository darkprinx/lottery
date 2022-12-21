from django.db import connections


def query_count_all() -> (int, float):
    time = 0.0
    total_query = 0
    all_connections = connections.all()
    for connection in all_connections:
        total_query += len(connection.queries)
        for query in connection.queries:
            time += float(query['time'])
    return total_query, time
