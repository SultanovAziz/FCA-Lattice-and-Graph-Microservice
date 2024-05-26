from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from neo4j import GraphDatabase

db = SQLAlchemy()
migrate = Migrate()

class Neo4jDriver:
    def __init__(self):
        self.driver = None

    def init_app(self, app):
        self.driver = GraphDatabase.driver(
            app.config['NEO4J_URI'],
            auth=(app.config['NEO4J_USER'], app.config['NEO4J_PASSWORD'])
        )

neo4j_driver = Neo4jDriver()

