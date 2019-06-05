from .models import Gist


def search_gists(db_connection, **kwargs):
    search = "SELECT * FROM gists"
    if 'github_id' in kwargs:
        search = "SELECT * FROM gists WHERE github_id = :github_id"
    elif 'created_at' in kwargs:
        search = "SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)"

    r = []
    cursor = db_connection.execute(search,kwargs)
    for row in cursor:
        r.append(Gist(row))
    return r
    
    
    
