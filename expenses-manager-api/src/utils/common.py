from src import engine_container

def cleanup(session):
    """
    This method cleans up the session object and also closes the connection pool using the dispose method
    """
    session.close()
    engine_container.dispose()