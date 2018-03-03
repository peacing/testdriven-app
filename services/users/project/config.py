
class BaseConfig:
    """Base Configuration"""
    TESTING = False
    
class DevelopmentConfig(BaseConfig):
    """Development Config"""
    pass
    
class TestingConfig(BaseConfig):
    """Testing Config"""
    TESTING = True
    
    
class ProductionConfid(BaseConfig):
    """Production config"""
    pass